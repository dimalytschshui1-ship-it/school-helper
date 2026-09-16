name: Build APK

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y build-essential git openjdk-17-jdk zlib1g-dev libffi-dev libssl-dev libncurses5-dev libstdc++6 autoconf libtool pkg-config patch

    - name: Accept Android licenses
      run: |
        mkdir -p ~/.android
        echo "y" > ~/.android/repositories.cfg

    - name: Build with Buildozer
      uses: ArtemSBulgakov/buildozer-action@v1
      id: buildozer
      with:
        command: buildozer -v android debug

    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: package
        path: bin/*.apk
