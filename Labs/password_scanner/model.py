def find_weak_passwords(df):
    filtered = df[(df["password"].str.len() <= 8) &
    (df["password"].str.contains("123"))
    ]
    return filtered