import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Function to calculate average values for given columns and countries
# -----------------------------
def compute_country_averages(data_dict, column_names, country_indices):
    country_average = {}
    for country, indices in country_indices.items():
        averages = []
        for column in column_names:
            total = 0
            count = 0
            for idx in indices:
                value = data_dict[column][idx]
                if value != 0:
                    total += value
                    count += 1
            count = count if count != 0 else 1
            averages.append(total / count)
        country_average[country] = averages
    return country_average

# -----------------------------
# Function to normalize the country averages per column
# -----------------------------
def normalize_data(country_average, column_names, countries):
    norm_data = {}
    for i, column in enumerate(column_names):
        values = [country_average[country][i] for country in countries]
        max_val = max(values)
        norm_data[column] = [val / max_val for val in values]
    return norm_data

# -----------------------------
# Function to rank countries based on normalized data
# -----------------------------
def rank_countries(norm_data, countries, rank_type):
    scores = [0] * len(countries)
    for values in norm_data.values():
        for i, val in enumerate(values):
            scores[i] += val
    ranked = sorted(zip(countries, scores), key=lambda x: x[1], reverse=True)
    print(f"\nThe Factor in which Rank should be {'High' if rank_type == 'increasing' else 'Low'}:")
    for i, (country, _) in enumerate(ranked, 1):
        print(f"{i} rank goes to: {country}")
    return ranked

# -----------------------------
# Function to plot the data
# -----------------------------
def plot_normalized_data(norm_data, countries, title, color_scheme):
    for i, (column, values) in enumerate(norm_data.items()):
        plt.figure()
        plt.bar(countries, values, label=column, color=color_scheme)
        plt.plot(countries, values, '-o', color='black')
        plt.title(f'{title} - {column}')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# -----------------------------
# Main script
# -----------------------------
df = pd.read_csv('Gapminder.csv')
df = df.fillna(0)

column_names_all = list(df.columns)
data_array = df.values

# Map columns to data arrays
data_dict = {column: data_array[:, idx] for idx, column in enumerate(column_names_all)}

# List of countries of interest
countries_of_interest = ["Afghanistan", 'Canada', 'Germany', 'Australia', "France", "China", "Italy", "Pakistan"]

# Create index dictionary mapping each country to its row indices in the dataset
country_indices = {country: [i for i, c in enumerate(data_array[:, 0]) if c == country] for country in countries_of_interest}

# -------- Increasing Factors --------
increasing_columns = ['AgriculturalLand', 'Exports', 'IncomePerPerson', 'TotalhealthspendingperpersonUS', 'Forestarea']
increasing_averages = compute_country_averages(data_dict, increasing_columns, country_indices)
increasing_norm = normalize_data(increasing_averages, increasing_columns, countries_of_interest)
increasing_ranking = rank_countries(increasing_norm, countries_of_interest, 'increasing')
plot_normalized_data(increasing_norm, countries_of_interest, 'Increasing Factor', color_scheme='skyblue')

# -------- Decreasing Factors --------
decreasing_columns = ['Inflation', 'Populationtotal', 'ChildrenPerWoman', 'Imports']
decreasing_averages = compute_country_averages(data_dict, decreasing_columns, country_indices)
decreasing_norm = normalize_data(decreasing_averages, decreasing_columns, countries_of_interest)
decreasing_ranking = rank_countries(decreasing_norm, countries_of_interest, 'decreasing')
plot_normalized_data(decreasing_norm, countries_of_interest, 'Decreasing Factor', color_scheme='salmon')