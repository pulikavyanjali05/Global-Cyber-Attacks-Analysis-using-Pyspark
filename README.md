🌍 Global Cyber Attacks Analysis using PySpark
📌 Project Overview
In today’s digital world, cyber attacks are increasing rapidly in frequency, scale, and complexity. Organizations generate huge amounts of security data, making it difficult to analyze using traditional systems.
This project focuses on analyzing cyber attack data using Apache Spark and PySpark, enabling fast and scalable processing of large datasets.
🎯 Problem Statement
Traditional systems like manual log analysis and relational databases are not efficient for handling massive cyber security data.
Slow processing speed
Limited scalability
Inability to detect new threats
No real-time insights
👉 Hence, a big data-based solution is required for efficient cyber attack analysis.
🎯 Objectives
Process large-scale cyber datasets using distributed computing
Identify attack patterns and suspicious behavior
Detect top attacking countries
Analyze attacker behavior (typing speed, tools used)
Generate visual insights for better understanding
🏗️ Architecture

Data Source (CSV Dataset)
        ↓
Data Storage (Local/Cloud)
        ↓
Apache Spark Processing
        ↓
Analytics (Patterns, Behavior, Countries)
        ↓
Visualization (Charts & Graphs)
        ↓
User / Output
📊 Dataset Details
File Name: hack_data_100_rows.csv
Format: CSV
Records: 100
Type: Structured Data
🔑 Features:
Session Connection Time
Bytes Transferred
Kali Trace Used
Servers Corrupted
Pages Corrupted
Typing Speed (WPM)
Location
🛠️ Technologies Used
Python
Apache Spark
PySpark
Pandas
NumPy
Matplotlib
Seaborn
Jupyter Notebook / Google Colab
⚙️ Implementation
Python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Cyber Attack Analysis") \
    .getOrCreate()

df = spark.read.csv("hack_data_100_rows.csv",
                    header=True,
                    inferSchema=True)

df.show()
📈 Results
Identified top attacking countries
Visualized attack distribution (bar chart, pie chart)
Analyzed typing speed patterns
Generated correlation heatmap
Extracted meaningful insights for security analysis
✅ Conclusion
Successfully analyzed cyber attack data using Spark
Improved performance with distributed computing
Helped understand attack trends and patterns
Supports better cybersecurity decision-making
🚀 Future Enhancements
Real-time analysis using Spark Streaming
Machine learning for anomaly detection
Interactive dashboards (Power BI / Tableau)
Cloud integration (AWS, Azure, GCP)
Automated alert systems
👩‍💻 Team Members
P. Kavyanjali
K. Vedhanjali
D. Akshitha
📚 References
Apache Spark Documentation
PySpark Documentation
Big Data Analytics in Cybersecurity Research Papers
