import hid
import macmouse
import time

# SayoDevice E1
VENDOR_ID = 0x8089
PRODUCT_ID = 0x0007

def open_device():
    try:
        dev = hid.device()
        dev.open(VENDOR_ID, PRODUCT_ID)
        dev.set_nonblocking(True)
        return dev
    except IOError as e:
        print(f"Could not open device: {e}")
        return None

def main():
    print(f"Opening device 0x{VENDOR_ID:04x}:0x{PRODUCT_ID:04x}...")
    dev = open_device()
    if not dev:
        print("Device not found or could not be opened.")
        return

    print("Device opened. Turn the knob to scroll.")
    print("Press Ctrl+C to exit.")

    try:
        while True:
            data = dev.read(64)
            if data:
                # Debug: print raw data to understand the protocol
                # hex_data = " ".join(f"{b:02x}" for b in data)
                # print(f"Data: {hex_data}")
                
                # Logic based on observed data:
                # 04 ea 00 -> Direction A
                # 04 e9 00 -> Direction B
                # 04 00 00 -> Neutral/Release (Ignore)
                
                if data[0] == 0x04:
                    if data[1] == 0xea:
                        # Assuming EA is one direction (e.g., Right/Down)
                        macmouse.wheel(-1)
                        print("Scroll Down")
                    elif data[1] == 0xe9:
                        # Assuming E9 is the other direction (e.g., Left/Up)
                        macmouse.wheel(1)
                        print("Scroll Up")
            
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        dev.close()

if __name__ == '__main__':
    main()
