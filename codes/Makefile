# Variables
CXX = g++
CXXFLAGS = -std=c++11 -O2
TARGET = edit_distance
PYTHON_SCRIPT = run_experiments.py
OUTPUT_CSV = averaged_experiment_results_cpp.csv
IMAGES = comparison_execution_times.png speedup_ratio.png execution_times_vs_length.png execution_time_distribution.png

# Regla principal: compilar y ejecutar el script de Python
all: $(TARGET) run_python

# Compilar el programa de C++
$(TARGET): $(TARGET).cpp
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(TARGET).cpp

# Ejecutar el script de Python
run_python:
	python3 $(PYTHON_SCRIPT)

# Limpiar archivos generados
clean:
	rm -f $(TARGET) $(OUTPUT_CSV) $(IMAGES)
