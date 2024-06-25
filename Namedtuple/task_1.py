from collections import namedtuple
from datetime import datetime

User = namedtuple('User', ['first_name', 'last_name', 'birthday'], defaults=['Иванов', datetime.now()])
u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))
print(u_1)
print(u_1.first_name, u_1.birthday.year)

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
a = Point(2, 3, 4)
b = a._replace(z=0, x=a.x + 4)
print(b)

data = [Point(2, 200, 4), Point(10, -100, -500), Point(3, 7, 11), Point(2, 3, 1)]
print(sorted(data))

# Кейс с неизменяемым типом данных

d = {
    Point(2, 3, 4): 'first',
    Point(10, -100, -500): 'second',
    Point(3, 7, 11): 'last',
}
print(d)
mut_point = Point(2, [3, 4, 5], 6) # <- Стал изменяемым из-за list
print(mut_point)
d.update({mut_point: 'bad_point'}) # TypeError
