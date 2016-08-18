# -*- coding:utf-8 -*-

import requests
import copy
from urllib.parse import urlencode

from .common import (
    RequestBase,
    ServiceManager,
    field_checker
)    

         
class Message(RequestBase):
  

    __fields__ = ('appid', 'project', 'to',
       'content', 'multi', 'vars','timestamp',
       'signature', 'sign_type')

    def __init__(self, manager, **kwargs):
        super(Message, self).__init__(manager, **kwargs)

    @property
    def req_type(self):
        return 'message'

    @field_checker
    def __setitem__(self, key, value):
        # fuck code, to bad,anyone fix it,please!
        if key in ("multi", 'vars'):
            if key == 'multi':
                if 'vars' in self._req_data:
                    raise Exception("Can't assign 'multi' and 'vars' simultaneously")
                if 'multi' not in self._req_data:
                    self._req_data['multi'] = []
                self._req_data['multi'].append(value)
            if key == 'vars':
                if 'multi' in self._req_data:
                    raise Exception("Can't assign 'multi' and 'vars' simultaneously")
                self._req_data['vars'] = value
        else:
            self._req_data[key] = value

    @property
    def req_data(self):
        tmp_msg = copy.deepcopy(self.raw_req_data)
        if 'vars' in self.raw_req_data:
            tmp_msg['vars'] = json.dumps(tmp_msg['vars'])
        if 'multi' in self.raw_req_data:
            tmp_msg['multi'] = json.dumps(tmp_msg['multi'])
        return tmp_msg
        

class Template(RequestBase):
    
    __fields__ = (
       'appid', 'template_id', 'timestamp',
       'sign_type', 'signature', 'sms_title', 
       'sms_signature','sms_content'
    )
  
    def __init__(self, manager, **kwargs):
        super(Template, self).__init__(manager, **kwargs)
   
    @property
    def req_type(self):
        return 'template'


class Log(RequestBase):
    
    __fields__ = (
        'appid', 'signature', 'recipient',
        'project' ,'result_status', 'start_date',
        'end_date', 'order_by' ,'rows', 'offset',
        'timestamp', 'sign_type'
    )
  
    def __init__(self, manager, **kwargs):
        super(Log, self).__init__(manager, **kwargs)

    @property
    def req_type(self):
        return 'log'


class SMSRequestSenderMeta(type):

    def __init__(cls, name, base, attrs):
        if not hasattr(cls,'_sms_request_sender'):
            cls._sms_request_sender = {}
        else:
            name = name.lower()
            cls._sms_request_sender[name] = cls
        return super(SMSRequestSenderMeta, cls).__init__(name, base, attrs)


class SMSRequestSender(object, metaclass=SMSRequestSenderMeta):

    def __init__(self, data=""):
        self._data = data

    @classmethod
    def resolve_sender(cls, sender_name, data=""):
        sender_name = sender_name.lower() + 'requestsender'
        sender = None
        try:
            sender = cls._sms_request_sender.get(sender_name)(data)
        except Exception:
            raise Exception("no definition for '5s' sender" % send_name)
        return sender

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data


class TemplateRequestSender(SMSRequestSender):
       
    url = "https://api.submail.cn/message/template.json"
    
    def get(self):
        req = requests.get(self.url, params=self._data)
        return req.json()
    
    def create(self):
        req = requests.post(self.url, data=self._data)
        return req.json()

    def update(self):
        req = requests.put(self.url, data=self._data)
        return req.json()

    def delete(self):
        req = requests.delete(self.url, data=self._data)
        return req.json()         
     
        
class MessageSender(object):

    urls = {
        "xsend":"",
        "multixsend":"",
        "send":"",
    }

    def __init__(self, send_type="xsend"):
        r"""
        @Args:
             'send','xsend','multixsend'
        """
        assert send_type.lower() in ("send", "xsend", "multixsend")
        self._send_type = send_type

    def send(self, data):
        url  = self.urls.get(self._send_type)
        req = requests.post(url, data=data)
        return req.json()


class SimpleMessageSender(MessageSender):
    
    urls = {
        "xsend":"https://api.submail.cn/message/xsend.json",
        "send":"https://api.submail.cn/message/send.json",
        "multixsend":"https://api.submail.cn/message/multixsend.json",
    }


class InterMessageSender(MessageSender):

    urls = {
        "xsend":"https://api.submail.cn/internationalsms/xsend.json",
        "send":"https://api.submail.cn/internationalsms/send.json",
        "multixsend":"https://api.submail.cn/internationalsms/multixsend.json",
    }
    

class MessageRequestSender(SMSRequestSender):
 
    def send(self, *, stype="xsend", inter=False): 
        r"""
            send message 
            @Args:
                stype: str, send type ('xsend','multixsend','send')
                inter: boolean, international sms send
            @Returns:
                response 
        """
        if inter:
            return InterMessageSender(stype).send(self._data)
        else:
            return SimpleMessageSender(stype).send(self._data)


class LogRequestSender(SMSRequestSender):
 
    url = "https://api.submail.cn/log/message.json"

    def get(self):
        req = requests.post(self.url, data=self._data)
        return req.json()        


class SMSManager(ServiceManager):
   
    def __init__(self):
        self._message = None

    def message(self, **kwargs):
        self._message = Message(self, **kwargs)
        return self._message
    
    def template(self, **kwargs):
        return Template(self , **kwargs)

    def log(self, **kwargs):
        return Log(self, **kwargs) 

    def request_sender(self, req, method):
        return getattr(SMSRequestSender.resolve_sender(req.req_type, req.req_data), method)
   

