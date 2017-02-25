# coding=utf8

import unittest
import decimal
from mydict import MyDict


class MyDictTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__access_a_member_with_get(self):

        d = MyDict(foo='bar')
        self.assertEqual(d.get('foo'), 'bar')

    def test__access_a_member_with_get_and_a_path(self):
        """
        d = MyDict(foo={'bar': 'baz'})
        d.get('foo.bar') == 'baz'

        **Only dot notation 'foo.bar.baz'
        **Not supported yet things like: 'foo.bar[0].baz'
        """

        d = MyDict(foo={'bar': 'baz'})
        self.assertEqual(d.get('foo.bar'), 'baz')

    def test__access_a_member_with_get_and_a_path_with_brackets_notation(self):
        """
        d = MyDict(foo={'bar': 'baz'})
        d['foo.bar'] == 'baz'

        **Only dot notation 'foo.bar.baz'
        **Not supported yet things like: 'foo.bar[0].baz'
        """

        d = MyDict(foo={'bar': 'baz'})
        self.assertEqual(d['foo.bar'], 'baz')

    def test__access_with_brackets_notation(self):
        """
        d = MyDict(foo='bar')
        d['foo'] == 'bar'
        """

        d = MyDict(foo='bar')
        self.assertEqual(d['foo'], 'bar')

    def test__check_existence_with_in(self):

        d = MyDict(foo='bar')

        self.assertTrue('foo' in d)
        self.assertFalse('baz' in d)

    def test__set_a_new_member(self):

        d = MyDict()
        d.foo = 'This is a test'

        self.assertNotEqual(d.foo, None)

    def test__non_existing_member(self):

        d = MyDict()
        self.assertIsNone(d.foo)

    def test__replacing_existing_member(self):

        d = MyDict()
        d.foo = 'bar'
        d.foo = 1

        self.assertNotEqual(d.foo, 'bar')
        self.assertEqual(d.foo, 1)

    def test__replace_existing_member_with_object(self):

        d = MyDict()
        d.foo = 'bar'
        d.foo = {'bar': 'baz'}

        self.assertNotEqual(d.foo, 'bar')
        self.assertEqual(d.foo.bar, 'baz')

    def test__use_underscore_for_name(self):

        d = MyDict()
        d._foo = 'bar'
        d.__baz = 123

        self.assertEqual(d._foo, 'bar')
        self.assertEqual(d.__baz, 123)

    def test__set_str_value(self):

        d = MyDict()
        d.str_value = 'This is a test'

        self.assertEqual(d.str_value, 'This is a test')

    def test__set_float_value(self):

        d = MyDict()
        d.float_value = 123.45

        self.assertEqual(d.float_value, 123.45)

    def test__set_int_value(self):

        d = MyDict()
        d.int_value = 100

        self.assertEqual(d.int_value, 100)

    def test__set_decimal_value(self):

        d = MyDict()
        d.decimal_value = decimal.Decimal(123)

        self.assertEqual(d.decimal_value, decimal.Decimal('123'))

    def test__set_list_value(self):

        d = MyDict()
        d.list_value = [1, 2, 3]

        self.assertEqual(d.list_value, [1, 2, 3])

    def test__access_a_list(self):

        d = MyDict()
        d.list_value = [1, 2, 3]

        self.assertEqual(d.list_value[1], 2)

    def test__set_complex_list(self):

        d = MyDict()
        d.complex_list = [1, 2, {'foo': 'bar', 'baz': [1, 2, 3]}]

        self.assertEqual(d.complex_list[2].foo, 'bar')
        self.assertEqual(d.complex_list[2].baz[2], 3)

    def test__set_tuple_value(self):

        d = MyDict()
        d.tuple_value = (1, 2, 3)

        self.assertEqual(d.tuple_value, (1, 2, 3))

    def test__access_a_tuple(self):

        d = MyDict()
        d.t = (1, 2, 3)

        self.assertEqual(d.t[1], 2)

    def test__set_complex_tuple(self):

        d = MyDict()
        d.t = (1, 2, {'foo': 'bar', 'baz': [1, 2, 3]})

        self.assertEqual(d.t[2].foo, 'bar')
        self.assertEqual(d.t[2].baz[2], 3)

    def test__set_dict_value(self):

        d = MyDict()
        d.dict_value = {'foo': 'bar', 'baz': 1}

        self.assertEqual(d.dict_value.foo, 'bar')
        self.assertEqual(d.dict_value.baz, 1)

    def test__set_mydict_value(self):

        d = MyDict()
        d.mydict = MyDict({'baz': 1}, foo='bar')

        self.assertEqual(d.mydict.baz, 1)
        self.assertEqual(d.mydict.foo, 'bar')

    def test__initialization_with_keywords(self):

        d = MyDict(foo='bar', baz=1, a=2)

        self.assertEqual(d.foo, 'bar')
        self.assertEqual(d.baz, 1)
        self.assertEqual(d.a, 2)

    def test__initialization_with_dict(self):

        d = MyDict({'foo': 'bar', 'baz': [1, 2, 3]})

        self.assertEqual(d.foo, 'bar')
        self.assertEqual(d.baz[2], 3)

    def test__initialization_with_dict_and_keywords(self):

        d = MyDict({'foo': 'bar'}, baz=[1, 2, 3])

        self.assertEqual(d.foo, 'bar')
        self.assertEqual(d.baz[1], 2)

    def test__complex_initialization(self):

        d = MyDict(foo={'bar': 'baz'}, lst=[1, decimal.Decimal('2.2'), {'foo': 'bar', 'baz': 1}, MyDict(foo='bar')])

        self.assertEqual(d.foo.bar, 'baz')
        self.assertEqual(d.lst[1], decimal.Decimal('2.2'))
        self.assertEqual(d.lst[2].foo, 'bar')
        self.assertEqual(d.lst[2].baz, 1)

        self.assertEqual(d.lst[3].foo, 'bar')

    def test__dict_comparison(self):

        d = MyDict(foo='bar', baz=123)

        self.assertEqual(d, {'foo': 'bar', 'baz': 123})

    def test__create_from_json(self):

        d = MyDict.from_json('{"foo": "bar", "baz": [1, 2.2, "baz", {"foo": "bar"}]}')

        self.assertEqual(d.foo, 'bar')
        self.assertEqual(d.baz[0], 1)
        self.assertEqual(d.baz[3].foo, 'bar')


if __name__ == '__main__':
    unittest.main(verbosity=3)
