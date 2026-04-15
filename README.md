# 🤖 Build Your First AI Agent - Workshop

A beginner-friendly 3-hour hands-on workshop for building AI agents using the Strands Agents SDK.

## What You'll Learn

- What agentic AI systems are and how they work
- How to build conversational AI agents
- Adding tools (calculator, web search, custom tools)
- Customizing agent personality and behavior
- Building one of three project options:
  - 📚 Study Buddy Agent
  - 💻 Code Explainer Agent
  - 👨‍🍳 Recipe Budget Calculator

## Prerequisites

- Python 3.10 or higher
- Basic Python knowledge
- A code editor (VS Code recommended)
- Anthropic API key (free credits for new accounts!)

## Quick Start

```bash
# Clone this repository
git clone https://github.com/YOUR_USERNAME/strands-workshop.git
cd strands-workshop

# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Get your API key from https://console.anthropic.com
# Then set it:
export ANTHROPIC_API_KEY="sk-ant-your-key-here"

# Verify setup
python starter-code/01_basic_agent.py
```

## Getting Your API Key

1. Go to https://console.anthropic.com
2. Sign up for a free account
3. Navigate to Settings → API Keys
4. Create a new key and copy it
5. New accounts get free credits - enough for this workshop!

## Workshop Structure

| Section | Duration | Description |
|---------|----------|-------------|
| 1. Introduction | 5 min | What is agentic AI? |
| 2. Environment Setup | 15 min | Install and configure |
| 3. First Agent | 45 min | Build basic agent |
| 4. Adding Tools | 30 min | Calculator & search |
| 5. Customization | 60 min | Build your project |
| 6. Demo Prep | 15 min | Test and present |

## Repository Structure

```
strands-workshop/
├── README.md                 # You are here
├── TUTORIAL.md               # Full workshop tutorial
├── requirements.txt          # Python dependencies
├── starter-code/             # Code templates to build from
│   ├── 01_basic_agent.py     # Section 3: Your first agent
│   ├── 02_agent_with_tools.py # Section 4: Adding tools
│   └── 03_custom_agent.py    # Section 5: Build your own!
└── slides/                   # Optional presentation slides
    └── workshop-slides.md
```

## Resources

- [Full Tutorial](./TUTORIAL.md)
- [Strands Documentation](https://strandsagents.com/latest/)
- [Strands GitHub](https://github.com/strands-agents/strands-agents)

## License

Feel free to use this for your own workshops!
