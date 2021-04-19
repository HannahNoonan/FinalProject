import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

McDonalds_menu = pd.read_csv("McDonald's Nutritional Info.csv")

print(McDonalds_menu.head())

McDonalds_menu.info()

calories_per_item = McDonalds_menu[["Category","Item","Calories"]]
print(calories_per_item)
McDonalds_menu_ind = calories_per_item.set_index("Item")
print(McDonalds_menu_ind)
highest_cals = calories_per_item.sort_values(["Calories","Item","Category"],ascending=[False,True,True]).drop_duplicates("Category")
print(highest_cals)

sns.barplot(data=highest_cals, y="Calories", x="Item", hue="Category",dodge=False)
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.5, top=.95)
plt.title('Highest Calorie Item per Category')
plt.xlabel('Item')
plt.ylabel('Calories')
plt.show()

