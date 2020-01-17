# class Connection:
#     """普通方案，好多个判断语句，效率低下~~"""
#
#     def __init__(self):
#         self.state = 'CLOSED'
#
#     def read(self):
#         if self.state != 'OPEN':
#             raise RuntimeError('Not open')
#         print('reading')
#
#     def write(self, data):
#         if self.state != 'OPEN':
#             raise RuntimeError('Not open')
#         print('writing')
#
#     def open(self):
#         if self.state == 'OPEN':
#             raise RuntimeError('Already open')
#         self.state = 'OPEN'
#
#     def close(self):
#         if self.state == 'CLOSED':
#             raise RuntimeError('Already closed')
#         self.state = 'CLOSED'


class Connection(object):

    def __init__(self):
        self._new_state(ClosedState)
    def _new_state(self, stat):
        self._stat = stat

    def open(self):
        self._stat.open(self)
    def close(self):
        self._stat.close(self)
    def read(self):
        self._stat.read(self)
    def write(self):
        self._stat.write(self)


class ConnectionState:
    """
    定义一个虚类  明确要提供接口
    """
    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()


class ClosedState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')

    @staticmethod
    def open(conn):
        conn._new_state(OpenedState)  # 改变状态

    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')

class OpenedState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')

    @staticmethod
    def write(conn, data):
        print('writing')

    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')

    @staticmethod
    def close(conn):
        conn._new_state(ClosedState)


if __name__ == '__main__':
    c = Connection()
    # c.read()
    c.open()
    c.read()