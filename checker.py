import csv
import os

CSV_FILE = "users.csv"

# Initialize CSV if not present
def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])
            writer.writerow(["alice", "alice123"])
            writer.writerow(["bob", "bobpass"])
            writer.writerow(["charlie", "charlie@2025"])

def login(username, password):
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username:
                    if row["password"] == password:
                        return "✅ Login successful!"
                    else:
                        return "❌ Incorrect password!"
            return "❌ User not registered!"
    except FileNotFoundError:
        return "Error: Users database not found!"
    except Exception as e:
        return f"Unexpected error: {e}"

def register(username, password):
    try:
        with open(CSV_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        return "✅ User registered successfully!"
    except Exception as e:
        return f"Error while registering: {e}"

if __name__ == "__main__":
    init_csv()
    while True:
        print("\n--- Username Password Checker ---")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            u = input("Enter username: ")
            p = input("Enter password: ")
            print(login(u, p))
        elif choice == "2":
            u = input("Choose username: ")
            p = input("Choose password: ")
            print(register(u, p))
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")
