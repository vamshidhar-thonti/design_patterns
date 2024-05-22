#-----------------------------------------|
#|state      |action     |transaction     |
#|----------------------------------------|
#|Stop       |play       |Play            |
#|----------------------------------------|
#|Play       |pause      |Pause           |
#|           |stop       |Stop            |
#|----------------------------------------|
#|Pause      |play       |Play            |
#|           |stop       |Stop            |
#|----------------------------------------|

class Player:
    def __init__(self):
        self.state = StoppedState()

    def play(self):
        self.state.play(self)

    def stop(self):
        self.state.stop(self)

    def pause(self):
        self.state.pause(self)

class StoppedState:

    def play(self, player: Player):
        player.state = PlayingState()

    def stop(self, player: Player):
        print("Cannot stop with state being Stopped")

    def pause(self, player: Player):
        print("Cannot pause with state being Stopped")

class PlayingState:
    def play(self, player: Player):
        print("Player is already in playing state")

    def stop(self, player: Player):
        player.state = StoppedState()

    def pause(self, player: Player):
        player.state = PausedState()

class PausedState:
    def play(self, player: Player):
        player.state = PlayingState()

    def stop(self, player: Player):
        player.state = StoppedState()

    def pause(self, player: Player):
        print("Player is already in paused state")

player = Player()
print(player.state)
player.play()
print(player.state)
player.stop()
print(player.state)
player.play()
print(player.state)
player.pause()
print(player.state)
player.stop()
print(player.state)
