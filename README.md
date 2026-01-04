# Smart Expense & Budget Analyzer (Pure Python)
A menu-driven command-line application built using pure Python to record, store, and analyze daily expenses.<br>
This project is developed without using any external libraries, focusing entirely on core Python concepts.<br>

### Features
1.Add daily expense records<br>
2.View all recorded expenses<br>
3.Category-wise expense summary<br>
4.Monthly expense analysis<br>
5.Budget limit comparison with alerts<br>
6.File-based permanent data storage<br>

### Technologies Used
1.Python (Core only)<br>
2.File Handling<br>
3.Strings<br>
4.Lists & Dictionaries<br>
5.Conditional Logic<br>
6.Loops & Functions<br>

### How to Run the Project
1. Clone the repository:<br>
git clone https://github.com/saqibyafi20/expense-manager.git<br>
2. Navigate to the project folder:<br>
cd expense-analyzer<br>
3. Run the program:<br>
python main.py<br>

### How It Works
This project is a menu-driven command-line application built using pure Python, without any external libraries.<br>
It follows a simple and clear execution flow:<br>
1: Application Start:<br>
* When the program starts, it displays a menu with multiple options:<br>
Add Expense<br>
View Expenses<br>
Category Summary<br>
Monthly Report & Budget Check<br>
Exit<br>

2: Adding an Expense
* The user enters:<br>
Date (YYYY-MM-DD)<br>
Category (e.g., Food, Travel)<br>
Amount<br>
Note<br>

3: Reading Expenses from File
* Whenever data analysis is required, the program:<br>
opens the file in read mode<br>
Reads all expense records<br>
Converts each record into a dictionary<br>
All expense dictionaries are stored in a list for further processing.<br>
This approach makes data handling efficient and easy to analyze.<br>

4: Viewing All Expenses
The program reads all stored expenses from the file<br>
Displays them one by one in a structured dictionary format<br>
This helps users review their complete spending history<br>

5: Category-wise Expense Summary
The program groups expenses by category<br>
It calculates the total amount spent per category<br>
A dictionary is used to store category names as keys and total amounts as values<br>

6: Monthly Expense Analysis
The user enters a month in YYYY-MM format<br>
The program:<br>
Filters expenses based on the month using string slicing<br>
Calculates total spending for that month<br>
This is done without using any date or analytics libraries<br>

7: Budget Check
The user enters a monthly budget<br>
The program compares:<br>
Total monthly expenses vs Budget<br>
Displays:<br>
Remaining budget OR<br>
Budget exceeded warning<br>
This provides real-time financial awareness.<br>

8: Program Exit
The application exits cleanly when the user selects the exit option<br>
The loop terminates and the program stops execution<br>

### Author
Saqib Yafi



