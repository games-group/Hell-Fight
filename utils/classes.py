import functools
import types
import logging
from abc import ABCMeta, abstractmethod


logging.basicConfig(level = logging.DEBUG)
logging.disable(logging.CRITICAL)

def __repr__(self):
    name = self.__class__.__name__
    args = ', '.join(self._args)
    keyword_args = ', '.join(('%s=%r' % (k, v)) for k, v in self._key_args)
    if args and keyword_args:
        return "{name}({args}, {key_args})".format_map({"name": name, "args": args, "key_args": keyword_args})
    else:
        return "{name}({stuff})".format_map({"name": name, "stuff": args or keyword_args})


def __init__(self, *args, **kwds):
    raise NotImplementedError("__init__ of class %s not implemented" % self.__class__.__name__)


class MyMeta(ABCMeta):
    def __call__(cls, *args, **key_args):
        inst = super().__call__(*args, **key_args)
        inst._args = [repr(i) for i in args]
        inst._key_args = tuple(key_args.items())
        return inst

    def __new__(mcs, class_name, bases, class_dict):
        logging.debug("metaclassing %s" % class_name)
        for k in class_dict:
            if not isinstance(class_dict[k], types.FunctionType):
                if k.upper() == k:  # const
                    continue
            if k.lower() != k:
                raise NameError("Bad name: %s" % k)
        class_dict.setdefault("__repr__", __repr__)
        functools.wraps(class_dict.get("__init__", __init__))(mcs.__call__)  # hack: set the correct call signature
        return super().__new__(mcs, class_name, bases, class_dict)


class Root(metaclass=MyMeta):
    def __init__(self):
        pass
