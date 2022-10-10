from enum import Enum

from pydantic import BaseModel


class IntolernaceEnum(str, Enum):
    alcohol_free = 'alcohol-free'
    immuno_supportive = 'immuno-supportive'
    celery_free = 'celery-free'
    crustacean_free = 'crustacean-free'
    dairy_free = 'dairy-free'
    dash = 'DASH'
    egg_free = 'egg-free'
    fish_free = 'fish-free'
    fodmap_free = 'fodmap-free'
    gluten_free = 'gluten-free'
    keto_friendly = 'keto-friendly'
    kidney_friendly = 'kidney-friendly'
    kosher = 'kosher'
    low_potassium = 'low-potassium'
    lupine_free = 'lupine-free'
    mediterranean = 'Mediterranean'
    mustard_free = 'mustard-free'
    low_fat_abs = 'low-fat-abs'
    no_oil_added = 'No-oil-added'
    low_sugar = 'low-sugar'
    paleo = 'paleo'
    peanut_free = 'peanut-free'
    pecatarian = 'pecatarian'
    pork_free = 'pork-free'
    red_meat_free = 'red-meat-free'
    sesame_free = 'sesame-free'
    shellfish_free = 'shellfish-free'
    soy_free = 'soy-free'
    sugar_conscious = 'sugar-conscious'
    tree_nut_free = 'tree-nut-free'
    vegan = 'vegan'
    vegetarian = 'vegetarian'


class Intolerance(BaseModel):
    intolerance_id: int
    intolerance_name: IntolernaceEnum
    intolerance_type: str
