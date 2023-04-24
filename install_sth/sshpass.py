import os

os.system('sudo yum install gcc make automake autoconf libtool openssl-devel')
os.system('cd /tmp; wget https://sourceforge.net/projects/sshpass/files/latest/download -O sshpass.tar.gz')
os.system('tar -xvzf /tmp/sshpass.tar.gz')
os.system('cd /tmp/sshpass-*; ./configure && make && make install')
