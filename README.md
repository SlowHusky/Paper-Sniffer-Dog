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
2. Armazenar os dados da consulta em um banco de dados (usarei o sqlite3 por uma questão de conveniência. Quem testar o projeto saberá que ele foi escrito com um DB SQL e não precisará adicionar nada na sua máquina) **(ainda não desenvolvido)**
3. Webpage para mostrar e listar às ações **(desenvolvido)**
4. Ferramentas para configurar os ativos monitorados **(ainda não desenvolvido)**
5. Sistema de envio de e-mails **(ainda não desenvolvido)**

### Extras (ainda não desenvolvidos)

1. Bot de mensagem via telegram
2. Uso de uma página web com gráficos

## Ferramentas usadas

1. Python 3
2. Django 4
3. JQuery
4. SQLite
5. Yahooquery (https://yahooquery.dpguthrie.com/)
6. Celery (Escalonador de tarefas)