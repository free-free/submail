##  submail sdk 

## Enviroment

python version: >=3.x
requirements: requests

## Installation

```sh
$ pip3.x setup install
```

## QuickStarted

### 1. send message

```python
    from submail import MessageManager
    
    # send single  message
    manager = MessageManager()
    msg = manager().message()
    msg['appid'] = 'your submail app id'
    msg['project'] = 'your message template id'
    msg['signature'] = 'your app secret key'
    msg['to'] = 'mobile phone number'
    # variables in your message template
    msg['vars'] = {"var1":"xxxxx","var2":"yyyy"} 
    # send message,return response
    result = msg.send()

```

## License
[MIT License](LICENSE)
