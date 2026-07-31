#!/usr/bin/env python3
"""
Script helper para parsear notebooks (.ipynb) y convertirlos a una representación de texto
limpia y estructurada para ser analizada por el Agente Evaluador de IA.
"""

import json
import sys
import os

def parse_notebook(filepath: str) -> str:
    if not os.path.exists(filepath):
        return f"[ERROR] El archivo {filepath} no existe."
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except Exception as e:
        return f"[ERROR] No se pudo parsear el archivo {filepath} como JSON/Notebook: {str(e)}"
    
    parsed_content = [f"# Contenido del Notebook: {os.path.basename(filepath)}\n"]
    
    cells = nb.get('cells', [])
    for idx, cell in enumerate(cells, 1):
        cell_type = cell.get('cell_type', 'unknown')
        source = "".join(cell.get('source', []))
        
        if cell_type == 'markdown':
            parsed_content.append(f"### [Celda {idx} - Markdown]\n{source}\n")
        elif cell_type == 'code':
            parsed_content.append(f"### [Celda {idx} - Código Python]\n```python\n{source}\n```\n")
            
            # Revisar si hay salidas de texto o errores significativos
            outputs = cell.get('outputs', [])
            error_outputs = []
            text_outputs = []
            for out in outputs:
                if out.get('output_type') == 'error':
                    ename = out.get('ename', '')
                    evalue = out.get('evalue', '')
                    error_outputs.append(f"{ename}: {evalue}")
                elif out.get('output_type') in ['stream', 'execute_result']:
                    text = "".join(out.get('text', []))
                    if text.strip():
                        # Truncar salidas extremadamente largas
                        lines = text.strip().split('\n')
                        if len(lines) > 10:
                            text = "\n".join(lines[:5]) + "\n... [salida truncada] ...\n" + "\n".join(lines[-5:])
                        text_outputs.append(text)
            
            if error_outputs:
                parsed_content.append(f"**Error de Ejecución Registrado en Celda:**\n```text\n" + "\n".join(error_outputs) + "\n```\n")
            elif text_outputs:
                parsed_content.append(f"**Salida Impresa de Celda (Muestreo):**\n```text\n" + "\n".join(text_outputs) + "\n```\n")

    return "\n".join(parsed_content)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python parse_notebook.py <path_al_notebook.ipynb>")
        sys.exit(1)
        
    path = sys.argv[1]
    result = parse_notebook(path)
    print(result)
