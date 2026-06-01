import pandas as pd
def find_weak_passwords(df):
    filtered = df[(df["password"].str.len() <= 8) &
    (df["password"].str.contains("123"))
    ]
    return filtered

def extract_features(password):
    #Calculate password length
    length = len(password)
    #Detect numbers
    has_num = False  
    for word in password:
        if word.isdigit():
            has_num = True
    #Detect symbols
    has_symbol = False
    if not password.isalnum():
        has_symbol = True
    #Detect uppercase letters
    upper = False
    for char in password:
        if char.isupper():
            upper = True
            break
    #Return Feature Dictionary
    fdict = {
        "length": length,
        "has_number": has_num,
        "has_symbol": has_symbol,
        "has_uppercase": upper
    }
    return fdict

def build_transformed_dataframe(df):
    #Create storage structure
    List = []
    #Loop through passwords
    for char in df["password"]:
    #Extract the features from each
        item = extract_features(char)
    #Store the result
        List.append(item)
    #Convert the result into Dataframe
    feature_df = pd.DataFrame(List)
    return feature_df

def get_common_length(df):
#create separate column for password length
    lengths = []
    for p in df["password"]:
        lengths.append(len(p))

    df["length"] = lengths
    #group dataframe by password length
    length_freq = df.groupby("length").size()
    #sort counts in descending order
    length_freq = length_freq.sort_values(ascending=False)
    #Display results
    common_length = length_freq.index[0]
    return common_length
