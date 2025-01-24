import csv
import random
import time
from tqdm import tqdm

def load_customers_from_csv(file_path):
    """Load customer emails from a CSV file."""
    customers = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            # Skip header if present
            next(csv_reader, None)
            for row in csv_reader:
                customers.append(row[0])  # Assuming emails are in the first column
    except FileNotFoundError:
        print("Error: File not found. Make sure the file path is correct.")
    except Exception as e:
        print(f"Error: {e}")
    return customers

def pick_random_winner(customers):
    """Pick a random winner from the list of customers."""
    print("\nSelecting a winner...")

    # Simulate spinning wheel animation
    for _ in tqdm(range(30), desc="Spinning the wheel", ascii=True):
        time.sleep(0.3)

    winner = random.choice(customers)
    print("\n\n🎉 And the winner is... 🎉\n")
    time.sleep(1)
    print(f"🌟 {winner}! Congratulations! 🌟")

def main():
    print("Welcome to the Random Winner Picker! 🎲")
    file_path = "data.csv"

    customers = load_customers_from_csv(file_path)

    if not customers:
        print("No customers found in the file. Please check your CSV file and try again.")
        return

    pick_random_winner(customers)

if __name__ == "__main__":
    main()
