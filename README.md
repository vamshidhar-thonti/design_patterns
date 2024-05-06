# Design Patterns

## Object Oriented Programming (OOP)

- **Encapsulation** - Gathering all the required data and functionality together in a class. For example Author can be an object that is being in the Book class to refer the Author's information in it. So, the Book class is encapsulated with all the required data and complex functionality from both Author and Book.
- **Inheritance** - Generalizing a class to its basic form with a very generic/common attributes and methods that can be reused to create a new class which inherits everything from its parent. For example Animal is generic class with some attributes and methods. Now a Dog class can inherit the Animal class and still use all the attributes and methods from its parent class Animal.

  - **Interfaces** - Even though python doesn't really have strict interface syntax, we can use ABC, abstract method to implement one.
    - Interfaces creates _contract_ which means the the methods which are decorated with `absractmethod` has to be implemented for sure which it is inherited in the child classes.
    - Interfaces have only abstract methods (doesn't have any implementation)

  ```python
  from abc import ABC, abstractmethod

  class MyInterface(ABC):
      @abstractmethod
      def my_method(self):
          pass // No implementation yet

  class MyClass(MyInterface):
      def my_method(self):
          print("My Method implementation in MyClass")
  ```

  - **Abstract classes** - The classes that can have attributes and can have methods that are actually implemented along with abstract methods. This helps in reusing the classes rather than writing the same code multiple times.

- **Abstraction** - Hiding the functionality on how its implemented and its logic and showing only the method with its parameters to make use of it is Abstraction. It is by default available with all the class based implementations.

- **Ploymorphism** - There are 2 types of polymorphism
  1. Compile-time polymorphism (overloading)
     - Function/methods with same name but has different amount of arguments/parameters is called over loading. Python doesn't support over loading. Even if implemented the interpreter considers only the latest method in the sequence.
  2. Run-time polymorphism (overriding)
     - Implementing the method with same name and signature is over riding. This is acheived in the inheritance - interfaces where we declare abstract methods and implemented those later in the inherited classes.
