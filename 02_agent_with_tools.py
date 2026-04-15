"""
Section 4: Adding Tools
========================
This template shows how to add tools to your agent.

Goal: Create an agent that can perform calculations and more.
"""

from strands import Agent
from strands.models.anthropic import AnthropicModel
from strands_tools import calculator

# Set up the model
model = AnthropicModel(model_id="claude-sonnet-4-20250514")

# Create agent with calculator tool
agent = Agent(
    model=model,
    system_prompt="""You are a helpful math tutor named Buddy. 
    When asked math questions, use your calculator tool to ensure accuracy.
    Explain your calculations step by step.""",
    tools=[calculator]
)

print("🧮 Math Buddy is ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Keep practicing! 📐")
        break
    
    response = agent(user_input)
    print(f"Math Buddy: {response}\n")


# ============================================
# ✅ CHECKPOINT 3: Test tool usage
# ============================================
# Try asking:
#   - "What's 15% of 85?"
#   - "Calculate 234 * 567" (should be 132,678)
#   - "If I invest $1000 at 7% annual interest, how much after 5 years?"
#
# Your agent should use the calculator tool automatically!


# ============================================
# 🚀 EXTENSION: Add more tools
# ============================================
# Uncomment below to add web search capability:
#
# from strands_tools import http_request
# 
# agent = Agent(
#     model=model,
#     system_prompt="You are a research assistant with math and web search abilities.",
#     tools=[calculator, http_request]
# )
