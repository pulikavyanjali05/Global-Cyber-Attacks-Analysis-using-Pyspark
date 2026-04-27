# =========================
# 1. Install Libraries
# =========================
!pip install pyspark pandas matplotlib seaborn

# =========================
# 2. Import Libraries
# =========================
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as _sum, avg, col
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# 3. Start Spark Session
# =========================
spark = SparkSession.builder \
    .appName("Cyber Attack Analysis") \
    .getOrCreate()

print("Spark Started Successfully")

# =========================
# 4. Upload Dataset (Colab)
# =========================
from google.colab import files
uploaded = files.upload()

# =========================
# 5. Load Dataset
# =========================
df = spark.read.csv("hack_data_100_rows.csv",
                    header=True,
                    inferSchema=True)

print("Dataset Preview")
df.show(10)

print("Schema")
df.printSchema()

# =========================
# 6. Top Attacking Countries
# =========================
country_attack = df.groupBy("Location") \
    .agg(_sum("Servers_Corrupted").alias("Total_Attacks")) \
    .orderBy(col("Total_Attacks").desc())

country_attack.show()

# =========================
# 7. Convert to Pandas (Top 10)
# =========================
pdf = country_attack.toPandas().head(10)

# =========================
# 8. Bar Chart
# =========================
plt.figure(figsize=(12,6))
plt.bar(pdf["Location"], pdf["Total_Attacks"])
plt.title("Top Countries for Cyber Attacks")
plt.xlabel("Country")
plt.ylabel("Total Attacks")
plt.xticks(rotation=45)
plt.show()

# =========================
# 9. Pie Chart
# =========================
plt.figure(figsize=(8,8))
plt.pie(pdf["Total_Attacks"],
        labels=pdf["Location"],
        autopct='%1.1f%%')
plt.title("Attack Distribution by Country")
plt.show()

# 10. Typing Speed Analysis
typing_df = df.select("Location", "WPM_Typing_Speed").toPandas()

plt.figure(figsize=(12,6))
sns.boxplot(x="Location",
            y="WPM_Typing_Speed",
            data=typing_df)

plt.title("Typing Speed Analysis")
plt.xticks(rotation=45)
plt.show()

#  Correlation Heatmap
full_df = df.toPandas()

plt.figure(figsize=(10,6))
sns.heatmap(full_df.corr(numeric_only=True),
            annot=True,
            cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()

spark.stop()
print("Spark Session Stopped")
