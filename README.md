# MyDict

A **Python** _dict_ subclass which tries to act like **JavaScript** objects, so you can use the **dot notation** (_d.foo_) to access members of the object. If the member doesn't exist yet then it's created when you assign a value to it. Brackets notation (_d['foo']_) is also possible.

    d = MyDict()
    d.foo = 'bar'

    print(d.foo)
    # ==> 'bar'

If you try to get the value of a non-existing member then a _None_ value is returned

    d = MyDict()
    if d.foo is None:
        print('"foo" does not exist yet!')

If that value is "complex" (a _dict_ or another _MyDict_ instance), then it's also **recursively** transformed into a _MyDict_ object, so you can access it in the same way

    d = MyDict()
    d.foo = {'bar': 'baz', 'lst': [{'a': 123}]}

    print(d.foo.bar)
    # ==> 'baz'

    print(d.foo.bar)
    # ==> 'baz'

    print(d.foo.lst[0].a)
    # ==> 123

Values in lists are accessed, as you expect, with the brackets notation (_d[0]_):

    d = MyDict()
    d.foo = [1, 2, 3]

    print(d.foo[2])
    # ==> 3

We can instantiate it from a _dict_ of any level of complexity

    d = MyDict({'foo': 'bar', 'baz': [1, 2, {'foo': 'bar', 'baz': 'Hello, world!'}}])

    print(d.foo)
    # ==> 'bar'

    print(d.baz[0])
    # ==> 1

    print(d.baz[2].foo)
    # ==> 'bar'

with keywords in the _constructor_

    d = MyDict(a=1, b=2.2, c=[1, 2, 3], d=[{'x': 1, 'y': [100, 200, 300]}])
    ...
    d.a == 1
    d.b == 2.2
    d.c[0] == 1
    d.d[0].x == 1
    d.d[0].y[1] == 200

or both

    d = MyDict({'foo': 'bar'}, baz=123)
    ...
    d.foo == 'bar'
    d.baz == 123

It's also possible to access members using a _path_ with **get** or _brackets notation_ (_d['...']_):

    d = MyDict(foo={'bar': 'baz'})
    ...
    d['foo.bar'] == 'baz'
    d.get('foo.bar') == 'baz'

The tests passed successfully with **Python 3.6** and **Python 2.7** versions.
