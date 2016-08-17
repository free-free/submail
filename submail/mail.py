# coding=utf-8


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
        'timestamp','sign_type'
    )
        
    def __init__(self, manager, **kwargs):
        super(Mail, self).__init__(manager, **kwargs):
   
    @property
    def req_type(self):
        return 'mail'

 


class MailManager(ServiceManager):


    def request_sender(self, req, method):
        pass
