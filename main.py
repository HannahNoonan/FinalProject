import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

McDonalds_menu = pd.read_csv("McDonald's Nutritional Info.csv")

print(McDonalds_menu.head())

McDonalds_menu.info()

calories_per_item = McDonalds_menu[["Category", "Item", "Calories"]]
print(calories_per_item)
McDonalds_menu_ind = calories_per_item.set_index("Item")
print(McDonalds_menu_ind)
highest_cals = calories_per_item.sort_values(["Calories", "Item", "Category"], ascending=[False, True, True]).drop_duplicates("Category")
print(highest_cals)

sns.barplot(data=highest_cals, y="Calories", x="Item", hue="Category", dodge=False)
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.5, top=.95)
plt.title('Highest Calorie Item per Category')
plt.xlabel('Item')
plt.ylabel('Calories')
plt.show()







# Second - %fat in the top 5 calorie items

Fat_Calorie_items = McDonalds_menu[["Category", "Item", "Calories", "Calories from Fat"]].sort_values([
    "Calories","Calories from Fat", "Item", "Category"],
    ascending=[False, False, True, True]).drop_duplicates("Category").head(5)
print(Fat_Calorie_items)


Item = ["Chicken McNuggets (40 piece)", "Big Breakfast with Hotcakes (Large Biscuit)",
         "McFlurry with M&M’s Candies (Medium)", "Frappé Chocolate Chip (Large)",
         "Double Quarter Pounder with Cheese"]
Total_Cals = [1880, 1150, 930, 760, 750]
Fat_Cals = [1060, 540, 290, 290, 280]
d = {"Item": Item, "Total_Cals": Total_Cals, "Fat_Cals": Fat_Cals}

Cals_per_top_five = pd.DataFrame(d)
#print(Cals_per_top_five)

Cals_per_top_five['Perc_Cals_from_Fat'] = (Cals_per_top_five['Fat_Cals'] / Cals_per_top_five['Total_Cals']) *100
Cals_per_top_five['Perc_Cals_from_Fat'] = np.round(Cals_per_top_five['Perc_Cals_from_Fat'], decimals=2)
print(Cals_per_top_five)









