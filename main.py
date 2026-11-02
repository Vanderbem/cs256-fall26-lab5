# ==============================================================================
# LAB 6: Campus Cafe using Funtions and Loops
# Add YOUR NAME HERE
# ==============================================================================

# ------------------------------------------------------------------------------
# TASK 1: Initialize Menu 
# ------------------------------------------------------------------------------
def initialize_menu(num_items):
    # TODO: Initialize and return the menu & prices for a given number of items
    pass
  
# ------------------------------------------------------------------------------
# TASK 2: Collect Customer Order 
# ------------------------------------------------------------------------------
def collect_customer_order(menu_prices):
    # TODO: Interactively prompts user for item names and quantities they wish to purchase
    #       Return the order
    pass

# ------------------------------------------------------------------------------
# TASK 3: Calculate bill 
# ------------------------------------------------------------------------------
def caculate_bill(order_items, menu_prices):
    # TODO: Calculate and return the total cost of the order based on menu prices.
    #      Print subtotal charges for each item
    pass


# ------------------------------------------------------------------------------
# MAIN: Orchestrates menu initialization, order collection and bill calculation
# ------------------------------------------------------------------------------
def main():
    print("--- WELCOME TO CAMPUS CAFE ---")
    print(" Let's populate the menu and prices for the cafe.")
    # Prompt user for number of menu items and then initialize menu
    print("\n.... time for place your order ....\n")
    # Collect order from user and print the oder
    print()
    print("Order Collected:") # print order here
    print("\n Time to calculate the bill ....\n")
    print()
    # Caclulate bill
    print(f"Total Cost: $") # print total cost here


# --- Run System ---
if __name__ == "__main__":
    main()
