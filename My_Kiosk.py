
def welcome():
    Kiosk_name = input('Enter your Kiosk Name: ').strip().title()
    Owners_name = input('Enter the Kiosk Owner: ').title().strip()
    print(f'Welcome to {Kiosk_name} kiosk Manager, run by {Owners_name.title()}')
    return Kiosk_name, Owners_name

# --------- File Handling -------
def load_inventory(filename='inventory.txt'):
    stock = {}
    try:
        with open (filename, 'r') as f:
            for line in f:
                item, price, qty = line.strip().split(',')
                stock[item] = {'price': int(price), 'quantity': int(qty)}
    except FileNotFoundError:
        # File doesn't exist yet --> start with default inventory
        stock = {'Bread': {'Price': 65, 'quantity': 20},
                 'Milk': {'Price': 50, 'quantity': 10}}
        return stock

def save_inventory(stock, filename='inventory.txt'):
    with open(filename, 'w') as f:
        for item, details in stock.items():
            f.write(f'{item},{details['price']},{details['quantity']}\n')

def save_sales(sales_log, filename='sales.txt'):
    with open(filename, 'a') as f:
        for sale in sales_log:
            f.write(f'{sale[0]}2,{sale[1]},{sale[2]}\n')

# ------- Inventory ------
def view_stock(stock):
    print('\n==== Inventory ====')
    print(f'{'Product':<12}{'Price':<10}')
    for item, details in stock.items():
        print(f'{item:<12}{details['Price']:<10}{details['quantity']:<10}')

def add_product(stock):
    item = input('Product name: ').strip().title()
    price = input('Price: ')
    qty = input('Quantity: ')
    if not price.isdigit():
        print('Invalid input! price must be numbers.')
    if not qty.isdigit():
        print('Invalid input! quantity must be numbers.')
        return
    price, qty = int(price), int(qty)
    if item in stock:
        stock[item]['quantity'] += qty
    else:
        stock[item] = {'Price': price, 'quantity': qty}
    print(f'{item} updated!')

# ----- Selling -----
def sell_product(stock, sales_log, sold_set):
    item = input('Which product? ').strip().title()
    if item not in stock:
        print('Product not found!')
        return
    qty = input('How many units? ')
    if not qty.isdigit():
        print('Invalid input! Quantity must be a number.')
        return
    qty = int(qty)
    if stock[item]['quantity'] < qty:
        print('Not enough stock!')
        return
    total = stock[item]['Price'] * qty
    stock[item]['quantity'] -= qty
    sales_log.append((item, qty, total))
    sold_set.add(item)
    print(f'sold {qty} {item} for KES {total}')

# ------- Sales Report --------
def sales_report(sales_log, sold_set):
    total_revenue = sum(sale[2] for sale in sales_log)
    print('\n=== Sales Report ===')
    for sale in sales_log:
        print(f'{sale[0]}*{sale[1]} = KES {sale[2]}')
    print(f'\nTotal revenue: KES {total_revenue}')
    print(f'Unique products sold: {len(sold_set)}')

    if sales_log:
        best = max(sales_log, key=lambda s: s[1]) #by quantity
        print(f'Best-Selling product: {best[0]} ({best[1]} units)')

# -------- Search -----
def search_products(stock):
    term = input('Enter search term: ').strip().lower()
    matches = [item for item in stock if term in item.lower()]
    if matches:
        print('\nMatches Found:')
        for item in matches:
            print(f'{item} - price: {stock[item]['price']}, Qty: {stock[item]['quantity']}')
    else:
        print('No matches found')

# ------ Main -----
def main():
    Kiosk_name, Owners_name = welcome()
    stock = load_inventory()
    sales_log = []
    sold_set = set()

    while True:
        print("\n===== MAIN MENU =====")
        print("1. View Stock\n2. Add/Restock a Product\n3. Sell a Product\n4. View Sales Report\n5. Search Products\n6. Exit")
        choice = input("Enter your choice: ")
        if not choice.isdigit():
            print("Invalid input!")
            continue
        choice = int(choice)

        if choice == 1: view_stock(stock)
        elif choice == 2: add_product(stock)
        elif choice == 3: sell_product(stock, sales_log, sold_set)
        elif choice == 4: sales_report(stock, sales_log, sold_set)
        elif choice == 5: search_products(stock)
        elif choice == 6:
            print('Saving data... Goodbye!')
            save_inventory(stock)
            save_sales(sales_log)
            break
        else: print('Invalid choice!')

if __name__ == '__main__':
    main()







