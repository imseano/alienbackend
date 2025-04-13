import main

ssid = main.start_game()

main.ask_alien(ssid, "Who are you and why are you here?")
main.ask_alien(ssid, "Do you want to destroy Earth?")

main.end_game(ssid)
