# Tutorialutorial-raspagem-dados

## Descrição
spider desenvolvido seguindo o tutorial de apresentação do site da ferramenta scrapy

##  como utilizar
1. git clone git@github.com:IgorBarreto/Tutorialutorial-raspagem-dados.git
2.  python -m venv venv
3. Ativando ambiente virtual
3.1 Windows 
    venv\Scripts\activate.bat
3.2 Linux
    source venv\bin\activate
4. Instalando dependencias
4.1 Produção
    pip install -r requirements.txt
4.2 Desenvolvimento
    pip install -r requirements-dev.txt
5. Executando o spider
    scrapy crawl quotesv4 -O autores.json
6. Spider existentes
    quotesv1
    quotesv2
    quotesv3
    quotesv4





