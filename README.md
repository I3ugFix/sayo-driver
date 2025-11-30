# SayoDevice E1 Knob Driver para Logic Pro

[English](#english) | [Español](#español)

---

<a name="english"></a>
## 🇬🇧 English

### What does this do?

This script turns your **SayoDevice E1** physical knob into a tactile control surface for Logic Pro. 

**In simple terms:** Instead of clicking and dragging faders/knobs with your mouse, you can use the physical knob to control them - giving you a more natural, hands-on mixing experience like professional hardware control surfaces.

**Product Link:** [AliExpress](https://es.aliexpress.com/item/1005006020111017.html)

---

### How It Works (Simple Explanation)

1. You place your mouse cursor over any control in Logic Pro (a fader, a knob, pan control, etc.)
2. You rotate the physical knob
3. The script automatically:
   - Clicks and holds the mouse button
   - Drags the control as you rotate
   - Releases when you stop rotating

**Result:** The control moves smoothly, just like you're using a professional hardware mixer!

**No configuration in Logic Pro needed** - it works automatically with any control.

---

### What You Need

- **macOS** (any recent version)
- **Python 3** (usually pre-installed on macOS)
- **SayoDevice E1** connected via USB
- **5 minutes** to set it up

### ⚠️ Important: System Permissions

**macOS may ask for permissions when you run the script. You MUST grant them for the script to work!**

The script needs permissions to control your mouse and simulate mouse movements in your DAW. If macOS prompts you for any permissions, click **"Allow"** or **"Open System Settings"** and enable them.

**Without granting the requested permissions, the script cannot control the knob as a mouse and will not work in your DAW.**

---

### Step-by-Step Installation

#### Step 1: Download and Setup

1. Open Terminal (Applications > Utilities > Terminal)
2. Navigate to the project folder:
   ```bash
   cd /path/to/sayo-driver
   ```

#### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

That's it! Installation complete.

---

### How to Use

#### Step 1: Start the Script

```bash
./run_drag.sh
```

Or if that doesn't work:
```bash
source venv/bin/activate
python3 knob_drag.sh
```

#### Step 2: Grant System Permissions ⚠️ REQUIRED

**If macOS asks for permissions, you MUST grant them!**

When you run the script, macOS may prompt you for permissions to control your mouse. This is required for the script to work - it needs to simulate mouse movements to control faders and knobs in your DAW.

- Click **"Allow"** when prompted, or
- Click **"Open System Settings"** and enable the requested permissions

**The script will not work without granting the requested permissions!**

#### Step 3: Use in Logic Pro

**For Vertical Faders (Volume, Send levels, etc.):**
1. Place your mouse cursor over the fader
2. Rotate the physical knob
3. The fader moves up and down! ✨

**For Horizontal Knobs (Pan, EQ knobs, etc.):**

**Option 1 - Temporary (while holding key):**
1. **Hold down the Right Shift key** on your keyboard
2. Place your mouse cursor over the knob
3. Rotate the physical knob
4. The knob moves left and right! ✨
5. Release Right Shift when done

**Option 2 - Permanent toggle:**
1. **Single-click the knob button** to switch to horizontal mode
2. Place your mouse cursor over any horizontal knob
3. Rotate the physical knob
4. The knob moves left and right! ✨
5. Click the knob button again to switch back to vertical mode

**That's it!** No other configuration needed.

---

### Quick Reference

| Control Type | How to Use |
|-------------|------------|
| **Vertical Fader** | Place cursor + Rotate knob (no keys needed) |
| **Horizontal Knob** | Option 1: Hold **Right Shift** + Place cursor + Rotate knob<br>Option 2: Click knob button once to toggle to horizontal mode, then rotate |
| **Toggle Mode** | Single-click the knob button to permanently switch between vertical/horizontal mode |

---

### Run in Background (Optional)

To keep it running without keeping Terminal open:

```bash
nohup ./run_drag.sh > /dev/null 2>&1 &
```

To stop it later:
```bash
pkill -f knob_drag.py
```

---

### Troubleshooting

**Problem:** Script says "Device not found"
- **Solution:** Make sure the SayoDevice E1 is connected via USB

**Problem:** Controls don't move in Logic Pro
- **Solution:** Make sure you granted any permissions that macOS requested when you ran the script. The script needs permissions to control your mouse. If you denied permissions, you'll need to grant them in System Settings and restart the script.

**Problem:** Horizontal mode doesn't work
- **Solution:** 
  - If using Right Shift: Make sure you're holding **Right Shift** (the right side Shift key, not the left one)
  - If using knob button toggle: Click the knob button once and check the console message to confirm mode change

**Problem:** Button gets "stuck" on a control
- **Solution:** Press Ctrl+C to stop the script, then restart it

---

<a name="español"></a>
## 🇪🇸 Español

### ¿Qué hace esto?

Este script convierte tu knob físico **SayoDevice E1** en una superficie de control táctil para Logic Pro.

**En términos simples:** En lugar de hacer click y arrastrar faders/knobs con el ratón, puedes usar el knob físico para controlarlos - dándote una experiencia de mezcla más natural y táctil, como las superficies de control hardware profesionales.

**Enlace del producto:** [AliExpress](https://es.aliexpress.com/item/1005006020111017.html)

---

### Cómo Funciona (Explicación Simple)

1. Colocas el cursor del ratón sobre cualquier control en Logic Pro (un fader, un knob, control de pan, etc.)
2. Giras el knob físico
3. El script automáticamente:
   - Hace click y mantiene presionado el botón del ratón
   - Arrastra el control mientras giras
   - Suelta cuando dejas de girar

**Resultado:** ¡El control se mueve suavemente, como si usaras un mezclador hardware profesional!

**No necesitas configuración en Logic Pro** - funciona automáticamente con cualquier control.

---

### Lo Que Necesitas

- **macOS** (cualquier versión reciente)
- **Python 3** (normalmente viene pre-instalado en macOS)
- **SayoDevice E1** conectado por USB
- **5 minutos** para configurarlo

### ⚠️ Importante: Permisos del Sistema

**macOS puede pedirte permisos cuando ejecutes el script. ¡DEBES darlos para que el script funcione!**

El script necesita permisos para controlar tu ratón y simular movimientos del ratón en tu DAW. Si macOS te solicita permisos, haz clic en **"Permitir"** o **"Abrir Preferencias del Sistema"** y actívalos.

**Sin conceder los permisos solicitados, el script no puede controlar el knob como un ratón y no funcionará en tu DAW.**

---

### Instalación Paso a Paso

#### Paso 1: Descargar y Configurar

1. Abre Terminal (Aplicaciones > Utilidades > Terminal)
2. Navega a la carpeta del proyecto:
   ```bash
   cd /ruta/a/sayo-driver
   ```

#### Paso 2: Crear Entorno Virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

¡Listo! Instalación completa.

---

### Cómo Usar

#### Paso 1: Iniciar el Script

```bash
./run_drag.sh
```

O si eso no funciona:
```bash
source venv/bin/activate
python3 knob_drag.py
```

#### Paso 2: Dar Permisos del Sistema ⚠️ REQUERIDO

**¡Si macOS pide permisos, DEBES darlos!**

Cuando ejecutes el script, macOS puede pedirte permisos para controlar el ratón. Esto es necesario para que el script funcione - necesita simular movimientos del ratón para controlar faders y knobs en tu DAW.

- Haz clic en **"Permitir"** cuando se solicite, o
- Haz clic en **"Abrir Preferencias del Sistema"** y activa los permisos solicitados

**¡El script no funcionará sin conceder los permisos solicitados!**

#### Paso 3: Usar en Logic Pro

**Para Faders Verticales (Volumen, niveles de Send, etc.):**
1. Coloca el cursor del ratón sobre el fader
2. Gira el knob físico
3. ¡El fader se mueve arriba y abajo! ✨

**Para Knobs Horizontales (Pan, knobs de EQ, etc.):**

**Opción 1 - Temporal (mientras mantienes la tecla):**
1. **Mantén presionada la tecla Right Shift** en tu teclado
2. Coloca el cursor del ratón sobre el knob
3. Gira el knob físico
4. ¡El knob se mueve izquierda y derecha! ✨
5. Suelta Right Shift cuando termines

**Opción 2 - Toggle permanente:**
1. **Haz un solo click en el botón del knob** para cambiar a modo horizontal
2. Coloca el cursor del ratón sobre cualquier knob horizontal
3. Gira el knob físico
4. ¡El knob se mueve izquierda y derecha! ✨
5. Haz click en el botón del knob otra vez para volver al modo vertical

**¡Eso es todo!** No necesitas otra configuración.

---

### Referencia Rápida

| Tipo de Control | Cómo Usar |
|-----------------|-----------|
| **Fader Vertical** | Coloca cursor + Gira knob (sin teclas) |
| **Knob Horizontal** | Opción 1: Mantén **Right Shift** + Coloca cursor + Gira knob<br>Opción 2: Click en el botón del knob una vez para cambiar a modo horizontal, luego gira |
| **Alternar Modo** | Un solo click en el botón del knob para cambiar permanentemente entre modo vertical/horizontal |

---

### Ejecutar en Segundo Plano (Opcional)

Para dejarlo corriendo sin tener Terminal abierto:

```bash
nohup ./run_drag.sh > /dev/null 2>&1 &
```

Para detenerlo después:
```bash
pkill -f knob_drag.py
```

---

### Solución de Problemas

**Problema:** El script dice "Device not found"
- **Solución:** Asegúrate de que el SayoDevice E1 esté conectado por USB

**Problema:** Los controles no se mueven en Logic Pro
- **Solución:** Asegúrate de haber concedido cualquier permiso que macOS haya solicitado al ejecutar el script. El script necesita permisos para controlar el ratón. Si denegaste permisos, necesitarás concederlos en Preferencias del Sistema y reiniciar el script.

**Problema:** El modo horizontal no funciona
- **Solución:** 
  - Si usas Right Shift: Asegúrate de estar manteniendo presionado **Right Shift** (la tecla Shift del lado derecho, no la izquierda)
  - Si usas el toggle del botón: Haz click en el botón del knob una vez y verifica el mensaje en la consola para confirmar el cambio de modo

**Problema:** El botón se queda "pillado" en un control
- **Solución:** Presiona Ctrl+C para detener el script, luego reinícialo

---

## License

This project is provided as-is for personal use.
