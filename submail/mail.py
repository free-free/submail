# coding=utf-8

import json
import copy

import requests

from .common import(
    RequestBase,
    ServiceManager,
    field_checker
)


class Mail(RequestBase):

    __fields__ = (
        'appid', 'signature', 'to',
        'addressbook', 'from', 'from_name',
        'reply', 'cc', 'bcc', 'subject',
        'text', 'html', 'vars', 'links',
        'attachments', 'headers', 'asynchronous',
        'timestamp', 'sign_type', 'tag', 'project'
    )
        
    def __init__(self, manager, **kwargs):
        super(Mail, self).__init__(manager, **kwargs)
 
    @field_checker
    def __setitem__(self, key, value):
         if key in ('to', 'addressbook', 'cc', 'bcc'):
             if key not in self._req_data:
                 self._req_data[key] = []
             self._req_data[key].append(value)
         else:
             self._req_data[key] = value  

    @property
    def req_type(self):
        return 'mail'

    @property
    def req_data(self):
        tmp_data = copy.deepcopy(self._req_data)
        for key in ('to', 'addressbook', 'cc', 'bcc'):
            if key in self._req_data:
                tmp_data[key] = ','.join(tmp_data[key])
        for key in ('vars', 'links', 'headers'):
            if key in self._req_data:
                tmp_data[key] = json.dumps(tmp_data[key])
        return tmp_data
 

class MailRequestSenderBaseMeta(type):
     
    def __init__(cls, name, base, attrs):
        if not hasattr(cls, '_mail_sender'):
            cls._mail_sender = {}
        else:
            name = name.lower()
            cls._mail_sender[name] = cls
        return super().__init__(name, base, attrs)


class MailRequestSenderBase(object, metaclass=MailRequestSenderBaseMeta):
    
    def __init__(self, data=""):
        self._data = data

    @classmethod
    def resolve_sender(cls, sender_name, data=""):
        sender_name = sender_name + 'requestsender'
        sender = None
        try:
            sender = cls._mail_sender.get(sender_name)(data)
        except Exception:
            raise Exception("no such mail sender '%s'" % sender_name)
        return sender
   
    @property
    def data(self):
        return self._data
  
    @data.setter
    def data(self, data):
        self._data = data

    
class MailRequestSender(MailRequestSenderBase):
     
    urls = {
        "send": "https://api.submail.cn/mail/send.json",
        "xsend": "https://api.submail.cn/mail/xsend.json",
    }

    def send(self, stype="send"):
        url = self.urls.get(stype or "send")
        req = requests.post(url, data=self._data)
        return req.json()


class MailManager(ServiceManager):

     
    def mail(self, **kwargs):
        return Mail(self, **kwargs)

    def request_sender(self, req, method):
        return getattr(MailRequestSenderBase.resolve_sender(req.req_type,req.req_data), method)
