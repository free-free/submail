# coding=utf-8

import functools


def field_checker(func):
    @functools.wraps(func)
    def wrapper(self, field_name, value):
        if field_name not in self.req_fields:
            raise Exception("no such request field '%s'" % field_name)
        return func(self, field_name, value)
    return wrapper


class ServiceManagerMeta(type):
    
    def __init__(cls, name, base, attrs):
        if not hasattr(cls, '_srv_manager'):
            cls._srv_manager = {}
        else:
            name = name.lower()
            cls._srv_manager[name] = cls
        return super(ServiceManagerMeta, cls).__init__(
           name, base, attrs)


class ServiceManager(object, metaclass=ServiceManagerMeta):
 
    def request_sender(self, req, method):
        raise NotImplementedError()

    @classmethod
    def resolve_manager(cls, srv_name):
        srv_name = srv_name + 'manager'
        srv_manager = None
        try:
            srv_manager = cls._srv_manager.get(srv_name)()
        except Exception as e:
            print(e)
            raise Exception("submail has no '%s' service" % srv_name)
        return srv_manager 


class RequestBase(object):

    __slots__ = ('_req_data', '_manager')
    # request data all field name tuple
    __fields__ = tuple()

    def __init__(self, manager, **kwargs):
        self._manager = manager
        self._req_data = {}
        for key, value in kwargs.items():
            self.__setitem__(key, value)

    @property
    def req_fields(self):
        return self.__fields__

    @property
    def req_type(self):
        raise NotImplementedError()

    def __getattr__(self, attr):
        return self._manager.request_sender(self, attr)
    
    def __delattr__(self, attr):
        if attr in self._req_data:
            del self._req_data[attr]

    def __contains__(self, key):
        return key in self._req_data
    
    @field_checker
    def __setitem__(self, key, value):
        # write setter rules for every request type
        self._req_data[key] = value

    def __getitem__(self, key):
        return self._req_data.get(key)
   
    def __delitem__(self, key):
        if key in self._req_data:
            del self._req_data[key]

    @property
    def raw_req_data(self):
        # return raw request data
        return self._req_data

    @property
    def req_data(self):
        # return processed request data
        return self._req_data
        
    def clear(self):
        # clear request data
        del self._req_data
        self._req_data = {}
