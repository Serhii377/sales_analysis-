import os
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("sales.csv")
df["total"] = df["quantity"] * df["price"]

category_sales = df.groupby("category")["total"].sum()

plt.figure(figsize=(7, 7))
plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"][:len(category_sales)]
)

plt.title("Частка кожної категорії у загальній сумі продажів", fontsize=14)
plt.tight_layout()

os.makedirs("graphs", exist_ok=True)
plt.savefig("graphs/category_share.png")
print("Графік 'Частка продажів за категоріями' збережено в graphs/category_share.png")
plt.show()