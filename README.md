# ATM-Simulator
I built a Python ATM simulator using a dictionary to store accounts. It verifies user PINs, loops an interactive menu, and runs modular functions to check balances, deposit cash, and safely withdraw funds without allowing negative balances.

# Simple ATM Simulator

A simple, menu-driven command-line ATM simulator written in Python. This program allows users to log in with an account number and PIN to perform basic banking operations like checking balances, depositing funds, and withdrawing cash.

## Features

- **User Authentication:** Simple verification using an account number and PIN.
- **Check Balance:** View the current balance in real-time.
- **Deposit Money:** Add money to the account (validates positive amounts).
- **Withdraw Money:** Withdraw cash with overdraft protection to prevent negative balances.
- **Session Loop:** Perform multiple transactions without restarting the script.

## Project Structure

The project uses modular functions for each operation:
- `login(acc, pin)`: Verifies user credentials against the account database.
- `show_balance(acc)`: Displays the current account balance.
- `deposit_money(acc)`: Handles deposits and updates the balance.
- `withdraw_money(acc)`: Handles withdrawals after validating available funds.

## Prerequisites

- Python 3.x installed on your system.

## How to Run

1. Clone or download this repository:
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
