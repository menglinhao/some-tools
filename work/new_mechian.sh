# /bin/bash

yum install -y python39
ln -s /usr/bin/python3.9 /usr/bin/python39
ln -s /usr/bin/python3.9 /usr/bin/python
yum install -y git

repos=(
    https://18539043730:Azby1334@codeup.aliyun.com/616f6e5b65b9775dd591f821/nslb/lbengine-agent.git
    https://18539043730:Azby1334@codeup.aliyun.com/616f6e5b65b9775dd591f821/nslb/go-controller.git
    https://18539043730:Azby1334@codeup.aliyun.com/616f6e5b65b9775dd591f821/nslb/go_healthcheck.git
    https://gitee.com/Hey_friends/some_tools.git 
)
echo $repos
mlh_dir=/root/mlh
mkdir -p $mlh_dir
cd $mlh_dir && \
    for repo in "${repos[@]}"; do
        git clone $repo
    done
    python39 some_tools/install_sth/zsh.py

python39 /root/mlh/some_tools/work/alias.py  # 他娘的天才


# ssh-keygen
# authorized_keys
