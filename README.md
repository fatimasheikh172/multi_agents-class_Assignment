# Multi-Agent Assistant with Chainlit Interface

A conversational AI system that uses multiple specialized agents to help users with specific tasks. The system is built with OpenAI Agents and provides a web interface through Chainlit.

## Features

- **Multi-Agent System**: Three specialized agents for different domains
- **Web Interface**: Beautiful chat interface powered by Chainlit
- **Restricted Responses**: Only responds to 3 specific areas of expertise
- **Gemini Integration**: Uses Google's Gemini 2.0 Flash model

## Available Agents

### 1. Web Developer Agent
- **Purpose**: Building websites and web applications
- **Capabilities**: Frontend, backend, and full-stack development assistance

### 2. App Developer Agent  
- **Purpose**: Creating cross-platform mobile apps for iOS and Android
- **Capabilities**: Mobile app development, cross-platform solutions

### 3. Marketing Agent
- **Purpose**: Creating and executing marketing strategies for product launches
- **Capabilities**: Marketing strategy, campaign planning, product launches

## System Behavior

The system is designed to be very specific about its capabilities:

- ✅ **Responds to**: Web development, mobile app development, and marketing queries
- ❌ **Declines**: All other topics (cooking, sports, movies, general chat, etc.)
- 💬 **Response**: "Sorry, I can only help with web development, mobile app development, and marketing. Please ask me about one of these topics."

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Class_Assignmnet
   ```

2. **Set up environment variables**
   Create a `.env` file with:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Usage

1. **Start the application**
   ```bash
   chainlit run main.py -w
   ```

2. **Open your browser**
   Navigate to the URL shown in the terminal (usually `http://localhost:8000`)

3. **Start chatting**
   Ask questions about:
   - Web development
   - Mobile app development  
   - Marketing strategies


## Dependencies

- `chainlit` - Web interface framework
- `openai-agents` - Multi-agent system
- `openai` - OpenAI client for Gemini integration
- `python-dotenv` - Environment variable management

## Configuration

The system uses Google's Gemini 2.0 Flash model through OpenAI's API format. Make sure you have:
- A valid Gemini API key
- Proper base URL configuration for Gemini API
"# multi_agents-class_Assignment" 
