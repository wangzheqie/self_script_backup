#!/bin/bash

wget http://ftp.sjtu.edu.cn/ubuntu/pool/universe/u/umbrello/umbrello-dbg_4.13.0-0ubuntu1_amd64.deb
sudo dpkg -i umbrello_4.13.0-0ubuntu1_amd64.deb
sudo apt-get -f install
sudo dpkg -i umbrello_4.13.0-0ubuntu1_amd64.deb
