[app]

# (str) Title of your application
title = Помощник по школе

# (str) Package name
package.name = schoolhelper

# (str) Package domain (needed for android packaging)
package.domain = org.school

# (str) Source files where the let it be (relative to directory of spec)
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions
#source.include_patterns = assets/*,images/*.png

# (list) List of exclusions
#source.exclude_exts = spec

# (list) List of directory to exclude
#source.exclude_dirs = tests, bin

# (list) List of exclusions in source files
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd

# (str) Custom source folders for requirements
#requirements.source.dirname =

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 27.3.13750724

# (bool) Use --private data storage (True) or public data storage (False)
#android.private_storage = True

# (str) Android orientation (portrait, landscape, sensor or all)
orientation = portrait

# (bool) Indicate whether the application should be full screen or not
fullscreen = 0

# (list) The android archs to build for,, can be: arm64-v8a, armeabi-v7a, x86, x86_64
android.archs = arm64-v8a

# (bool) Enables Android auto backup feature (Android API >= 23)
android.allow_backup = True

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1
