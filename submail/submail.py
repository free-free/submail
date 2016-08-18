# coding=utf-8


from .common import ServiceManager
from .sms import SMSManager
from .mail import MailManager



class submail(object):
   

    @classmethod
    def build(self, srv_name):
        return ServiceManager.resolve_manager(srv_name)

    
