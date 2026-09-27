import os
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("sales.csv")
df["date"] = pd.to_datetime(df["date"])
df["total"] = df["quantity"] * df["price"]

daily_sales = df.groupby("date")["total"].sum().sort_index()

plt.figure(figsize=(10, 5))
plt.plot(daily_sales.index, daily_sales.values, marker="o", color="crimson", linewidth=2)

plt.title("Динаміка продажів за днями", fontsize=14)
plt.xlabel("Дата", fontsize=12)
plt.ylabel("Сума продажів за день", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=30)
plt.tight_layout()

os.makedirs("graphs", exist_ok=True)
plt.savefig("graphs/sales_dynamics.png")
print("Графік 'Динаміка продажів' збережено в graphs/sales_dynamics.png")
plt.show()