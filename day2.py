#Calculate the Total Revenue
#List Low Stock item if Stock is Less than 5
#Calculte the Category-Wise Revenue

inventory = [
    # name,       category,   unit_price, units_sold, units_left
    
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]

#1st question
for i in inventory:
    p=i[2]
    s=i[3]
    r=p*s
print(r)
print(f"----------------------------------")
#2nd question
for i in inventory:
    if i[4]<5:
        print(i[0])
print(f"--------------------------------------")

#3rd question
for it in inventory:
    c=it[1]
    p=it[2]
    s=it[3]
    r=p*s
    print(r)
