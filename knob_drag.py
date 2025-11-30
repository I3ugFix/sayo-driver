import hid
import macmouse
import time
try:
    from pynput import keyboard
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False
    print("Warning: pynput not installed. Horizontal mode (Space key) will not work.")
    print("Install it with: pip install pynput")

# SayoDevice E1
VENDOR_ID = 0x8089
PRODUCT_ID = 0x0007

def open_device():
    """Abre el dispositivo HID, intentando todas las instancias disponibles"""
    try:
        # Intentar encontrar todas las instancias del dispositivo
        devices = []
        for device_info in hid.enumerate():
            if device_info['vendor_id'] == VENDOR_ID and device_info['product_id'] == PRODUCT_ID:
                devices.append(device_info)
        
        if not devices:
            print(f"Device 0x{VENDOR_ID:04x}:0x{PRODUCT_ID:04x} not found.")
            print("Please make sure the device is connected via USB.")
            return None
        
        print(f"Found {len(devices)} instance(s) of the device.")
        
        # Intentar abrir cada instancia hasta que una funcione
        for i, device_info in enumerate(devices):
            try:
                dev = hid.device()
                dev.open_path(device_info['path'])
                dev.set_nonblocking(True)
                print(f"Successfully opened device instance {i+1}.")
                return dev
            except IOError as e:
                if i < len(devices) - 1:
                    print(f"Could not open instance {i+1}, trying next...")
                    continue
                else:
                    raise e
                    
    except IOError as e:
        print(f"Could not open device: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure no other program is using the device")
        print("2. Try unplugging and replugging the USB cable")
        print("3. Check if another instance of this script is running")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def main():
    print(f"Opening device 0x{VENDOR_ID:04x}:0x{PRODUCT_ID:04x}...")
    dev = open_device()
    if not dev:
        print("Device not found or could not be opened.")
        return

    print("\n" + "="*60)
    print("SayoDriver - Generic Control for Logic Pro")
    print("="*60)
    print("How it works:")
    print("1. Place your cursor over ANY control (fader, knob, etc.)")
    print("2. Rotate the physical knob")
    print("3. The control will activate and move automatically")
    print("\nMovement modes:")
    print("  - VERTICAL mode (default): For vertical faders")
    print("  - HORIZONTAL mode: For horizontal knobs")
    print("\nTo change mode:")
    print("  - Press RIGHT SHIFT (hold for horizontal mode)")
    print("  - Or press the KNOB BUTTON once (toggles mode)")
    print("\nPress Ctrl+C to exit.")
    print("If the button gets 'stuck', press Ctrl+C and restart the script.")
    print("="*60 + "\n")
    
    # Estado del modo horizontal (usando una lista para poder modificar desde callbacks)
    # Se puede activar con Right Shift O con el botón del knob (single click)
    horizontal_mode = [False]
    
    # Listener de teclado para detectar Right Shift
    def on_press(key):
        try:
            # Right Shift - método principal
            if key == keyboard.Key.shift_r:
                horizontal_mode[0] = True
                print(">>> Right Shift PRESSED - HORIZONTAL mode activated <<<")
            # También verificar por string (por si acaso)
            elif str(key) == 'Key.shift_r' or 'shift_r' in str(key).lower():
                horizontal_mode[0] = True
                print(">>> Right Shift PRESSED (alternative) - HORIZONTAL mode activated <<<")
        except Exception as e:
            # Debug: mostrar qué tecla se presionó
            try:
                print(f"Key pressed: {key} (type: {type(key)})")
            except:
                pass
    
    def on_release(key):
        try:
            if key == keyboard.Key.shift_r:
                horizontal_mode[0] = False
                print(">>> Right Shift RELEASED - VERTICAL mode <<<")
            elif str(key) == 'Key.shift_r' or 'shift_r' in str(key).lower():
                horizontal_mode[0] = False
                print(">>> Right Shift RELEASED (alternative) - VERTICAL mode <<<")
        except:
            pass
        if key == keyboard.Key.esc:
            return False
    
    # Iniciar listener de teclado en un hilo separado
    listener = None
    if PYNPUT_AVAILABLE:
        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start()

    last_move_time_ea = 0  # Tiempo del último evento 0xea (separado para cada dirección)
    last_move_time_e9 = 0  # Tiempo del último evento 0xe9
    move_cooldown = 0.015  # 15ms entre movimientos (aumentado para más suavidad)
    mouse_pressed = False
    last_move_event_time = 0
    move_timeout = 0.2  # 200ms sin eventos = soltar el botón (aumentado)
    
    # Sensibilidad del movimiento (velocidad normal aumentada 20%)
    move_sensitivity = 5  # píxeles por evento de knob (4 * 1.2 = 4.8, redondeado a 5)
    
    try:
        while True:
            current_time = time.time()
            
            # Verificar timeout - si no hay eventos, soltar el botón
            # Esto es CRÍTICO para evitar que se quede "pillado"
            if mouse_pressed and (current_time - last_move_event_time) >= move_timeout:
                macmouse.release()
                mouse_pressed = False
                last_move_time_ea = 0
                last_move_time_e9 = 0
                # print("Mouse released (timeout)")
            
            data = dev.read(64)
            if data:
                # Detectar rotación del knob (ignorar el click físico 04 e2)
                if data[0] == 0x04 and len(data) > 1 and data[1] != 0xe2:
                    current_time = time.time()
                    
                    # Determinar qué dirección y verificar su cooldown específico
                    should_process = False
                    direction = None
                    
                    if data[1] == 0xea:
                        # Verificar cooldown para esta dirección específica
                        if current_time - last_move_time_ea >= move_cooldown:
                            should_process = True
                            direction = 'ea'
                    elif data[1] == 0xe9:
                        # Verificar cooldown para esta dirección específica
                        if current_time - last_move_time_e9 >= move_cooldown:
                            should_process = True
                            direction = 'e9'
                    
                    if should_process:
                        # Si el botón no está presionado, presionarlo para iniciar el arrastre
                        if not mouse_pressed:
                            macmouse.press()
                            mouse_pressed = True
                            # print("Mouse pressed (iniciando arrastre)")
                        
                        # Actualizar el tiempo del último evento (para timeout general)
                        last_move_event_time = current_time
                        
                        # Obtener posición actual del ratón
                        current_pos = macmouse.get_position()
                        
                        # Determinar dirección según el modo (horizontal o vertical)
                        # EJES INVERTIDOS: 0xea y 0xe9 están intercambiados
                        if horizontal_mode[0]:
                            # Modo HORIZONTAL (para knobs horizontales)
                            if direction == 'ea':
                                # Mover hacia la izquierda (invertido)
                                new_x = current_pos[0] - move_sensitivity
                                macmouse.move(new_x, current_pos[1])
                                last_move_time_ea = current_time
                            elif direction == 'e9':
                                # Mover hacia la derecha (invertido)
                                new_x = current_pos[0] + move_sensitivity
                                macmouse.move(new_x, current_pos[1])
                                last_move_time_e9 = current_time
                        else:
                            # Modo VERTICAL (para faders verticales)
                            if direction == 'ea':
                                # Mover hacia arriba (invertido: arrastrar hacia arriba = subir el fader)
                                new_y = current_pos[1] - move_sensitivity
                                macmouse.move(current_pos[0], new_y)
                                last_move_time_ea = current_time
                            elif direction == 'e9':
                                # Mover hacia abajo (invertido: arrastrar hacia abajo = bajar el fader)
                                new_y = current_pos[1] + move_sensitivity
                                macmouse.move(current_pos[0], new_y)
                                last_move_time_e9 = current_time
                
                # Detectar click físico del knob (04 e2 00) - solo si no hay scroll activo
                if not mouse_pressed:
                    if data[0] == 0x04 and len(data) > 1 and data[1] == 0xe2:
                        # Single click del knob - alternar modo vertical/horizontal
                        horizontal_mode[0] = not horizontal_mode[0]
                        mode_text = "HORIZONTAL" if horizontal_mode[0] else "VERTICAL"
                        print(f">>> Mode changed to: {mode_text} (knob button click) <<<")
                        time.sleep(0.15)  # Evitar múltiples detecciones
            
            time.sleep(0.003)  # 3ms para balance entre responsividad y CPU
            
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        # Asegurarse de soltar el botón si está presionado
        if mouse_pressed:
            macmouse.release()
        if listener is not None:
            listener.stop()
        if dev:
            dev.close()
        print("Device closed.")

if __name__ == '__main__':
    main()

