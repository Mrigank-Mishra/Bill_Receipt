# Grocery Store Billing Program
grocery_items = {
    "Rice": 45,
    "Maggii": 40,
    "Milk": 30,
    "Egg": 6,
    "Oil": 120,
    "Apple": 80,
    "Banana": 50,
    "Bread": 25
}
cart = {}
print("Available Items:")
for item, price in grocery_items.items():
    print(f"{item} - ₹{price}")
print("Welcome to Grocery Store")
while True:
    item_name = input("Enter item name to add to cart or type 'done' to finish : ")
    if item_name == "done":
        break
    elif item_name not in grocery_items:
        print("Item not found! Please try again.")
        continue
    qty = int(input("Enter quantity: "))
    cart[item_name] = cart.get(item_name, 0) + qty
print("BILL RECEIPT")
subtotal = 0
for item, qty in cart.items():
    price = grocery_items[item]
    total_price = price * qty
    subtotal += total_price
    print(f"{item} (x{qty}) - ₹{total_price}")
gst = subtotal * 0.05
grand_total = subtotal + gst
print("Subtotal: ₹", subtotal)
print("GST (5%): ₹", gst)
print("Grand Total: ₹", int(grand_total))
print("Thank you for shopping!")
