[app]

# ---------------------------------------------------------------------------
# Identidad de la app
# ---------------------------------------------------------------------------
title = Agrowillay
package.name = agrowillay
package.domain = org.agrowillay

# Carpeta fuente (donde esta main.py)
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

version = 1.0.0

# ---------------------------------------------------------------------------
# Requerimientos de Python
# ---------------------------------------------------------------------------
# NOTA: no incluimos "google-generativeai" porque main.py llama a la API de
# Gemini directamente por REST (con "requests"), lo cual es mucho mas liviano
# y evita dependencias problematicas de compilar para Android (grpc, protobuf).
requirements = python3,kivy==2.3.0,kivymd==1.2.0,requests,pillow,plyer,certifi,urllib3,charset-normalizer,idna

# ---------------------------------------------------------------------------
# Recursos visuales: icono y splash screen
# ---------------------------------------------------------------------------
# Coloca tu icono en assets/icon.png (recomendado 512x512, PNG con fondo)
# y tu splash en assets/presplash.png (recomendado 1080x1920 o similar).
icon.filename = %(source.dir)s/assets/icon.png
presplash.filename = %(source.dir)s/assets/presplash.png

# Color de fondo del splash mientras carga (formato: R,G,B,A entre 0 y 1)
android.presplash_color = #0F6B4E

orientation = portrait
fullscreen = 0

# ---------------------------------------------------------------------------
# Permisos de Android
# ---------------------------------------------------------------------------
android.permissions = INTERNET,CAMERA,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# ---------------------------------------------------------------------------
# Configuracion de compilacion Android
# ---------------------------------------------------------------------------
android.api = 34
android.minapi = 24
android.ndk = 25b
android.sdk = 34
android.accept_sdk_license = True

# Arquitecturas: arm64-v8a cubre casi todos los celulares modernos.
# Agrega armeabi-v7a solo si necesitas compatibilidad con equipos muy viejos
# (aumenta bastante el tiempo de compilacion).
android.archs = arm64-v8a

# Kivy necesita esta bandera para usar el modo de pantalla completa/adaptativo
android.allow_backup = True

# Necesario para "Chrome Custom Tabs": al abrir Google Maps (ubicacion/ayuda
# cercana), esto muestra una flecha "<-" en la parte de arriba de la pagina
# para volver directo a la app, en vez de dejar al usuario sin forma de
# regresar (lo que pasaba usando el navegador externo normal).
android.enable_androidx = True
android.gradle_dependencies = androidx.browser:browser:1.5.0

# Si tu app necesita usar la camara del sistema (intent) en vez de la libreria
# nativa, plyer ya se encarga de eso via android.permissions declarados arriba.

[buildozer]
log_level = 2
warn_on_root = 1
