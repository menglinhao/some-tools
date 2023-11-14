# /bin/bash

yum install -y git
mlh_dir=/root/mlh
mkdir -p $mlh_dir
git clone https://gitee.com/Hey_friends/some_tools.git $mlh_dir
cd $mlh_dir && python3 some_tools/install_sth/zsh.py
