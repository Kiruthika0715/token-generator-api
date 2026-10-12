# Token Generator API

A small FastAPI project that serves an interactive HTML form and a tokenization API endpoint.

## Features
- Interactive browser form for entering participant details and text
- `POST /generate` endpoint that accepts JSON with a `text` field
- Returns the tokenized words and a SHA-256 checksum of the input
- API documentation available automatically via FastAPI docs

## Run locally

1. Create and activate a virtual environment
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the app:

```bash
uvicorn main:app --reload
```

4. Open the browser at:

```text
http://127.0.0.1:8000/
```

## API usage

Send a POST request to `/generate`:

```json
{
  "text": "Hello world from FastAPI"
}
```

Response:

```json
{
  "text": "Hello world from FastAPI",
  "tokens": ["Hello", "world", "from", "FastAPI"],
  "checksum": "5d4e6d..."
}
```

## Notes
The endpoint uses a simple tokenizer based on non-whitespace text splitting. A checksum is calculated using SHA-256 for quick validation of the original input.
