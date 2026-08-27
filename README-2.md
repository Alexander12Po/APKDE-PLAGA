# Agrowillay — App Android (Kivy + KivyMD)

Version movil nativa de la web Agrowillay. Diagnostico de plagas en
plantas en 3 pasos: foto -> diagnostico con IA (Gemini) -> ayuda cercana
(viveros/agronomos via Google Maps).

## Estructura

```
APKPLAHS/
├── main.py            # App completa (UI + logica + llamada a Gemini)
├── buildozer.spec      # Configuracion de empaquetado a APK
├── assets/
│   ├── icon.png         # Icono de la app (agregalo tu, 512x512)
│   └── presplash.png     # Pantalla de carga (agregalo tu)
└── README.md
```

## Como funciona la API Key (importante)

La app **no trae ninguna clave incluida**. La primera vez que la abras:

1. Toca el icono de engranaje (Ajustes) en la barra superior.
2. Pega tu clave de Gemini (gratis en https://aistudio.google.com/apikey).
3. Toca "Guardar".

La clave se guarda en un archivo JSON dentro del almacenamiento privado de
la app en el propio telefono (`config.json`) — nunca viaja a ningun
servidor tuyo, no esta en el codigo fuente, y no queda dentro del APK.

## Compilar el APK sin computadora Linux (via Google Colab)

Ver el archivo `colab_build_apk.ipynb` (o `COLAB_INSTRUCCIONES.md`) que
acompaña este repositorio: contiene los pasos exactos para clonar este
repo, instalar Buildozer en Colab, compilar y descargar el `.apk`.

## Probar en escritorio antes de compilar (opcional)

```bash
pip install kivy kivymd requests pillow plyer
python main.py
```

En escritorio, la camara/GPS via `plyer` puede no estar disponible segun tu
sistema operativo — eso es normal, esas funciones estan pensadas para
Android. La seleccion de imagen desde archivo y la llamada a Gemini si
funcionan igual.

## Notas

- Modelo usado: `gemini-2.5-flash` (rapido y economico para vision).
- La app llama a la API de Gemini directamente por REST (sin el SDK
  `google-generativeai`) para mantener el APK liviano y evitar
  dependencias nativas dificiles de compilar para Android.
- El diagnostico es orientativo: para casos graves, consulta a un
  agronomo o especialista certificado.
- **Audio**: el boton "Escuchar diagnostico" usa el motor de texto a voz
  nativo del telefono (via `plyer.tts`), no la API de Gemini, para no
  generar costo extra ni depender de internet una vez que ya llego el
  diagnostico.
- **Ayuda cercana (Google Maps)**: los enlaces se abren con "Chrome
  Custom Tabs" en vez del navegador externo normal. Esto muestra una
  flecha "<-" en la parte de arriba de la pantalla para volver
  directamente a Agrowillay con un toque, en vez de tener que usar el
  boton/gesto de retroceso del sistema.

## Cambio de nombre de paquete (importante si ya instalaste una version anterior)

`buildozer.spec` ahora usa `package.name = agrowillay` y
`package.domain = org.agrowillay`. Android trata esto como una **app
distinta** a cualquier version anterior con otro nombre de paquete: no
se puede "actualizar" sobre la version vieja, hay que desinstalar la
version anterior del telefono antes de instalar este nuevo APK.
