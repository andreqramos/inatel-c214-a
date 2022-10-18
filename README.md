# FizzBuzz

![Python](https://img.shields.io/badge/python-v3.8-green)

> O propósito deste projeto é apresentar a ferramenta de testes pytest


## Step 1:   Criando um ambiente Virtual

➡️ Abra a pasta raiz do projeto no terminal e execute os comandos abaixo:

```bash
virtualenv venv -p python3

source venv/bin/activate
```

➡️ Altere, no VSCode para o interpretador python do ambiente virtual criado 

## Step 2:   Instalando os requirements
O pytest pode ser instalado utilizando o comando

```bash
pip install -U pytest
```
Para manter o padrão de projeto, também existe um arquivo requirements.txt que também possui o pytest como dependência. Para fazer a instalação utilizando o requirements, basta utilizar os comandos abaixo:

``` bash
pip3 install --upgrade pip

pip3 install -r requirements.txt
```
## Step 3:   Executando

O projeto possui como código fonte apenas a função fizzbuzz() que está localizada na pasta src/fizzbuzz.py. A função pode ser acessada por outros códigos python, ou por ferramentas externas que consigam ler funções em python (como o IPython)

Ao chamar a função é necessário enviar um valor numérico como parâmetro. O programa retorna em seguida uma string que contém:
- "fizz": caso o número seja divisível por 3
- "buzz": caso o número seja divisível por 5
- "fizzbuzz": caso o número seja divisível por 3 e também por 5

A função também possui uma validação para tratar valores inválidos como strings e arrays.

### 📈 Testes

Os testes estão escritos na pasta tests/test_fizzbuzz.py.
Para executá-los, com o pytest instalado, basta executar o comando ```pytest``` e a bateria de testes será executada por inteiro.

Caso queira executar apenas um caso de teste, é possível utilizar o comando abaixo:
```bash
pytest tests/test_fizzbuzz.py::test_when_1_then_1
```