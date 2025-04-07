from agents.recommendation_agent import RecommendationAgent

class InteractionAgent:
    def __init__(self, recommendation_agent: RecommendationAgent):
        self.recommendation_agent = recommendation_agent

    def handle_query(self, customer_id):
        recommendations = self.recommendation_agent.generate_recommendations(customer_id)
        print("Recommended Products:")
        print(recommendations)
        # In a real system, you would capture user feedback and call:
        # self.recommendation_agent.refine_recommendations(customer_id, feedback)
