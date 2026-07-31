#!/usr/bin/env python3
"""
Agente Evaluador Automático para GitHub Pull Requests (Redes Neuronales).
Utiliza la API de Gemini para generar retroalimentación estructurada en los 6 ejes.
"""

import os
import sys
import json
import urllib.request
import urllib.error
from parse_notebook import parse_notebook

RUBRIC_PATH = "docs/rubrica_6_ejes.md"

PROMPT_SYSTEM = """Eres un Asistente y Profesor Evaluador Experto en Redes Neuronales y Visión por Computador.
Tu objetivo es revisar las entregas de proyectos de estudiantes de nivel universitario y proporcionar retroalimentación constructiva, detallada y motivadora mediante Pull Requests de GitHub.

Debes evaluar el entregable proporcionado en función de los siguientes 6 EJES DE EVALUACIÓN:
1. Validez y lógica del código
2. Cumplimiento de requerimientos
3. Razonamiento y documentación
4. Toma de decisiones (hiperparámetros, arquitecturas, preprocesamiento)
5. Originalidad del proceso
6. Calidad de resultados y análisis de métricas

REGLAS DE RESPUESTA:
- Utiliza formato Markdown limpio con emojis y alertas para facilitar la lectura.
- Organiza tu respuesta en secciones para cada uno de los 6 Ejes.
- Para cada eje, otorga una valoración ("✅ Excelente", "⚠️ A Mejorar", o "❌ Deficiente") seguida de justificación.
- Incluye una sección final de "💡 Sugerencias Concretas de Acción" con los pasos exactos que los estudiantes deben realizar en su próximo commit para resolver las debilidades señaladas.
- Mantén un tono respetuoso, pedagógico y alentador.
"""

def load_rubric():
    if os.path.exists(RUBRIC_PATH):
        with open(RUBRIC_PATH, 'r', encoding='utf-8') as f:
            return f.read()
    return "Ejes de evaluación estándar de redes neuronales."

def call_gemini_api(api_key: str, content_to_review: str, rubric: str) -> str:
    # Endpoint de Gemini API (Gemini 1.5 Flash o Gemini 2.0 Flash)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    prompt_user = f"""
 RÚBRICA Y CONTEXTO DEL CURSO:
{rubric}

 ENTREGABLE A EVALUAR:
{content_to_review}

Por favor genera la evaluación detallada según las instrucciones del sistema.
"""
    
    payload = {
        "contents": [{
            "parts": [{"text": PROMPT_SYSTEM + "\n\n" + prompt_user}]
        }],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 2048
        }
    }
    
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode('utf-8')
            res_json = json.loads(res_body)
            candidates = res_json.get('candidates', [])
            if candidates:
                parts = candidates[0].get('content', {}).get('parts', [])
                if parts:
                    return parts[0].get('text', '')
            return "No se pudo obtener una respuesta válida del agente revisor."
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8')
        print(f"HTTPError en Gemini API ({e.code}): {err_msg}", file=sys.stderr)
        return f"Error en la consulta al Agente de IA (HTTP {e.code}). Verifique la API Key de Gemini."
    except Exception as e:
        print(f"Error general consultando Gemini API: {str(e)}", file=sys.stderr)
        return f"Error al comunicar con la API de IA: {str(e)}"

def post_github_comment(github_token: str, repo: str, pr_number: str, comment_body: str):
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    payload = {"body": comment_body}
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json',
        'Content-Type': 'application/json'
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            print("Comentario de retroalimentación publicado exitosamente en el PR.")
    except Exception as e:
        print(f"Error al publicar el comentario en GitHub: {str(e)}", file=sys.stderr)

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    github_token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")
    pr_number = os.getenv("PR_NUMBER")
    changed_files = os.getenv("CHANGED_FILES", "").split()

    if not api_key:
        print("Error: Falta la variable de entorno GEMINI_API_KEY", file=sys.stderr)
        sys.exit(1)

    print(f"Iniciando evaluación de archivos modificados: {changed_files}")
    
    content_to_review = ""
    for file in changed_files:
        if file.endswith('.ipynb'):
            content_to_review += f"\n--- ARCHIVO NOTEBOOK: {file} ---\n"
            content_to_review += parse_notebook(file)
        elif file.endswith('.py') or file.endswith('.md'):
            if os.path.exists(file):
                with open(file, 'r', encoding='utf-8') as f:
                    content_to_review += f"\n--- ARCHIVO {file} ---\n" + f.read()

    if not content_to_review.strip():
        print("No se encontraron notebooks ni archivos relevantes para evaluar.")
        return

    rubric = load_rubric()
    feedback = call_gemini_api(api_key, content_to_review, rubric)

    final_comment = f"##  Retroalimentación Automática del Agente Evaluador\n\n{feedback}\n\n---\n*Nota: Este análisis fue generado automáticamente. Pueden subir un nuevo commit con mejoras para actualizar la revisión.*"

    print("\n--- FEEDBACK GENERADO ---\n")
    print(feedback)

    if github_token and repo and pr_number:
        post_github_comment(github_token, repo, pr_number, final_comment)

if __name__ == '__main__':
    main()
