from .agent import Agent
from data.handler.vectorizer import Vectorizer
from data.handler.csv_handler import CSVHandler

class RecommendationAgent(Agent):
    def __init__(self, context="You are a dietary assistant that recommends meals based on user preferences and dietary restrictions."):
        super().__init__(context)
        self.csv_handler = CSVHandler("data/datasets/NewRecipes.csv")
        self.dataset = self.csv_handler.get_dataset()
        self.vectorizer = Vectorizer(self.dataset)
        self.dietary_restrictions = {}

    def update_filters(self, new_filters):
        """
        Update the dietary restrictions filters.
        :param new_filters: Dictionary containing new dietary restrictions.
        """
        self.dietary_restrictions.update(new_filters)
        print("Filters updated:", self.dietary_restrictions)

    def filter_and_recommend(self, user_input, dietary_restrictions=None):
        """
        Get a recommendation based on user input and filter recipes by dietary restrictions.
        If no dietary restrictions are passed, it uses the agent's current filters.
        """
        if dietary_restrictions is None:
            dietary_restrictions = self.dietary_restrictions

        filtered_recipes = self.csv_handler.filter_recipes(dietary_restrictions)

        if filtered_recipes.empty:
            return "No recipes match your dietary restrictions."

        self.vectorizer = Vectorizer(filtered_recipes)

        recommendations = self.vectorizer.search(user_input, k=3)

        recommendations_text = "\n\n".join(
            [
                (
                    f"**{row['Name']}**\n"
                    f"- **Recipe ID**: {row['RecipeId']}\n"
                    f"- **Author**: {row['AuthorName']} (ID: {row['AuthorId']})\n"
                    f"- **Cook Time**: {row['CookTime']} | **Prep Time**: {row['PrepTime']} | **Total Time**: {row['TotalTime']}\n"
                    f"- **Published On**: {row['DatePublished']}\n"
                    f"- **Category**: {row['RecipeCategory']}\n"
                    f"- **Description**: {row['Description']}\n"
                    f"- **Nutritional Info**:\n"
                    f"  - Calories: {row['Calories']}\n"
                    f"  - Fat: {row['FatContent']} | Saturated Fat: {row['SaturatedFatContent']}\n"
                    f"  - Cholesterol: {row['CholesterolContent']}\n"
                    f"  - Sodium: {row['SodiumContent']}\n"
                    f"  - Carbohydrates: {row['CarbohydrateContent']}\n"
                    f"  - Fiber: {row['FiberContent']} | Sugar: {row['SugarContent']}\n"
                    f"  - Protein: {row['ProteinContent']}\n"
                    f"- **Servings**: {row['RecipeServings']} | **Yield**: {row['RecipeYield']}\n"
                    f"- **Instructions**: {row['RecipeInstructions']}\n"
                )
                for _, row in recommendations.iterrows()
            ]
        )

        #recommendations_text = "\n".join(
        #    [f"- {row['Name']}" for _, row in recommendations.iterrows()]
        #)

        return recommendations_text

    def chat_and_recommend(self, user_input, dietary_restrictions=None):
        """
        Combines chat-based interaction and filtered recommendation system.
        """
        # Get recommendation based on user input and current filters
        recommendations = self.filter_and_recommend(user_input, dietary_restrictions)

        # Return both the agent's response and the recipe recommendations
        return super().receive_message(message=f"User input: '{user_input}', AI recommendation: {recommendations}",history=False)
