# MyDict

A **Python** _dict_ subclass which tries to act like **JavaScript** objects, so you can use the **dot notation** (_d.foo_) to access members of the object. If the member doesn't exist yet then it's created when you assign a value to it. Brackets notation (_d['foo']_) is also accepted.

## Installation

```shell
$ pip install mydict
```

## Examples

Let's give it a try

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

We can instantiate it from a _dict_ of any level of complexity

```python
d = MyDict({'foo': 'bar', 'baz': [1, 2, {'foo': 'bar', 'baz': 'Hello, world!'}]})

print(d.foo)
# ==> 'bar'

print(d.baz[0])
# ==> 1

print(d.baz[2].foo)
# ==> 'bar'
```

with keywords in the _constructor_

```python
d = MyDict(a=1, b=2.2, c=[1, 2, 3], d=[{'x': 1, 'y': [100, 200, 300]}])
# ...
d.a == 1
d.b == 2.2
d.c[0] == 1
d.d[0].x == 1
d.d[0].y[1] == 200
```

or both

```python
d = MyDict({'foo': 'bar'}, baz=123)
# ...
d.foo == 'bar'
d.baz == 123
```

Please, take into account that keyword initialization has precedence over the _dict_ (first parameter of the _constructor_)

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

But when those keys _with dots_ exists in the tree they are accessed using the corresponding key

```python
d = MyDict({'foo.bar': 'baz'})
# ...
# 'foo.bar' is not interpreted as a path because the key exists
d['foo.bar'] = 'baz'
```

But there's a particular case, if a _dotted key_ exists and match an existing _path_, then this ain't work properly, or work in a different way depending on the method of access used, to be correct

```python
d = MyDict({'foo': {'bar': 'baz'}, 'foo.bar': 'BAZ'})
# ...
d['foo.bar'] = 'BAZ'  # the "dotted field" ('foo.bar') has precedence over the path
d.foo.bar = 'baz'  # it's not possible to detect a "dotted key" using "dot notation"
```

Personally, I don't see this as a great issue because I generally avoid using dots in keys, like in the previous case

#### Initialization from JSON

It's also possible to load a JSON from _str_, _bytes_, and file-like objects (with a _.read()_ method) using the _static_ method **from_json**:

```python
d = MyDict.from_json('{"foo": "bar"}')
# d.foo == 'bar'

d = MyDict.from_json(b'{"foo": "bar"}')
# d.foo == 'bar'

d = MyDict.from_json(open('/path/to/file.json', 'r'))
# d = MyDict.from_json(open('/path/to/file.json', 'rb')) also work
```

```python
from io import StringIO, BytesIO

s = StringIO()
s.write('{"foo": "bar"}')

d = MyDict.from_json(s)
# d.foo == 'bar'

# ...

b = StringIO()
b.write(b'{"foo": "bar"}')

d = MyDict.from_json(b)
# d.foo == 'bar'
```

The tests passed successfully with **Python 3.6**. With **Python 2.7** fail on "bytes stuff" tests, regarding the use of the static method **from_json()**.

```shell
$ pytest mydict -v
```
