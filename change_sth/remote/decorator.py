from fabric import Connection
from loguru import logger


class CustomConn():
    def __init__(self, conn: Connection):
        self.conn = conn

    def try_run(self, cmd):
        try:
            res = self.conn.run(cmd)
            if res.return_code == 0:
                return True, res.stdout
        except Exception:
            logger.error(f'{cmd} 执行失败: {res.stderr}')
            return False, res.stderr

    def put(self, local_file, remote_file):
        self.conn.put(local_file, remote_file)
