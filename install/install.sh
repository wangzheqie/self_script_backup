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
sudo apt-get install -y fcitx-pinyin

################################at last 
#sudo apt-get update 
#sudo apt-get upgrade
#sudo apt autoremove -y
