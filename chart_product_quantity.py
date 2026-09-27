import os
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("sales.csv")

product_qty = df.groupby("product")["quantity"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
product_qty.plot(kind="bar", color="seagreen", edgecolor="black")

plt.title("Кількість проданих одиниць для кожного товару", fontsize=14)
plt.xlabel("Товар", fontsize=12)
plt.ylabel("Кількість проданих одиниць (шт.)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

os.makedirs("graphs", exist_ok=True)
plt.savefig("graphs/product_quantity.png")
print("Графік 'Кількість проданих товарів' збережено в graphs/product_quantity.png")
plt.show()