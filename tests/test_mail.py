# coding=utf-8

import unittest
import pytest

from submail import submail



class TestMail(unittest.TestCase):

    manager = submail.build('mail')
    appid = 11635
    signature = "7e3faf32a3ca595bc3e81ff121bcad38"
    to_mail = "18281573692@163.com"
    from_mail = "whoami@huzhugc.com"
    from_name = "whoami"
    subject = "hello this is test mail"
    project = "wIrmM3" 
   
    def test_00_mail_build(self):
        mail = self.manager.mail()
        mail['appid'] = self.appid
        mail['signature'] = self.signature
        mail['to'] = self.to_mail
        mail['from']  =self.from_mail
        mail['from_name'] = self.from_name
        mail['subject'] = self.subject
        with self.assertRaises(Exception):
            mail['xxx'] = 21
        fields = ('appid', 'signature', 'to', 'from', 'from_name')
        for field in fields:
            self.assertIn(field, mail.req_data.keys())

    def test_01_mail_send(self):
        mail = self.manager.mail()
        mail['appid'] = self.appid
        mail['signature'] = self.signature
        mail['to'] = self.to_mail
        mail['from']  =self.from_mail
        mail['from_name'] = self.from_name
        mail['subject'] = self.subject
        result = mail.send()
        self.assertEqual(result['status'], 'success')

    def test_02_mail_xsend(self):
        mail = self.manager.mail()
        mail['appid'] = self.appid
        mail['signature'] = self.signature
        mail['to'] = self.to_mail
        mail['from']  =self.from_mail
        mail['from_name'] = self.from_name
        mail['project'] = self.project
        result = mail.send("xsend")
        print(result)
        self.assertEqual(result['status'], 'success')
