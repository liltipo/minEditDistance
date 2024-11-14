#include <iostream>
#include <string>
#include <vector>
#include <climits>
#include <fstream>
#include <sstream>

using namespace std;

// Tablas de costos
vector<vector<int>> cost_insert;
vector<vector<int>> cost_delete;
vector<vector<int>> cost_replace;
vector<vector<int>> cost_transpose;

// Función para cargar una tabla de costos desde un archivo
void loadCostTable(const string &filename, vector<vector<int>> &costTable) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error: No se pudo abrir el archivo " << filename << endl;
        return;
    }

    string line;
    while (getline(file, line)) {
        istringstream iss(line);
        vector<int> row;
        int value;
        while (iss >> value) {
            row.push_back(value);
        }
        costTable.push_back(row);
    }
    file.close();
}

// Inicialización de las tablas de costos
void initCostTables() {
    loadCostTable("cost_insert.txt", cost_insert);
    loadCostTable("cost_delete.txt", cost_delete);
    loadCostTable("cost_replace.txt", cost_replace);
    loadCostTable("cost_transpose.txt", cost_transpose);
}

// Funciones de costo
int insertCost(int c) {
    return cost_insert[c][0]; // Asumiendo que solo se usa la primera columna
}

int deleteCost(int c) {
    return cost_delete[c][0]; // Asumiendo que solo se usa la primera columna
}

int replaceCost(int c1, int c2) {
    return cost_replace[c1][c2];
}

int transposeCost(int c1, int c2) {
    return cost_transpose[c1][c2];
}

// Fuerza Bruta
int editDistanceBrute(string S1, string S2, int i, int j) {
    if (i == S1.length()) return S2.length() - j;
    if (j == S2.length()) return S1.length() - i;

    if (S1[i] == S2[j]) return editDistanceBrute(S1, S2, i + 1, j + 1);

    int insert = insertCost(0) + editDistanceBrute(S1, S2, i, j + 1); // Suponiendo c = 0 para el costo de inserción
    int del = deleteCost(0) + editDistanceBrute(S1, S2, i + 1, j); // Suponiendo c = 0 para el costo de eliminación
    int replace = replaceCost(S1[i] - 'a', S2[j] - 'a') + editDistanceBrute(S1, S2, i + 1, j + 1);
    int transpose = INT_MAX;

    if (i + 1 < S1.length() && j + 1 < S2.length() &&
        S1[i] == S2[j + 1] && S1[i + 1] == S2[j]) {
        transpose = transposeCost(S1[i] - 'a', S2[j] - 'a') + editDistanceBrute(S1, S2, i + 2, j + 2);
    }

    return min(insert, min(del, min(replace, transpose)));
}

// Programación Dinámica
int editDistanceDP(string S1, string S2) {
    int m = S1.length();
    int n = S2.length();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1));

    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0) {
                dp[i][j] = j * insertCost(0); // Costo de insertar j caracteres
            } else if (j == 0) {
                dp[i][j] = i * deleteCost(0); // Costo de eliminar i caracteres
            } else if (S1[i - 1] == S2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1]; // No hay costo si son iguales
            } else {
                int insert = dp[i][j - 1] + insertCost(0);
                int del = dp[i - 1][j] + deleteCost(0);
                int replace = dp[i - 1][j - 1] + replaceCost(S1[i - 1] - 'a', S2[j - 1] - 'a');
                int transpose = INT_MAX;

                if (i > 1 && j > 1 && S1[i - 1] == S2[j - 2] && S1[i - 2] == S2[j - 1]) {
                    transpose = dp[i - 2][j - 2] + transposeCost(S1[i - 1] - 'a', S2[j - 1] - 'a');
                }

                dp[i][j] = min(insert, min(del, min(replace, transpose)));
            }
        }
    }
    return dp[m][n];
}

int main(int argc, char* argv[]) {
    if (argc < 3) {
        cerr << "Error: Faltan argumentos. Proporcione dos cadenas." << endl;
        return 1;
    }

    // Inicializar las tablas de costos
    initCostTables();

    string S1 = argv[1];
    string S2 = argv[2];

    int brute_result = editDistanceBrute(S1, S2, 0, 0);
    int dp_result = editDistanceDP(S1, S2);

    cout << "Brute Force Result: " << brute_result << endl;
    cout << "DP Result: " << dp_result << endl;

    return 0;
}
