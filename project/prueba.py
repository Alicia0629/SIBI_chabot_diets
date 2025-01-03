from agents.recommendation_agent import RecommendationAgent
# Create the agent
agent = RecommendationAgent()

# Update filters (for example, to avoid dairy and gluten)
agent.update_filters({'HasDairy': True, 'HasGluten': True})

# Get recommendations based on user input
user_input = "I want a quick lunch"
recommendations = agent.chat_and_recommend(user_input)

print(recommendations)

