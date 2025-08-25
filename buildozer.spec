[app]
title = anigye kojo amenlemah's robotics project (mental math duel)
package.name = mathduel
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.2

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.archs = armeabi-v7a,arm64-v8a
android.ndk_path = /usr/local/android-ndk-r23b

# your icon file (place 512x512 PNG at ./icon.png)
icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
bin_dir = bin