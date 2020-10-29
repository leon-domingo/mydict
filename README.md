# MyDict

> Version 2.X is a breaking-API step regarding the functions that transforms the MyDict object into/from something else. Those methods have been moved to another module: mydict.jsonify. Everything else remains the same, and Python 2.X is totally discouraged at this point.

A **Python** _dict_ subclass which tries to act like **JavaScript** objects, so you can use the **dot notation** (_d.foo_) to access members of the object. If the member doesn't exist yet then it's created when you assign a value to it. Brackets notation (_d['foo']_) is also accepted.

## Installation

```shell
$ pip install mydict
```

## Examples

Let's give it a try.

```python
d = MyDict()
d.foo = 'bar'

print(d.foo)
# ==> 'bar'
```

If you try to get the value of a non-existing member then a _None_ value is returned

```python
d = MyDict()
if d.foo is None:
    print('"foo" does not exist yet!')
```

If that value is "complex" (a _dict_ or another _MyDict_ instance), then it's also **recursively** transformed into a _MyDict_ object, so you can access it in the same way

```python
d = MyDict()
d.foo = {'bar': 'baz', 'lst': [{'a': 123}]}

print(d.foo.bar)
# ==> 'baz'

print(d.foo.lst[0].a)
# ==> 123
```

Values in lists are accessed, as you expect, with the brackets notation (_d[0]_):

```python
d = MyDict()
d.foo = [1, 2, 3]

print(d.foo[2])
# ==> 3
```

We can instantiate it from a _dict_ of any level of complexity:

```python
d = MyDict({'foo': 'bar', 'baz': [1, 2, {'foo': 'bar', 'baz': 'Hello, world!'}]})

print(d.foo)
# ==> 'bar'

print(d.baz[0])
# ==> 1

print(d.baz[2].foo)
# ==> 'bar'
```

with keywords in the _constructor_:

```python
d = MyDict(a=1, b=2.2, c=[1, 2, 3], d=[{'x': 1, 'y': [100, 200, 300]}])
# ...
d.a == 1
d.b == 2.2
d.c[0] == 1
d.d[0].x == 1
d.d[0].y[1] == 200
```

or both:

```python
d = MyDict({'foo': 'bar'}, baz=123)
# ...
d.foo == 'bar'
d.baz == 123
```

Please, take into account that keyword initialization has precedence over the _dict_ (first parameter of the _constructor_):

```python
d = MyDict({'foo': 'bar'}, foo='BAR')
# ...
d.foo == 'BAR'
```

It's also possible to access members using a _path_ with **get** or _brackets notation_ (_d['...']_):

```python
d = MyDict(foo={'bar': 'baz'})
# ...
d['foo.bar'] == 'baz'
d.get('foo.bar') == 'baz'
```

But when those keys _with dots_ exists in the tree they are accessed using the corresponding key:

```python
d = MyDict({'foo.bar': 'baz'})
# ...
# 'foo.bar' is not interpreted as a path because the key exists
d['foo.bar'] = 'baz'
```

But there's a particular case, if a _dotted key_ exists and match an existing _path_, then this ain't work properly, or work in a different way depending on the method of access used, to be correct:

```python
d = MyDict({'foo': {'bar': 'baz'}, 'foo.bar': 'BAZ'})
# ...
d['foo.bar'] = 'BAZ'  # the "dotted field" ('foo.bar') has precedence over the path
d.foo.bar = 'baz'  # it's not possible to detect a "dotted key" using "dot notation"
```

Personally, I don't see this as a great issue because I generally avoid using dots in keys, like in the previous case.

#### Transformation

You have at your disposal a couple of functions to retrieve the **MyDict** object transformed into _something else_. For the **version 2** the original methods (to_json, from_json, get_dict) have been moved to another module: *mydict.jsonify*.

##### Types of case

The available types of case are:
 - *mydict.SNAKE_CASE* : *snake_case*
 - *mydict.CAMEL_CASE* : *camelCase*
 - *mydict.PASCAL_CASE* : *PascalCase*

More on this later on.

##### mydict.jsonify.to_json

Returns the **MyDict** object as a _JSON_ string (_str_):

```python
d = MyDict(foo="bar", arr=[1, 2, {"three": 3}])
mydict.jsonify.to_json(d)
# '{"foo": "bar", "arr": [1, 2, {"three": 3}]}'
```

In addition, it's also possible to handle the _case type_ of the keys inside the object. For example, we can use *snake_case* in **MyDict** object and then "export" it with those keys in *camelCase*. Let's see it in action:

```python
d = MyDict(my_foo='bar', my_arr=[1, 2, {"other_key": 3}])
mydict.jsonify.to_json(d, case_type=mydict.CAMEL_CASE)
# '{"myFoo": "bar", "myArr": [1, 2, {"otherKey": 3}]}'
```

##### mydict.jsonify.get_dict

In some occasions you'll need a _plain old_ Python _dict_ representation of the **MyDict** object, though is a _dict_ subclass:

```python
d = MyDict(foo="bar", arr=[{"one": 1}, {"two": 2}])
mydict.jsonify.get_dict(d)
# {'foo': 'bar', 'arr': [{'one': 1}, {'two': 2}]}
```

In addition, it's also possible to handle the **case type** of the keys inside the object, in the same way **to_json** works. For example, we can use *snake_case* in **MyDict** object and then "export" it with those keys in *camelCase*. Let's see it in action:

```python
d = MyDict(my_foo='bar', my_arr=[1, 2, {"other_key": 3}])
mydict.jsonify.get_dict(d, case_type=mydict.CAMEL_CASE)
# {'myArr': [1, 2, {'otherKey': 3}], 'myFoo': 'bar'}
```

#### Initialization from JSON

It's also possible to load a JSON from _str_, _bytes_, and file-like objects (with a _.read()_ method) using the function **mydict.jsonify.from_json**:

```python
d = mydict.jsonify.from_json('{"foo": "bar"}')
# d.foo == 'bar'

d = mydict.jsonify.from_json(b'{"foo": "bar"}')
# d.foo == 'bar'

d = mydict.jsonify.from_json(open('/path/to/file.json', 'r'))
# d = mydict.jsonify.from_json(open('/path/to/file.json', 'rb')) also works
```

```python
from io import StringIO, BytesIO

s = StringIO()
s.write('{"foo": "bar"}')

d_from_s = mydict.jsonify.from_json(s)
# d_from_s.foo == 'bar'

b = BytesIO()
b.write(b'{"foo": "bar"}')
# b.write('{"foo": "bar"}'.encode('utf8')) is equivalent

d_from_b = mydict.jsonify.from_json(b)
# d_from_b.foo == 'bar'
```

Please, notice whether the _source_ is string or bytes the result is always *string*.

In addition, there's also a param *case_type* in the **from_json** function. It works in the same way we previously mentioned for **to_json** and **get_dict**. For example:

```python
d = mydict.jsonify.from_json('{"myFoo": "bar", "myArr": [1, 2, {"otherKey": 3}]}', case_type=mydict.SNAKE_CASE)
# d.my_foo == 'bar'
# d.my_arr == [1, 2, {'other_key': 3}]
# d.my_arr[2].other_key == 3
```

Very useful when we collect data from an API which uses _camelCase_ for its keys but we want a more _pythonic_ way for those keys.

The tests passed successfully with **Python 3.6**. **Python 2.X** is totally discouraged at this stage of the library. We recommend using **Python +3.X**

```shell
$ pip install pytest
$ pytest mydict -v
```
