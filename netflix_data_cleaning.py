import pandas as pd

# Read CSV file
df = pd.read_csv("netflix_dataset.csv")

# Print original dataset
print("Original Dataset:\n")
print(df)

# Check missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Fill missing values with average
df["ReleaseYear"].fillna(df["ReleaseYear"].mean(), inplace=True)
df["Rating"].fillna(df["Rating"].mean(), inplace=True)
df["Duration"].fillna(df["Duration"].mean(), inplace=True)

# Print cleaned dataset
print("\nCleaned Dataset:\n")
print(df)

# Average rating
average_rating = df["Rating"].mean()

print("\nAverage Rating:", average_rating)

# Save cleaned dataset
df.to_csv("cleaned_netflix_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")