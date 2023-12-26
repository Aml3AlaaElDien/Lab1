def determine_vegetable_preference():
    soup_items = ['vegetables', 'seafood', 'mushroom']
    meal_items = ['burger', 'grilled chicken', 'mashed potatoes']

    soup_order = input("Enter Engy's soup order: ").lower()
    meal_order = input("Enter Engy's main dish order: ").lower()

    if all(vegetable in soup_order for vegetable in soup_items) and all(vegetable not in meal_order for vegetable in soup_items):
        print("She loves vegetables.")
    else all(vegetable not in soup_order for vegetable in soup_items) and all(vegetable not in meal_order for vegetable in soup_items):
        print("She hates vegetables.")

determine_vegetable_preference()
