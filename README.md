# Proyecto Integrado V – Análisis de Estilos de Vida y Riesgos de Salud

Repositorio: https://github.com/JuanUrrego/EA_proyecto_integrado_V_20251-2

Este proyecto desarrolla un proceso completo de ingeniería de datos aplicado a un dataset de estilos de vida, con el objetivo de identificar patrones asociados a riesgos de salud en población adulta. Forma parte del Proyecto Integrado V y documenta todo el flujo: ingesta → limpieza → enriquecimiento → análisis exploratorio, junto con evidencia técnica, scripts y el informe académico en Normas APA.

## Objetivo General
Implementar un proceso de transformación y análisis descriptivo de datos basado en un dataset público de estilos de vida, con el fin de comprender patrones asociados a riesgos de salud en población adulta de Medellín.

## Objetivos Específicos
--Preparar y depurar los datos descargados desde Kaggle, asegurando su calidad mediante estandarización, corrección de inconsistencias y validación estructural.
--Enriquecer el dataset mediante la creación de variables temporales (año, mes, día) y categorías analíticas como grupos de edad, niveles de IMC, sueño, ejercicio e ingesta de azúcar.
--Realizar un análisis exploratorio robusto, empleando estadísticas descriptivas y visualizaciones iniciales para identificar patrones generales y relaciones entre las variables clave.
--Construir un dashboard descriptivo en Power BI que permita sintetizar, comparar e interpretar de manera visual los principales hallazgos del análisis.
--Documentar todo el proceso técnico y analítico en el repositorio de GitHub y en el informe académico siguiendo las Normas APA, garantizando trazabilidad y claridad metodológica.

## Dataset
Fuente: Kaggle – Lifestyle and Health Risk Prediction Dataset  
Autor: zahranusrat  
Licencia: CC0 (Dominio Público)  
Registros: 4.257  
https://www.kaggle.com/datasets/zahranusrat/lifestyle-and-health-risk-prediction-dataset

=======
Repositorio: https://github.com/JuanUrrego/EA_proyecto_integrado_V_20251-2

Este dataset contiene información clave sobre hábitos y condiciones relacionadas con la salud:
Edad (age)
Índice de Masa Corporal (bmi)
Horas de sueño (sleep)
Ingesta de azúcar (sugar_intake)
Ejercicio semanal (exercise)

🏗️ Metodología Aplicada

El desarrollo del proyecto siguió un enfoque ágil utilizando Scrum, organizando cada fase en sprints académicos y documentando las evidencias técnicas en GitHub.

1️⃣ Ingesta y Preparación de Datos

Descarga del dataset desde Kaggle.
Registro de licencia, fuente y ruta.
Carga a una base SQLite.

Exportación a CSV como validación de integridad.

2️⃣ Diseño del Pipeline de Procesamiento
Dataset (Kaggle) → Limpieza → Enriquecimiento → SQLite → CSV Final


## Ejecución
```
pip install -r requirements.txt
python scripts/load_to_sqlite.py --csv data/lifestyle_health_kaggle.csv --db db/proyecto.db --table lifestyle_health
=======
Incluye:

Control de versiones GitHub
Scripts para ingestión y exportación
Notebook con trazabilidad completa

3️⃣ Limpieza de Datos

Eliminación de duplicados
Corrección de valores inconsistentes
Normalización de tipos de datos
Estandarización de nombres de columnas
Documentación de cada transformación

4️⃣ Enriquecimiento del Dataset

Creación de fechas aleatorias (2022–2024)
Derivación de columnas: año, mes, día
Categorización:
grupos de edad
IMC
niveles de sueño
niveles de ejercicio
niveles de ingesta de azúcar

5️⃣ Análisis Exploratorio (EDA)

Incluyó:
Estadísticas descriptivas
Histogramas
Gráficos de barras
Matriz de correlación
Tendencias temporales
Principales hallazgos:
Edad promedio: ~49 años
IMC promedio: 26.8 (sobrepeso)
Actividad física baja/moderada predominante
Horas de sueño centradas entre 6–8
Ingesta de azúcar mayormente baja/media

6️⃣ Construcción del Dashboard Descriptivo en Power BI

Se desarrolló un dashboard interactivo que consolidó los hallazgos del análisis, permitiendo una visualización clara del comportamiento de las cinco variables clave (edad, IMC, ejercicio, sueño e ingesta de azúcar).
Incluyó:
Tarjetas resumen de indicadores principales
Gráficos de columnas y barras comparativas
Distribución del IMC por categoría y grupo de edad
Relación entre ejercicio e ingesta de azúcar
Gráfico temporal basado en la fecha generada
Filtros interactivos por año, grupo de edad y categorías analíticas
Este dashboard fortaleció la interpretación del análisis, permitiendo identificar visualmente la prevalencia de sobrepeso/obesidad, los bajos niveles de ejercicio y las diferencias entre edades en patrones de sueño y consumo de azúcar.

📁 Estructura del Repositorio
├── data/
│   └── lifestyle_health_kaggle.csv
├── db/
│   ├── proyecto.db
│   └── export.csv
├── docs/
│   ├── APA_Etapa1.docx
│   └── APA_Etapa2.docx
│   └── graficos/
├── notebooks/
│   └── etapa_2_limpieza_enriquecimiento.ipynb
├── scripts/
│   ├── load_to_sqlite.py
│   └── export_from_sqlite.py
├── src/
│   └── ingestar.py
├── requirements.txt
└── README.md



⚙️ Ejecución del Pipeline
1. Instalar dependencias
pip install -r requirements.txt

2. Cargar datos a SQLite
python scripts/load_to_sqlite.py --csv data/lifestyle_health_kaggle.csv --db db/proyecto.db --table lifestyle_health

3. Exportar a CSV
python scripts/export_from_sqlite.py --db db/proyecto.db --table lifestyle_health --out db/export.csv
```

## Estructura del Repositorio
data/, db/, docs/, src/, README.md

## Resultados
Resumen de patrones de IMC, ejercicio, sueño e ingesta de azúcar, con tendencias estables entre 2022–2024.

El proyecto permitió obtener un dataset limpio, estructurado y enriquecido, acompañado de un análisis descriptivo robusto y un dashboard interactivo que resume:
Patrones de IMC, mostrando más del 50% en sobrepeso u obesidad
Predominio de actividad física baja
Niveles de sueño entre 6–8 horas
Ingesta de azúcar baja o media en la mayoría
Tendencias temporales estables entre 2022–2024
El dashboard facilita la exploración de estos patrones de forma dinámica, convirtiéndose en un insumo clave para la interpretación y toma de decisiones relacionadas con la salud y el estilo de vida de la población.

## Referencias
- Kaggle  
- Python 3.9.12  
- Pandas  
- Purdue OWL APA 7  
=======
📈 Resultados del Análisis

El análisis descriptivo, complementado con el dashboard interactivo en Power BI, permitió caracterizar de manera integral los hábitos y condiciones de la población analizada. Entre los principales hallazgos se destacan:
Predominio de sedentarismo, evidenciado en que la mayoría de registros se concentran en niveles bajos o moderados de actividad física.
Hábitos de sueño relativamente adecuados, con una distribución que se mantiene mayoritariamente entre 6 y 8 horas diarias.
Alta prevalencia de sobrepeso y obesidad, lo cual se refleja en que más del 50 % de la población se ubica en categorías superiores al IMC normal.
Consumo de azúcar predominantemente bajo o medio, aunque con diferencias entre grupos de edad.
Poca variación temporal, debido a que las fechas generadas fueron sintéticas y se distribuyen de forma estable entre 2022 y 2024.
Estas tendencias fueron reafirmadas visualmente a través del dashboard, el cual permitió identificar y comparar patrones entre categorías de IMC, grupos etarios, niveles de ejercicio y otros factores clave relacionados con la salud y el estilo de vida.


📝 Referencias

Kaggle – Lifestyle and Health Risk Prediction Dataset
Python Software Foundation – Documentación Python 3.9.12
Pandas Development Team
Purdue OWL – APA 7

