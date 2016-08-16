##  submail sdk 

## Enviroment

**python version**: >=3.x

**requirements**: requests

## Installation

```sh
$ pip3.x setup install
```

## QuickStarted

### 1. send message

> send single message

```python
    from submail import submail
    
  
    manager = submail.build("message")
    msg = manager.message()
    msg['appid'] = 'your submail app id'
    msg['project'] = 'your message template id'
    msg['signature'] = 'your app secret key'
    msg['to'] = 'mobile phone number'
    # variables in your message template
    msg['vars'] = {"var1":"xxxxx","var2":"yyyy"} 
    # send message,return response
    result = msg.send(stype="xsend", inter=False)

```

> send multi message

```python
    from submail import submail


    manager = submail.build("message")
    msg = manager.message()
    msg['appid'] = 'your submail app id'
    msg['project'] = 'your message template id'
    msg['signature'] = 'your app secret key'
    msg['multi'] ={"to":"phone number1","vars":{"var1":"2323","vars2":"dede"}}
    msg['multi'] ={"to":"phone number2","vars":{"var1":"2323","vars2":"dede"}}
    # send message,return response
    result = msg.send(stype="multixsend", inter=False)

```
## License
[MIT License](LICENSE)
