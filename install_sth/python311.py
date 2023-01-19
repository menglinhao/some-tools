import os
import subprocess
# https://www.workaround.cz/howto-build-compile-install-latest-python-311-310-39-38-37-centos-7-8-9/
os.system('sudo yum -y update')
os.system('sudo yum -y install wget yum-utils gcc openssl-devel bzip-devel bzip2-devel libffi-devel')

tmp_cwd = '/tmp/'
download = """wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz"""
if not os.path.exists('/tmp/Python-3.11.1.tgz'):
    subprocess.run(download, shell=True, cwd=tmp_cwd)

decompression_python = 'tar xzf Python-3.11.1.tgz'
subprocess.run(decompression_python, shell=True, cwd=tmp_cwd)

python311_cwd = '/tmp/Python-3.11.1/'

configure_cmd = 'sudo ./configure --prefix=/opt/python311 \
--enable-optimizations --with-system-ffi --with-computed-gotos --enable-loadable-sqlite-extensions'
subprocess.run(configure_cmd, shell=True, cwd=python311_cwd)

# """ """ real newline, don't need \n
make_cmd = """sudo make -j "$(nproc)" 
sudo make altinstall
"""
subprocess.run(make_cmd, shell=True, cwd=python311_cwd)

python311_soft_link = 'sudo ln -s /opt/python311/bin/python3.11 /usr/bin/python311'
os.system(python311_soft_link)
