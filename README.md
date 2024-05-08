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
- **I**nterface segregation principle - `A derving class from an interface should have only required methods. Any unwanted methods leads to a bulk or fatty interface which violates the principle`. For example, a logger interface has a method called _log_, then if DBLogger and FileLogger are derived from the interface which has to declare different methods that the other derived class doesn't need, violates the principle. To solve it, we can create sub interfaces that derives from the actual one with its custom methods, this approach segregates the interfaces with holding relevant methods.
  - [Refer this example](./SOLID%20Principles%20examples/interface_segregation_principle.py)
- **D**ependeny Inversion principle - `Depend upon abstractions, not concretions`. For example, a manager can supervise different types of employees like developers, testers etc., that doesn't mean that we have to let the Manager class let know the employee type being supervised before hand. Instead we can create a generic Employee class that can be used to create additional employee types and just add to the supervising list whenever needed thus removing the predefined code. [Refer this site](https://www.geeksforgeeks.org/dependecy-inversion-principle-solid/)
  - [Refer this example](./SOLID%20Principles%20examples/dependency_inversion_principle.py)

## Singleton Pattern

- `At any given point of time, a class should have only one instance of it`. When instance of this class types are created it should produce the same common instance. This pattern can be in loggers, DB connections, caching, thread pools etc...

  - The principles of this pattern are:
    1. Ensure the class has only one single instance
    2. Provide global access to this instance
    3. Control how it is instantiated
    4. Any critical part of its code is being entered serially (when threading is used)

- Design considerations:

  1. `lazy construction` which means that create class instance only when its first needed. Or consider `eager loading` which means that singleton instance to be always ready and loaded fast.
  2. `thread safety` - to properlly control the access and lock it accordingly.

- Implementation:

  1. Gang of Four Implementation (classic way):

  ```python
  class ClassicSingleton:
    _instance = None

    def __init__(self):
      # Restricting user from creating new class instances
      raise RuntimeError("Call get_instance() for ClassicSingleton instance")

    @classmethod
    def get_instance(cls):
      if not _instance: # lazy instanstiation
        cls._instance = cls.__new__(cls) # Creating an instance

      return cls._instance

  singleton_instance = ClassicSingleton.get_instance() # getting a singleton instance
  ```

  2. Simple python way of implementation:

  ```python
  class Singleton:
    _instance = None

    def __new__(cls): # Overriding the builtin __new__ method (which creates instances of a class) to return only a single global instance of the class
      if not cls._instance: # lazy instanstiation
        cls._instance = super().__new__(cls)

      return cls._instance

  singleton_instance = Singleton()
  ```

  3. Using metaclass (**_recommended_**):

  - `metaclass` - In Python metaclass is a class that defines the behaviour and rules for creating other classes. These are `classes of classes`. By default, all python classes implicitly inherit from the `type` builtin class which is a metaclass itself. It allows to `customize the class creation process`.

  ```python
  # Lazy instantiation
  class SingletonMeta(type):
    _instances = {} # Store and tracks all the instances.

    def __call__(cls, *args, **kwargs):
      if cls not in _instances: # create an instance only if the dictionary doesn't have an instance existing with the class
        instance = super().__call__(*args, **kwargs)
        cls._instance[cls] = instance

      return cls._instances[cls]

  class Singleton(metaclass=SingletonMeta):
    def some_business_logic():
      pass

  singleton_instance = Singleton() # When instantied, as Singleton inherits the metaclass, the __call__ method of the metaclass will be invoked.
  ```

  ```python
  # Eager loading
  class SingletonMeta(type):
    _instances = {}

    def __init__(cls, name, bases, dct):
      super().__init__(name, bases, dct)
      cls._instaces[cls] = super().__call__()

    def __call__(cls, *args, **kwargs):
      return cls._instances[cls]

  class Singleton(metaclass=SingletonMeta):
    def __init__(self):
      # Initialize attributes here
      pass

  singleton_instance = Singleton() # Even before everything loaded, metclasses load first and an instance will be created.
  ```

4. Thread safe implementation

- When using threads, there a possibility of mutiple threads trying to execute the same function (called race condition) which can lead to unpredicted output. To avoid that scenario we use Lock mechanism where the thread executing the function acquires the lock and releases only when its work is done and made available to the next thread. Once the lock is acquired, rest of the threads will be in the waiting queue.

```python
import threading

class ThreadSafeSingleton:
  _instance = None
  _lock = threading.Lock()

  def __new__(cls):
    with cls._lock: # acquires the lock before creating instance
      if not _instance:
        cls._instance = super().__new__(cls)

      return cls._instance # Releases the lock as the with block end here

singleton_instance = ThreadSafeSingleton()
```
