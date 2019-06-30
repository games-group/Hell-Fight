import functools
import types
import sys
import logging.handlers
from abc import ABCMeta


FMT = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d]'
                        '[function:%(funcName)s]'
                        ' - %(levelname)s: %(message)s')
DATEFMT = '%Y %H:%M:%S'
logger = logging.getLogger(__name__)
logging.disable(logging.CRITICAL)


# ************************************Meta Classes****************
def __repr__(self):
    name = self.__class__.__name__
    args = ', '.join(self._args)
    keyword_args = ', '.join(('%s=%r' % (k, v)) for k, v in self._key_args)
    if args and keyword_args:
        return "{name}({args}, {key_args})".format_map(
            {"name": name, "args": args, "key_args": keyword_args})
    else:
        return "{name}({stuff})".format_map(
            {"name": name, "stuff": args or keyword_args})


def __init__(self, *args, **kwds):
    raise NotImplementedError("__init__ of class %s not implemented but "
                              "called with args:%s kwds:%r" %
                              (self.__class__.__name__, args, kwds))


class MyMeta(ABCMeta):
    def __call__(cls, *args, **key_args):
        inst = super().__call__(*args, **key_args)
        inst._args = [repr(i) for i in args]
        inst._key_args = tuple(key_args.items())
        return inst

    def __new__(mcs, class_name, bases, class_dict):
        logger.debug("meta classing %s" % class_name)
        for k in class_dict:
            if not isinstance(class_dict[k], types.FunctionType):
                if k.upper() == k:  # const
                    continue
            if k.lower() != k:
                raise NameError("Bad name: %s" % k)
        class_dict.setdefault("__repr__", __repr__)
        functools.wraps(class_dict.get("__init__", __init__))(mcs.__call__)
        # hack: set the correct call signature
        return super().__new__(mcs, class_name, bases, class_dict)


class Root(metaclass=MyMeta):
    def __init__(self):
        pass


# *******************CONFIG LOGGING****************************
file_handler = logging.handlers.RotatingFileHandler("logs/log.log",
                                                    maxBytes=2048,
                                                    backupCount=5,
                                                    encoding="ascii")
file_handler.setFormatter(FMT)
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(FMT)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)
