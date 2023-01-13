import os

os.system('yum -y install python3-pip')
pip_dir = '/root/.pip'
pip_conf_path = '/root/.pip/pip.conf'
download_ori_content = """[global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple
"""
if not os.path.exists(pip_conf_path):
    os.mkdir(pip_dir)
    with open(pip_conf_path, mode='w+')as f:
        f.write(download_ori_content)
else:
    print('ok')

