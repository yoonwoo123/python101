import my_module

my_module.greeting()
my_module.greeting('윤영우')

from my_module import greeting
greeting('아이린')

from my_module import pi as p
print(my_module.pi)

print(p)