from .agent import Agent
from data.handler.vectorizer import Vectorizer
from data.handler.csv_handler import CSVHandler
from config import USING_RAG

class RecommendationAgent(Agent):
    def __init__(self, context="You are a dietary assistant that recommends meals based on user preferences and dietary restrictions.",file="data/datasets/NewRecipes.csv", using_rag=USING_RAG):
        super().__init__(context)
        self.using_rag = using_rag
        if self.using_rag:
            self.csv_handler = CSVHandler(file)
            self.dataset = self.csv_handler.get_dataset()
            self.vectorizer = Vectorizer(self.dataset)
        self.dietary_restrictions = {}

    def update_filters(self, dietary_restrictions):
        """
        Update the dietary restrictions filters.
        :param dietary_restrictions: Dictionary containing new dietary restrictions.
        """
        if not(dietary_restrictions is None or dietary_restrictions==self.dietary_restrictions):
            self.dietary_restrictions = dietary_restrictions 

            if self.using_rag:
                filtered_recipes = self.csv_handler.filter_recipes(dietary_restrictions)

                if filtered_recipes.empty:
                    return "No recipes match your dietary restrictions."

                self.vectorizer = Vectorizer(filtered_recipes)

    def filter_and_recommend(self, user_input, dietary_restrictions=None):
        """
        Get a recommendation based on user input and filter recipes by dietary restrictions.
        If no dietary restrictions are passed, it uses the agent's current filters.
        """
        self.update_filters(dietary_restrictions=dietary_restrictions)

        if self.using_rag:
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
        else:
            recommendations_text = ""


        return recommendations_text

    def refine_prompt(self, user_input):
        """
        Get the user input and changes the text to obtain a valid text for the rag
        """
        return super().receive_message(message=f"Refine this prompt to focus on the text we are going to send the RAG, wirte only the new prompt: {user_input}",history=False)
        

    def chat_and_recommend(self, user_input, dietary_restrictions=None):
        """
        Combines chat-based interaction and filtered recommendation system.
        """
        # Create new prompt to the RAG
        if self.using_rag:
            prompt = self.refine_prompt(user_input=user_input)
        else: 
            prompt = ""

        # Get recommendation based on user input and current filters
        recommendations = self.filter_and_recommend(prompt, dietary_restrictions)

        # Get array of allergies
        allergies = "El usuario tiene las alergias: '"
        for key, value in dietary_restrictions.items():
            if value:
                allergies += key.lower().replace("has","")+", "
        allergies += "'"

        # Return both the agent's response and the recipe recommendations
        return super().receive_message(message=f"Devuelve respuesta en español. Usuario dice: '{user_input}',{allergies}, recomendación de la ia: {recommendations}",history=False)
