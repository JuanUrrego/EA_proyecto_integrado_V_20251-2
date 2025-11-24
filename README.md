# Proyecto Integrado V – Análisis de Estilos de Vida y Riesgos de Salud

Repositorio: https://github.com/JuanUrrego/EA_proyecto_integrado_V_20251-2

Este proyecto desarrolla un proceso completo de ingeniería de datos aplicado a un dataset de estilos de vida, con el objetivo de identificar patrones asociados a riesgos de salud en población adulta. Forma parte del Proyecto Integrado V y documenta todo el flujo: ingesta → limpieza → enriquecimiento → análisis exploratorio, junto con evidencia técnica, scripts y el informe académico en Normas APA.

## Objetivo General
Implementar un proceso de transformación y análisis descriptivo de datos basado en un dataset público de estilos de vida, con el fin de comprender patrones asociados a riesgos de salud en población adulta de Medellín.

## Objetivos Específicos
- Preparar y depurar los datos descargados desde Kaggle.
- Enriquecer la información mediante variables temporales y categorías analíticas.
- Realizar análisis exploratorio con estadísticas y visualizaciones.
- Documentar todo el proceso en GitHub y APA.

## Dataset
Fuente: Kaggle – Lifestyle and Health Risk Prediction Dataset  
Autor: zahranusrat  
Licencia: CC0 (Dominio Público)  
Registros: 4.257  

## Metodología
1. Ingesta y preparación de datos  
2. Diseño del pipeline  
3. Limpieza de datos  
4. Enriquecimiento del dataset  
5. Análisis exploratorio descriptivo (EDA)

## Ejecución
```
pip install -r requirements.txt
python scripts/load_to_sqlite.py --csv data/lifestyle_health_kaggle.csv --db db/proyecto.db --table lifestyle_health
python scripts/export_from_sqlite.py --db db/proyecto.db --table lifestyle_health --out db/export.csv
```

## Estructura del Repositorio
data/, db/, docs/, notebooks/, scripts/, src/, README.md

## Resultados
Resumen de patrones de IMC, ejercicio, sueño e ingesta de azúcar, con tendencias estables entre 2022–2024.

## Referencias
- Kaggle  
- Python 3.9.12  
- Pandas  
- Purdue OWL APA 7  
