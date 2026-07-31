# Proyecto de Redes Neuronales - Plantilla de Entrega

¡Bienvenidos al proyecto de Redes Neuronales! Este repositorio servirá como la plantilla base para las entregas y la retroalimentación continua de su proyecto.

---

## 📁 Estructura del Repositorio

```text
├── .github/
│   └── workflows/
│       └── ai_reviewer.yml      # Workflow de evaluación automática en PRs
├── data/                       # Instrucciones o enlaces a datasets (no subir archivos pesados)
├── docs/                       # Guías y rúbrica del proyecto
│   └── rubrica_6_ejes.md
├── notebooks/                  # Entregables principales (.ipynb)
│   └── avance_proyecto.ipynb
├── src/                        # Módulos auxiliares en Python (opcional)
└── README.md                   # Descripción del proyecto de su grupo
```

---

## 🚀 Flujo de Trabajo y Entregas (Pull Requests)

Para recibir retroalimentación automática y del equipo docente en cada entrega:

1. **Trabajar en su repositorio de grupo**:
   - Cada integrante puede trabajar en una rama (branch) propia, por ejemplo `feature/preprocesamiento` o `feature/modelo`.
2. **Abrir un Pull Request (PR)**:
   - Cuando tengan listo un avance o entrega en la carpeta `notebooks/`, abran un Pull Request hacia la rama `main`.
3. **Revisión por Agente IA (Feedback)**:
   - Al abrir o actualizar el PR, un **Agente Evaluador IA** revisará su entrega automáticamente en unos minutos y dejará un comentario detallado en el PR con sugerencias de mejora basadas en los **6 ejes de evaluación**.
4. **Iterar y Mejorar**:
   - Lean las sugerencias del agente, realicen los ajustes necesarios en su notebook/código y hagan un nuevo `push` a la misma rama del PR.
   - El agente volverá a evaluar los cambios hasta que la entrega cumpla con los estándares requeridos.

---

## 📊 Ejes de Evaluación

Cada entrega se evaluará bajo los siguientes criterios:

1. **Validez y lógica del código**: Ausencia de errores lógicos, manejo correcto de datos/tensores y librerías (PyTorch, TensorFlow, OpenCV, Scikit-learn, etc.).
2. **Cumplimiento de requerimientos**: Completitud de todos los puntos solicitados en la guía específica de la entrega.
3. **Razonamiento y documentación**: Uso claro de celdas Markdown en el notebook explicando el proceso técnico y la justificación teórica.
4. **Toma de decisiones**: Justificación en la elección de la arquitectura, funciones de pérdida, optimizadores y técnicas de data augmentation.
5. **Originalidad del proceso**: Enfoque propio en la resolución del problema y análisis crítico.
6. **Calidad de resultados**: Interpretación adecuada de métricas (Accuracy, Precision, Recall, Loss, Matriz de Confusión, Overfitting/Underfitting).
