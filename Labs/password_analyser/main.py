from data import load_passwords
from model import find_weak_passwords, build_transformed_dataframe, get_common_length
df = load_passwords()

if df is not None:
    results = find_weak_passwords(df)

print("Potentially weak passwords:\n")
for password in results["password"]:
    print(f"[!] {password}")

feature_df = build_transformed_dataframe(df)
print(feature_df)

common = get_common_length(df)
print(f"The most common length in current dataframe is {common}")