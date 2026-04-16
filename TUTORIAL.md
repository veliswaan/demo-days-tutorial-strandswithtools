# Build Your First AI Agent with Strands Agents SDK

**Workshop Duration:** 3 hours  
**Skill Level:** Beginner  
**What You'll Build:** A fully functional AI agent with tools and memory

---

## 1. Introduction (5 minutes)

### What is an Agentic AI System?

Think of an AI agent like a smart assistant that can:
- **Think** about what you ask
- **Decide** what actions to take
- **Use tools** to get things done
- **Remember** context from your conversation

**Analogy:** Imagine a chef. You tell them "I want something Italian for dinner." They don't just recite a recipe, they think about what ingredients are available, decide on a dish, use their knives and pans to cook it, and remember that you mentioned you don't like mushrooms earlier. An AI agent works the same way: it reasons, decides, acts, and remembers.

### What is Strands Agents SDK?

Strands is an open-source framework that makes building AI agents simple. It handles the complex parts so you can focus on what your agent should do.

**Why Strands?**
- 🚀 Simple to start and scale
- 🔧 Easy tool integration
- 🧠 Built-in memory management
- 📚 Great documentation

**Official Documentation:** https://strandsagents.com/latest/

### What We'll Build Today

By the end of this workshop, you'll have built your own AI agent with:
- A custom personality and purpose
- The ability to use tools (like calculators, APIs, or your own custom tools)
- Conversational memory within a session

What kind of agent? That's up to you!

---

## 2. Environment Setup (15 minutes)

### Prerequisites

Before we start, make sure you have:
- [ ] Python 3.10 or higher installed
- [ ] A code editor (VS Code recommended)
- [ ] A terminal/command prompt

### Step 1: Get Your Anthropic API Key (5 minutes)

We'll use Anthropic's Claude API for this workshop. New accounts get free credits!

> 💡 **Alternative:** If you prefer to use a different model provider (AWS Bedrock, OpenAI, or Google Gemini), see the [Alternative Model Providers](#alternative-model-providers) section at the end of this setup.

1. Go to **https://console.anthropic.com**
2. Click "Sign Up" and create an account (email verification required)
3. Once logged in, go to **Settings → API Keys**
4. Click "Create Key" and give it a name like "workshop"
5. **Copy the key immediately** - you won't see it again!

> 💡 **Tip:** New accounts typically get $5 in free credits - more than enough for this workshop.

### Step 2: Create Your Project Folder

```bash
mkdir my-first-agent
cd my-first-agent
```

### Step 3: Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate
```

### Step 4: Install Strands SDK
([Python Quickstart read more here](https://strandsagents.com/docs/user-guide/quickstart/python/).)
```bash
pip install strands-agents strands-agents-tools strands-agents-builder
```

### Step 5: Set Your API Key

**Mac/Linux:**
```bash
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

**Windows (Command Prompt):**
```cmd
set ANTHROPIC_API_KEY=sk-ant-your-key-here
```

**Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

> ⚠️ **Important:** You'll need to set this every time you open a new terminal, or add it to your shell profile.

### Alternative Model Providers

If you have an AWS account with Bedrock access:

```bash
pip install strands-agents strands-agents-tools

export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_REGION="us-east-1"
```

Then use the default Agent without specifying a model:
```python
from strands import Agent
agent = Agent()  # Uses AWS Bedrock by default
```

If you have an OpenAI API key:

```bash
pip install strands-agents strands-agents-tools strands-agents-builder

export OPENAI_API_KEY="sk-your-key-here"
```

```python
from strands import Agent
from strands.models.openai import OpenAIModel

model = OpenAIModel(model_id="gpt-4o")
agent = Agent(model=model)
```

If you have a Google AI API key:

```bash
pip install strands-agents strands-agents-tools strands-agents-builder

export GOOGLE_API_KEY="your-key-here"
```

```python
from strands import Agent
from strands.models.gemini import GeminiModel

model = GeminiModel(model_id="gemini-2.0-flash")
agent = Agent(model=model)
```

---

## 3. Building Your First Agent (45 minutes)

### Understanding the Core Components

An agent has three main parts:

```
┌─────────────────────────────────────┐
│            YOUR AGENT               │
├─────────────────────────────────────┤
│  � Model                           │
│     (The LLM that powers it)        │
├─────────────────────────────────────┤
│  🧠 System Prompt                   │
│     (Personality & Instructions)    │
├─────────────────────────────────────┤
│  � Tools                           │
│     (Actions the agent can take)    │
└─────────────────────────────────────┘
```

### Creating Your First Agent

Create a new file called `my_agent.py`:

```python
# my_agent.py
from strands import Agent
from strands.models.anthropic import AnthropicModel

# Set up the model (using Anthropic's Claude)
model = AnthropicModel(model_id="claude-sonnet-4-20250514")

# Create a basic agent with a personality
agent = Agent(
    model=model,
    system_prompt="You are a friendly assistant named Buddy. You're helpful, concise, and occasionally use emojis."
)

# Have a conversation
print("Agent is ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye! 👋")
        break
    
    response = agent(user_input)
    print(f"Buddy: {response}\n")
```

Run it:
```bash
python my_agent.py
```

### Try These Conversations

```
You: Hi! What's your name?
You: Can you help me understand what an AI agent is?
You: What did I just ask you about?
```

### ✅ Checkpoint 1
Your agent should:
- Respond with a friendly personality
- Remember what you talked about in the same session
- Use emojis occasionally (as instructed)

### Understanding What Just Happened

```python
# Set up which AI model to use
model = AnthropicModel(model_id="claude-sonnet-4-20250514")

# This line creates the agent with a personality
agent = Agent(
    model=model,
    system_prompt="You are a friendly assistant..."  # This shapes HOW the agent responds
)

# This line sends a message and gets a response
response = agent(user_input)  # The agent thinks and responds
```

**Documentation:** Learn more about [Agent basics](https://strandsagents.com/)

---

## 4. Adding Tools (30 minutes)

### What Are Tools?

Tools give your agent superpowers! Instead of just talking, it can:
- 🧮 Do math calculations
- 🔍 Search the web
- 📁 Read files
- 🌐 Make API calls

**Analogy:** Tools are like apps on your phone. Your phone (the agent) becomes more useful with each app (tool) you add.

### Adding a Calculator Tool

**Documentation:**Learn about all [built-in (community) tools here](https://strandsagents.com/docs/user-guide/concepts/tools/community-tools-package/).

Update your `my_agent.py`:

```python
# my_agent.py - with calculator
from strands import Agent
from strands.models.anthropic import AnthropicModel
from strands_tools import calculator

# Set up the model
model = AnthropicModel(model_id="claude-sonnet-4-20250514")

# Create agent with calculator tool
agent = Agent(
    model=model,
    system_prompt="You are a helpful math tutor named Buddy. When asked math questions, use your calculator tool to ensure accuracy.",
    tools=[calculator]
)

print("Math Buddy is ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    
    response = agent(user_input)
    print(f"Buddy: {response}\n")
```

### Test the Calculator

```
You: What's 15% of 85?
You: If I have $1000 and it grows 7% per year, how much after 5 years?
You: What's the square root of 144?
```

### Adding a Web Search Tool

```python
# my_agent.py - with multiple tools
from strands import Agent
from strands.models.anthropic import AnthropicModel
from strands_tools import calculator, http_request

model = AnthropicModel(model_id="claude-sonnet-4-20250514")

agent = Agent(
    model=model,
    system_prompt="""You are a helpful research assistant named Buddy. 
    You can do calculations and look up information online.
    Always cite your sources when searching.""",
    tools=[calculator, http_request]
)
```

### ✅ Checkpoint 2
Test that your agent can:
- Correctly calculate `234 * 567` (should be 132,678)
- Answer a question that requires current information

### How Tools Work Behind the Scenes

```
User: "What's 25% of 80?"
         │
         ▼
┌─────────────────────┐
│   Agent Thinks:     │
│   "I need to        │
│   calculate this"   │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│   Uses Calculator   │
│   Tool: 80 * 0.25   │
│   Result: 20        │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│   Agent Responds:   │
│   "25% of 80 is 20" │
└─────────────────────┘
```


### Creating a Custom Tool

**Documentation:** You can create [your own custom tools](https://strandsagents.com/docs/user-guide/concepts/tools/custom-tools/), learn more here.

You can create your own tools! Here's a simple example:

```python
from strands import tool

@tool
def get_greeting(name: str, language: str = "english") -> str:
    """
    Returns a greeting for the given name in the specified language.
    
    Args:
        name: The name of the person to greet
        language: The language for the greeting (english, spanish, french)
    
    Returns:
        A greeting string
    """
    greetings = {
        "english": f"Hello, {name}!",
        "spanish": f"¡Hola, {name}!",
        "french": f"Bonjour, {name}!"
    }
    return greetings.get(language.lower(), f"Hello, {name}!")

# Add to your agent
agent = Agent(
    system_prompt="You are a multilingual greeter.",
    tools=[get_greeting]
)
```

**Documentation:** Learn to [build custom tools](https://strandsagents.com/latest/user-guide/concepts/tools/custom-tools/)

---

## 5. Customization Phase (60 minutes)

Now it's time to build YOUR agent! This is your creative playground.

### What Will You Build?

Think about something that would be useful or fun for YOU. Here are some ideas to spark your imagination:

| Category | Agent Ideas |
|----------|-------------|
| 🎓 Learning | Study buddy, language tutor, interview prep coach |
| 💻 Coding | Code explainer, debugging helper, documentation writer |
| 🎮 Fun | Story writer, game master, joke teller, trivia host |
| 🏃 Lifestyle | Fitness coach, meal planner, travel advisor |
| 💼 Productivity | Meeting summarizer, email drafter, task prioritizer |
| 🎨 Creative | Art critic, music recommender, writing prompt generator |

**Or invent something completely new!**

### Building Your Agent

Open `starter-code/03_custom_agent.py` and customize it:

**Step 1: Give your agent a name and personality**
```python
AGENT_NAME = "Coach Max"  # Your agent's name

SYSTEM_PROMPT = f"""You are {AGENT_NAME}, a motivational fitness coach.

Your personality:
- Energetic and encouraging, but not annoying
- You celebrate small wins
- You use fitness analogies for everything

When helping users, you should:
- Ask about their fitness goals first
- Suggest realistic, beginner-friendly exercises
- Always remind them to stay hydrated 💧
"""
```

**Step 2: Add custom tools (optional but powerful!)**
```python
@tool
def calculate_calories(exercise: str, minutes: int) -> str:
    """
    Estimates calories burned for an exercise.
    
    Args:
        exercise: Type of exercise (running, walking, cycling, etc.)
        minutes: Duration in minutes
    """
    calories_per_minute = {
        "running": 10,
        "walking": 4,
        "cycling": 8,
        "swimming": 9,
        "yoga": 3,
    }
    rate = calories_per_minute.get(exercise.lower(), 5)
    total = rate * minutes
    return f"{exercise} for {minutes} min burns approximately {total} calories"
```

**Step 3: Test and iterate!**
- Run your agent
- Try different conversations
- Adjust the system prompt based on how it responds
- Add more tools if needed

### Tips for Great Agents

1. **Be specific in your system prompt** - Vague instructions = vague responses
2. **Give examples** - Show your agent how you want it to respond
3. **Set boundaries** - Tell it what NOT to do
4. **Add personality** - Emojis, catchphrases, and quirks make it memorable
5. **Tools are superpowers** - If your agent needs to DO something (not just talk), make a tool

### ✅ Checkpoint 3
Your custom agent should:
- Have a distinct personality that comes through in responses
- Stay in character throughout the conversation
- Use tools when appropriate (if you added any)
- Be something YOU find useful or entertaining

### Extension Challenges (For Fast Learners)

**Challenge 1: Add Memory Persistence**
Make your agent remember conversations between sessions.

```python
# Hint: Look into conversation history
# Documentation: https://strandsagents.com/latest/user-guide/concepts/agents/agent-memory/
```

**Challenge 2: Multi-Agent System**
Create two agents that can work together.

```python
# Hint: One agent can call another
# Documentation: https://strandsagents.com/latest/user-guide/concepts/agents/multi-agent-systems/
```

**Challenge 3: Add Error Handling**
Make your agent gracefully handle errors.

```python
try:
    response = agent(user_input)
except Exception as e:
    print(f"Oops! Something went wrong: {e}")
    print("Let me try again...")
```

---

## 6. Demo Preparation (15 minutes)

Time to show off what you built! First, let's save your work to GitHub, then you'll present to the group.

### Push Your Agent to GitHub

**Step 1: Create a GitHub repository**
1. Go to https://github.com/new
2. Name it something like `my-first-agent` or your agent's name
3. Keep it Public (so others can see your work!)
4. Don't add README, .gitignore, or license (we'll push our own files)
5. Click "Create repository"

**Step 2: Push your code**

In your terminal (from your project folder):

```bash
# Initialize git (if you haven't already)
git init

# Add all your files
git add .

# Commit your work
git commit -m "My first AI agent - [Your Agent Name]"

# Connect to GitHub (replace with YOUR repository URL)
git remote add origin https://github.com/YOUR_USERNAME/my-first-agent.git

# Push!
git push -u origin main
```

> ⚠️ **Important:** Make sure your API key is NOT in your code! It should only be in your environment variable.

**Step 3: Verify**
- Go to your GitHub repository in the browser
- You should see your agent code there
- Share the link in the workshop chat!

### Preparing Your Demo

**What to cover in your 2-3 minute demo:**
1. **What does your agent do?** (One sentence)
2. **Why did you build it?** (What problem does it solve or what makes it fun?)
3. **Live demo** - Show 2-3 interactions that highlight its best features
4. **One thing you learned** - Share something interesting from the process

### Test Your Agent

Before presenting, run through these scenarios:

```
You: [A typical first message a user would send]
You: [Something that uses your agent's main feature]
You: [An edge case - something unusual to see how it handles it]
```

### Demo Tips

- **Start strong** - Lead with the most impressive interaction
- **Have backup questions ready** - In case your first demo doesn't go as planned
- **It's okay if something breaks!** - Explain what happened and what you'd fix
- **Keep it short** - 2-3 interactions is plenty

### Troubleshooting Quick Fixes

| Issue | Quick Fix |
|-------|-----------|
| Agent not responding | Check API key, check internet connection |
| Tool not being used | Make your request more explicit ("calculate this for me") |
| Agent going off-topic | Strengthen your system prompt with clearer boundaries |
| Slow responses | This is normal for complex queries; be patient |

---

## Project Structure Reference

```
my-first-agent/
├── venv/                    # Virtual environment
├── my_agent.py              # Your main agent file
├── requirements.txt         # Dependencies
└── README.md                # Your project description
```

### requirements.txt
```
strands-agents
strands-agents-tools
```

---

## Quick Reference Card

### Creating an Agent
```python
from strands import Agent
agent = Agent(system_prompt="Your instructions here")
response = agent("User message")
```

### Adding Tools
```python
from strands_tools import calculator, http_request
agent = Agent(tools=[calculator, http_request])
```

### Creating Custom Tools
```python
from strands import tool

@tool
def my_tool(param: str) -> str:
    """Description of what this tool does."""
    return f"Result: {param}"
```

### Key Documentation Links
- [Getting Started](https://strandsagents.com/latest/user-guide/quickstart/)
- [Agent Concepts](https://strandsagents.com/latest/user-guide/concepts/agents/)
- [Tools Overview](https://strandsagents.com/latest/user-guide/concepts/tools/tools-overview/)
- [Custom Tools](https://strandsagents.com/latest/user-guide/concepts/tools/custom-tools/)
- [Examples](https://strandsagents.com/latest/user-guide/examples/)

---

## What's Next?

Congratulations on building your first AI agent! 🎉

Here are some ways to continue learning:

1. **Explore more tools**: File operations, API integrations, database connections
2. **Build multi-agent systems**: Agents that collaborate
3. **Add a web interface**: Use Streamlit or Gradio
4. **Deploy your agent**: Make it accessible online
5. **Join the community**: Share what you've built!

**Keep building, keep learning!** 🚀

**Let us know how you experienced the event** [by completing this survey](https://pulse.aws/survey/SRBZBBVS)
