class MyDict(dict):
    """
    A **Python** _dict_ subclass which tries to act like **JavaScript** objects, so you can use the **dot notation** (.) to access members of the object. If the member doesn't exist yet then it's created when you assign something to it. Brackets notation (d['foo']) is also possible.
    """

    def __init__(self, dict_source=None, **kw):
        if dict_source and isinstance(dict_source, (dict, MyDict)):
            for k, v in dict_source.items():
                self[k] = _transform(v)

        for key, value in kw.items():
            self[key] = _transform(value)

    def __getattr__(self, name):
        """
        Get a field "name" from the object in the form:
            obj.name
        """
        if name in self:
            return self[name]
        return None

    def __setattr__(self, name, value):
        """
        Sets a field into the object in the form:
            obj.name = value
        """
        self[name] = _transform(value)

    def __getitem__(self, name):
        """
        Get a field "key" value from the object in the form:
            obj[name]
        """
        return self.get(name)

    def has_path(self, key):
        """
        Check existence of "path" in the tree.

        d = MyDict({'foo': {'bar': 'baz'}})
        d.has_path('foo.bar') == True

        **It only supports "dot-notation" (d.foo.bar)
        """
        if super().__contains__(key):
            return True
        else:
            parts = str(key).split('.')
            if len(parts) > 1:
                k = '.'.join(parts[:1])
                return self[k].has_path('.'.join(parts[1:]))
            else:
                return super().__contains__(key)

    def get(self, key, default=None):
        """
        Returns the value for the given path "key" in the tree of keys, if exists. None if not, or the default value if it's supplied.
        """
        if key in self:
            return super().get(key, default)
        else:
            parts = str(key).split('.')
            if len(parts) > 1:
                try:
                    return self.get(parts[0]).get('.'.join(parts[1:]), default)
                except Exception:
                    return None
            else:
                return super().get(key, default)


def _transform(source):
    if isinstance(source, (dict, MyDict)):
        return MyDict(source)
    elif isinstance(source, list):
        return [item for item in map(_transform, source)]
    elif isinstance(source, tuple):
        result = None
        for item in source:
            if not result:
                result = (_transform(item),)
            else:
                result = result + (_transform(item),)
        return result
    else:
        return source
