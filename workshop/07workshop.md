# 07workshop




```python
class Circle:
    pi = 3.14
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    
    def area(self):
        return self.pi * self.r * self.r
    
    def circumference(self):
        return 2 * self.pi * self.r
```

```python
c1 = Circle(2, 4, 3)
```

```python
print(c1.circumference)
print(c1.area)
```

```
28.259999999999998
18.84
```

