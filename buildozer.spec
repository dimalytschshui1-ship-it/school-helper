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

android.api = 35
android.minapi = 21
android.ndk = 28c
android.archs = arm64-v8a

android.permissions = INTERNET,POST_NOTIFICATIONS,VIBRATE

android.enable_androidx = True

android.entrypoint = org.kivy.android.PythonActivity
android.activity_class_name = org.kivy.android.PythonActivity

debug = 0
