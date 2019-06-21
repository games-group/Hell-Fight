import inspect


def __repr__(self):
    name = self.__class__.__name__
    args = ', '.join(self._args)
    keyword_args = ', '.join(('%s=%r' % (k, v)) for k, v in self._kwds)
    if args and keyword_args:
        return "{name}({args}, {key_args})".format_map({"name": name, "args": args, "key_args": keyword_args})
    else:
        return "{name}({stuff})".format_map({"name": name, "stuff": args or keyword_args})


class ReprMeta(type):
    def __call__(cls, *args, **key_args):
        inst = super().__call__(*args, **key_args)
        inst._args = [repr(i) for i in args]
        inst._key_args = tuple(key_args.items())
        return inst

    def __new__(mcs, class_name, bases, class_dict):
        class_dict.setdefault("__repr__", __repr__)
        class_dict.setdefault("__signature__", inspect.signature(class_dict["__init__"]))
        return super().__new__(mcs, class_name, bases, class_dict)


class Root(metaclass=ReprMeta):
    def __init__(self):
        pass
