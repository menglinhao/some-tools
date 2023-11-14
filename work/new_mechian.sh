# /bin/bash

yum install -y git
mlh_dir=/root/mlh
mkdir -p $mlh_dir
git clone https://gitee.com/Hey_friends/some_tools.git $mlh_dir
yum install -y python39
ln -s /usr/bin/python3.9 /usr/bin/python39 
cd $mlh_dir && python39 some_tools/install_sth/zsh.py
