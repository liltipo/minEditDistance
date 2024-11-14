# Comparación de Enfoques: Fuerza Bruta vs Programación Dinámica

Este repositorio está diseñado para comparar los tiempos de ejecución de dos enfoques para calcular la distancia de edición entre cadenas: **Fuerza Bruta** y **Programación Dinámica**. Los algoritmos están implementados en **C++**, y se utilizan **Python** para generar gráficos comparativos basados en los resultados experimentales obtenidos.

## Contenido del Repositorio

- **C++ Code**: Implementaciones de los algoritmos de Fuerza Bruta y Programación Dinámica para calcular la distancia de edición entre cadenas.
- **Python Scripts**: Scripts para generar gráficos y visualizar los resultados experimentales de los algoritmos.
- **Informe en LaTeX**: Un informe en formato LaTeX que describe el problema, los enfoques, los experimentos y los resultados obtenidos. Este informe también puede ser utilizado como plantilla para futuros trabajos o investigaciones.

## Cómo Ejecutar el Proyecto

1. **Python**:
   - Instala las dependencias necesarias (por ejemplo, `matplotlib`, `numpy`):
     ```bash
     pip install matplotlib numpy
     ```
     
2. **Makefile**:
   - Navega al directorio que contiene archivo Makefile.
   - Compila y ejecuta los programas con el siguiente comando:
     ```bash
     make
     ```
   - Elimina el ejecutable y los archivos generados con:
     ```bash
     make
     ```

3. **LaTeX**:
   - El informe está escrito en LaTeX y puede ser compilado con cualquier editor LaTeX como Overleaf o un editor local (por ejemplo, VSCode con la extensión LaTeX).
   - Para compilar el informe, ejecuta el siguiente comando:
     ```bash
     pdflatex tarea_main.tex
     ```

## Propósito del Proyecto

Este proyecto tiene como objetivo principal mostrar cómo la **Programación Dinámica** puede ser más eficiente que el enfoque de **Fuerza Bruta** en la resolución de problemas de distancia de edición. A través de la ejecución de experimentos y la comparación de los tiempos de ejecución de ambos enfoques, se proporcionan datos empíricos que respaldan esta afirmación.
