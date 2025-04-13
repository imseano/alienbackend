import json
import uuid
import re
from system import System, Session

known_words = ["yes", "no", "you", "me", "help", "danger", "safe", "friend", "enemy"]
motive = "destroy Earth"
personality = "funny"
stress = 0.0

bat_reduction = 10

def start_game():
    game_id = str(uuid.uuid4())
    system = System(known_words, personality, motive, stress)
    Session(game_id).create_session_file(system)

    return game_id

def ask_alien(game_id, message):
    system = Session(game_id).load_session_file()

    alien = system.alien

    reply = alien.generate_response(message)

    def extract_json_from_text(text: str):
        try:
            # Match the first full JSON object in the text
           json_match = re.search(r"\{.*?\}", text, re.DOTALL)
           if json_match:
            return json.loads(json_match.group(0))
        except json.JSONDecodeError as e:
            print("JSON decode error:", e)
        return None

    json_data = extract_json_from_text(reply.content)

    print(json_data)

    print(json_data['response'])

    system.remaining_bat -= bat_reduction

    system.add_history(json_data)

    system.save_to_json(game_id)

    if (system.remaining_bat <= 0):
        return "__END__"

    return json_data['response']

def teach_alien(game_id, word):
    pass

def get_session_data(game_id):
    return Session(game_id).load_session_file().to_dict()

def end_game(game_id):
    final_data = Session(game_id).load_session_file().to_dict()
    Session(game_id).delete_session_file()
    print(final_data)
    return final_data
