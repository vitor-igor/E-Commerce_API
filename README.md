# E-Commerce API
Curso Introdutório de Python com Flask da Rocketseat.

<div align="center">
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/python.png" alt="Python" title="Python"/></code>
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/flask.png" alt="Flask" title="Flask"/></code>
</div>

<!-- Icons obtidos do site: https://marwin1991.github.io/profile-technology-icons/ -->
<br>

# Executando
## Baixando as dependências
Para o funcionamento desse projeto, é necessário a instalação das dependências presentes no arquivo "requirements.txt". Execute a linha de comando abaixo para instalação local em sua máquina:

```
pip install -r requirements.txt
```

Ou utilize um ambiente virtual:
```
python -m venv <nome_do_ambiente>

# ativação no Windows
<nome_do_ambiente>\Scripts\activate
# ativação no Linux/macOS
source <nome_do_ambiente>/bin/activate

pip install -r requirements.txt
```

## Criação do Banco de Dados
Digite os seguintes comandos no terminal para criar o banco de dados:

```
flask shell
>>> db.create_all()
>>> db.session.comit()
>>> exit()
```

Depois disso, basta executar 

## Execução
Execute o arquivo "app.py".

```
python app.py
```