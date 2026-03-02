import pandas as pd
path = "vireon_sample_data.tsv"
df = pd.read_csv(path,sep="\t")

df.columns = df.columns.str.strip().str.lower()
df["timestamp"] = pd.to_datetime(df["timestamp"])

for shed in df["location"].unique():
    d = df[df["location"] == shed]
    gap = d["timestamp"].diff().dt.total_seconds() / 60
    missed = gap[gap <= 5]
    danger = gap[gap > 10]
    print(danger)
    completness = 100 - ((len(danger)+len(missed))/len(d))*100
    print("Shed:", shed)
    print("Ttal reading: ", len(d))
    print("Danger : ",len(danger))
    print("%", completness)
    print("Missed : ", len(missed))