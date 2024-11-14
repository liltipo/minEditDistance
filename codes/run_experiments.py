import time
import subprocess
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

# Función para ejecutar el programa de C++ y obtener los resultados
def run_cpp_algorithm(S1, S2):
    # Ejecutar el programa de C++ y pasarle las cadenas S1 y S2 como argumentos
    result = subprocess.run(['./edit_distance', S1, S2], capture_output=True, text=True)

    # Parsear la salida del programa de C++
    output = result.stdout.splitlines()
    brute_result = int(output[0].split(":")[1].strip())
    dp_result = int(output[1].split(":")[1].strip())

    return brute_result, dp_result

# Medir tiempos de ejecución y resultados para diferentes casos
def run_experiment(S1, S2):
    results = {}

    # Fuerza Bruta
    start = time.time()
    brute_result, dp_result = run_cpp_algorithm(S1, S2)
    brute_time = time.time() - start

    # Programación Dinámica
    start = time.time()
    _, dp_result = run_cpp_algorithm(S1, S2)
    dp_time = time.time() - start

    results['Brute Force Result'] = brute_result
    results['Brute Force Time (s)'] = brute_time
    results['DP Result'] = dp_result
    results['DP Time (s)'] = dp_time

    return results

# Crear casos de prueba
datasets = [
    ("", ""),                                   # Caso 1: Cadenas vacías
    ("", "abcdefg"),                            # Caso 2: Una cadena vacía
    ("aaaaaaaaaa", "aaaaaaaa"),                 # Caso 3: Caracteres repetidos
    ("abba", "baba"),                           # Caso 4: Necesidad de transposición
    ("kitten", "sitting"),                      # Caso 5: Sustituciones
    ("abcdefgh", "ijklmnop"),                   # Caso 6: Ningún carácter en común
    ("abcdef", "abcfed"),                       # Caso 7: Transposición parcial y sustitución
    ("longstringtest", "lontgsritenst"),        # Caso 8: Transposiciones múltiples
    ("abcdefghijklmnop", "abcdefghijklmnop"),   # Caso 9: Cadenas idénticas
    ("abcdefghijklmnop", "efghijk"),            # Caso 10: Subcadena
    ("intention", "execution"),                 # Caso 11: Ejemplo pdf
]

# Generar más casos para ampliar el dataset
extended_datasets = datasets * 100  # Repetir los casos x veces

# Diccionario para almacenar tiempos de los experimentos
time_results = defaultdict(lambda: {'Brute Force Time (s)': [], 'DP Time (s)': [], 'Brute Force Result': [], 'DP Result': []})

# Ejecutar los experimentos y promediar los resultados para los mismos casos
for S1, S2 in extended_datasets:
    res = run_experiment(S1, S2)
    time_results[(S1, S2)]['Brute Force Time (s)'].append(res['Brute Force Time (s)'])
    time_results[(S1, S2)]['DP Time (s)'].append(res['DP Time (s)'])
    time_results[(S1, S2)]['Brute Force Result'].append(res['Brute Force Result'])
    time_results[(S1, S2)]['DP Result'].append(res['DP Result'])

# Promediar los tiempos para cada caso
averaged_results = []
for (S1, S2), values in time_results.items():
    avg_brute_time = sum(values['Brute Force Time (s)']) / len(values['Brute Force Time (s)'])
    avg_dp_time = sum(values['DP Time (s)']) / len(values['DP Time (s)'])
    avg_brute_result = sum(values['Brute Force Result']) / len(values['Brute Force Result'])
    avg_dp_result = sum(values['DP Result']) / len(values['DP Result'])
    
    averaged_results.append({
        'S1': S1,
        'S2': S2,
        'Average Brute Force Time (s)': avg_brute_time,
        'Average DP Time (s)': avg_dp_time,
        'Brute Force Result': avg_brute_result,
        'DP Result': avg_dp_result
    })

# Convertir los resultados a un DataFrame de pandas
df = pd.DataFrame(averaged_results)

# Guardar los resultados en un archivo CSV
df.to_csv("averaged_experiment_results_cpp.csv", index=False)

# Mostrar los resultados
print(df)

# Tabla de diferencias absolutas
df['Time Difference (Brute - DP)'] = df['Average Brute Force Time (s)'] - df['Average DP Time (s)']
print(df[['S1', 'S2', 'Average Brute Force Time (s)', 'Average DP Time (s)', 'Time Difference (Brute - DP)']])

# Graficar tiempos de ejecución de Fuerza Bruta vs Programación Dinámica
plt.figure(figsize=(16, 6))
plt.plot(df['S1'], df['Average Brute Force Time (s)'], label='Fuerza Bruta', marker='o')
plt.plot(df['S1'], df['Average DP Time (s)'], label='Programación Dinámica', marker='o')
plt.xlabel('Casos de Prueba')
plt.ylabel('Tiempo de Ejecución Promedio (s)')
plt.title('Comparación de Tiempos de Ejecución Promedio entre Fuerza Bruta y Programación Dinámica')
plt.legend()
plt.grid(True)
plt.savefig('comparison_execution_times.png')

# Gráficar razón entre los tiempos
df['Speedup Ratio (Brute/DP)'] = df['Average Brute Force Time (s)'] / df['Average DP Time (s)']

plt.figure(figsize=(16, 6))
plt.plot(df['S1'], df['Speedup Ratio (Brute/DP)'], marker='o')
plt.xlabel('Casos de Prueba')
plt.ylabel('Razón de Tiempos (Fuerza Bruta / Programación Dinámica)')
plt.title('Razón de Tiempos entre Fuerza Bruta y Programación Dinámica')
plt.grid(True)
plt.savefig('speedup_ratio.png')

# Gráficar tiempos vs longitud de las cadenas

# Calcular la longitud promedio de las cadenas
df['Average Length'] = (df['S1'].apply(len) + df['S2'].apply(len)) / 2

plt.figure(figsize=(12, 6))
bar_width = 0.35
indices = np.arange(len(df))
plt.bar(indices, df['Average Brute Force Time (s)'], width=bar_width, label='Fuerza Bruta', alpha=0.7)
plt.bar(indices + bar_width, df['Average DP Time (s)'], width=bar_width, label='Programación Dinámica', alpha=0.7)
plt.xlabel('Casos de Prueba')
plt.ylabel('Tiempo de Ejecución Promedio (s)')
plt.title('Comparación de Tiempos vs Longitud de Cadenas')
plt.xticks(indices + bar_width / 2, df['Average Length'].round(2))  
plt.legend()
plt.grid(axis='y')
plt.tight_layout() 
plt.savefig('execution_times_vs_length.png') 

# Boxplot de tiempos de ejecución
plt.figure(figsize=(10, 6))
plt.boxplot([df['Average Brute Force Time (s)'], df['Average DP Time (s)']], showfliers=True, tick_labels=['Fuerza Bruta', 'Programación Dinámica'])
plt.ylabel('Tiempo de Ejecución Promedio (s)')
plt.title('Distribución de Tiempos de Ejecución (Sin Outliers)')
plt.grid(True)
plt.savefig('execution_time_distribution.png')