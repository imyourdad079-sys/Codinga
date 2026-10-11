# ===========================
# --- Recepie Explorer ---
# ===========================

pasta = ("Pasta Arrabiata", "Itallian", 20, "Medium")
biryani = ("Pasta Arrabiata", "Itallian", 20, "Medium")

print('Recepie 1:', pasta)
print('Name:', pasta[0])
print('Cuisine:', pasta[1])
print('Difficulty:', pasta[-1])

all_recepies = (pasta, biryani)
print('\nFirst recepie name:', all_recepies[0][0])
print('Second recepie time:', all_recepies[1][2] ,'mins')
print('Pasta detail (Slice):', pasta[1:3])

print('\nPasta Recipe details:')
for detail in pasta:
    print("-", detail)


pasta_ingredients = {"tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"}
biryani_ingredients = {"rice", "chicken", "garlic", "onion", "tomato", "spices"}

print('\nPasta ingredients:', pasta_ingredients)
print('Biryani ingredients:', biryani_ingredients)
print('Total pasta ingredients:', len(pasta_ingredients))

pasta_ingredients.add('parmesan')
pasta_ingredients.discard('chili')
print('Updated pasta ingredients:', pasta_ingredients)

all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print('\nAll ingredients (Union):', all_ingredients)
print('Common ingredients (Intersecton):', common)
print('Only in pasta (Diffirence):', only_pasta)
print('Not shared (Symmetric_Diffirence):', unique_to_each)