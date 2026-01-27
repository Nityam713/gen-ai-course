# Task 1: Discount Rules

print("------------------------------------------")
print("-----------------# Task 1-----------------")

try:
    order_amount = int(input("Enter the order amount: "))
except ValueError:
    print("Please enter an integer")
    exit()

if order_amount >= 2000:
    discount =  0.15
elif order_amount >= 1500 and order_amount < 2000:
    discount = 0.10
elif order_amount >= 1000 and order_amount < 1500:
    discount = 0.07
else:
    discount = 0

discount_amount = order_amount * discount
subtotal = order_amount - discount_amount

tax_rate = 0.05
tax = subtotal * tax_rate
final_amount = subtotal + tax

print("subtotal:", subtotal)
print("tax:", tax)
print("final_amount:", final_amount)

print("------------------------------------------")
print("-----------------# Task 2-----------------")


# Task 2: Process Multiple Orders

orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discounted_orders_count = 0

print("Order Amount | Discount % | Final Amount")
print("------------------------------------------")

for order in orders:
    if order >= 2000:
        discount_rate = 0.15
    elif order >= 1500:
        discount_rate = 0.10
    elif order >= 1000:
        discount_rate = 0.07
    else:
        discount_rate = 0.0

    discount_amount = order * discount_rate
    final_amount = order - discount_amount

    # Count discounted orders
    if discount_rate > 0:
        discounted_orders_count += 1

    # Add to total revenue
    total_revenue += final_amount

    # Print summary row
    print(order, " | ", int(discount_rate * 100), "% | ", final_amount)

print("------------------------------------------")
print("Total revenue after discounts:", total_revenue)
print("Number of orders with discount:", discounted_orders_count)

# Task 3: User Menu (while loop + break/continue)

print("------------------------------------------")
print("-----------------# Task 3-----------------")

Order = []

while True:
    print("\nMenu:")
    print("1 - Add order amount")
    print("2 - Show all orders and totals after discount")
    print("q - Quit")

    choice = input("Enter your choice: ")

    try:
        if choice == "q":
            print("Exiting the program...") 
            break
        elif choice == "1":
            try:
                order_amount = int(input("Enter the order amount: "))
                Order.append(order_amount)
                print("Order added successfully")
            except ValueError:
                print("Please enter an integer")
                continue
        elif choice == "2":
            if not Order:
                print("No orders added yet")
                continue
            
            total_revenue = 0

            print("\nOrder Amount | Discount % | Final Amount")
            print("------------------------------------------")

            for order in Order:
                if order >= 2000:
                    discount_rate = 0.15
                elif order >= 1500:
                    discount_rate = 0.10
                elif order >= 1000:
                    discount_rate = 0.07
                else:
                    discount_rate = 0.0

                final_amount = order - (order * discount_rate)
                total_revenue += final_amount

                print(order, " | ", int(discount_rate * 100), "% | ", final_amount)

            print("------------------------------------------")
            print("Total revenue after discounts:", total_revenue)
            continue
        else:
            raise ValueError("Invalid choice")
    except ValueError as e:
        print("Invalid choice, please try again. Enter 1, 2, or q")
        continue

# Task 4: Loop Control with Conditions (break & continue)

print("------------------------------------------")
print("-----------------# Task 4-----------------")

daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

for sale in daily:
    try:
        if sale == -1:
            print("Corrupted data, stopping the loop")
            break
        elif sale == 0:
            print("No sales, skipping this day")
            continue
        else:
            total_sales += sale
            print("Adding sales for this day:", sale)
    except ValueError:
        print("Invalid data, please enter a valid number")
        continue

print("Final total after the loop completes:", total_sales)