# cs256-fall26-lab6
This repo contains a starter python file for Lab 5: A More Realistic Campus Cafe Order

## Overview
Functions allow us to break our code into reusable, modular blocks, eliminating repetitive logic. Loops allow us to execute lines of code multiple times until a specific stopping condition is met. 

In this lab, you will create a interactive Campus Cafe system that uses loops to construct a menu, collect a customer's order, and calculate their total bill. You will write **three helper functions** in addition to `main()`.

> **Rule of the Lab:** Write one function at a time, call and test it immediately in `main()` to verify it works, and only then move on to the next task!

---

## Getting Started (GitHub & VS Code Workflow)

1. **Fork this repository:** Click the **Fork** button in the top-right corner of this GitHub page to create a personal copy under your account.
2. **Clone to VS Code:**
   * Open VS Code.
   * Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) to open the Command Palette.
   * Type `Git: Clone` and press **Enter**.
   * Select **Clone from GitHub**, choose **your fork** (`YOUR-USERNAME/cs256-lab5-campus-cafe`), and select a folder on your computer.
   * Click **Open** when prompted.
3. **Open Starter File:** Open `main.py` to begin writing your solution.

---

## Functional & Technical Requirements

You must implement the following three helper functions and coordinate them inside `main()`:

### Task 1: Initialize Menu
* **Goal:** Populate a container mapping item names to their prices based on user input.
* **Parameters:** `num_items`, `menu_prices`
* **Behavior:**
  1. Prompt the user to enter an item name and its price `num_items` times (e.g., if `4` is passed in, prompt for 4 items and prices).
  2. Store each name and price pair in the `menu_prices` container.
  3. Return `menu_prices`.
* *Test this function from `main()` before moving on to Task 2!*

### Task 2: Take Order
* **Goal:** Interactively collect the menu items and quantities the user wants to purchase.
* **Parameters:** `menu_prices`
* **Behavior:**
  1. Start with an empty container to hold the user's order (items and quantities).
  2. Print the menu options and prices based on `menu_prices`.
  3. Prompt the user to enter the name of the item they want to purchase (or type `'done'` to finish).
  4. If the user enters `'done'`, exit the loop.
  5. If the item is not in `menu_prices`, display an error message and repeat the prompt.
  6. Otherwise, prompt for the quantity (`int`) and add the item and quantity to the user's order container.
  7. Return the order container.
* *Test this function from `main()` before moving on to Task 3!*

### Task 3: Calculate Bill
* **Goal:** Compute item subtotals and the grand total by iterating through the customer's order.
* **Parameters:** `order_items`, `menu_prices`
* **Behavior:**
  1. Iterate through the order, using the item quantity and menu price to calculate a subtotal for each item.
  2. Print an itemized line showing the item name, quantity, price, and subtotal.
  3. Accumulate and return the grand total for all items.

### Task 4: Implement `main()`
* **Goal:** Coordinate the complete workflow. Execute each function above to demonstrate how a menu is built, an order is placed, and the final bill details are displayed.

---

## ⚠️ Important Code Constraints

Your completed `main.py` **must** satisfy all of the following requirements:
* [ ] You should only have **one** `main()` function entry point.
* [ ] Implement at least **one default parameter** (e.g., in `num_items` or another parameter).
* [ ] All functions must have a **docstring with 3 required parts**:
  1. Description of what the function does
  2. Parameters listing and types
  3. Return value description
* [ ] Use at least one `for` loop.
* [ ] Use at least one `while` loop.
* [ ] Use at least one `break` statement.
* [ ] Use at least one `continue` statement.

---

## Submission Requirements

To complete and submit this lab, fulfill all three parts below:

### 1. GitHub Version Control
* Save your changes in VS Code.
* Open the **Source Control** panel (`Ctrl+Shift+G` / `Cmd+Shift+G`), type a commit message, click **Commit**, and click **Sync Changes** (or **Push**).
* Copy the URL of your personal GitHub fork (e.g., `https://github.com/YOUR-USERNAME/cs256-lab5-campus-cafe`).

### 2. Google Doc Report
Create a Google Doc with a descriptive title and header containing your name and course details, containing:
1. **Code:** Paste your complete Python code from VS Code as text (ensure all docstrings are included).
2. **Screenshot:** Attach a screenshot showing terminal output for a menu with **at least 4 items** and an order with **at least 2 different items** (at least one item must have a quantity greater than 1).
3. **Requirement Comments:** Use Google Doc comments to clearly tag where you implemented each required item under *Important Code Constraints* (default parameter, docstrings, `for` loop, `while` loop, `break`, `continue`).
4. **Reflection:** Include a few sentences reflecting on what you learned, challenges you overcame, anything you used that wasn't covered in class (and where you learned it), and any remaining questions you have.

### 3. Moodle Submission
Upload your single `.py` file **AND** submit the link to your Google Doc on **Moodle** to notify your instructor that your lab is ready to be graded.

```
