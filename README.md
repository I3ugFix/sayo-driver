# SayoDevice E1 Knob Scroll

Este proyecto permite usar el knob SayoDevice E1 como una rueda de scroll en macOS.

https://es.aliexpress.com/item/1005006020111017.html?spm=a2g0o.order_list.order_list_main.29.45d0194dZaTGvv&gatewayAdapt=glo2esp

## Requisitos

- Python 3
- `hidapi`
- `macmouse`

## Instalación

1. Crear un entorno virtual (opcional pero recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instalar dependencias:
   ```bash
   pip install hidapi macmouse
   ```

## Uso

1. Activar el entorno virtual (si no está activo):
   ```bash
   source venv/bin/activate
   ```

2. Ejecutar el script:
   ```bash
   python3 knob_scroll.py
   ```
   *Nota: Necesitarás dar permisos de Accesibilidad a tu Terminal o aplicación Python en Preferencias del Sistema.*

## Ejecutar en segundo plano

Para dejarlo corriendo sin tener la terminal abierta:

```bash
nohup python3 knob_scroll.py > /dev/null 2>&1 &
```
