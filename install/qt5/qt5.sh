#!/bin/bash
wget http://download.qt.io/official_releases/qt/5.7/5.7.0/qt-opensource-linux-x64-5.7.0.run 
chmod +x qt-opensource-linux-x64-5.7.0.run
./qt-opensource-linux-x64-5.7.0.run
sudo apt-get install -y build-essential
sudo apt-get install -y libfontconfig1
sudo apt-get install -y mesa-common-dev
sudo apt-get install -y libglu1-mesa-dev 

