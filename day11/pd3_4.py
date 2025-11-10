import pandas as pd

df = pd.DataFrame(
    {
        "Name": ["Abhishek", "Usha", "Shreya", "Vijay"],
        "Physics": [88, 81, 90, 87],
        "Chemistry": [82, 91, 85, 89],
        "Mathematics": [95, 97, 89, 91]
    }
)
print(df, "\n")

print(df.iloc[1], "\n")

df["Biology"] = [82, 79, 90, 80]
print(df, "\n")

df["Aggregate"] = df[["Physics", "Chemistry", "Mathematics", "Biology"]].sum(axis = 1)
print(df, "\n")

df["Average"] = df[["Physics", "Chemistry", "Mathematics", "Biology"]].mean(axis = 1)
print(df, "\n")

df["Median"] = df[["Physics", "Chemistry", "Mathematics", "Biology"]].median(axis = 1)
print(df, "\n")