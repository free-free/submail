# coding=utf-8


from .message import MessageManager




class submail(object):
    
    _srv_manager = {
        'message':MessageManager
    }

    @classmethod
    def build(self, service):
        if service not in self._srv_manager:
            raise Exception("submail no such service")
        return self._srv_manager.get(service)()

    
