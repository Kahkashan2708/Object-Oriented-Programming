## Hierarchical Inheritance

Hierarchical inheritance occurs when multiple child classes inherit from the same parent class.

```python
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

class Cat(Animal):
    pass
```
