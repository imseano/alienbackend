from alien import Alien
import system

class Player:
    def __init__(self, battery, alien: Alien):
        self.name = "Player"
        self.battery = battery
        self.alien = alien

    def send_ask(self, message):
        self.alien.generate_response(message)

    def teach_vocab(self, word):
        self.alien.learn_vocab(word)
