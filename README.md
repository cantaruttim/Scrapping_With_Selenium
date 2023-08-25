# Scrapping With Selenium

Este projeto tem como objeitvo melhorar a performance de uma atividade rotineira de qualquer **empresa**. Em um serviço onde a busca de informações em sites são comuns
podemos encontrar locais que tenham muitos dados e que poderíamos demorar algum tempo para 'copiá-los' de forma manual.
Proponho então um programação de automação, realizado em **python** que busca retirar informações de uma tabela em um site.

O intuito é otimizar a tarefa. O que levaria horas, realizei nesta primeira parte em menos de 8 min e 20 segundos.

## Tabela
A página é uma página estática onde possui apenas 1 única tabela.

Inicialmente vemos a tabela dessa forma 
<img width="752" alt="Tabela 1" src="https://github.com/cantaruttim/Scrapping_With_Selenium/assets/81988636/7e306868-42e8-4c8a-b62c-58d1c6f699e9">

E ao rolarmos o mouse até o final encontramos um botão 

<img width="796" alt="Tabela 2" src="https://github.com/cantaruttim/Scrapping_With_Selenium/assets/81988636/b65f32b4-12e6-48dc-9a16-de64e5103f24">

Resumo da tabela. 
Possui 8 colunas e 480 linhas (shape: 480, 8)

Queria apenas a primeira tabela neste primeiro momento, dessa forma, precisava carregar toda a página para que pudesse extrair todas as 480 linhas.

## _Scrapping_

Utilizei para esse projeto a Biblioteca <a href="https://selenium-python.readthedocs.io/index.html" /> Selenium

## Resultados iniciais

Uma atividade que posteriormente levaria em média 1 hora e 30 realizando de forma manual.
Com o programa conseguimos um tempo de 8 min e 20 segundos.


<EM CONSTRUÇÃO>
