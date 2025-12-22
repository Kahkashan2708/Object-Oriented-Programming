# Polymorphism in Object-Oriented Programming (OOP)

## 1. What is Polymorphism?

Polymorphism is one of the four fundamental principles of Object-Oriented Programming.
The word *polymorphism* means **“many forms.”**

In OOP, polymorphism allows **the same method or operation to behave differently for different objects**.

In simple terms:
> Polymorphism = One interface, multiple behaviors

---

## 2. Why Polymorphism is Needed

Polymorphism helps to:
- Write flexible and scalable code
- Reduce conditional logic
- Improve code readability
- Allow objects to behave differently using the same method name
- Support dynamic behavior at runtime

---

## 3. Real-World Analogy

Consider a word **“drive”**:
- A person drives a car
- A pilot drives a plane
- A manager drives a team

Same word, different actions — this is polymorphism.

---

## 4. Types of Polymorphism

There are two main types of polymorphism:

1. Compile-Time Polymorphism  
2. Run-Time Polymorphism  

---

## 5. Compile-Time Polymorphism

Compile-time polymorphism is achieved **before program execution**.
It is mainly implemented using:
- Method overloading
- Operator overloading

> Note: Python does not support traditional method overloading like C++ or Java.

---

## 6. Method Overloading (Python Style)

In Python, method overloading is achieved using:
- Default arguments
- Variable-length arguments

Example:
```python
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

