# 📘 Assignment: Python Automation

## 🎯 Objective

Practice using Python to automate everyday tasks by working with functions, loops, dictionaries, and simple file-related logic. This assignment helps you turn repetitive work into reusable scripts.

## 📝 Tasks

### 🛠️ Daily Task Summary

#### Descrição
Escreva uma função chamada `build_task_summary(tasks)` que recebe uma lista de tarefas e retorna um resumo fácil de ler.

#### Requisitos
O programa concluído deve:

- Aceitar uma lista de dicionários com pelo menos as chaves `name`, `priority` e `done`.
- Contar o número total de tarefas.
- Contar quantas tarefas foram concluídas.
- Contar quantas tarefas têm prioridade alta.
- Retornar uma string formatada como resumo final.
- Incluir um exemplo de uso com pelo menos 4 tarefas.

Exemplo:
```python
print(build_task_summary([
    {"name": "Estudar Python", "priority": "high", "done": True},
    {"name": "Lavar louça", "priority": "low", "done": False},
    {"name": "Fazer exercícios", "priority": "high", "done": True},
    {"name": "Organizar mochila", "priority": "medium", "done": False}
]))
```

Saída esperada:
```python
Total de tarefas: 4
Concluídas: 2
Prioridade alta: 2
```

### 🛠️ File Organizer

#### Descrição
Escreva uma função chamada `organize_files(files)` que organiza uma lista de nomes de arquivos por extensão.

#### Requisitos
O programa concluído deve:

- Receber uma lista de strings com nomes de arquivos.
- Agrupar os arquivos por extensão (por exemplo: `.py`, `.txt`, `.csv`).
- Usar um dicionário para guardar a organização.
- Incluir arquivos sem extensão na categoria `other`.
- Retornar um dicionário com os grupos organizados.
- Exibir um exemplo prático com pelo menos 5 arquivos.

Exemplo:
```python
files = ["notes.txt", "main.py", "data.csv", "image.png", "README"]
print(organize_files(files))
```

Saída esperada:
```python
{
    'txt': ['notes.txt'],
    'py': ['main.py'],
    'csv': ['data.csv'],
    'png': ['image.png'],
    'other': ['README']
}
```

### 🛠️ Expense Tracker

#### Descrição
Escreva uma função chamada `calculate_expenses(expenses)` para somar gastos por categoria.

#### Requisitos
O programa concluído deve:

- Receber uma lista de dicionários com as chaves `category` e `amount`.
- Somar todos os valores por categoria.
- Retornar um dicionário com o total de cada categoria.
- Exibir o gasto total geral ao final.
- Tratar entradas inválidas com segurança, como valores negativos ou não numéricos.
- Incluir um exemplo de uso com pelo menos 5 despesas.

Exemplo:
```python
expenses = [
    {"category": "food", "amount": 25.50},
    {"category": "transport", "amount": 12.00},
    {"category": "food", "amount": 10.75},
    {"category": "books", "amount": 30.00}
]
print(calculate_expenses(expenses))
```

Saída esperada:
```python
{
    'food': 36.25,
    'transport': 12.0,
    'books': 30.0,
    'total': 78.25
}
```
