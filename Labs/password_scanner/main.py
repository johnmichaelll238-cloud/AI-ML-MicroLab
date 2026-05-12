from data import load_passwords
from model import find_weak_passwords

df = load_passwords()
results = find_weak_passwords(df)

print("Potentially weak passwords:\n")
for password in results["password"]:
    print(f"[!] {password}")