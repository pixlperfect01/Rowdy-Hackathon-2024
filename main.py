
import pandas as pds

df = pds.read_csv(input("CSV File name? "), low_memory=False)

concentration = {}

pesticides = df["Pesticide Name"].unique()

p_counts = []

for pest in pesticides:
    p_counts += [[pest, df["Pesticide Name"].value_counts()[pest]]]

p_counts.sort(key=lambda p: p[1], reverse=True)

top_5_pests = p_counts[0:5]

i = 0

for pest_arr in top_5_pests:
    i += 1
    print(str(i) + ") " + pest_arr[0])

for pest_arr in p_counts:
    concentration[pest_arr[0]] = 0

for index, row in df.iterrows():
    pesticide = row["Pesticide Name"]
    concentration[pesticide] += row["Concentration"]

for pest_arr in top_5_pests:
    print(pest_arr[0], concentration[pest_arr[0]] / float(pest_arr[1]))