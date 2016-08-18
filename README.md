##  submail sdk 

[![MIT](https://img.shields.io/dub/l/vibe-d.svg)](LICENSE)
[![Build Status](https://travis-ci.org/free-free/submail.svg?branch=master)](https://travis-ci.org/free-free/submail)

## Enviroment

**python version**: >=3.3

**requirements**: requests,pytest


## TO DO

| submail service  api  |     yes/no     |
|:---------------------:|:--------------:|
|  sms                  |      yes       |
| international sms     |      yes       |
|  mail                 |      yes       |
|  cell phone traffic   |      no        |
|  voice                |      no        |
|  addressbook          |      no        |



## Installation

```sh
$ pip3.x setup install
```

## QuickStarted

### 1.  sms service

> send single message

```python
    from submail import submail
    
  
    manager = submail.build("sms")
    msg = manager.message()
    msg['appid'] = 'your submail app id'
    msg['project'] = 'your message template id'
    msg['signature'] = 'your app secret key'
    msg['to'] = 'mobile phone number'
    # variables in your message template
    msg['vars'] = {"var1":"xxxxx","var2":"yyyy"} 
    # send message,return response
    result = msg.send(stype="xsend", inter=False)
    
    # send international message
    result = msg.send(stype="xsend", inter=True)

```

> send multi message

```python
    from submail import submail


    manager = submail.build("sms")
    msg = manager.message()
    msg['appid'] = 'your submail app id'
    msg['project'] = 'your message template id'
    msg['signature'] = 'your app secret key'
    msg['multi'] ={"to":"phone number1","vars":{"var1":"2323","vars2":"dede"}}
    msg['multi'] ={"to":"phone number2","vars":{"var1":"2323","vars2":"dede"}}
    # send message,return response
    result = msg.send(stype="multixsend", inter=False)
   
    # send inernational message
    result = msg.send(stype="multixsend", inter=True)

```

> template opertion

```python
   from submail import submail
   
   manager = submail.build("sms")
   
   # create template
   tmpl = manager.template()
   tmpl['appid'] = 'your appid'
   tmpl['signature'] = 'your signature'
   tmpl['sms_signature'] = 'your sms signature'
   tmpl['sms_content'] = 'your sms_content'
   result = tmpl.create()
   
   # get template
   tmpl = manager.template()
   tmpl['appid'] = "your appid"
   tmpl['signature'] = "your signature"
   tmpl['template_id'] = "template id"
   result = tmpl.get()
  
   # update template 
   tmpl = manager.template()
   tmpl['appid'] = 'your appid'
   tmpl['signature'] = 'your signature'
   tmpl['sms_signature'] = 'your sms signature'
   tmpl['sms_content'] = 'your sms_content'
   tmpl['template_id'] = 'template id'
   result = tmpl.update()

   # delete template
   tmpl = manager.template()
   tmpl['appid'] = 'your appid'
   tmpl['signature'] = 'your signature'
   tmpl['template_id'] = 'template id'
   tmpl.delete()

```

> log operation

```python
   from submail import submail
   
   manager = submail.build("sms")

   log = manager.log()
   log['appid'] = "your appid"
   log['signature'] = "your appid"
   result = log.get()

```

### 2. mail service

> mail send

```python

    from submail import submail
   
    manager = submail.build("mail")
    
    # send api
    mail = manager.mail()
    mail['appid'] = "your app id"
    mail["signature"] = "your signature"
    mail["subject"] = "title"
    mail["to"] = "to mail address"
    mail["from"] = "your mail address"
    mail["from_name"] = "your mail address"
    mail.send()

    # xsend api 
    mail = manager.mail()
    mail["appid"] = "your appid"
    mail["signature"] = "your signature"
    mail["project"] = "mail project id"
    mail["to"] = "to mail address"
    mail["from"] = "your mail address"
    mail.send("xsend") 

```
    
## License
[MIT License](LICENSE)
