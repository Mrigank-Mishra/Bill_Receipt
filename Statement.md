# Problem Statement
The lack of a quick, automated system for calculating sales totals, applying taxes, and generating itemized receipts leads to slow checkout times and potential human error in manual calculations. The core problem is the need for a simple, digital solution to efficiently process customer purchases based on a fixed inventory list, ensuring accurate tax calculation and clear record-keeping for each transaction.

# Scope of the Project
The scope of this project is strictly limited to a console-based billing transaction simulation.
In Scope: Defining a fixed inventory with unit prices, interactively processing a single customer transaction (cart), validating item input, calculating the subtotal, applying a fixed 5% GST, and displaying a final receipt summary. The system manages the flow from item entry to final bill calculation.
Out of Scope: This project does not include persistent data storage (e.g., saving transactions to a file or database), advanced inventory management (e.g., tracking stock levels), handling variable tax rates, generating user accounts, or featuring a graphical user interface (GUI).

# Target Users
The system is designed for individuals who directly interact with customers to process sales transactions.
Primary User: The Cashier or Store Clerk, who will operate the system via the command line, inputting item names and quantities as customers check out.
Secondary User: A Store Owner or Manager who may use the system to understand fundamental billing logic or verify transaction calculations.

# High-Level Features
The program offers the following core capabilities:
Inventory Display and Access: The program starts by clearly displaying the available products and their corresponding unit prices, which are loaded from a hardcoded list.
Interactive Cart Management: Users can input multiple items and quantities in a continuous loop. The system validates whether the entered item exists before updating the cart.
Automatic Quantity Accumulation: The program correctly tracks and aggregates the total quantity of any item added more than once.
Sales Calculation: The system performs comprehensive financial processing, including calculating line totals, accumulating the subtotal, applying the fixed 5% GST, and determining the grand total.
Receipt Generation: A final, itemized receipt is outputted to the console, providing a clear summary of all purchased items and the final costs.
