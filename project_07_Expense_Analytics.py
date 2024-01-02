# Napisz program, który ułatwi milionom Polaków śledzenie własnych wydatków oraz ich analizę. 
# Program pozwala na łatwe dodawanie nowych wydatków i generowanie raportów. 
# Aplikacja działa także pomiędzy uruchomieniami, przechowując wszystkie dane w pliku. 
# Każdy wydatek ma id, opis oraz wielkość kwoty.
# 1. Program posiada podkomendy add, report, export-python oraz import-csv. 
# 2. Podkomenda add pozwala na dodanie nowego wydatku. Należy wówczas podać jako kolejne argumenty wiersza poleceń 
# wielkość wydatku (jako int) oraz jego opis (w cudzysłowach). Na przykład:
# $ python budget.py add 100 "stówa na zakupy". 
# Jako id wybierz pierwszy wolny id - np. jeśli masz już wydatki z id = 1, 2, 4, 5, wówczas wybierz id = 3.
# 3. Podkomenda report wyświetla wszystkie wydatki w tabeli. W tabeli znajduje się także kolumna "big?", 
# w której znajduje się ptaszek, gdy wydatek jest duży, tzn. co najmniej 1000. Dodatkowo, na samym końcu wyświetlona jest suma wszystkich wydatów.
# 4. Podkomenda export-python wyświetla listę wszystkich wydatków jako obiekt (hint: zaimplementuj poprawnie metodę __repr__ w klasie reprezentującej pojedynczy wydatek).
# 5. Podkomenda import-csv importuję listę wydatków z pliku CSV.
# 6. Program przechowuje pomiędzy uruchomieniami bazę wszystkich wydatków w pliku budget.db. Zapisuj i wczytuj stan używając modułu pickle. 
# Jeżeli plik nie istnieje, to automatycznie stwórz nową, pustą bazę. Zauważ, że nie potrzebujemy podpolecenia init.
# 7. Wielkość wydatku musi być dodatnią liczbą. Gdzie umieścisz kod sprawdzający, czy jest to spełnione? W jaki sposób zgłosisz, że warunek nie jest spełniony?

import csv
import pickle
import sys
from dataclasses import dataclass
from typing import List

import click

DB_FILENAME = "./M07/solutions/budget.db"
BIG_EXPENSE_THRESHOLD = 1000.00

@dataclass
class Expense:
    id: int
    description: str
    amount: float

    def __post_init__(self):
        try:
            self.amount = float(self.amount)
        except ValueError:
            print("amount must be a numerical value")
        if self.amount < 0:
            raise ValueError("amount cannot be a negative number")
        if not self.description:
            raise ValueError("description cannot be empty")
        if not self.amount:
            raise ValueError("amount cannot be empty")
        
    def is_big(self) -> bool:
        return self.amount >= BIG_EXPENSE_THRESHOLD

def persist_expenses_list(list_of_expenses: List[Expense], overwrite: bool = True) -> None:
    if overwrite:
        mode = 'wb'
    else:
        mode = 'xb'

    try:
        with open(DB_FILENAME, mode) as stream:
            pickle.dump(list_of_expenses, stream)
    except FileExistsError:
        print("Nie można stworzyć bazy - baza już istnieje")
    else:
        print("Stworzono bazę")


def get_saved_expenses() -> List[Expense]:
    try:
        with open(DB_FILENAME, 'rb') as stream:
            obj_restored = pickle.load(stream)
    except FileNotFoundError:
        obj_restored = []
        persist_expenses_list(obj_restored)

    return obj_restored

def print_report(expenses: List[Expense]) -> None:
    """ For given list of entries, prints report of total time per tag and this tag"""
    big = ''
    total = 0
    print ("--ID-- -AMOUNT- -BIG?- --DESCRIPTION-----------------")
    for expense in expenses:
        if expense.is_big():
            big = '(!)'
        else:
            big = ''
        print(f"{expense.id:>6d} {round(float(expense.amount),2):<8.2f} {big:^6} {expense.description:<30}") 
        total += expense.amount
    print (f"TOTAL: {total:<8.2f}")


def find_new_id(expenses: List[Expense])->int:
    ids = {expense.id for expense in expenses}
    counter = 1
    while counter in ids:
        counter +=1
    return counter


def add_expense(amount_: float, descr: str, expenses: List[Expense]) -> None:
    expense = Expense(
        id=find_new_id(expenses),
        amount = amount_,
        description= descr
    )
    expenses.append(expense) 


@click.group()
def cli():
    pass  


# @cli.command()
# @click.option('--example', is_flag=True)  
# def init(example: bool):
#     expenses: List[Expense]
#     if example:
#         expenses = [
#             Expense(id=1, description='Chleb', amount=10.1),
#             Expense(id=2, description='Tablet', amount=1000.00),
#             Expense(id=3, description='Gra', amount=200.15)
#         ]
#     else:
#         expenses = []
    
#     persist_expenses_list(expenses, overwrite=False)
    
    
@cli.command()
def report():
    expenses_list = get_saved_expenses()
    print_report(expenses_list)


@cli.command()
@click.argument('amount', type=float)
@click.argument('new_expense_description')  
def add(amount: float, new_expense_description: str):
    expenses_list = get_saved_expenses()
    try:
        add_expense(amount, new_expense_description, expenses_list)
    except ValueError as e:
        print(f"Błąd: {e.args[0]}")
        sys.exit(1)

    persist_expenses_list(expenses_list)


@cli.command(name='import-csv')
@click.argument('path_to_file')
def import_csv(path_to_file: str):
    rows = []
    expenses_list = get_saved_expenses()
    with open(path_to_file, encoding='utf-8') as stream:
        reader = csv.DictReader(stream)
        for row in reader:
            rows.append(row)

    for row in rows:
        try:
            add_expense(amount = float(row['amount']), descr = row['description'], expenses = expenses_list)
        except ValueError as e:
            print(f"Błąd: {e.args[0]}")
            sys.exit(1)
       
    persist_expenses_list(expenses_list)


@cli.command(name='export-python')
def export_python():
    expenses_list = get_saved_expenses()
    print(expenses_list.__repr__())


if __name__ == "__main__":
    cli()
