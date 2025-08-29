#Este é um detector de palavras em INGLÊS. Ele verificará se em seu arquivo PDF escrito em PT-BR há palavras em inglês. !! Vale ressaltar que este detector também irá mostrar palavras que são morfologicamente idênticas às do léxico do corpus original (PT-BR).

import fitz
import re
from wordfreq import zipf_frequency

def extrair_texto_pdf(arquivo_pdf: str) -> str:
    doc = fitz.open(arquivo_pdf)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    return texto

def encontrar_palavras_ingles(texto: str) -> set:
    palavras = re.findall(r"\b\w+\b", texto.lower())
    ingles_detectadas = set()

    for palavra in palavras:
        if not palavra.isalpha():  # ignora números e tokens com dígitos
            continue

        freq_pt = zipf_frequency(palavra, "pt")
        freq_en = zipf_frequency(palavra, "en")

        if freq_en > 0 and (freq_pt == 0 or freq_en > freq_pt):
            ingles_detectadas.add(palavra)

    return ingles_detectadas

if __name__ == "__main__":
    arquivo = r"" # Neste string "", insira o diretório direto para seu arquivo PDF (Exemplo: "C:\Downloads\seuarquivo.pdf")
    texto = extrair_texto_pdf(arquivo)

    palavras_em_ingles = encontrar_palavras_ingles(texto)

    print("Palavras em inglês detectadas:")
    for p in sorted(palavras_em_ingles):
        print(p)
