# Connect_deepSeek_Flask
# DeepSeek R1 Distill Llama-70B API Integration

## Overview

This project is a Flask-based API that integrates with DeepSeek R1 Distill Llama-70B using the Groq API to generate responses based on user queries. The API validates input and handles text generation in a structured manner.

## Features

- Flask-based API with CORS support.
- Integration with DeepSeek R1 Distill Llama-70B via Groq API.
- Input validation to ensure non-empty requests.
- Error handling for improved reliability.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.8+
- Flask
- Flask-CORS
- `dotenv` for managing environment variables
- Groq API access

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/thirumurugan2001/Connect_deepSeek_Flask.git
   cd Connect_deepSeek_Flask
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   - Create a `.env` file in the root directory.
   - Add your Groq API key:
     ```env
     GROQ_API_KEY=your_api_key_here
     ```

## Usage

### Start the Server

Run the Flask application:

```bash
python main.py
```

The server will start on `http://0.0.0.0:8080`.

### API Endpoints

#### `POST /deepseek`

Processes user questions and generates AI responses.

**Request Body:**

```json
{
  "Question": "Your question here"
}
```

**Response:**

```json
{
  "data": ["Generated text here"],
  "statusCode": 200
}
```

**Error Handling:**

- Missing `Question` field returns `400` with an error message.
- Empty `Question` field returns `400` with an invalid data message.
- Internal server errors return `500`.

## File Structure

```
project-folder/
│── app.py              # Flask application
│── checker.py          # Controller for validation and handling requests
│── deepSeek.py         # Groq API integration
│── .env                # Environment variables
│── requirements.txt    # Python dependencies
│── README.md           # Documentation
```

## License

This project is open-source and available under the MIT License.

