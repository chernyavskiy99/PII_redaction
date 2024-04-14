# PII Redaction

This project implements a REST API for redacting personally identifiable information (PII) from text using the OpenAI GPT-3.5-turbo model. The API is built with FastAPI and can be run using Docker Compose.

## Prerequisites

- Docker: Make sure you have Docker installed on your system. You can download and install Docker from the official website: https://www.docker.com/get-started

- OpenAI API Key: Obtain an API key from OpenAI. You can sign up for an API key at https://beta.openai.com/signup/

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/chernyavskiy99/PII_redaction.git
   cd PII_redaction
   ```

2. Create a `.env` file in the project root directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=YOUR_OPENAI_API_KEY
   ```

   Replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key.

3. Build and run the Docker container:

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker image and start the API service.

4. The API will be accessible at `http://localhost/pii-redact`.

## Usage

To redact PII from text, send a POST request to the `/pii-redact` endpoint with the `text` parameter containing the text you want to process.

Example request using cURL:

```bash
curl -X POST -F "text=My name is John Doe and my email is john@example.com." http://localhost/pii-redact
```

Example response:

```json
{
  "redacted_text": "My name is [REDACTED] and my email is [REDACTED]."
}
```

The response will be a JSON object with the `redacted_text` field containing the text with PII redacted.

## Customization

If you want to modify the API or add additional functionality, you can update the `main.py` file. After making changes, rebuild and restart the Docker container:

```bash
docker-compose down
docker-compose up --build
```

## Cleanup

To stop the API service and remove the Docker container, run:

```bash
docker-compose down
```

This command will stop and remove the running container.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
