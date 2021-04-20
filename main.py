import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

McDonalds_menu = pd.read_csv("McDonald's Nutritional Info.csv")

# check null values
print(McDonalds_menu.isnull().sum())

print(McDonalds_menu.head())

McDonalds_menu.info()


#First - Highest Calorie item per category

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

np_TotalCals = np.array(Total_Cals)
print(np_TotalCals)
np_FatCals = np.array(Fat_Cals)
print(np_FatCals)

Cals_per_top_five['Perc_Cals_from_Fat'] = np_FatCals / np_TotalCals *100
Cals_per_top_five['Perc_Cals_from_Fat'] = np.round(Cals_per_top_five['Perc_Cals_from_Fat'],
                                                   decimals=2)
Cals_per_top_five['Perc_Cals_Other'] = 100 - Cals_per_top_five['Perc_Cals_from_Fat']
print(Cals_per_top_five)

print(Cals_per_top_five['Perc_Cals_from_Fat'] > 40)

Cals_per_top_five.plot(x='Item', y=["Perc_Cals_from_Fat","Perc_Cals_Other"], kind='bar')
plt.ylabel('Percentage')
plt.title("Percentage Calories from Fat of top five Calorie items")
plt.show()

# Third - Average Cals in each category Piechart

Cat_sorted = McDonalds_menu.set_index("Category").sort_index()
print(Cat_sorted.loc[:, "Calories"])

avg_cals_by_category = np.round(Cat_sorted.groupby("Category")["Calories"].mean())
print(avg_cals_by_category)

avg_cals_by_category.plot(kind='pie', subplots=True, figsize=(8, 8))
plt.title("Pie Chart of Average Calories per Category")
plt.ylabel("")
plt.show()


Chicken_and_Fish = 553

if Chicken_and_Fish <= 250 :
    print("The avg calories in this category is less than 250")
elif Chicken_and_Fish <= 500 :
    print("The avg calories in this category is less than 500")
else :
    print("The avg calories in this category is over 500")


avg_cals_list = [["Beef & Pork", 494.0],
                 ["Beverages", 114.0],
                ["Breakfast", 527.0],
                 ["Chicken & Fish", 553.0],
                 ["Coffee & Tea", 284.0],
                 ["Desserts", 222.0],
                 ["Salads", 270.0],
                 ["Smoothies & Shakes",531.0],
                 ["Snacks & Sides",246.0]]
for x in avg_cals_list :
    print("The avg cals in the " + x[0] + " category is " + str(x[1]) + " cals")


# 4 sodium

fig, ax = plt.subplots(1,2)

ax[0].scatter(McDonalds_menu['Category'], McDonalds_menu['Sodium'], color='b')
ax[1].scatter(McDonalds_menu['Category'], McDonalds_menu['Cholesterol'], color='g')
plt.xticks(rotation=90)
plt.show()