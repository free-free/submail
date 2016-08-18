submail sdk 
=============

.. image:: https://img.shields.io/dub/l/vibe-d.svg
  :target: LICENSE
  :align: left
.. image:: https://travis-ci.org/free-free/submail.svg?branch=master
  :target: https://travis-ci.org/free-free/submail
  :align: left


Enviroment
------------

**python version** : >=3.3

**requirements** : requests,pytest


TO DO
--------

.. list-table::
   :widths: 70 30
   :header-rows: 1
    
   * - submail service api
     - yes/no
   * - sms  
     - yes
   * - international sms
     - yes
   * - mail
     - yes
   * - cell phone traffic
     - no
   * - voice
     - no
   * - addressbook
     - no


Installation
---------------

.. code-block:: bash

    $ python3.x setup.py install


or

.. code-block:: bash
    
    $ pip3.x install submail


QuickStarted
------------

sms service
^^^^^^^^^^^

send single message

.. code-block:: python

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


send multi message


.. code-block:: python

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


template opertion

.. code-block:: python

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


log operation

.. code-block:: python

   from submail import submail
   
   manager = submail.build("sms")

   log = manager.log()
   log['appid'] = "your appid"
   log['signature'] = "your appid"
   result = log.get()


mail service
^^^^^^^^^^^^

mail send

.. code-block:: python

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

    
License
-------

`MIT LICENSE <LICENSE>`_
