spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

def get_spiciest_foods(spicy_foods):
    spice_level = [food for food in spicy_foods if(food["heat_level"] >= 5)]
    return spice_level

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        spice_emoji = heat_level * "🌶"
        print(f"{name} ({cuisine}) | Heat Level: {spice_emoji}")
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    cuisine_origin = [food for food in spicy_foods if(food["cuisine"] == cuisine)]
    if cuisine_origin:
        return cuisine_origin[0]
    else:
        return None

def print_spiciest_foods(spicy_foods):
    my_list = get_spiciest_foods(spicy_foods)
    return print_spicy_foods(my_list)

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    average_heat = total_heat_level / len(spicy_foods)
    return average_heat

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
