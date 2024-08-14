import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data for countries
data = {
    "Country": ["USA", "Canada", "Germany", "UK", "France", "Japan", "Australia", "Italy", "Brazil", "India"],
    "Count": [250, 100, 150, 200, 180, 170, 120, 110, 130, 160]
}

df = pd.DataFrame(data)

# Plot the country distribution chart
plt.figure(figsize=(10, 6))
sns.barplot(x="Country", y="Count", data=df, palette="viridis")

plt.title("Country Distribution Chart")
plt.xlabel("Nation")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.show()
