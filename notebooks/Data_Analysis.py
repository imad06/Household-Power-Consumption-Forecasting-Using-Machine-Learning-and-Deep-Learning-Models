import pandas as pd
import seaborn as sns
#import matplotlib.pyplot as plt    
# Configurer les graphiques
sns.set(style="darkgrid")

df = pd.read_csv("data/household_power_consumption.csv")
print(df.head())
