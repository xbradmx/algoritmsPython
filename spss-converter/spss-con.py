import pyreadstat

file_path = "C:/Users/Dawn/OneDrive/Desktop/Github-vs code folder/python and algorithms/algoritmsPython/spss-converter/holidaydata.sav"

# Replace with your actual file path
df, meta = pyreadstat.read_sav(file_path)

df.to_csv("output.csv", index=False)  # Save as CSV


