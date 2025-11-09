[Lifestyle_and_Health_Risk_Prediction_Synthetic_Dataset (1).csv](https://github.com/user-attachments/files/23443070/Lifestyle_and_Health_Risk_Prediction_Synthetic_Dataset.1.csv)# EA_proyecto_integrado_V_20251-2

# Proyecto: Predicción de Riesgos de Salud a partir de Estilos de Vida

> **Stack base:** Python **3.9.12**, SQLite, pandas.  

## Objetivo
Evidenciar el flujo **dataset (Kaggle) → SQLite → CSV** y la documentación **APA (Etapa 1)** para este caso vamos a identificar patrones entre hábitos (ejercicio, sueño, consumo) y riesgos de salud (hipertensión/diabetes).

## Dataset
- **Nombre**: Lifestyle_and_Health_Risk_Prediction_Dataset  
- **Autor(a)**: zahranusrat  
- **Enlace**: https://www.kaggle.com/datasets/zahranusrat/lifestyle-and-health-risk-prediction-dataset
- Licencia: CC0: Public Domain (Dominio Público)
- Dataset: 
[Uploading Lifestyle_and_Health_Risk_Prediction_Synthetic_Dataset (1).csv…]()


## Requisitos
- Python **3.9.12**
- `pip install -r requirements.txt`

## Estructura
```
data/                 # dataset original o enlace en README
db/
  ├─ proyecto.db      # base SQLite
  └─ export.csv       # exportación desde SQLite
docs/
  ├─ APA_Etapa1.docx  # documento APA (Etapa 1)
  └─ Gantt.xlsx       # diagrama de Gantt (WBS)
scripts/
  ├─ load_to_sqlite.py
  └─ export_from_sqlite.py
src/
  └─ ingestar.py      # clase para ingesta Kaggle -> DataFrame
proyecto_integrador.py # wrapper (py_modules)
README.md
setup.py
requirements.txt
```

## Uso rápido (descarga Kaggle con `kagglehub`)
```python
from src.ingestar import Ingestar

ing = Ingestar()
# Referencia Kaggle:
# 'zahranusrat/lifestyle-and-health-risk-prediction-dataset'
path = ing.download_dataset_zip("zahranusrat/lifestyle-and-health-risk-prediction-dataset")
data_dir = ing.extract_zip_files(path)
df = ing.load_dataset_as_dataframe(data_dir)
print(df.head())
```

## Pipeline SQLite
```bash
python scripts/load_to_sqlite.py --csv data/lifestyle_health_sample.csv --db db/proyecto.db --table lifestyle_health
python scripts/export_from_sqlite.py --db db/proyecto.db --table lifestyle_health --out db/export.csv
```

## APA (Etapa 1)
Documento en `docs/APA_Etapa1.docx` con:
- Portada, listado de tablas/figuras.
- Resumen.
- Objetivo general y específicos.
- Metodología.
- Resultados-
- Referencias.

## Créditos y referencias
- Kaggle dataset (zahranusrat).
- Formato APA 7ª edición (OWL Purdue).
