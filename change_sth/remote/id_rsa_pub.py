import sys

from fabric import Connection

from change_sth.remote.decorator import CustomConn

host = '10.1.9.5'
usr = 'root'
pwd = 'jcwl@123'

id_rsa_pub_path = 'C:/Users/26982/.ssh/id_rsa.pub'
conn = Connection(host=host, user=usr, connect_kwargs={
    'password': pwd,
})
cus_conn = CustomConn(conn=conn)

ssh_dir_exist = conn.run('[ -d /root/.ssh ]')
if cus_conn.try_run('[ -d /root/.ssh ]'):
    if cus_conn.try_run('[ -f /root/.ssh/authorized_keys ]'):
        pass
    else:
        cus_conn.try_run('touch authorized_keys')
else:
    cus_conn.try_run('mkdir /root/.ssh')
    cus_conn.try_run('touch authorized_keys')


cus_conn.put(id_rsa_pub_path, '/tmp/id_ras.pub')
cus_conn.try_run('cat /tmp/id_ras.pub >> /root/.ssh/authorized_keys')
