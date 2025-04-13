import json
from fastapi import FastAPI
import uuid
import re
from system import System, Session
from llmclient import Cerebras
from typing import List
from pydantic import BaseModel
import random


app = FastAPI()



# Predefined word banks
VOCABULARY_SETS = {
    "emotive": [
        "love", "hate", "pain", "peace", "joy", "fear", "anger", "trust", "alone", "together"
    ],
    "militaristic": [
        "attack", "defend", "weapon", "enemy", "ally", "command", "target", "retreat", "victory", "nuke"
    ],
    "spiritual": [
        "spirit", "soul", "light", "dark", "ascend", "truth", "ritual", "dream", "balance", "circle"
    ],
    "technological": [
        "system", "data", "input", "error", "signal", "construct", "core", "upload", "machine", "code"
    ],
    "diplomatic": [
        "talk", "agree", "disagree", "peace", "gift", "share", "trust", "listen", "help", "deal"
    ],
    "primal": [
        "hunt", "food", "fire", "water", "sky", "earth", "kill", "run", "hide", "burn"
    ],
    "cosmic": [
        "star", "void", "infinity", "cycle", "watch", "change", "above", "fall", "ascend", "unknowable"
    ],
    "childlike": [
        "yes", "no", "friend", "bad", "happy", "sad", "hug", "play", "run", "big"
    ]
}

motives = ["You wish for an alliance with the Earth", "You wish to destroy countless worlds and conquer the universe", 
           "You simply came to visit and have no other purpose", "You wish to spare the Earth but destroy the human race", "You wish for a peaceful coexistence", "You want to give a nice gift to the humans", "You want to give a terrible curse to the humans"]

d_known_words = ["yes", "no", "you", "me", "help", "danger", "safe", "friend", "enemy"]
d_motive = "You wish to destroy countless worlds and conquer the universe"
d_personality = "bloodthirsty"
d_stress = 0.0



bat_reduction = 10

def choose_random_set():
    name, vocab = random.choice(list(VOCABULARY_SETS.items()))
    return name, vocab.copy()

def choose_random_motive():
    return random.choice(motives)

@app.post("/start_game")
def start_game(use_random: bool = True):
    game_id = str(uuid.uuid4())
    if (use_random):
        personality, known_words = choose_random_set()
        motive = choose_random_motive()
        stress = d_stress
    else:
        print("Making default alien")
        known_words = d_known_words
        personality = d_personality
        motive = d_motive
        stress = d_stress
    system = System(known_words, personality, motive, stress)
    Session(game_id).create_session_file(system)
    return {"message": "Game started successfully", "game_id": game_id}

@app.post("/ask")
def ask_alien(game_id, message):
    system = Session(game_id).load_session_file()

    alien = system.alien

    reply = alien.generate_response(message)

    def extract_json_from_text(text: str):
        try:
            # Match the first full JSON object in the text
           json_match = re.search(r"\{.*?\}", text, re.DOTALL)
           if json_matchostileh:
            return json.loads(json_match.group(0))
        except json.JSONDecodeError as e:
            print("JSON decode error:", e)
        return None

    json_data = extract_json_from_text(reply.content)

    print(json_data['response'])

    system.remaining_bat -= bat_reduction
    alien.calculate_stress_change(json_data['main_emotion'])

    system.add_history(json_data)

    system.save_to_json(game_id)

    return {"response": json_data['response'],
            "remaining_bat": system.remaining_bat
            }

@app.post("/teach")
def teach_alien(game_id, word):
    system = Session(game_id).load_session_file()
    alien = system.alien
    alien.learn_vocab(word)
    system.remaining_bat -= bat_reduction
    system.history.append(f"Alien has learned the word: {word}")

    system.save_to_json(game_id)

    return {"message": "Alien has learned the word: " + word,
            "remaining_bat": system.remaining_bat}


@app.get("/get")
def get_session_data(game_id):
    return Session(game_id).load_session_file().to_dict()

@app.post("/end_game")
def end_game(game_id):
    final_data = Session(game_id).load_session_file().to_dict()
    Session(game_id).delete_session_file()
    print(final_data)
    return final_data
