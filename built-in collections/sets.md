# Set
###### date: 4/11/2020, 7:41:15 AM
---

- Unordered collection of unique elements.
- is mutable. (Elements can be removed and added to the sets)
- elements in a set must be immutable.

```python
  >>> p = {5,324,123,23142123}
  >>> p
  {123, 324, 5, 23142123} #set is unordered
  >>> type(p)
  <class 'set'>
  >>> d = {} #empty curly braces creates a dictionary
  >>> type(d)
  <class 'dict'>
  >>> e = set() #for creating an emty set, use set constructor
  >>> e
  set() #python echos back to us.
```

##### Set constructor can create a set from any iterable series, such as list
PS. Duplicates are discarded

```python
>>> s = set([1,2,3,2,4,3])
>>> s
{1,4,3,2}
```
---
##### Common use of them is efficiently remove duplicate items from a series of objects.

Sets are iterable, but the order is arbitary
```python

```>>> for x in {1,2,4,8,16,32}:
...     print(x)
... 
32
1
2
4
8
16
```
---
#### Membership (```in``` and ```not in```) is fundamental operation for sets:

```python
>>> q= {2,9,6,4,2,4,5,7,8}
>>> q
{2, 4, 5, 6, 7, 8, 9}
>>> 3 in q
False
>>> 2 in q
True
>>> 3 not in q
True

```
---
#### Adding to the set:
Single element:
```python
>>> k = {1,2,3}
>>> k.add(54)
>>> k
{1, 2, 3, 54}
```
PS. Adding element that is already exist has no effect on set, and not produces error.

Multiple elements:
```python
>>> k.update([1,2,4,7,5,4564,3453654,98])
>>> k
{1, 2, 3, 4, 5, 98, 7, 4564, 54, 3453654}
```
---
#### Removing from the set:
1. .remove() --- requires element to be removed is present in the set, or it will throw Key Error is produced.
2. .discard() --- has no effect if element not in the set.

```python
>>> k
{1, 2, 3, 4, 5, 98, 7, 4564, 54, 3453654}
>>> k.remove(2)
>>> k
{1, 3, 4, 5, 98, 7, 4564, 54, 3453654}
>>> k.remove(345678234123)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 345678234123
>>> k.discard(345678234123)
>>> k.discard(3)
>>> k
{1, 4, 5, 98, 7, 4564, 54, 3453654}

```
---
#### Set algebra operations:
![Screenshot from 2020-04-11 08-06-49.png](:storage/baf00a12-4139-44c6-a700-7ab14ccda48e/8f04c11d.png)

```python
>>> group_mates = {"Kamil", "Azer", "Linus","Robert"}
>>> university_people = {"Sahil", "Kamil","Imran"}
>>> group_mates.union(university_people)
{'Sahil', 'Robert', 'Azer', 'Kamil', 'Linus', 'Imran'}
>>> group_mates.difference(university_people)
{'Robert', 'Linus', 'Azer'}
>>> group_mates.intersection(university_people)
{'Kamil'}
>>> group_mates.union(university_people) == university_people.union(group_mates)
True
```