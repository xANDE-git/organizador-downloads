# Organizador de Downloads

Um script em Python que organiza uma pasta automaticamente, separando os
arquivos soltos em subpastas por tipo.

## O que ele faz

Olha cada arquivo da pasta e move para a subpasta certa, de acordo com a extensão
(sem diferenciar maiúscula de minúscula: `.JPG` e `.jpg` são tratados igual).

| Pasta        | Extensões                                             |
|--------------|-------------------------------------------------------|
| Imagens      | .jpg, .jpeg, .png, .gif, .webp                        |
| Documentos   | .pdf, .docx, .doc, .txt, .xlsx, .pptx, .md, .sql      |
| Vídeos       | .mp4, .avi, .mov, .mkv, .webm, .srt (legendas)        |
| Executáveis  | .exe, .msi, .bat, .msix                               |
| Áudios       | .mp3, .wav, .flac, .aac, .ogg                         |
| Códigos      | .html, .css, .js, .php, .py, .java, .c, .cpp          |
| Compactados  | .zip, .rar, .tar, .gz, .7z                            |

## Regras de segurança

- Nenhum arquivo é apagado, só movido.
- Pastas existentes são ignoradas.
- Arquivos temporários do Office (que começam com `~$`) são ignorados.
- Arquivos de tipos desconhecidos ("Outros") ficam onde estão.
- As legendas (.srt) vão para a pasta Vídeos, junto com os filmes.

## Como usar

1. Tenha o Python 3 instalado.
2. **Teste primeiro.** Rode `python criar_teste.py` para criar a pasta
   `teste_downloads` com arquivos vazios de mentira.
3. Rode `python organizador.py`. Por padrão ele organiza a pasta de teste.
4. Para organizar outra pasta, troque esta linha no `organizador.py`:

```python
   pasta = Path.home() / "teste_downloads"
```

   Por exemplo, `Path.home() / "Downloads"`.

> Atenção: mover arquivos não tem "desfazer". Teste na pasta de mentira antes.

## Status

Em desenvolvimento. Este é meu primeiro projeto em Python.

## O que eu quero melhorar depois

- Decidir o que fazer com os arquivos de tipo desconhecido
- Avisar quando já existir um arquivo com o mesmo nome no destino
- Mostrar um resumo do que foi movido
- Permitir escolher a pasta pelo terminal, sem editar o código
- Criar uma interface gráfica simples (janela com botão para escolher a pasta e organizar)