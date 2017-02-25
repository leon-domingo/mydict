# coding=utf8

import json


class MyDict(dict):
    """
    A **Python** _dict_ subclass which tries to act like **JavaScript** objects, so you can use the **dot notation** (.) to access members of the object. If the member doesn't exist yet then it's created when you assign something to it. Brackets notation (d['foo']) is also possible.
    """

    def __init__(self, dict_source=None, **kw):
        if dict_source and isinstance(dict_source, (dict, MyDict)):
            for k, v in dict_source.items():
                self[k] = self._transform(v)

        for k, v in kw.items():
            self[k] = self._transform(v)

    def _transform(self, v):
        if isinstance(v, (dict, MyDict)):
            return MyDict(v)

        elif isinstance(v, list):
            return [item for item in map(self._transform, v)]

        elif isinstance(v, tuple):
            v_ = None
            for item in v:

                if isinstance(v, (dict, MyDict)):
                    if not v_:
                        v_ = (MyDict(item),)

                    else:
                        v_ = v_ + (MyDict(item),)

                else:
                    if not v_:
                        v_ = (self._transform(item),)

                    else:
                        v_ = v_ + (self._transform(item),)

            return v_

        else:
            return v

    def __getattr__(self, name):
        """Get a field "name" from the object in the form: obj.name"""
        if name in self:
            return self[name]

    def __setattr__(self, name, value):
        """Sets a field into the object in the form obj.name = value"""
        self[name] = self._transform(value)

    def __getitem__(self, name):
        return self.get(name)

    def get(self, key, default=None):
        parts = str(key).split('.')
        if len(parts) > 1:
            try:
                return self.get(parts[0]).get('.'.join(parts[1:]))

            except:
                return None

        else:
            return super(MyDict, self).get(key, default)

    @staticmethod
    def from_json(s):
        """Returns a "MyDict" instance using a JSON string"""
        d = json.loads(s)
        return MyDict(**d)
