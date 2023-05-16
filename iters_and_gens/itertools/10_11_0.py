from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

height_groups = groupby(sorted(persons, key=lambda person: person.height), key=lambda person: person.height)
for height, persons in height_groups:
    print(
        f'{height}: ', end=''
    )
    print(
        *[person.name for person in sorted(persons)], sep=', '
    )