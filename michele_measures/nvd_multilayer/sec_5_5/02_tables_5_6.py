import glob
import pandas as pd

airlines = {1: 'Lufthansa', 2: 'Ryanair', 3: 'Easyjet', 4: 'British_Airways', 5: 'Turkish_Airlines', 6: 'Air_Berlin', 7: 'Air_France', 8: 'Scandinavian_Airlines', 9: 'KLM', 10: 'Alitalia', 11: 'Swiss_International_Air_Lines', 12: 'Iberia', 13: 'Norwegian_Air_Shuttle', 14: 'Austrian_Airlines', 15: 'Flybe', 16: 'Wizz_Air', 17: 'TAP_Portugal', 18: 'Brussels_Airlines', 19: 'Finnair', 20: 'LOT_Polish_Airlines', 21: 'Vueling_Airlines', 22: 'Air_Nostrum', 23: 'Air_Lingus', 24: 'Germanwings', 25: 'Panagra_Airways', 26: 'Netjets', 27: 'Transavia_Holland', 28: 'Niki', 29: 'SunExpress', 30: 'Aegean_Airlines', 31: 'Czech_Airlines', 32: 'European_Air_Transport', 33: 'Malev_Hungarian_Airlines', 34: 'Air_Baltic', 35: 'Wideroe', 36: 'TNT_Airways', 37: 'Olympic_Air'}

df = []
for txt in glob.glob("*.csv"):
   df.append(pd.read_csv(txt, sep = "\t"))

df = pd.concat(df)

df2 = df.groupby(by = ["c1", "layer"])[["dist", "edge_count", "node_count"]].mean().reset_index()
df2["name"] = df2["layer"].map(airlines)
df2.to_csv("layer_country_distance.csv", sep = "\t", index = False)

df3 = df.groupby(by = "layer")[["dist", "edge_count", "node_count"]].mean().reset_index()
df3["name"] = df3["layer"].map(airlines)
df3.to_csv("layer_distance.csv", sep = "\t", index = False)
