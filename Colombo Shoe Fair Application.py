# -------------------------------------------------------------
# Colombo Shoe Fair Online Booking System
# Author: [Your Name]
# Purpose: To simulate an online booking system using in-memory
#          data structures and algorithms (no file or DB storage).
# -------------------------------------------------------------

# Dictionary to store available items (Item Code: [Item Name, Unit Price])
items = {
    "S001": ["Men’s Leather Shoes", 5500.00],
    "S002": ["Women’s Heels", 4000.00],
    "S003": ["Casual Sneakers", 3200.00],
    "S004": ["Children’s Sandals", 2000.00],
    "S005": ["Running Shoes", 4800.00],
    "S006": ["Flip-Flops", 1200.00]
}

# Global in-memory order records (OrderNo: {items, payment_type, total})
orders = {}

# Function to display all available items
def display_items():
    print("\n--- Available Footwear Items ---")
    print(f"{'Code':<6} {'Item':<25} {'Price (LKR)':>10}")
    print("-" * 45)
    for code, details in items.items():
        print(f"{code:<6} {details[0]:<25} {details[1]:>10.2f}")
    print("-" * 45)

# Function to generate a unique order number
def generate_order_no():
    return f"ORD{1000 + len(orders) + 1}"

# Function to calculate total based on selected items
def calculate_total(selected_items):
    total = 0
    for code, qty in selected_items.items():
        total += items[code][1] * qty
    return total

# Function to create a new booking
def create_booking():
    display_items()
    selected_items = {}
    while True:
        code = input("Enter Item Code to add (or 'done' to finish): ").upper()
        if code == "DONE":
            break
        elif code in items:
            qty = int(input(f"Enter quantity for {items[code][0]}: "))
            selected_items[code] = selected_items.get(code, 0) + qty
        else:
            print("Invalid Item Code! Please try again.")

    if not selected_items:
        print("No items selected. Booking cancelled.")
        return

    subtotal = calculate_total(selected_items)
    order_no = generate_order_no()
    print(f"\nSubtotal for Order {order_no}: LKR {subtotal:.2f}")

    # Choose payment type
    print("\nPayment Options:\n1. Online Payment (3% fee)\n2. On-site Payment")
    choice = input("Enter option (1/2): ")

    if choice == "1":
        payment_type = "Online"
        total = subtotal * 1.03  # Add 3% fee
        print(f"3% online processing fee applied.")
    else:
        payment_type = "On-site"
        total = subtotal

    # Store order in memory
    orders[order_no] = {
        "items": selected_items,
        "payment_type": payment_type,
        "total": total
    }

    print(f"\nOrder Created Successfully! Order Number: {order_no}")
    print(f"Total Bill: LKR {total:.2f}")
    print("---------------------------------------------------")

# Function to add more items to existing on-site orders
def modify_order():
    order_no = input("Enter your existing Order Number: ").upper()
    if order_no not in orders:
        print("Order not found!")
        return
    if orders[order_no]["payment_type"] != "On-site":
        print("Only on-site payment orders can be modified.")
        return

    display_items()
    while True:
        code = input("Enter new Item Code to add (or 'done' to finish): ").upper()
        if code == "DONE":
            break
        elif code in items:
            qty = int(input(f"Enter quantity for {items[code][0]}: "))
            orders[order_no]["items"][code] = orders[order_no]["items"].get(code, 0) + qty
        else:
            print("Invalid Item Code!")

    # Recalculate total
    new_total = calculate_total(orders[order_no]["items"])
    orders[order_no]["total"] = new_total
    print(f"\nUpdated total for {order_no}: LKR {new_total:.2f}")
    print("Order successfully updated!")

# Function to search and display an order by order number
def search_order():
    order_no = input("Enter Order Number to search: ").upper()
    if order_no not in orders:
        print("Order not found!")
        return

    order = orders[order_no]
    print(f"\n--- Order Details for {order_no} ---")
    for code, qty in order["items"].items():
        print(f"{items[code][0]} (x{qty}) - LKR {items[code][1] * qty:.2f}")
    print(f"Payment Type: {order['payment_type']}")
    print(f"Total Bill: LKR {order['total']:.2f}")
    print("---------------------------------------------")

# Function to calculate total revenue from all orders
def calculate_revenue():
    total_revenue = sum(order["total"] for order in orders.values())
    print(f"\nTotal Revenue Generated: LKR {total_revenue:.2f}")
    print("---------------------------------------------")

# Main program loop
def main():
    while True:
        print("\n========== COLOMBO SHOE FAIR SYSTEM ==========")
        print("1. Create New Booking")
        print("2. Modify Existing On-site Order")
        print("3. Search Order by Order Number")
        print("4. Display Total Revenue")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_booking()
        elif choice == "2":
            modify_order()
        elif choice == "3":
            search_order()
        elif choice == "4":
            calculate_revenue()
        elif choice == "5":
            print("Exiting system... Thank you!")
            break
        else:
            print("Invalid option, please try again!")

# Run program
if __name__ == "__main__":
    main()
