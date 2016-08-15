# -*- coding:utf-8 -*-

import functools
import requests
import json
import copy
from urllib.parse import urlencode
    


class MessageSender(object):
 
    def send(self, msg):
        raise NotImplementedError()


class SimpleMessageSender(MessageSender):
    
    urls = {
        "xsend":"https://api.submail.cn/message/xsend.json",
        "send":"https://api.submail.cn/message/send.json",
        "multixsend":"https://api.submail.cn/message/multixsend.json",
    }
    def __init__(self, send_type="xsend"):
        r"""
        @Args:
             'send','xsend','multixsend'
        """
        assert send_type.lower() in ("send", "xsend", "multixsend")
        self._send_type = send_type

    def send(self, msg):
        url  = self.urls.get(self._send_type)
        req = requests.post(url, data=msg)
        return req.text


class InterMessageSender(MessageSender):
   
    def __init__(self, send_type):
        pass # To DO
 
    def send(self, msg):
        pass # To DO
         

class Message(object):
  
    __slots__ = ('_msg', '_manager')

    __fields__ = ('appid', 'project', 'to',
       'content', 'multi', 'vars','timestamp',
       'signature', 'sign_type')

    def __init__(self, manager, **kwargs):
        self._manager = manager
        self._msg = {}
        for key, value in kwargs.items():
            self.__setitem__(key, value)

    def __getattr__(self, attr):
        if attr == 'send':
            return self._manager.send
        return self._msg.get(attr)
    
    def __delattr__(self, attr):
        if attr in self._msg:
            del self._msg[attr]

    def __contains__(self, key):
        return key in self._msg

    def __setitem__(self, key, value):
        # fuck code, to bad,anyone fix it,please!
        if  key in self.__fields__:
            if key in ("multi", 'vars'):
                if key == 'multi':
                    if 'vars' in self._msg:
                        raise Exception("Can't assign 'multi' and 'vars' simultaneously")
                    if 'multi' not in self._msg:
                        self._msg['multi'] = []
                    self._msg['multi'].append(value)
                if key == 'vars':
                    if 'multi' in self._msg:
                        raise Exception("Can't assign 'multi' and 'vars' simultaneously")
                    self._msg['vars'] = value
            else:
                self._msg[key] = value
        else:
            raise Exception("Key Error,No such '%s' key"  % key)     

    def __getitem__(self, key):
        return self._msg.get(key)
   
    def __delitem__(self, key):
        if key in self._msg:
            del self._msg[key]

    @property
    def raw_body(self):
        return self._msg

    @property
    def body(self):
        tmp_msg = copy.deepcopy(self._msg)
        if 'vars' in self._msg:
            tmp_msg['vars'] = json.dumps(tmp_msg['vars'])
        if 'multi' in self._msg:
            tmp_msg['multi'] = json.dumps(tmp_msg['multi'])
        return tmp_msg
        
    def clear(self):
        del self._msg
        self._msg = {}

        
class MessageManager(object):

    def __init__(self):
        self._message = None
        self._stype = 'xsend'

    def send(self, inter=False): 
        if not self._message:
            raise Exception("no message to sent")
        msg = self._message.body
        if inter:
            return InterMessageSender(self._stype).send(msg)
        else:
            return SimpleMessageSender(self._stype).send(msg)

    def message(self, *, stype="xsend", **kwargs):
        self._stype = stype
        if not self._message:
            self._message = Message(self,**kwargs)
        return self._message
 

if __name__ == '__main__':
    manager = MessageManager()
    msg = manager.message()
    msg['appid'] = 11852
    msg['project'] = "ba5Al1"
    msg["signature"] =  "8dccf3143aeb0b6002c39e5c9ebf26b5"
    msg["to"] = "18281573692"
    msg["vars"] = {"email_name":"163", "email_list":"<18281573692@163.com>,<19941222hb@gmail.com>"}
    print(msg.send())
