
from main import end_game, start_game, ask_alien, teach_alien
import time

def main():
    print("👽 Welcome to Alien Chat!")
    print("You are a human diplomat speaking to a strange alien being.")
    print("Type messages to the alien. Type 'exit' to quit.")
    print("-" * 50)

    game_id = start_game(True)
    print(f"[Session started: {game_id}]\nSay something to the alien...\n")

    while True:
        user_input = input("🧑 You: ").strip()
        if user_input.lower() == 'exit':
            print("👋 Ending communication. Farewell.")
            break

        if user_input.lower().startswith("teach "):
            try:
                word = user_input[6:].strip()
                if not word:
                    print("⚠️ You must specify a word to teach.")
                    continue
                teach_alien(game_id, word)
                print(f"📘 The alien has learned a new word: '{word}'")
                time.sleep(1)
            except Exception as e:
                print("⚠️ An error occurred while teaching:", e)
            continue  # Skip normal ask flow
        try:
            response = ask_alien(game_id, user_input)

            if response == "__END__" or user_input == "quit":
                # `ask_alien()` should return this if battery is 0
                print("\n⚡ Your battery has run out!")
                print("📋 FINAL DECISION:")
                decision = input("💀 Do you want to [spare] or [kill] the alien? ").strip().lower()
                if decision == "spare":
                    print("🕊️ You chose mercy. Perhaps this alien has changed...")
                elif decision == "kill":
                    print("☠️ You ended the alien. Earth may be safe, but at what cost?")
                else:
                    print("🤷‍♂️ No decision made. History will remember your silence.")
                end_game(game_id)
                break

            print("👽 Alien:", response)
            time.sleep(1)

        except Exception as e:
            print("⚠️ An error occurred:", e)

if __name__ == "__main__":
    main()
