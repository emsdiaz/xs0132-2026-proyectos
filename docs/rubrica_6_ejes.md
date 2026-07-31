# Rúbrica de Evaluación de Proyectos de Redes Neuronales

Esta rúbrica es utilizada por el **Agente Evaluador Automático** y por el equipo docente para otorgar retroalimentación en los Pull Requests de cada entrega.

---

## 📋 Los 6 Ejes de Evaluación

### 1. Validez y Lógica del Código
* **Excelente**: El código corre sin fallos, utiliza eficientemente vectorización en tensores/arrays, gestiona adecuadamente la carga y formateo de imágenes, y sigue buenas prácticas de programación.
* **A Mejorar**: Presencia de bloques redundantes, errores sintácticos, problemas de dimensión en tensores o uso inadecuado del GPU/CPU.

### 2. Cumplimiento de Requerimientos
* **Excelente**: Cumple con el 100% de los puntos definidos en la guía del entregable actual (ej. división de datasets, arquitectura específica, análisis de métricas).
* **A Mejorar**: Omitir secciones obligatorias, no presentar gráficos solicitados o falta de implementación de componentes requeridos.

### 3. Razonamiento y Documentación
* **Excelente**: Uso sobresaliente de celdas Markdown intercaladas con el código. Explicación teórica clara de los algoritmos y transformación de datos.
* **A Mejorar**: Notebook con únicamente celdas de código sin explicaciones o Markdown superficial que no justifica el flujo de trabajo.

### 4. Toma de Decisiones
* **Excelente**: Justificación técnica de las decisiones (elección de hiperparámetros como learning rate, batch size, funciones de activación, regularización y data augmentation).
* **A Mejorar**: Selección arbitraria de hiperparámetros sin explicación ni contrastación experimental.

### 5. Originalidad del Proceso
* **Excelente**: Demuestra exploración propia, pruebas con distintas arquitecturas o variaciones en el preprocesamiento, y aportes analíticos propios.
* **A Mejorar**: Uso de scripts genéricos copiados sin adaptación ni interpretación específica al dataset asignado.

### 6. Calidad de Resultados
* **Excelente**: Presentación clara de curvas de aprendizaje (Loss/Accuracy en Train vs Val), matriz de confusión, métricas globales y análisis profundo de errores/sesgos en las imágenes.
* **A Mejorar**: Mostrar métricas aisladas sin gráficos, omitir el análisis de overfitting/underfitting o sacar conclusiones no respaldadas por los datos.
