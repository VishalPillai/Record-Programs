emp = {'John': {'January': 4500, 'February': 5200, 'March': 4800},
       'Emily': {'January': 6000, 'February': 6200, 'March': 5800},
       'Anu': {'January': 7000, 'February': 7500, 'March': 7200}}

def increase_sales():
    for name in emp:
        avg = sum(emp[name].values()) / len(emp[name])
        if avg > 6000:
            for m in emp[name]:
                emp[name][m] = emp[name][m] * 1.10
    print(emp)
    print()

def highest_month():
    for name, sales in emp.items():
        highest = 0
        highest_month_name = ""
        
        for month, amount in sales.items():
            if amount > highest:
                highest = amount
                highest_month_name = month
                
        print(name, "had highest sales in", highest_month_name, "with sales", highest)
        print()

def vowel_names():
    for name in emp:
        if name[0].lower() in 'aeiou':
            print(name, emp[name])

increase_sales()
highest_month()
vowel_names()
