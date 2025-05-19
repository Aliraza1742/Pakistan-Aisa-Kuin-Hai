# 🌍 Gapminder Data Analysis

This project performs a comparative analysis of various development indicators across a selected set of countries using data from the Gapminder dataset. The analysis identifies how countries rank based on **increasing** (positive) and **decreasing** (negative) development factors and visualizes this through charts.

---

## 📁 Dataset

The input file is expected to be a CSV named **`Gapminder.csv`**, containing rows of countries and various socio-economic indicators such as:

- `Country`
- `AgriculturalLand`
- `Exports`
- `IncomePerPerson`
- `TotalhealthspendingperpersonUS`
- `Forestarea`
- `Inflation`
- `Populationtotal`
- `ChildrenPerWoman`
- `Imports`

Missing values (NaN) are automatically filled with 0.

---

## ⚙️ How It Works

### 🔹 Step 1: Load and Preprocess Data
- The script reads the CSV file.
- Fills missing values with zero.
- Maps column names to data for efficient access.

### 🔹 Step 2: Select Countries
Analyzes a predefined set of 8 countries:

 ```bash
Afghanistan
Canada
Germany
AustraliaFr
France
China
Italy
Pakistan
```

### 🔹 Step 3: Calculate Averages
For each country, it computes the **average value** for each selected indicator, ignoring any zeros.

### 🔹 Step 4: Normalize Data
Each country's average is normalized by dividing by the maximum value in that column to bring everything to a common [0, 1] scale.

### 🔹 Step 5: Ranking
- Countries are ranked based on the sum of their normalized scores.
- **Higher scores** indicate better ranks for **positive factors**.
- **Lower scores** indicate better ranks for **negative factors**.

### 🔹 Step 6: Visualization
- Each indicator is plotted using **bar charts with overlaid line plots**.
- Separate plots are generated for:
  - Increasing (positive) factors.
  - Decreasing (negative) factors.

---

## 📊 Indicators Used

### 🟢 Increasing (Positive) Indicators
These reflect factors where a **higher value** is better:
- AgriculturalLand
- Exports
- IncomePerPerson
- TotalhealthspendingperpersonUS
- Forestarea

### 🔴 Decreasing (Negative) Indicators
These reflect factors where a **lower value** is better:
- Inflation
- Populationtotal
- ChildrenPerWoman
- Imports

---

## 🖼️ Sample Output

The script outputs:

- Country rankings based on normalized values.
- Bar and line plots for each indicator showing comparative performance across the selected countries.

---

## 🧰 Requirements

Install the required Python libraries:
```bash
pip install pandas matplotlib
```

