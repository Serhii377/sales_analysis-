import os
import matplotlib.pyplot as plt
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
graphs_dir = os.path.join(current_dir, "graphs")

os.makedirs(graphs_dir, exist_ok=True)

df = pd.read_csv(os.path.join(current_dir, "sales.csv"))
df["total"] = df["quantity"] * df["price"]
category_sales = df.groupby("category")["total"].sum()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar", color="royalblue", edgecolor="black")

plt.title("Загальна сума продажів за категоріями", fontsize=14)
plt.xlabel("Категорія", fontsize=12)
plt.ylabel("Сума продажів", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

save_path = os.path.join(graphs_dir, "category_sales.png")
plt.savefig(save_path)
print(f"Файл успішно створено за шляхом: {save_path}")

plt.show()
plt.close()