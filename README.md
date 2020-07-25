# stateful
Trying to implement "stateful" objects in python

I had a thought today; what if we had object types in python. By stateful, I mean an object that retains its previous values (states) as it changes, and I set out to do a little implementation. 
N.B.: I fully acknowledge the "pythonic" philosophy of simplicity, this is just an experiment I thought would be fun, having said that; If you know of any other data types I can add to this, please feel free to let me know or add to the repo

#Usage

```
a = 2
a = _(a)
a = _(392, a)
a = _([2,3,4,5,6], a)
a = _(None, a)
a = _("foo", a)
a = _(2.0, a)
a = _({
	"foo": 1,
	"bar": 2,
	}, a)
a = _(tuple("foobar1"), a)

print(a.states)
print(a.states[-1].state)
print(type(a))
a.switch(set)
print(a.state)
a.switch(list)
print(a.state)
```

```
#output
[2, 392, [2, 3, 4, 5, 6], 'None', 'foo', 2.0, {'foo': 1, 'bar': 2}, ('f', 'o', 'o', 'b', 'a', 'r', '1')]
('f', 'o', 'o', 'b', 'a', 'r', '1')
<class 'states.StatefulTuple'>
{'a', 'b', 'f', '1', 'o', 'r'}
['f', 'o', 'o', 'b', 'a', 'r', '1']



[Finished in 0.2s]
```
