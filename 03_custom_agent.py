"""
Section 5: Build YOUR Agent!
=============================
This is your creative playground. Build any agent you can imagine!

Need inspiration? Here are some ideas:
  - Study Buddy: Helps explain concepts and quizzes you
  - Code Helper: Explains code and helps debug
  - Travel Planner: Suggests destinations and creates itineraries
  - Fitness Coach: Creates workout plans and tracks progress
  - Recipe Assistant: Suggests meals based on ingredients you have
  - Language Tutor: Helps practice a new language
  - Story Writer: Collaborates on creative writing
  - Interview Prep: Practices job interview questions
  - Personal Finance: Helps budget and track expenses
  - Game Master: Runs a text-based adventure game

Or come up with your own unique idea!
"""

from strands import Agent, tool
from strands.models.anthropic import AnthropicModel
from strands_tools import calculator

# Set up the model
model = AnthropicModel(model_id="claude-sonnet-4-20250514")


# ============================================
# STEP 1: Define your agent's personality
# ============================================
# Fill in the blanks to create your unique agent!

AGENT_NAME = "Your Agent Name"  # Give your agent a name

SYSTEM_PROMPT = f"""You are {AGENT_NAME}, a [describe what your agent does].

Your personality:
- [How does your agent communicate? Friendly? Professional? Funny?]
- [What makes your agent unique?]
- [Any special quirks or catchphrases?]

When helping users, you should:
- [What's the first thing your agent does?]
- [How does your agent approach problems?]
- [What should your agent avoid doing?]
"""


# ============================================
# STEP 2: Create custom tools (optional)
# ============================================
# Tools let your agent DO things, not just talk.
# Here's a template - modify it for your agent's needs!

@tool
def my_custom_tool(user_input: str) -> str:
    """
    Describe what this tool does in one sentence.
    The agent reads this description to know when to use the tool.
    
    Args:
        user_input: What the user provided
    
    Returns:
        The result of your tool's action
    """
    # Your logic here - this could:
    # - Look something up in a dictionary
    # - Do a calculation
    # - Format data in a special way
    # - Generate something random
    # - Anything you can code!
    
    result = f"Processed: {user_input}"
    return result


# ============================================
# STEP 3: Create your agent
# ============================================
# Combine your personality + tools

agent = Agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    tools=[calculator, my_custom_tool]  # Add or remove tools as needed
)


# ============================================
# STEP 4: Run your agent!
# ============================================

print(f"🤖 {AGENT_NAME} is ready!")
print("Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye! 👋")
        break
    
    response = agent(user_input)
    print(f"{AGENT_NAME}: {response}\n")


# ============================================
# 💡 IDEAS FOR CUSTOM TOOLS
# ============================================
# 
# Random picker:
#   import random
#   @tool
#   def pick_random(options: str) -> str:
#       """Picks a random item from comma-separated options."""
#       items = [x.strip() for x in options.split(",")]
#       return random.choice(items)
#
# Simple database lookup:
#   @tool  
#   def lookup_fact(topic: str) -> str:
#       """Looks up a fact about a topic."""
#       facts = {
#           "python": "Python was created by Guido van Rossum in 1991",
#           "ai": "The term AI was coined in 1956 at Dartmouth",
#       }
#       return facts.get(topic.lower(), "I don't have info on that topic")
#
# Calculator with memory:
#   running_total = 0
#   @tool
#   def add_to_total(amount: float) -> str:
#       """Adds amount to running total and returns new total."""
#       global running_total
#       running_total += amount
#       return f"Added {amount}. New total: {running_total}"
