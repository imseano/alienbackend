# AlienBackend
A backend for First Encounter game for FullyHacks 2025. Frontend: [FullyHacks](https://github.com/EdwardCValencia/FullyHacks)

## Software Requirements
- Python 3.13


## How to run
1. Create a .env and include CEREBRAS_API_KEY
2. Run 'pip install -r requirements.txt' to install dependencies
3. run 'uvicorn main:app' in src/ and access the API at http://localhost:8000


## API Endpointsy

### POST /new_session

Creates a new alien session with default settings.
Request Body

```
{
  "game_id": "new-session-id"
}
```

Response
```
{
  "message": "Session created",
  "starting_words": ["hello", "friend"]
}
```
