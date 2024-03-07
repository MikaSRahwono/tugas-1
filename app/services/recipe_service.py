from typing import List
import random

from app.models.recipe import Recipe
from app.sample_data import sample_recipes

class RecipeService:
    def __init__(self, recipes):
        self.recipes = recipes

    def get_recommendations(self, user_id: int, num_recommendations: int) -> List[Recipe]:
        return self.recipes[:num_recommendations]
    
    def get_random(self) -> List[Recipe]:
        num = random.randint(11, len(sample_recipes) - 1)
        return self.recipes[num-10 : num]
    
    def get_recommendations_by_ingredients(self, user_id: int, user_ingredients: List[str]) -> List[Recipe]:
        matched_recipes = []
        
        for recipe in self.recipes:
            recipe_ingredients = [recipe.get(f"strIngredient{i}", "") for i in range(1, 21)]
            
            if all(ingredient.lower() in recipe_ingredients for ingredient in user_ingredients):
                matched_recipes.append(Recipe(**recipe))
        
        return matched_recipes[:10]