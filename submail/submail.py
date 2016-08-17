# coding=utf-8


from .sms import SMSManager
from .common import ServiceManager




class submail(object):
   

    @classmethod
    def build(self, srv_name):
        return ServiceManager.resolve_manager(srv_name)

    
