import os
import subprocess

res = subprocess.check_output('cat /etc/os-release', shell=True).decode()

install_tool = 'yum'
if 'Ubuntu' in res:
    install_tool = 'apt'

os.system(f'{install_tool} -y install python3-pip')
pip_dir = '/root/.pip'
pip_conf_path = '/root/.pip/pip.conf'
download_ori_content = """[global]
    index-url = https://pypi.douban.com/simple
    trusted-host = https://pypi.douban.com/simple
"""
# index-url = https://pypi.tuna.tsinghua.edu.cn/simple
if not os.path.exists(pip_conf_path):
    os.mkdir(pip_dir)
    with open(pip_conf_path, mode='w+')as f:
        f.write(download_ori_content)
else:
    print('change pip ok')

