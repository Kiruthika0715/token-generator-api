<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Token Generator</title>
    <style>
      :root {
        --bg: #f5f5f5;
        --panel: #ffffff;
        --text: #111827;
        --muted: #4b5563;
        --primary: #2563eb;
        --border: #d1d5db;
      }

      * { box-sizing: border-box; }

      body {
        margin: 0;
        font-family: Arial, Helvetica, sans-serif;
        background: var(--bg);
        color: var(--text);
      }

      .container {
        max-width: 900px;
        margin: 40px auto;
        padding: 24px;
      }

      .panel {
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
      }

      h1 {
        margin-top: 0;
        margin-bottom: 16px;
        font-size: 2rem;
      }

      .welcome {
        font-size: 1.2rem;
        margin-bottom: 20px;
        color: var(--muted);
      }

      label {
        display: block;
        margin-bottom: 16px;
        font-weight: 600;
      }

      input,
      textarea,
      button {
        width: 100%;
        font: inherit;
      }

      input,
      textarea {
        margin-top: 8px;
        padding: 12px 14px;
        border: 1px solid var(--border);
        border-radius: 8px;
        background: #fff;
      }

      textarea {
        min-height: 140px;
        resize: vertical;
      }

      button {
        padding: 12px 18px;
        border: none;
        border-radius: 8px;
        background: var(--primary);
        color: white;
        font-weight: 700;
        cursor: pointer;
      }

      button:hover {
        opacity: 0.95;
      }

      .result {
        margin-top: 22px;
        padding: 16px;
        background: #f8fafc;
        border: 1px solid var(--border);
        border-radius: 8px;
        white-space: pre-wrap;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="panel">
        <h1>Token Generator</h1>

        <div id="welcome-message" class="welcome">Welcome, friend!</div>

        <label>
          Participant name
          <input id="participant-name" type="text" placeholder="Enter your name" value="friend" />
        </label>

        <label>
          Text to tokenize
          <textarea id="text-input" placeholder="Type or paste text here...">Hello world from FastAPI</textarea>
        </label>

        <button id="generate-btn" type="button">Generate Tokens</button>

        <div id="result" class="result">No output yet.</div>
      </div>
    </div>

    <script>
      const participantNameInput = document.getElementById('participant-name');
      const welcomeMessage = document.getElementById('welcome-message');
      const textInput = document.getElementById('text-input');
      const resultBox = document.getElementById('result');

      function updateWelcomeMessage() {
        const name = participantNameInput.value.trim() || 'friend';
        welcomeMessage.textContent = `Welcome, ${name}!`;
      }

      participantNameInput.addEventListener('input', updateWelcomeMessage);
      updateWelcomeMessage();

      document.getElementById('generate-btn').addEventListener('click', async () => {
        const text = textInput.value;
        const name = participantNameInput.value.trim() || 'friend';

        try {
          const response = await fetch('/generate', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text }),
          });

          if (!response.ok) {
            throw new Error('Request failed');
          }

          const data = await response.json();
          resultBox.textContent = `Welcome, ${name}!\n\nTokens: ${JSON.stringify(data.tokens, null, 2)}\n\nChecksum: ${data.checksum}`;
        } catch (error) {
          resultBox.textContent = `Error generating tokens: ${error.message}`;
        }
      });
    </script>
  </body>
</html>
