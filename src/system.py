import os
import json
from alien import Alien
from player import Player
from llmclient import Cerebras

SESSIONS_DIR = "sessions"

class System:
    def __init__(self, known_words, personality, motive, stress, history=[], remaining_bat=100):
        self.known_words = known_words
        self.personality = personality
        self.motive = motive
        self.stress = stress
        self.history = history
        self.remaining_bat = remaining_bat

        self.alien = Alien(self.known_words, self.personality, self.motive, Cerebras().client)
        self.player = Player(self.remaining_bat, self.alien)



    def add_history(self, message):
        self.history.append(message)

    def to_dict(self):
        return {
            "known_words": self.known_words,
            "personality": self.personality,
            "motive": self.motive,
            "stress": self.stress,
            "history": self.history,
            "remaining_bat": self.remaining_bat
        }

    @classmethod
    def from_dict(cls, data):
        system = cls(
            known_words=data.get("known_words", []),
            personality=data.get("personality", "neutral"),
            motive=data.get("motive", "unknown"),
            stress=data.get("stress", 0.0),
            remaining_bat=data.get("remaining_bat", 100)
        )
        system.history = data.get("history", [])
        return system


    def save_to_json(self, session_id):
        os.makedirs(SESSIONS_DIR, exist_ok=True)
        file_path = get_session_file(session_id)
        with open(file_path, "w") as f:
            json.dump(self.to_dict(), f, indent=2)


    @classmethod
    def load_from_json(cls, session_id):
        file_path = get_session_file(session_id)
        if not os.path.exists(file_path):
            return None
        with open(file_path, "r") as f:
            data = json.load(f)
            return cls.from_dict(data)

class Session:
    def __init__(self, game_id):
        self.game_id = game_id

    def create_session_file(self, game_state: System):
        game_state.save_to_json(self.game_id)

    def load_session_file(self):
        return System.load_from_json(self.game_id)

    def delete_session_file(self):
        file_path = get_session_file(self.game_id)
        if os.path.exists(file_path):
            print(os.remove(file_path))
            return
        print("Error: file not found")
        return
        

def get_session_file(session_id):
    return os.path.join(SESSIONS_DIR, f"{session_id}.json")
        
