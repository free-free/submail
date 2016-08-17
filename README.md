##  submail sdk 

[![MIT](https://img.shields.io/dub/l/vibe-d.svg)](LICENSE)


## Enviroment

**python version**: >=3.x

**requirements**: requests,pytest


## TO DO

| submail service  api  |     yes/no     |
|:---------------------:|:--------------:|
|  sms                  |      yes       |
| international sms     |      yes       |
|  mail                 |      no        |
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


## License
[MIT License](LICENSE)
