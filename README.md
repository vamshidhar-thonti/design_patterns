# Design Patterns

## Object Oriented Programming (OOP)

- **Encapsulation** - Gathering all the required data and functionality together in a class. For example Author can be an object that is being in the Book class to refer the Author's information in it. So, the Book class is encapsulated with all the required data and complex functionality from both Author and Book.
- **Inheritance** - Generalizing a class to its basic form with a very generic/common attributes and methods that can be reused to create a new class which inherits everything from its parent. For example Animal is generic class with some attributes and methods. Now a Dog class can inherit the Animal class and still use all the attributes and methods from its parent class Animal.

  - **Interfaces** - Even though python doesn't really have strict interface syntax, we can use ABC, abstract method to implement one.
    - Interfaces creates _contract_ which means the the methods which are decorated with `absractmethod` has to be implemented for sure which it is inherited in the child classes.
    - Interfaces have only abstract methods (doesn't have any implementation)
    - Instances cannot be created from the interface class, instead those can derived in a new class.

  ```python
  from abc import ABC, abstractmethod

  class MyInterface(ABC):
      @abstractmethod
      def my_method(self):
          pass # No implementation yet

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

## Hallmarks of Good Architecture

- **Loose Coupling** - When an object instance of other class is required and we create it right away in the current class, the current class will be tightly coupled with other class. So, any change made to the other class will effect the current class's object which needs modification. To avoid such issues we make the classes independent by creating interfaces which doesn't create conflicts with the other existing methods.

- **Seperation of Concerns** - Breaking the architecture/system into tiers like `Presentation layer`, `Business/Service layer`, `Data Access layer`. This can achieved by modularisation, encapsulation and arrangement of code in different layers.

- **Law of Demeter (Principle of Least Knowledge)** - Considereing the 3 layered architecture from Seperation of concerns, each layer in the sequence should communicate with the next immediate layer only but not beyond that. For example, Presentation layer should have the knowledge and should communicate only with Service layer but not with the Data Access layer.

## SOLID principles

- **S**ingle Responsibility principle - `Any given class should have only one single responsibility`. For example, a Logger class should implement the code that does logging related functionality only. Or a class thats created for validations should have only validation related code.
  - [Refer this example](./SOLID%20Principles%20examples/single_responsibility_principle.py)
- **O**pen-Closed principle - `Software entities/classes should be open for extension but closed for modification`. For example, if we basic Calculator class is created once and a different calculator is needed (say scientific calculator) the existing calculator should modified, instead a new ScientificCalculator has to extend the basic one.
  - [Refer this example](./SOLID%20Principles%20examples/open-closed_principle.py)
- **L**iskov Substitution principle - `As long as the sub class is substituable by the derived class (base class)`, it satisfies the principle.
  - [Refer this example](./SOLID%20Principles%20examples/liskov_substitution_principle.py)
- **I**nterface segregation principle - `A derving class from an interface should have only required methods. Any unwanted methods leads to a bulk or fatty interface which violates the principle`. For example, a logger interface has a method called _log_, then if DBLogger and FileLogger are derived from the interface which has to declare different methods that the other interface doesn't need violates the principle. To solve it, we can create sub interfaces that derives from the actual one with its custom methods, this approach segregates the interfaces with holding relevant methods.
  - [Refer this example](./SOLID%20Principles%20examples/interface_segregation_principle.py)
- **D**ependeny Inversion principle - `Depend upon abstractions, not concretions`. For example, a manager can supervise different types of employees like developers, testers etc., that doesn't mean that we have to let the Manager class let know the type employee being supervised before hand. Instead we can create a generic Employee class that can be used to create additional employee types and just add to the supervising list whenever needed thus removing the predefined code. [Refer this site](https://www.geeksforgeeks.org/dependecy-inversion-principle-solid/)
  - [Refer this example](./SOLID%20Principles%20examples/dependency_inversion_principle.py)
