
from pathlib import Path
data = """
host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")
alias setproxy="export all_proxy=http://$host_ip:7890;export http_proxy=http://$host_ip:7890;export https_proxy=http://$host_ip:7890;"
alias unsetproxy="unset all_proxy;unset http_proxy;unset https_proxy;"
"""

rc_list = ['/root/.zshrc', '/root/.bashrc']
for rc in rc_list:
    if Path(rc).exists():
        with open(rc, 'a+')as f:
            f.write(data)
