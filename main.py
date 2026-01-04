# -----------------------------------------------------
# Function: add_expense
# Purpose : Saves a single expense record into a file
# -----------------------------------------------------

def add_expense(date, category, amount, note):                            # Open file in append mode so old data is not deleted
    with open("expenses.txt", "a") as f:                                  # Store expense as a single line using | as separator
        f.write(date + "|" + category + "|" + amount + "|" + note + "\n")

# -----------------------------------------------------
# Function: read_expenses
# Purpose : Reads all expenses from file and converts
#           them into a list of dictionaries
# -----------------------------------------------------

def read_expenses():         
    expenses = []                                                          # This list will store all expense records
    with open("expenses.txt", "r") as f:
        lines = f.readlines()[1:]                                          # Read all lines and skip the header line
        for line in lines:
            d, c, a, n = line.strip().split("|")                           # Remove newline and split data using |
            expenses.append({                                              # Store each expense as a dictionary
                "date": d,
                "category": c,
                "amount": int(a),
                "note": n
            })
    return expenses

# -----------------------------------------------------
# Function: category_total
# Purpose : Calculates total expense for each category
# -----------------------------------------------------

def category_total(expenses):                                              
    result = {}                                                            # Dictionary to store category totals
    for e in expenses:
        if e["category"] in result:                                        # If category already exists, add amount
            result[e["category"]] += e["amount"]
        else:
            result[e["category"]] = e["amount"]                            # Otherwise, create new category entry
    return result

# -----------------------------------------------------
# Function: monthly_total
# Purpose : Calculates total expense for a given month
#           (Uses string slicing instead of datetime)
# -----------------------------------------------------

def monthly_total(expenses, month):
    total = 0
    for e in expenses:
        if e["date"][:7] == month:                                        # Extract YYYY-MM from date string to match month
            total += e["amount"]
    return total

# -----------------------------------------------------
# Function: budget_check
# Purpose : Compares total spending with budget limit
# -----------------------------------------------------

def budget_check(total, budget):
    if total > budget:
        print("⚠ Budget Exceeded by", total - budget)
    else:
        print("✅ Budget Remaining:", budget - total)

# =====================================================
# MAIN PROGRAM (Menu Driven System)
# =====================================================

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Monthly Report")
    print("5. Exit")

    choice = input("Enter choice: ")

# ---------------- OPTION 1 ----------------

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")                          # Take expense details from user
        category = input("Enter category: ")
        amount = input("Enter amount: ")
        note = input("Enter note: ")
        add_expense(date, category, amount, note)                          # Save expense to file

# ---------------- OPTION 2 ----------------

    elif choice == "2":
        expenses = read_expenses()                                         # Read and display all expenses
        for e in expenses:
            print(e)


# ---------------- OPTION 3 ----------------
    elif choice == "3":
        expenses = read_expenses()                                         # Display category-wise spending summary                         
        summary = category_total(expenses)
        for k in summary:
            print(k, ":", summary[k])

# ---------------- OPTION 4 ----------------

    elif choice == "4":
        expenses = read_expenses()                                          # Monthly expense analysis with budget check
        month = input("Enter month (YYYY-MM): ")
        total = monthly_total(expenses, month)
        print("Total spent:", total)
        budget = int(input("Enter your budget: "))
        budget_check(total, budget)

# ---------------- OPTION 5 ----------------

    elif choice == "5":
        print("Exiting...")
        break

# ---------------- INVALID INPUT ----------------

    else:
        print("Invalid choice")

