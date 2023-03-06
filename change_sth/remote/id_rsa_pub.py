from fabric import Connection

host = '10.1.9.5'
usr = 'root'
pwd = 'jcwl@123'
with Connection(host=host, user=usr, connect_kwargs={
    'password': pwd,
}) as conn:
    conn.put('')
    conn.run('ls')
