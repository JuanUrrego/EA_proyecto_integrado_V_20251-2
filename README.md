# Proyecto Integrado V – Análisis de Estilos de Vida y Riesgos de Salud

<<<<<<< HEAD
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
=======
📘 Proyecto Integrado V – Análisis de Estilos de Vida y Riesgos de Salud
Ingeniería de Software y Datos – IU Digital de Antioquia

Repositorio: https://github.com/JuanUrrego/EA_proyecto_integrado_V_20251-2

Este proyecto desarrolla un proceso completo de ingeniería de datos aplicado a un dataset de estilos de vida, con el objetivo de identificar patrones asociados a riesgos de salud en población adulta. Forma parte del Proyecto Integrado V y documenta todo el flujo: ingesta → limpieza → enriquecimiento → análisis exploratorio, junto con evidencia técnica, scripts y el informe académico en Normas APA.

🧭 Objetivo General

Implementar un proceso de transformación y análisis descriptivo de datos basado en un dataset público de estilos de vida, con el fin de comprender patrones asociados a riesgos de salud en población adulta de Medellín.

🎯 Objetivos Específicos

Preparar y depurar los datos descargados desde Kaggle, registrando su origen, estandarizando nombres y corrigiendo duplicados o inconsistencias.

Enriquecer la información mediante variables temporales (año, mes, día) y categorías analíticas (IMC, grupos de edad, sueño, actividad física, ingesta de azúcar).

Realizar análisis exploratorio mediante estadísticas descriptivas, histogramas, correlaciones y tendencias.

Documentar todo el proceso y garantizar trazabilidad mediante notebooks, scripts y el documento APA.

📊 Dataset

Fuente: Kaggle – Lifestyle and Health Risk Prediction Dataset
Autor: zahranusrat
Licencia: CC0 (Dominio Público)
Registros: 4.257

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
>>>>>>> 9108beb04c142740ff8024f888d594c953bd0f54

## Metodología
1. Ingesta y preparación de datos  
2. Diseño del pipeline  
3. Limpieza de datos  
4. Enriquecimiento del dataset  
5. Análisis exploratorio descriptivo (EDA)

<<<<<<< HEAD
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

📁 Estructura del Repositorio
├── data/
│   └── lifestyle_health_kaggle.csv
├── db/
│   ├── proyecto.db
│   └── export.csv
├── docs/
│   ├── APA_Etapa1.docx
│   ├── APA_Etapa2.docx
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
>>>>>>> 9108beb04c142740ff8024f888d594c953bd0f54
python scripts/export_from_sqlite.py --db db/proyecto.db --table lifestyle_health --out db/export.csv

<<<<<<< HEAD
## Estructura del Repositorio
data/, db/, docs/, notebooks/, scripts/, src/, README.md

## Resultados
Resumen de patrones de IMC, ejercicio, sueño e ingesta de azúcar, con tendencias estables entre 2022–2024.

## Referencias
- Kaggle  
- Python 3.9.12  
- Pandas  
- Purdue OWL APA 7  
=======
📈 Resultados del Análisis

El análisis descriptivo permitió caracterizar los hábitos de la población y detectar:

Riesgo nutricional asociado al sobrepeso.

Tendencias de sedentarismo.

Hábitos de sueño relativamente adecuados.

Poca variación temporal en los registros (fechas sintéticas).

Estos resultados generan un insumo analítico sólido para la Etapa 3, donde se realizarán visualizaciones y posibles modelos predictivos.

📝 Referencias

Kaggle – Lifestyle and Health Risk Prediction Dataset

Python Software Foundation – Documentación Python 3.9.12

Pandas Development Team

Purdue OWL – APA 7
>>>>>>> 9108beb04c142740ff8024f888d594c953bd0f54
