[app]

# (str) Title of your applicationr
title = Jamui AI App

# (str) Package name
package.name = jamuiaiapp

# (str) Package domain (needed for android packaging)
package.domain = org.jamui

# (list) Source files to include (let it include python files and assets)
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (list) Application requirements
requirements = python3,kivy,requests,certifi,urllib3,idna,charset-normalizer

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android arch to build for
android.archs = arm64-v8a,armeabi-v7a

# (bool) Enable/disable auto-acceptance of the sdk license
android.accept_sdk_license = True
