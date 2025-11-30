import hid
print("hidapi imported successfully")
try:
    for device in hid.enumerate():
        print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")
except Exception as e:
    print(f"Error enumerating devices: {e}")
