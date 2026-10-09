from pathlib import Path 
SIMULAR = True

pasta = Path("Downloads") / "teste_downloads"
for item in list(pasta.iterdir()):
    extensao = item.suffix.lower()
    if item.is_file() and not item.name.startswith("~$"):
        if extensao in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
         categoria = "Imagens"
        elif extensao in [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".doc", ".md", ".sql"]:
         categoria = "Documentos"
        elif extensao in [".mp4", ".avi", ".mov", ".mkv", ".webm", ".srt"]:
         categoria = "Vídeos"
        elif extensao in [".exe", ".msi", ".bat", ".msix"]:
         categoria = "Executáveis"
        elif extensao in [".mp3", ".wav", ".flac", ".aac", ".ogg"]:
         categoria = "Áudios"
        elif extensao in [".html", ".css", ".js", ".php", ".py", ".java", ".c", ".cpp"]:
         categoria = "Códigos"
        elif extensao in [".zip", ".rar", ".tar", ".gz", ".7z"]:
         categoria = "Compactados"
        else:
            categoria = "Outros"
        if categoria != "Outros":
            destino = pasta / categoria
            destino_arquivo = destino / item.name
            if destino_arquivo.exists():
                print(f"{item.name} já existe em {categoria}, pulando")
            else:
                destino.mkdir(exist_ok=True)
                item.rename (destino_arquivo)
                print (f"{item.name} -> {categoria}")
                       