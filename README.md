# Paper Sniffer Dog

## Introdução

O objetivo do sistema é auxiliar um investidor nas suas decisões de comprar/vender ativos. Para tal, ele deve registrar periodicamente a cotação atual de ativos da B3 e também avisar, via e-mail, caso haja oportunidade de negociação.

Os seguintes requisitos funcionais são necessários:

1. Obter periodicamente as cotações de alguma fonte pública qualquer e armazená-las, em uma periodicidade configurável, para consulta posterior
2. Expor uma interface web para permitir consultar os preços armazenados, configurar os ativos a serem monitorados e parametrizar os túneis de preço de cada ativo
3. Enviar e-mail para o investidor sugerindo Compra sempre que o preço de um ativo monitorado cruzar o seu limite inferior, e sugerindo Venda sempre que o preço de um ativo monitorado cruzar o seu limite superior


## Linha de pensamento construtivo

Para desenvolver o projeto, a ordem de criação dos elementos será a seguinte:

1. Criação de uma consulta a API de ações da B3 **(desenvolvido)**
2. Armazenar os dados da consulta em um banco de dados (usarei o sqlite3 por uma questão de conveniência. Quem testar o projeto saberá que ele foi escrito com um DB SQL e não precisará adicionar nada na sua máquina) **(desenvolvido)**
3. Webpage para mostrar e listar às ações **(desenvolvido)**
4. Ferramentas para configurar os ativos monitorados **(desenvolvido)**
5. Sistema de envio de e-mails **(desenvolvido usando o django.core.mail.backends.console.EmailBackend)**

Optei pelo envio de e-mails pelo console pois já está formatado e deixei os parâmetros no settings para caso queiram usar um servidor SMTP.

### Extras
1. Páginas de informações das empresas
2. Página para ver o log de alertas

## Ferramentas principais usadas

1. [Python 3.10](https://docs.python.org/3/)
2. [Django 4](https://docs.djangoproject.com/pt-br/4.0/)
3. [JQuery](https://api.jquery.com/)
4. [SQLite](https://www.sqlite.org/docs.html)
5. [Yahooquery](https://yahooquery.dpguthrie.com/)
6. [Celery](https://docs.celeryq.dev/en/latest/index.html)


## Testar

Para testar, execute o virtualenv com às dependências do projeto, rode em um terminal separado o servidor redis com o comando ```redis-server```. Execute o servidor django, executando na pasta ```papersnifferdog``` o comando ```python3 manage.py runserver```


Acesse ```http://localhost:8000/getpapers/firstexec``` e aguarde a inserção dos primeiros dados. Ao fim, você será direcionado a página inicial

Abra outro terminal, ainda dentro do virtualenv e executar ```celery -A papersnifferdog worker -B -l info```