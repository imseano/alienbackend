# AlienBackend
A backend for First Encounter game for FullyHacks 2025. Frontend: [FullyHacks](https://github.com/EdwardCValencia/FullyHacks)

## Software Requirements
- Python 3.13


## How to run
1. Create a .env and include CEREBRAS_API_KEY
2. Run 'pip install -r requirements.txt' to install dependencies
3. run 'uvicorn main:app' in src/ and access the API at http://localhost:8000


## API Endpoints

### POST /ask

Sends a message to the alien and gets a JSON-formatted response.
#### Request Body
```
{
  "game_id": "your-session-id",
  "message": "hello"
}
```
#### Response
```
{
  "response": "friend",           // Alien's chosen word(s)
  "remaining_battery": 85         // Battery left
}
```
### POST /teach

Adds a new word to the alien's vocabulary.
#### Request Body
```
{
  "game_id": "your-session-id",
  "word": "peace"
}
```
#### Response
```
{
   "word-list": "words"
}
```
### POST /new_session

Creates a new alien session with default settings.
#### Request Body
```
{
  "game_id": "new-session-id"
}
```
#### Response
```
{
  "message": "Session created",
  "starting_words": ["hello", "friend"]
}
```
### POST /end_game

Deletes the session and returns game data.
#### Request Body
```
{
   "game_id": "session-id"
}
```
#### Response
```
{
   "game_data": "game-data"
}
```
