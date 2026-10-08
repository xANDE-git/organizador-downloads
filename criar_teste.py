from pathlib import Path

pasta_teste = Path.home() / "teste_downloads"
pasta_teste.mkdir(exist_ok=True)

nomes = [
    "foto.jpg", "FOTO2.PNG", "relatorio.pdf", "filme.mkv", "filme.srt",
    "setup.exe", "musica.mp3", "arquivos.zip", "script.py",
    "estranho.xyz", "~$temporario.docx",
]

for nome in nomes:
    (pasta_teste / nome).touch()