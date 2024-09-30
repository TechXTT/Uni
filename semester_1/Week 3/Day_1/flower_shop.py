# Fred sells bunches of flowers at the local shopping center and enters each sol bunch of flowers in the
# system by pressing “S” (Sold) followed by the name of the flowers (e.g. Roses) and the price (e.g.
# 12.30).
# One day Fred's boss, Joe, tells Fred that at any time during the day he (Joe) will need to know:
# • how many bunches of flowers have been sold
# • what was the value of the most expensive bunch sold
# • what was the value of the least expensive bunch sold
# • what is the average value of bunches sold
# He can print this information by pressing “I” (Information).

def print_menu():
    print("Welcome to the Flower Shop!")
    print("Press 'S' to enter a sale.")
    print("Press 'I' to get information.")
    print("Press 'Q' to quit.")

def main():
    sales = []
    while True:
        print_menu()
        choice = input("Enter choice: ")
        if choice == "S":
            name = input("Enter name of flowers: ")
            price = float(input("Enter price: "))
            sales.append({name: name, price: price})
        elif choice == "I":
            if len(sales) == 0:
                print("No sales have been made.")
            else:
                total_sales = 0
                max_price = 0
                min_price = float("inf")
                for sale in sales:
                    price = sale["price"]
                    total_sales += price
                    if price > max_price:
                        max_price = price
                    if price < min_price:
                        min_price = price
                average_price = total_sales / len(sales)
                print(f"Total sales: {len(sales)}")
                print(f"Most expensive sale: {max_price}")
                print(f"Least expensive sale: {min_price}")
                print(f"Average price: {average_price}")
        elif choice == "Q":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()