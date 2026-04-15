"""
Section 3: Building Your First Agent
=====================================
This is your starting template. Follow along with the tutorial!

Goal: Create a basic conversational agent with a custom personality.
"""

from strands import Agent
from strands.models.anthropic import AnthropicModel

# Set up the model (using Anthropic's Claude)
model = AnthropicModel(model_id="claude-sonnet-4-20250514")

# Create your agent with a system prompt
# The system prompt defines your agent's personality
agent = Agent(
    model=model,
    system_prompt="You are a friendly assistant named Buddy. You're helpful, concise, and occasionally use emojis."
)

# Conversation loop
print("🤖 Agent is ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye! 👋")
        break
    
    response = agent(user_input)
    print(f"Agent: {response}\n")


# ============================================
# ✅ CHECKPOINT 2: Test these conversations
# ============================================
# Try asking:
#   - "Hi! What's your name?"
#   - "Can you help me understand what an AI agent is?"
#   - "What did I just ask you about?"
#
# Your agent should:
#   - Respond with a friendly personality
#   - Remember the conversation context
#   - Use emojis occasionally
