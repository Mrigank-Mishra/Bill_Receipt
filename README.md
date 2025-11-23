# Bill Receipt 

# Overview of the Project
This project is a fundamental Python script that simulates a basic checkout system. It utilizes core Python concepts, specifically dictionaries, to manage inventory and transactions. The program allows a user (cashier) to interactively add items and quantities to a cart, validates the inputs, applies a Goods and Services Tax (GST), and generates a detailed, itemized receipt at the end of the transaction.

# Features
The program offers several key features:
Fixed Inventory Management: A dictionary (grocery_items) holds the predefined stock and unit prices.
Interactive Cart System: A continuous loop accepts item names and quantities purchased until the user enters "done."
Input Validation: The system confirms the item entered by the user exists in the inventory.
Quantity Accumulation: If the same item is entered multiple times, the script correctly adds the new quantity to the existing count in the cart.
Tax Calculation: A fixed 5% tax (GST) is applied to the calculated subtotal.
Comprehensive Receipt: The final output is an itemized bill that clearly displays the subtotal, the calculated GST amount, and the final grand total.

# Technologies/Tools Used
This project relies on standard, built-in components and requires minimal setup:
Language: Python 3.x is the sole programming language used.
Runtime: Any standard Python 3 interpreter environment.
Tools: A basic Command Line Interface or Terminal for running the script and providing input.
Libraries: None—the project uses only built-in Python data types and functions.
Steps to Install & Run the Project
Since this is a single, dependency-free script, installation is straightforward.

# Prerequisites
Ensure you have Python 3.x installed on your operating system.
Installation & Execution Instructions
Save the Code: Copy the entire program code and save it into a file named billing_program.py.
Open Terminal: Navigate to the directory where you saved the file.
Run the Script: Execute the file using the Python interpreter.
Interaction: The program will immediately start by displaying the available menu and waiting for your item input.

# Instructions for Testing
Test the program's core functionalities using these scenarios:
Test Case A: Item Accumulation and Subtotal
Action: Add Rice (quantity: 1), then add Rice again (quantity: 3).
Expected Result: The final cart should show Rice (x4). The subtotal should be calculated based on 4 units ($\text{4} \times \text{₹}45 = \text{₹}180$).
Test Case B: Tax Calculation
Action: Add Milk (quantity: 2) and Bread (quantity: 1), then type done.
Expected Logic: Subtotal ($\text{2} \times \text{₹}30) + (\text{1} \times \text{₹}25) = \text{₹}85$.
Expected Result: GST will be $\text{₹}85 \times 0.05 = \text{₹}4.25$. The Grand Total will be $\text{₹}89.25$ (displayed as ₹89 due to integer conversion).
Test Case C: Input Validation
Action 1: Enter an item name that doesn't exist (e.g., Coffee).
Expected Result 1: The program prints "Item not found! Please try again." and returns to the input prompt without crashing.
Action 2: Enter an item name with incorrect capitalization (e.g., milk).
Expected Result 2: Prints "Item not found! Please try again." as the program is case-sensitive.
