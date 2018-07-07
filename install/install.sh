#!/bin/bash 

#sudo mv /etc/apt/sources.list /etc/apt/sources.list.bk
#sudo cp sources.list /etc/apt/sources.list

#sudo apt-get update 
#sudo apt-get upgrade 

#sudo apt-get install -y git vim cmake gcc g++ libopencv-dev python-dev python3-dev python-pip python3-pip

################################python pip
#pip install --upgrade pip
#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy opencv-python
#mkdir ~/.config/pip
#echo "[global]" >> ~/.config/pip/pip.conf 
#echo "index-url = https://pypi.tuna.tsinghua.edu.cn/simple" >> ~/.config/pip/pip.conf 
#sudo -H pip install --upgrade pip
#sudo apt-get install python-tk 
#sudo -H pip install PyOpenGL PyOpenGL_accelerate
#sudo -H pip install ipython==5.7

################################git 
#git config --global user.email "wangzheqie@qq.com"
#git config --global user.name "Wang Zhe"
#mkdir ~/Git
#cd ~/Git 
#git clone https://github.com/wangzheqie/self_script_backup.git
#cd ~/Git/self_script_backup/install/
#./install.sh
#./update.sh

################################vim
#git clone https://github.com/chxuan/vimplus.git ~/.vimplus
#cd ~/.vimplus
#sudo ./install.sh
cp ../vim/vimplus.vimrc.local ~/.vimrc.local 


################################ibus
#sudo apt-get install -y ibus-pinyin 
#sudo apt-get install -y ibus ibus-clutter ibus-gtk ibus-gtk3 ibus-qt4
#im-switch -s ibus
#sudo apt-get install -y ibus-pinyin
#/usr/lib/ibus/ibus-setup-pinyin
#ibus-setup

################################fcitx 
#sudo apt-get install -y fcitx-pinyin

################################opengl
#sudo apt install -y  libboost-all-dev
#sudo apt install -y  mesa-common-dev
#sudo apt install -y  mesa-utils-extra
#sudo apt install -y  libgl1-mesa-dev
#sudo apt install -y  libglapi-mesa
#sudo apt-get install -y  glew-utils libglew-dev
#sudo apt install -y  libglfw3-dev
#sudo apt-get install -y  libfontconfig1-dev
#sudo apt-get install -y  libgtk-3-dev
#sudo apt-get install -y  libcurl4-openssl-dev

################################at last 
#sudo apt-get update 
#sudo apt-get upgrade
#sudo apt autoremove -y
