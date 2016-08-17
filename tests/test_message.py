#coding:utf-8



import unittest
import pytest
import json

from submail import submail


r'''
class MessageTest(unittest.TestCase):
 
    msg_manager = submail.build("sms")
    appid = 11852
    signature = "8dccf3143aeb0b6002c39e5c9ebf26b5"
    to = ["18281573692",]
    var = {"email_name":"163", "email_list":"<18281573692@163.com>,<19941222hb@gmail.com>"}
    project = "ba5Al1"
    inter_to = ["+1778889901"] # international mobile phone number

    def test_00_build_message(self):
        msg = self.msg_manager.message()
        msg['appid'] = self.appid
        msg['signature'] = self.signature
        msg['to'] = self.to[0]
        msg['vars'] = self.var
        msg['project'] = self.project
        with self.assertRaises(Exception):
            msg['multi'] = self.var

        with self.assertRaises(Exception):
            msg['xxx'] = 12
        
        fields = ('appid','signature','to','vars','project')
        for field in fields:
            self.assertIn(field, msg.req_data.keys())

    def test_01_message_xsend(self): 
        msg = self.msg_manager.message()
        msg['appid'] = self.appid
        msg['signature'] = self.signature
        msg['to'] = self.to[0]
        msg['vars'] = self.var
        msg['project'] = self.project
        result = msg.send(stype="xsend", inter=False)
        print(result)
        self.assertEqual(result['status'],'success')
     
    def test_02_message_multixsend(self):
        msg = self.msg_manager.message()
        msg['appid'] = self.appid
        msg['signature'] = self.signature
        msg['multi'] = {"to":self.to[0],"vars":self.var}
        msg['multi'] = {"to":"18048907875","vars":self.var}
        msg['project'] = self.project
        result = msg.send(stype="multixsend", inter=False)
        print(result)
        self.assertEqual(result[0]['status'],'success')
        self.assertEqual(result[1]['status'],'success')
 
    def test_03_message_send(self):
        # I have permission to this API, so I don't test it.
        # TO DO: test it
        pass
    
    def test_04_international_message_xsend(self):
        # I have no international phone number, so I don't test it.
        # TO DO: test it
        pass
   
    def test_05_international_message_multixsend(self):
        # I have no phone number, so I don't test it.
        # TO DO: test it
        pass

    def test_06_international_message_send(self):
        # I have no phone number, so I don't test it.
        # TO DO: test it
        pass
'''

class TemplateTest(unittest.TestCase):
    
    msg_manager = submail.build("sms")
    appid = 11858
    signature = "be72c77ae6720ae08be1e61d516ca0a8"
    sms_signature = "【TEST】"
    sms_content = "Hello master: this is testing @var(msg)"
    template_id = ""
    
    def test_00_build_template(self):
        message = self.msg_manager.template()
        message['appid'] = self.appid
        message['signature'] = self.signature
        message['sms_signature'] = self.sms_signature
        message['sms_content'] = self.sms_content
        with self.assertRaises(Exception):
            message['xxx'] = 12
        fields = ('appid','signature','sms_signature','sms_content')
        for field in fields:
            self.assertIn(field, message.req_data.keys())
       
    def test_01_template_create(self):
        message = self.msg_manager.template()
        message['appid'] = self.appid
        message['signature'] = self.signature
        message['sms_signature'] = self.sms_signature
        message['sms_content'] = self.sms_content
        result = message.create()
        type(self).template_id = result['template_id']
        self.assertEqual(result['status'],'success')
    
    def test_02_template_get(self):
        message = self.msg_manager.template()
        message['appid'] = self.appid
        message['signature'] = self.signature
        message['template_id'] = type(self).template_id
        result = message.get()
        self.assertEqual(result['status'],'success') 

    def test_03_template_update(self):
        message = self.msg_manager.template()
        message['appid'] = self.appid
        message['signature'] = self.signature
        message['sms_signature'] = self.sms_signature
        message['sms_content'] = self.sms_content
        message['template_id'] = type(self).template_id
        result = message.update()
        self.assertEqual(result['status'],'success')

    def test_04_template_delete(self):
        message = self.msg_manager.template()
        message['appid'] = self.appid
        message['signature'] = self.signature
        message['template_id'] = type(self).template_id
        result = message.delete()
        self.assertEqual(result['status'],'success') 


class LogTest(unittest.TestCase):
  
    msg_manager = submail.build("sms")
    appid = 11858
    signature = "be72c77ae6720ae08be1e61d516ca0a8"
    
    def  test_00_build_log(self):
        log = self.msg_manager.log()
        log['appid'] = self.appid
        log['signature'] = self.signature
        with self.assertRaises(Exception):
            log['xxx'] = 21
        for field in ('appid', 'signature'):
            self.assertIn(field, log.req_data.keys())
    
    def test_01_log_get(self):
         
        log = self.msg_manager.log()
        log['appid'] = self.appid
        log['signature'] = self.signature
        result = log.get()
        self.assertEqual(result['status'] ,'success')

if __name__ == '__main__':
    unittest.main()
