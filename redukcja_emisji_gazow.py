import pandas as pd
import matplotlib.pyplot as plt

# Dane emisji gazów cieplarnianych dla biogazu
emissions_data = {
    'Silnik': ['Silnik 1', 'Silnik 2', 'Silnik 3'],
    'Zużycie biogazu (m3/h)': [10, 15, 20],
    'Emisje CO2 (kg/m3)': [1.5, 1.5, 1.5],
    'Emisje CH4 (kg/m3)': [0.1, 0.1, 0.1],
    'Emisje N2O (kg/m3)': [0.01, 0.01, 0.01]
}

# Tworzenie DataFrame z danymi emisji
df_emissions = pd.DataFrame(emissions_data)

# Obliczanie emisji gazów cieplarnianych na godzinę pracy silnika
df_emissions['Emisje CO2 (kg/h)'] = df_emissions['Zużycie biogazu (m3/h)'] * df_emissions['Emisje CO2 (kg/m3)']
df_emissions['Emisje CH4 (kg/h)'] = df_emissions['Zużycie biogazu (m3/h)'] * df_emissions['Emisje CH4 (kg/m3)']
df_emissions['Emisje N2O (kg/h)'] = df_emissions['Zużycie biogazu (m3/h)'] * df_emissions['Emisje N2O (kg/m3)']

# Obliczanie całkowitych emisji gazów cieplarnianych (CO2e) na podstawie współczynników GWP (Global Warming Potential)
GWP_CO2 = 1
GWP_CH4 = 25
GWP_N2O = 298

df_emissions['Emisje CO2e (kg/h)'] = (df_emissions['Emisje CO2 (kg/h)'] * GWP_CO2 +
                                      df_emissions['Emisje CH4 (kg/h)'] * GWP_CH4 +
                                      df_emissions['Emisje N2O (kg/h)'] * GWP_N2O)

# Wykresy liniowe emisji CO2, CH4 i N2O dla różnych silników
plt.figure(figsize=(14, 8))

plt.subplot(2, 2, 1)
plt.plot(df_emissions['Silnik'], df_emissions['Emisje CO2 (kg/h)'], marker='o', label='CO2')
plt.title('Emisje CO2 dla różnych silników')
plt.xlabel('Silnik')
plt.ylabel('Emisje CO2 (kg/h)')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(df_emissions['Silnik'], df_emissions['Emisje CH4 (kg/h)'], marker='o', label='CH4', color='green')
plt.title('Emisje CH4 dla różnych silników')
plt.xlabel('Silnik')
plt.ylabel('Emisje CH4 (kg/h)')
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(df_emissions['Silnik'], df_emissions['Emisje N2O (kg/h)'], marker='o', label='N2O', color='red')
plt.title('Emisje N2O dla różnych silników')
plt.xlabel('Silnik')
plt.ylabel('Emisje N2O (kg/h)')
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(df_emissions['Silnik'], df_emissions['Emisje CO2e (kg/h)'], marker='o', label='CO2e', color='purple')
plt.title('Emisje CO2e dla różnych silników')
plt.xlabel('Silnik')
plt.ylabel('Emisje CO2e (kg/h)')
plt.grid(True)

plt.tight_layout()
plt.show()

# Wykres kołowy udziału poszczególnych gazów w całkowitych emisjach CO2e
total_emissions = df_emissions[['Emisje CO2 (kg/h)', 'Emisje CH4 (kg/h)', 'Emisje N2O (kg/h)']].sum()
total_emissions_CO2e = [total_emissions['Emisje CO2 (kg/h)'] * GWP_CO2,
                        total_emissions['Emisje CH4 (kg/h)'] * GWP_CH4,
                        total_emissions['Emisje N2O (kg/h)'] * GWP_N2O]

labels = ['CO2', 'CH4', 'N2O']
colors = ['blue', 'green', 'red']

plt.figure(figsize=(10, 6))
plt.pie(total_emissions_CO2e, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Udział poszczególnych gazów w całkowitych emisjach CO2e')
plt.show()
