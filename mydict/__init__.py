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

        for key, value in kw.items():
            self[key] = self._transform(value)

    def _transform(self, source):
        if isinstance(source, (dict, MyDict)):
            return MyDict(source)

        elif isinstance(source, list):
            return [item for item in map(self._transform, source)]

        elif isinstance(source, tuple):
            result = None
            for item in source:

                if not result:
                    result = (self._transform(item),)

                else:
                    result = result + (self._transform(item),)

            return result

        else:
            # no need for transformation (int, float, str, set, ...)
            return source

    def __getattr__(self, name):
        """Get a field "name" from the object in the form: obj.name"""
        if name in self:
            return self[name]

    def __setattr__(self, name, value):
        """Sets a field into the object in the form obj.name = value"""
        self[name] = self._transform(value)

    def __getitem__(self, name):
        """Get a field "key" value from the object in the form: obj[name]"""
        return self.get(name)

    def get(self, key, default=None):
        if key in self:
            return super(MyDict, self).get(key, default)

        else:
            parts = str(key).split('.')
            if len(parts) > 1:
                try:
                    return self.get(parts[0]).get('.'.join(parts[1:]))

                except:
                    return None

            else:
                return super(MyDict, self).get(key, default)

    @staticmethod
    def from_json(json_string):
        """Returns a "MyDict" instance from a JSON string"""
        json_obj = json.loads(json_string)
        return MyDict(json_obj)
