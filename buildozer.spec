[app]

# Название приложения
title = Школьный помощник

# Папка с main.py
package.name = schoolhelper
package.domain = org.schoolhelper

# Папка проекта
source.dir = .

# Файлы, которые должны попасть в APK
source.include_exts = py,json,png,jpg,jpeg,kv,atlas

# Версия приложения
version = 1.0

# Python-зависимости
requirements = python3,kivy,kivymd,plyer

# Ориентация приложения
orientation = portrait

# Полноэкранный режим
fullscreen = 0


# ------------------------------------------------------------------
# ANDROID
# ------------------------------------------------------------------

# Android API
android.api = 35

# Минимальная версия Android
android.minapi = 21

# NDK — используем стабильный r27c
android.ndk = 27.2.12479018

# Архитектура
android.arch = arm64-v8a

# Разрешения
android.permissions = INTERNET,POST_NOTIFICATIONS,VIBRATE


# ------------------------------------------------------------------
# НАСТРОЙКИ СБОРКИ
# ------------------------------------------------------------------

# Не добавлять системные сервисы
android.add_src =

# Не использовать AndroidX
android.enable_androidx = True

# Не включать автозапуск
android.entrypoint = org.kivy.android.PythonActivity

# Имя приложения в Android
android.activity_class_name = org.kivy.android.PythonActivity


# ------------------------------------------------------------------
# ICON / SPLASH
# ------------------------------------------------------------------

# Если появятся свои файлы, можно раскомментировать:
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png


# ------------------------------------------------------------------
# ЧЕРНОВОЙ РЕЖИМ
# ------------------------------------------------------------------

# Не включаем отладочный режим
debug = 0


[buildozer]

# Логи
log_level = 2

# Предупреждать о том, что Buildozer запущен от root
warn_on_root = 1
