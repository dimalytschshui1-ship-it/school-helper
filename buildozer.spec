[app]

title = Школьный помощник
package.name = schoolhelper
package.domain = org.schoolhelper

source.dir = .
source.include_exts = py,json,png,jpg,jpeg,kv,atlas

version = 1.0

requirements = python3,kivy,kivymd,plyer

orientation = portrait
fullscreen = 0

# Android
android.api = 35
android.minapi = 21
android.ndk = 28c
android.ndk_api = 21
android.archs = arm64-v8a

# Используем SDK, который уже установлен на GitHub Runner
android.sdk_path = /usr/local/lib/android/sdk

# Используем установленный NDK 28c
android.ndk_path = /usr/local/lib/android/sdk/ndk/28.2.13676358

# НЕ заставляем Buildozer скачивать/обновлять SDK
android.skip_update = True

# Автоматически принимаем лицензии
android.accept_sdk_license = True

android.permissions = INTERNET,POST_NOTIFICATIONS,VIBRATE

android.enable_androidx = True

android.entrypoint = org.kivy.android.PythonActivity
android.activity_class_name = org.kivy.android.PythonActivity

# Используем актуальную ветку python-for-android
p4a.branch = develop

# Python
python_version = 3.10

# Android build
android.add_src =
android.add_aars =
android.add_jars =

[buildozer]

log_level = 2
warn_on_root = 1
