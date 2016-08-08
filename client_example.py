
from yaoguang import KeyedValueService
from yaoguang.ttypes import InvalidOperation, Entity

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


class Client(object):
    def __init__(self, address, port):
        transport = TSocket.TSocket(address, port)
        self._transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(self._transport)
        self._client = KeyedValueService.Client(protocol)
        self._transport.open()

    def get_company(self, id):
        try:
            return self._client.get(Entity.COMPANY, id)
        except InvalidOperation, e:
            print e
            return None

    def get_contact(self, id):
        try:
            return self._client.get(Entity.CONTACT, id)
        except InvalidOperation, e:
            print e
            return None
    
    def close(self):
        self._transport.close()


yg = Client('storm01', 9197)
print yg.get_company('111')
print yg.get_contact('222')
yg.close()
