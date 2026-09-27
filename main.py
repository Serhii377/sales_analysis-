import os
import pandas as pd
os.makedirs("graphs", exist_ok=True)

print("  2) ЗАВАНТАЖЕННЯ ТА ОГЛЯД ДАНИХ")

df = pd.read_csv("sales.csv")

print("Перші 5 рядків таблиці:")
print(df.head())
print("-" * 50)

print("\nОстанні 5 рядків таблиці:")
print(df.tail())
print("-" * 50)

print("\nІнформація про таблицю (info):")
df.info()
print("-" * 50)

print("\nСтатистична інформація (describe):")
print(df.describe())
print("-" * 50)

print("  3) ПІДГОТОВКА ДАНИХ")

df["date"] = pd.to_datetime(df["date"])

df["total"] = df["quantity"] * df["price"]

df = df[["date", "product", "category", "quantity", "price", "total"]]
print("Дані успішно підготовлено. Стовпець 'total' додано.")
print("Порядок стовпців: date, product, category, quantity, price, total.")

print("  4) АНАЛІЗ ПРОДАЖІВ ЗА ДОПОМОГОЮ PANDAS")

total_quantity = df["quantity"].sum()

total_sales = df["total"].sum()

average_sale = df["total"].mean()

max_sale = df.loc[df["total"].idxmax()]

min_sale = df.loc[df["total"].idxmin()]

top_product_qty = df.groupby("product")["quantity"].sum().idxmax()
top_product_qty_val = df.groupby("product")["quantity"].sum().max()

top_category_sales = df.groupby("category")["total"].sum().idxmax()
top_category_sales_val = df.groupby("category")["total"].sum().max()

print(f"1. Загальна кількість проданих товарів: {total_quantity} шт.")
print(f"2. Загальна сума продажів: {total_sales:.2f}")
print(f"3. Середня сума одного продажу: {average_sale:.2f}")
print(
    f"4. Найдорожчий продаж: {max_sale['product']} (сума: {max_sale['total']:.2f}, дата: {max_sale['date'].strftime('%Y-%m-%d')})"
)
print(
    f"5. Найдешевший продаж: {min_sale['product']} (сума: {min_sale['total']:.2f}, дата: {min_sale['date'].strftime('%Y-%m-%d')})"
)
print(
    f"6. Товар із найбільшою кількістю проданих одиниць: {top_product_qty} ({top_product_qty_val} шт.)"
)
print(
    f"7. Категорія з найбільшою сумою продажів: {top_category_sales} ({top_category_sales_val:.2f})"
)
print("  5) ГРУПУВАННЯ ДАНИХ")

category_statistics = df.groupby("category").agg(
    operations_count=("total", "count"),
    total_quantity=("quantity", "sum"),
    total_sales=("total", "sum"),
    average_sale=("total", "mean"),
)

print("Таблицю 'category_statistics' успішно розраховано:")
print(category_statistics)