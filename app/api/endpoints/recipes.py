from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List

from app.services.recipe_service import RecipeService
from app.models.recipe import Recipe
from app.sample_data import sample_recipes
from app.utils import decode_jwt

router = APIRouter()
recipe_service = RecipeService(recipes=sample_recipes)

def get_meal_by_id(recipe_id: str) -> Recipe:
    for recipe in sample_recipes:
        print(recipe_id)
        print(recipe["id"])
        if recipe["id"] == recipe_id:
            return Recipe(**recipe)
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.get("/meals/{meal_id}", response_model=Recipe)
def read_recipe(recipe_id: str):
    return get_meal_by_id(recipe_id)

@router.get("/recommendations", response_model=List[Recipe])
def get_recommendations(num_recommendations:int, account=Depends(decode_jwt)):
    recommendations = recipe_service.get_recommendations(account.id, num_recommendations)
    return recommendations

@router.get("/random", response_model=List[Recipe])
def get_recommendations():
    recommendations = recipe_service.get_random()
    return recommendations

@router.get("/search", response_model=List[Recipe])
def search_recipes(query: str):
    matched_recipes = [recipe for recipe in sample_recipes if query.lower() in recipe["strMeal"].lower()]
    if not matched_recipes:
        raise HTTPException(status_code=404, detail="No recipes found for the given query")
    return matched_recipes

@router.get("/recommendations/ingredients", response_model=List[Recipe])
def recommend_recipes_by_ingredients(ingredients: List[str] = Query(..., min_length=1, description="List of ingredients the user has"),  account=Depends(decode_jwt)):
    recommended_recipes = recipe_service.get_recommendations_by_ingredients(account.id, ingredients)
    
    if not recommended_recipes:
        raise HTTPException(status_code=404, detail="No recommendations found for the given ingredients")
    
    return recommended_recipes

@router.get("/filter_by_area", response_model=List[Recipe])
def filter_recipes_by_area(area: str = Query(..., min_length=1, description="Filter recipes by area")):
    filtered_recipes = [recipe for recipe in sample_recipes if recipe["strArea"].lower() == area.lower()]
    
    if not filtered_recipes:
        raise HTTPException(status_code=404, detail="No recipes found for the given area")
    
    return filtered_recipes
