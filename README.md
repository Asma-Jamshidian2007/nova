# Nova AI Assistant

Nova is a voice-controlled AI assistant that can perform various tasks, such as searching Wikipedia, managing applications, checking the time, answering questions, and even interacting through AI-generated responses.

## Features

- **Voice Recognition**: Uses speech recognition to listen and respond to user commands.
- **Text-to-Speech**: Converts text responses into spoken output.
- **AI Chat Integration**: Uses Google's Gemini AI to generate intelligent responses.
- **Wikipedia Search**: Fetches summarized information from Wikipedia.
- **Application Management**:
  - Open applications
  - Close running applications
  - Install and uninstall applications using `winget`
- **System Control**:
  - Check the current time
  - Shutdown the computer via voice command
- **Answer Questions**: Responds to general knowledge questions using AI.

## How It Works

1. Listens to the user's command using the microphone.
2. Processes the command and determines the appropriate action.
3. If it is a general question, it interacts with Gemini AI.
4. If the command is related to applications, it opens, closes, installs, or uninstalls them accordingly.
5. Uses text-to-speech (TTS) to provide audible responses.

## Project Structure

```plaintext
nova_ai_assistant/
├── main.py          # Main script to run Nova
├── requirements.txt # Required Python libraries
├── README.md        # Project documentation
└── LICENSE          # License file
```

## Prerequisites

- **Python 3.x**
- Required libraries (install using `pip install RequiredlibrarieName `):
  - `speechrecognition`
  - `pyttsx3`
  - `wikipedia`
  - `requests`
  - `psutil`


Then, use voice commands like:
- "Hello"
- "Search Wikipedia for Python programming"
- "What time is it?"
- "Open Notepad"
- "Close Chrome"
- "Shutdown the computer"
- "What is the capital of France?"


---
Nova is a lightweight, voice-controlled AI assistant designed to make daily tasks easier through automation and intelligent responses.

