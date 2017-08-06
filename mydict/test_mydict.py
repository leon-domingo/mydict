# coding=utf8

import decimal
import os
from io import StringIO, BytesIO
from . import MyDict


class TestMyDict:

    def test__access_a_member_with_get(self):

        d = MyDict(foo='bar')
        assert d.get('foo') == 'bar'

    def test__access_a_member_with_get_and_a_path(self):
        """
        d = MyDict(foo={'bar': 'baz'})
        d.get('foo.bar') == 'baz'

        **Only dot notation 'foo.bar.baz'
        **Not supported yet things like: 'foo.bar[0].baz'
        """

        d = MyDict(foo={'bar': 'baz'})
        assert d.get('foo.bar') == 'baz'

    def test__access_a_member_with_get_and_a_path_with_brackets_notation(self):
        """
        d = MyDict(foo={'bar': 'baz'})
        d['foo.bar'] == 'baz'

        **Only dot notation 'foo.bar.baz'
        **Not supported yet things like: 'foo.bar[0].baz'
        """

        d = MyDict(foo={'bar': 'baz'})
        assert d['foo.bar'] == 'baz'

    def test__access_a_key_with_dots(self):
        """Access a key with dots in the name, where those dots don't represent a path"""

        d = MyDict({'foo.bar': 'baz', 'fuu': {'bar': 'baz'}})
        assert d['foo.bar'] == 'baz'
        assert d['fuu.bar'] == 'baz'

    def test__check_precedence_of_a_dotted_field_over_a_path(self):

        d = MyDict({'foo': {'bar': 'baz'}, 'foo.bar': 'BAZ'})

        assert d['foo.bar'] == 'BAZ'
        assert d.get('foo.bar') == 'BAZ'
        assert d.foo.bar == 'baz'

    def test__access_with_brackets_notation(self):
        """
        d = MyDict(foo='bar')
        d['foo'] == 'bar'
        """

        d = MyDict(foo='bar')
        assert d['foo'] == 'bar'

    def test__check_existence_with_in(self):

        d = MyDict(foo='bar')

        assert ('foo' in d) is True
        assert ('baz' in d) is False

    def test__check_path_existence_with_in(self):

        d = MyDict({'foo': {'bar': 'baz'}})

        assert d.has_path('foo') is True
        assert d.has_path('foo.bar') is True

    def test__items_method(self):

        d = MyDict(foo='Hello, MyDict!', bar=123, baz=[1, 2, 3])

        n = 0
        keys = {'foo', 'bar', 'baz'}
        for key, value in d.items():
            keys.remove(key)

            if key == 'foo':
                assert d.foo == 'Hello, MyDict!'

            elif key == 'bar':
                assert d.bar == 123

            elif key == 'baz':
                assert d.baz == [1, 2, 3]

            n += 1

        assert n == 3
        assert len(keys) == 0

    def test__new_member(self):

        d = MyDict()
        d.foo = 'This is a test'

        assert d.foo != None

    def test__non_existing_member(self):

        d = MyDict()
        assert d.foo is None

    def test__replacing_existing_member(self):

        d = MyDict()
        d.foo = 'bar'
        d.foo = 1

        assert d.foo != 'bar'
        assert d.foo == 1

    def test__replace_existing_member_with_object(self):

        d = MyDict()
        d.foo = 'bar'
        d.foo = {'bar': 'baz'}

        assert d.foo != 'bar'
        assert d.foo.bar == 'baz'

    def test__use_underscore_for_name(self):

        d = MyDict()
        d._foo = 'bar'
        d.__baz = 123

        assert d._foo == 'bar'
        assert d.__baz == 123

    def test__assign_str_value(self):

        d = MyDict()
        d.str_value = 'This is a test'

        assert d.str_value == 'This is a test'

    def test__assign_float_value(self):

        d = MyDict()
        d.float_value = 123.45

        assert d.float_value == 123.45

    def test__assign_int_value(self):

        d = MyDict()
        d.int_value = 123

        assert d.int_value == 123

    def test__assign_decimal_value(self):

        d = MyDict()
        d.decimal_value = decimal.Decimal(123)

        assert d.decimal_value == decimal.Decimal('123')

    def test__assign_list_value(self):

        d = MyDict()
        d.list_value = [1, 2, 3]

        assert d.list_value == [1, 2, 3]

    def test__access_a_list(self):

        d = MyDict()
        d.list_value = [1, 2, 3]

        assert d.list_value[1] == 2

    def test__assign_a_complex_list(self):

        d = MyDict()
        d.complex_list = [1, 2, {'foo': 'bar', 'baz': [1, 2, 3]}]

        assert d.complex_list[2].foo == 'bar'
        assert d.complex_list[2].baz[2] == 3

    def test__assign_a_tuple(self):

        d = MyDict()
        d.tuple_value = (1, 2, 3)

        assert d.tuple_value == (1, 2, 3)

    def test__access_a_tuple(self):

        d = MyDict()
        d.t = (1, 2, 3)

        assert d.t[1] == 2

    def test__assign_a_complex_tuple(self):

        d = MyDict()
        d.t = (1, 2, {'foo': 'bar', 'baz': [1, 2, 3]})

        assert d.t[2].foo == 'bar'
        assert d.t[2].baz[2] == 3

    def test__assign_a_dict_value(self):

        d = MyDict()
        d.dict_value = {'foo': 'bar', 'baz': 1}

        assert d.dict_value.foo == 'bar'
        assert d.dict_value.baz == 1

    def test__assign_a_mydict_value(self):

        d = MyDict()
        d.mydict = MyDict({'baz': 1}, foo='bar')

        assert d.mydict.baz == 1
        assert d.mydict.foo == 'bar'

    def test__assign_a_set_value(self):

        d = MyDict()
        d.assign_value = {1, 2, 3}

        assert d.assign_value == {1, 2, 3}

    def test__initialization_with_dict(self):

        d = MyDict({'foo': 'bar', 'baz': [1, 2, 3]})

        assert d.foo == 'bar'
        assert d.baz[2] == 3

    def test__initialization_with_mydict(self):

        d = MyDict(MyDict({'foo': 'bar', 'baz': 123}))
        assert d.foo == 'bar'
        assert d.baz == 123

    def test__initialization_with_keywords(self):

        d = MyDict(foo='bar', baz=1, a=2)

        assert d.foo == 'bar'
        assert d.baz == 1
        assert d.a == 2

    def test__initialization_with_dict_and_keywords(self):

        d = MyDict({'foo': 'bar'}, baz=[1, 2, 3])

        assert d.foo == 'bar'
        assert d.baz[1] == 2

    def test__initialization_with_keywords_overwrite(self):

        d = MyDict({'foo': 'bar'}, foo='BAR')
        assert d.foo == 'BAR'

    def test__complex_initialization(self):

        d = MyDict(foo={'bar': 'baz'}, lst=[1, decimal.Decimal('2.2'), {'foo': 'bar', 'baz': 1}, MyDict(foo='bar')])

        assert d.foo.bar == 'baz'
        assert d.lst[1] == decimal.Decimal('2.2')
        assert d.lst[2].foo == 'bar'
        assert d.lst[2].baz == 1
        assert d.lst[3].foo == 'bar'

    def test__dict_comparison(self):

        d = MyDict(foo='bar', baz=123)

        assert d == {'foo': 'bar', 'baz': 123}

    def test__create_from_json__string(self):

        d = MyDict.from_json('{"foo": "bar", "baz": [1, 2.2, "fuu", {"foo": "bar"}]}')

        assert d.foo == 'bar'
        assert d.baz[0] == 1
        assert d.baz[3].foo == 'bar'

    def test__create_from_json__bytes(self):

        d = MyDict.from_json('{"foo": "bar", "baz": [1, 2.2, "fuu", {"foo": "bar"}]}'.encode('utf8'))

        assert d.foo == 'bar'
        assert d.foo != b'bar'
        assert d.baz[0] == 1
        assert d.baz[3].foo == 'bar'
        assert d.baz[3].foo != b'bar'

    def test__create_from_json_file(self):

        json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test/test.json')

        d = MyDict.from_json(open(json_file, 'r'))

        assert d.foo == 'bar'
        assert d.baz[0] == 1
        assert d.baz[3].foo == 'bar'

    def test__create_from_json_file_b(self):

        json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test/test.json')

        d = MyDict.from_json(open(json_file, 'rb'))

        assert d.foo == 'bar'
        assert d.baz[0] == 1
        assert d.baz[3].foo == 'bar'

    def test__create_from_json_file_like__string(self):

        json_source = StringIO()
        json_source.write('{"foo": "bar", "baz": [1, 2.2, "fuu", {"foo": "bar"}]}')

        d = MyDict.from_json(json_source)

        assert d.foo == 'bar'
        assert d.baz[0] == 1
        assert d.baz[3].foo == 'bar'

    def test__create_from_json_file_like__bytes(self):

        json_source = BytesIO()
        json_source.write('{"foo": "bár", "baz": [1, 2.2, "fuu", {"foo": "bàr"}]}'.encode('utf8'))

        d = MyDict.from_json(json_source)

        assert d.foo == 'bár'
        assert d.baz[0] == 1
        assert d.baz[3].foo == 'bàr'

    def test__to_json(self):

        d = MyDict({'foo': {'bar': 123, 'baz': [1, 2, {'foo': 'bar'}]}})

        assert d.to_json() == '{"foo": {"bar": 123, "baz": [1, 2, {"foo": "bar"}]}}'

    def test__get_dict(self):

        d = MyDict({'foo': {'bar': 123, 'baz': [1, 2, {'foo': 'bar'}]}, 'bar': {'one': 1}})

        d_ = d.get_dict()

        assert d_ == {'foo': {'bar': 123, 'baz': [1, 2, {'foo': 'bar'}]}, 'bar': {'one': 1}} and not issubclass(type(d_), MyDict)

        assert not issubclass(type(d_['bar']), MyDict)
        assert isinstance(d_['bar'], dict)

        assert not issubclass(type(d_['foo']['baz'][2]), MyDict)
        assert isinstance(d_['foo']['baz'][2], dict)
