# Menu Items with Prices
menu = {
    "Tea": 10,
    "Coffee": 20,
    "Sandwich": 50,
    "Burger": 70,
    "Pizza": 120
}

order = {}  # Stores ordered items


# Function to show menu
def show_menu():
    print("\n===== Café Menu =====")
    for item, price in menu.items():
        print(f"{item}: Rs.{price}")
    print("=====================")


# Function to take customer order
def take_order():
    while True:
        item = input("\nEnter item to order (or type 'done' to finish): ").capitalize()
        if item == "Done":
            break
        elif item in menu:
            qty = int(input(f"Enter quantity of {item}: "))
            order[item] = order.get(item, 0) + qty
        else:
            print("❌ Item not in menu. Try again!")


# Function to generate bill
def generate_bill(customer_name):
    print("\n===== Bill =====")
    bill_lines = []
    bill_lines.append(f"Customer: {customer_name}\n")
    total = 0

    for item, qty in order.items():
        price = menu[item] * qty
        bill_lines.append(f"{item} x {qty} = Rs.{price}")
        total += price

    # GST and Discount
    gst = total * 0.05
    discount = 0
    if total > 200:  # Example: discount if bill > 200
        discount = total * 0.10

    final_total = total + gst - discount

    bill_lines.append(f"\nSubtotal       = Rs.{total}")
    bill_lines.append(f"GST (5%)       = Rs.{gst:.2f}")
    bill_lines.append(f"Discount (10%) = -Rs.{discount:.2f}")
    bill_lines.append(f"Total Bill     = Rs.{final_total:.2f}")
    bill_lines.append("\n✅ Thank you for visiting our cafe!")

    # Print on screen
    print("\n".join(bill_lines))

    # Save to file (UTF-8 safe)
    with open("bill.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(bill_lines))


# Main function
def main():
    print("☕ Welcome to Cafe ☕")
    customer_name = input("Enter Customer Name: ")
    show_menu()
    take_order()
    if order:  # Only if order is not empty
        generate_bill(customer_name)
    else:
        print("⚠ No items ordered. Bill not generated.")


# Run program
if __name__ == "__main__":

    main()
