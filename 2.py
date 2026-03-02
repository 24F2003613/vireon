import pandas as pd
path = "vireon_sample_data.tsv"
df = pd.read_csv(path,sep="\t")
df.head()
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df.columns = df.columns.str.strip().str.lower()
avg_ph = (df["current_r"] + df["current_y"] + df["current_b"]) / 3

v1 = df.loc[(df["voltage_unbalance_pct"] > 2) & df["voltage_unbalance_pct"] <= 5, ["timestamp", "location", "voltage_unbalance_pct"]].assign(alert = "Voltage Unbalance", type = "Warning")
v2 = df.loc[df["voltage_unbalance_pct"] > 5, ["timestamp", "location", "voltage_unbalance_pct"]].assign(alert = "Voltage Unbalance", type = "Critical")

pf1 = df.loc[(df["pf_avg"] < 0.9)& df["pf_avg"] >= 0.85,  ["timestamp", "location", "pf_avg"]].assign(alert = "Power Factor", type = "Warning")
pf2 = df.loc[df["pf_avg"]< 0.85, ["timestamp", "location", "pf_avg"]].assign(alert = "Power Factor", type = "Critical")

nc = df.loc[df["neutral_current_a"] > 0.1*avg_ph, ["timestamp", "location", "neutral_current_a"]].assign(alert = "Neutral Current", type = "Warning")

fr1 = df.loc[df["fire_risk_level"] == "WARNING", ["timestamp", "location", "fire_risk_level"]].assign(alert = "Fire Risk Level", type = "Warning")
fr2 = df.loc[df["fire_risk_level"] == "HIGH", ["timestamp", "location", "fire_risk_level"]].assign(alert = "Fire Risk Level", type = "Critical")

alert=[v1,v2,pf1,pf2,nc,fr1,fr2]

alert = pd.concat([v1,v2,pf1,pf2,nc,fr1,fr2], ignore_index=True)

print(alert["alert"].value_counts())
print(alert["location"].value_counts())
print("Max alerts from ", alert["alert"].value_counts().idxmax())