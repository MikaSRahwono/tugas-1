from typing import List, Optional
from pydantic import BaseModel

class Recipe(BaseModel):
    id: int
    strMeal: str
    strDrinkAlternate: Optional[str] = None
    strCategory: str
    strArea: str
    strInstructions: str
    strMealThumb: str
    strTags: Optional[str] = None
    strYoutube: Optional[str] = None
    strIngredient1: Optional[str] = None
    strIngredient2: Optional[str] = None
    strIngredient3: Optional[str] = None
    strIngredient4: Optional[str] = None
    strIngredient5: Optional[str] = None
    strIngredient6: Optional[str] = None
    strIngredient7: Optional[str] = None
    strIngredient8: Optional[str] = None
    strIngredient9: Optional[str] = None
    strIngredient10: Optional[str] = None
    strIngredient11: Optional[str] = None
    strIngredient12: Optional[str] = None
    strIngredient13: Optional[str] = None
    strIngredient14: Optional[str] = None
    strIngredient15: Optional[str] = None
    strIngredient16: Optional[str] = None
    strIngredient17: Optional[str] = None
    strIngredient18: Optional[str] = None
    strIngredient19: Optional[str] = None
    strIngredient20: Optional[str] = None
    strMeasure1: Optional[str] = None
    strMeasure2: Optional[str] = None
    strMeasure3: Optional[str] = None
    strMeasure4: Optional[str] = None
    strMeasure5: Optional[str] = None
    strMeasure6: Optional[str] = None
    strMeasure7: Optional[str] = None
    strMeasure8: Optional[str] = None
    strMeasure9: Optional[str] = None
    strMeasure10: Optional[str] = None
    strMeasure11: Optional[str] = None
    strMeasure12: Optional[str] = None
    strMeasure13: Optional[str] = None
    strMeasure14: Optional[str] = None
    strMeasure15: Optional[str] = None
    strMeasure16: Optional[str] = None
    strMeasure17: Optional[str] = None
    strMeasure18: Optional[str] = None
    strMeasure19: Optional[str] = None
    strMeasure20: Optional[str] = None
    strSource: Optional[str] = None
    strImageSource: Optional[str] = None
    strCreativeCommonsConfirmed: Optional[str] = None
    dateModified: Optional[str] = None