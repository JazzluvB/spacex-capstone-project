from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_filename = "presentacion_final_spacex.pdf"
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=landscape(A4),
    rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30
)

styles = getSampleStyleSheet()
title_style = ParagraphStyle('SlideTitle', parent=styles['Heading1'], fontSize=18, leading=22, textColor=colors.HexColor("#0f2537"))
subtitle_style = ParagraphStyle('SlideSubtitle', parent=styles['Heading2'], fontSize=12, leading=15, textColor=colors.HexColor("#1b5e20"))
body_style = ParagraphStyle('SlideBody', parent=styles['Normal'], fontSize=9, leading=13, textColor=colors.HexColor("#212121"))

story = []

def add_header(title_text, category_text=""):
    story.append(Paragraph(f"<b>{title_text}</b>", title_style))
    if category_text:
        story.append(Paragraph(f"<i>{category_text}</i>", subtitle_style))
    story.append(Spacer(1, 8))

# Diapositiva 1: Portada y GitHub
add_header("SpaceX Falcon 9 Landing Prediction Capstone", "IBM Applied Data Science Capstone Project")
story.append(Paragraph("<b>Presentado por:</b> Carlos Palacios Betancourt | Data & AI Professional", body_style))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>GitHub Repository URL:</b> <font color='blue'><u>https://github.com/JazzluvB/spacex-capstone-project</u></font>", body_style))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>Resumen:</b> Aplicación del ciclo de vida completo de ciencia de datos para predecir el éxito de aterrizaje de la primera etapa del cohete Falcon 9.", body_style))
story.append(PageBreak())

# Diapositiva 2: Resumen Ejecutivo
add_header("Resumen Ejecutivo", "Executive Summary")
story.append(Paragraph("Este proyecto analiza la reutilización de la primera etapa del Falcon 9 mediante la extracción de datos vía API y Web Scraping, análisis exploratorio con SQL y Pandas, visualización interactiva con Folium y Plotly Dash, y modelado predictivo de Machine Learning con una precisión del 83.33% en datos de prueba.", body_style))
story.append(PageBreak())

# Diapositiva 3: Introducción y Metodología
add_header("Introducción y Metodología", "Data Collection & Wrangling")
story.append(Paragraph("• <b>Extracción:</b> Uso de la API oficial de SpaceX y scraping de Wikipedia.<br/>• <b>Wrangling:</b> Limpieza de datos, manejo de nulos y creación de la variable binaria Class.<br/>• <b>EDA & SQL:</b> Consultas SQLite y visualizaciones con Seaborn para evaluar tendencias.", body_style))
story.append(PageBreak())

# Diapositiva 4: Mapas y Dashboards Interactivos
add_header("Análisis Espacial y Dashboard", "Folium & Plotly Dash Results")
story.append(Paragraph("• <b>Folium:</b> Mapeo geoespacial interactivo para evaluar la proximidad de los sitios de lanzamiento a la costa y vías de transporte.<br/>• <b>Plotly Dash:</b> Aplicación web con selectores dinámicos de sitios de lanzamiento y rangos de masa de carga útil.", body_style))
story.append(PageBreak())

# Diapositiva 5: Machine Learning y Conclusiones
add_header("Machine Learning y Conclusiones", "Model Performance & Conclusion")
story.append(Paragraph("Se evaluaron clasificadores (Logistic Regression, SVM, Decision Tree y KNN) mediante 10-fold CV, logrando una precisión de <b>83.33%</b> en el conjunto de prueba.<br/><br/><b>Conclusión:</b> La masa de carga y la órbita son los predictores clave para el éxito del aterrizaje, optimizando los costos de lanzamiento.", body_style))

doc.build(story)