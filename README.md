# The Kiosk Manager

A command-line stock and sales manager for a small Nairobi kiosk. It tracks inventory, records sales, produces a sales report, searches products, and saves everything to files so the data is still there the next time the program runs.

This is the group capstone project for Sessions 1 to 6 (variables, conditionals, loops, functions, data structures, and strings and files).

## What it does

| Feature | Description |
|---|---|
| **Welcome and setup** | Asks for the kiosk name and owner's name, cleans them with `.strip()` and `.title()`, and prints a welcome banner. |
| **Main menu** | A `while True` loop that runs until the user chooses Exit. Letters, empty input and out-of-range numbers print a friendly message instead of crashing. |
| **View stock** | Prints the whole inventory as a neat table with aligned columns. |
| **Add / restock a product** | Adds quantity to an existing product, or creates a new product with a price and quantity. Rejects non-numeric price or quantity. |
| **Sell a product** | Asks which product and how many units, checks there is enough stock, reduces the stock, works out the total in KES and records the sale. |
| **Sales report** | Lists every sale, the total revenue, how many unique products were sold, and the best-selling product by quantity. |
| **Search products** | Finds products from part of a name, ignoring upper and lower case, and shows each match with its price and quantity. |
| **Save and load** | Loads the inventory from `inventory.txt` at startup (or starts with a default one), and saves the inventory and the session's sales on exit. |

## Requirements

- **Python 3.12 or newer.** The code puts quotes of the same type inside f-strings (for example `f'{details['price']}'`), which older versions reject with a `SyntaxError`.
- No extra packages. It uses only built-in Python.

## How to run

```bash
python My_Kiosk.py
```

Follow the prompts. Choose **6** to exit, which saves your data.

## Main menu

```
===== MAIN MENU =====
1. View Stock
2. Add/Restock a Product
3. Sell a Product
4. View Sales Report
5. Search Products
6. Exit
```

## Example session

```
Enter your Kiosk Name: navas
Enter the Kiosk Owner: navas herbert
Welcome to Navas kiosk Manager, run by Navas Herbert

===== MAIN MENU =====
Enter your choice: 3
Which product? bread
How many units? 5
sold 5 Bread for KES 325

Enter your choice: 6
Saving data... Goodbye!
```

## How the skills are used

| Session | Where it shows up |
|---|---|
| 1. Basics | `input()` prompts, `int` conversions, f-string output throughout |
| 2. Conditionals | Stock checks before a sale, menu validation, duplicate-product handling |
| 3. Loops | The `while True` menu loop; `for` loops over stock and sales |
| 4. Functions | Every feature is its own function, called from a short `main()` |
| 5. Data structures | See the table below |
| 6. Strings and files | `.strip()`, `.title()`, `.lower()`, `.isdigit()`, `in` for search; reading and writing `.txt` files |

### Data structures

| Structure | Used for |
|---|---|
| **Dictionary** | `stock`: `{'Bread': {'price': 65, 'quantity': 20}, ...}` |
| **List** | `sales_log`: every sale made in the session |
| **Tuple** | Each sale: `(item, quantity, total)` |
| **Set** | `sold_set`: the unique product names sold in the session |

## Functions

| Function | Purpose |
|---|---|
| `welcome()` | Asks for the kiosk and owner names and prints the banner |
| `load_inventory(filename)` | Reads the inventory file, or returns the default inventory if the file does not exist yet |
| `save_inventory(stock, filename)` | Writes the inventory to the file (overwrites) |
| `save_sales(sales_log, filename)` | Appends this session's sales to the sales file |
| `view_stock(stock)` | Prints the inventory table |
| `add_product(stock)` | Adds a new product or restocks an existing one |
| `sell_product(stock, sales_log, sold_set)` | Validates, sells, and records a sale |
| `sales_report(sales_log, sold_set)` | Prints the sales, total revenue, unique products and best seller |
| `search_products(stock)` | Partial, case-insensitive product search |
| `main()` | The menu loop that connects everything |

## Data files

The program creates these files in the folder it is run from.

| File | Format | Behaviour |
|---|---|---|
| `inventory.txt` | One product per line: `item,price,quantity` (e.g. `Bread,65,20`) | Loaded on startup, overwritten on exit |
| `sales.txt` | One sale per line: `item,quantity,total` (e.g. `Bread,5,325`) | Appended on exit, so sales history is kept |

If `inventory.txt` does not exist, the program starts with a default inventory: Bread (KES 65, 20 units) and Milk (KES 50, 10 units).




