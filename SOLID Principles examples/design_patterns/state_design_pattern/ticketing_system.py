from abc import ABC, abstractmethod

#-----------------------------------------|
#|state      |action     |transaction     |
#|----------------------------------------|
#|New        |assign     |Assigned        |
#|           |close      |Closed          |
#|----------------------------------------|
#|Assigned   |resolve    |Resolved        |
#|----------------------------------------|
#|Resolved   |close      |Closed          |
#|           |re-assign  |Assigned        |
#|----------------------------------------|
#|Closed     |No-op      |End of Operation|
#|----------------------------------------|

# Step 1: Define the abstract base class TicketState
class TicketState(ABC):

    @abstractmethod
    def assign(self, ticket):
        pass

    @abstractmethod
    def resolve(self, ticket):
        pass

    @abstractmethod
    def close(self, ticket):
        pass

# Step 2: Implement the concrete state classes
class NewState(TicketState):

    def assign(self, ticket: 'Ticket'):
        # Implement the behavior for assigning a new ticket
        if ticket.state.__class__.__name__ == "NewState":
            ticket.state = AssignedState()
            print("Ticket has been assigned")
        else:
            print("Invalid state")

    def resolve(self, ticket: 'Ticket'):
        # Implement the behavior for resolving a new ticket
        print("Ticket cannot be resolved without assigning")

    def close(self, ticket: 'Ticket'):
        # Implement the behavior for closing a new ticket
        if ticket.state.__class__.__name__ == "NewState":
            ticket.state = ClosedState()
            print("Ticket has been closed")
        else:
            print("Invalid state")

# Implement the other concrete state classes: AssignedState, ResolvedState, and ClosedState
class AssignedState(TicketState):

    def assign(self, ticket: 'Ticket'):
        # Implement the behavior for assigning a new ticket
        print("Ticket has been already assigned")

    def resolve(self, ticket: 'Ticket'):
        # Implement the behavior for resolving a new ticket
        if ticket.state.__class__.__name__ == "AssignedState":
            ticket.state = ResolvedState()
            print("Ticket has been resolved")
        else:
            print("Invalid state")

    def close(self, ticket: 'Ticket'):
        # Implement the behavior for closing a new ticket
        print("Please resolve the ticket before closing")

class ResolvedState(TicketState):

    def assign(self, ticket: 'Ticket'):
        # Implement the behavior for assigning a new ticket
        if ticket.state.__class__.__name__ == "ResolvedState":
            ticket.state = AssignedState()
            print("Ticket has been re-assigned")
        else:
            print("Invalid state")

    def resolve(self, ticket: 'Ticket'):
        # Implement the behavior for resolving a new ticket
        print("Ticket has been already resolved")

    def close(self, ticket: 'Ticket'):
        # Implement the behavior for closing a new ticket
        if ticket.state.__class__.__name__ == "ResolvedState":
            ticket.state = ClosedState()
            print("Ticket has been closed")
        else:
            print("Invalid state")

class ClosedState(TicketState):

    def assign(self, ticket: 'Ticket'):
        # Implement the behavior for assigning a new ticket
        print("Please create a new ticket")

    def resolve(self, ticket: 'Ticket'):
        # Implement the behavior for resolving a new ticket
        print("Ticket has been already closed")

    def close(self, ticket: 'Ticket'):
        # Implement the behavior for closing a new ticket
        print("Ticket has been already closed")

# Step 3: Implement the Ticket class
class Ticket:

    def __init__(self):
        # Initialize the ticket's state attribute with an instance of the NewState class
        self.state = NewState()

    def assign(self):
        # Delegate the assign method call to the current state object
        self.state.assign(self)

    def resolve(self):
        # Delegate the resolve method call to the current state object
        self.state.resolve(self)

    def close(self):
        # Delegate the close method call to the current state object
        self.state.close(self)

# Step 4: Test the behavior of the ticket and its state transitions
def main():
    ticket = Ticket()

    # Test the initial state and transitions
    ticket.assign()
    ticket.resolve()
    ticket.close()

    # Test invalid transitions
    ticket.assign()
    ticket.resolve()

if __name__ == "__main__":
    main()
