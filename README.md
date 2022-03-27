# Tutorialutorial-raspagem-dados

## Descrição

spider desenvolvido seguindo o tutorial de apresentação do site da ferramenta scrapy

## como utilizar

1. git clone git@github.com:IgorBarreto/Tutorialutorial-raspagem-dados.git
2. Ambiente Virtual
    1. Criando o ambiente virtual

            - pyython -m venv venv

    2. Ativando ambiente virtual

        1. Windows

                - venv\Scripts\activate.bat

        2. Linux

                - source venv\bin\activate
3. Instalando dependencias
    1. Produção

            - pip install -r requirements.txt
    2. Desenvolvimento

            - pip install -r requirements-dev.txt
4. Executando o spider
    
        - scrapy crawl quotesv4 -O autores.json
5. Spider existentes
    * quotesv1
    * quotesv2
    * quotesv3
    * quotesv4