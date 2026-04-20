import pandas as pd
import matplotlib.pyplot as plt

# Load data
transactions = pd.read_csv("transactions_100k.csv")
stores = pd.read_csv("stores.csv")

# 🔥 FIX: remove duplicate column before merge
stores = stores.drop(columns=["store_type"])

# Merge
df = pd.merge(transactions, stores, on="store_id")

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Debug check (optional)
print("Columns:", df.columns)

# -------------------------------
# 📊 1. TOTAL REVENUE BY STORE TYPE
# -------------------------------
revenue_by_type = df.groupby('store_type')['revenue'].sum().sort_values(ascending=False)

print("\nTop Store Types by Revenue:\n", revenue_by_type)

plt.figure()
revenue_by_type.plot(kind='bar')
plt.title("Revenue by Store Type")
plt.xlabel("Store Type")
plt.ylabel("Total Revenue")
plt.show()

# -------------------------------
# 👥 2. CUSTOMER FOOTFALL ANALYSIS
# -------------------------------
customers_by_type = df.groupby('store_type')['customers_count'].sum().sort_values(ascending=False)

print("\nCustomer Footfall by Store Type:\n", customers_by_type)

plt.figure()
customers_by_type.plot(kind='bar')
plt.title("Customers by Store Type")
plt.xlabel("Store Type")
plt.ylabel("Total Customers")
plt.show()

# -------------------------------
# 💳 3. AVG BILL VALUE BY STORE TYPE
# -------------------------------
avg_bill_by_type = df.groupby('store_type')['avg_bill_value'].mean().sort_values(ascending=False)

print("\nAverage Bill Value by Store Type:\n", avg_bill_by_type)

plt.figure()
avg_bill_by_type.plot(kind='bar')
plt.title("Average Bill by Store Type")
plt.xlabel("Store Type")
plt.ylabel("Avg Bill")
plt.show()

# -------------------------------
# 📈 4. REVENUE TREND OVER TIME
# -------------------------------
revenue_trend = df.groupby('date')['revenue'].sum()

plt.figure()
revenue_trend.plot()
plt.title("Revenue Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.show()

# -------------------------------
# 📅 5. WEEKEND VS WEEKDAY ANALYSIS
# -------------------------------
weekend_analysis = df.groupby('day_type')['revenue'].sum()

print("\nWeekend vs Weekday Revenue:\n", weekend_analysis)

plt.figure()
weekend_analysis.plot(kind='bar')
plt.title("Weekend vs Weekday Revenue")
plt.ylabel("Revenue")
plt.show()

# -------------------------------
# 🏬 6. TOP 10 STORES
# -------------------------------
top_stores = df.groupby('store_name')['revenue'].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Stores:\n", top_stores)

plt.figure()
top_stores.plot(kind='bar')
plt.title("Top 10 Stores by Revenue")
plt.xlabel("Store Name")
plt.ylabel("Revenue")
plt.show()

# -------------------------------
# 🧠 7. CUSTOMER vs REVENUE (SCATTER)
# -------------------------------
plt.figure()
plt.scatter(df['customers_count'], df['revenue'])
plt.title("Customers vs Revenue")
plt.xlabel("Customers")
plt.ylabel("Revenue")
plt.show()

# -------------------------------
# 🏆 8. BEST PERFORMING STORE TYPE
# -------------------------------
best_store_type = revenue_by_type.idxmax()

print("\n🏆 Best Performing Store Type:", best_store_type)