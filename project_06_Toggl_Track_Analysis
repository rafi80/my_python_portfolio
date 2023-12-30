# Napisz własną analitykę do aplikacji do śledzenia czasu takich jak np. Toggl Track. Twój moduł wczytuje dane o czasie wykonania poszczególnych zadań w formacie CSV, a następnie generuje raport wykorzystania czasu z podziałem na projekty, klientów i inne tagi.
# 1. Dane w pliku CSV mają trzy kolumny: desc, time oraz tags. Desc jest opisem zadania. Time to liczba całkowita określająca czas wykonywania tego zadania w minutach. Natomiast tags jest listą tagów porozdzielanych spacjami. Jedno zadanie może mieć wiele tagów. Jednym tagiem może być otagowane wiele zadań. Tagi służą do oznaczania zadań wg projektów, klientów lub innych kryteriów.
# 2. Upakuj te trzy informacje w klasie Entry. Upewnij się, że ma ona metodę __repr__.
# 3. Program przyjmuje scieżkę do pliku CSV jako argument linii poleceń. Następnie wyświetla raport. Każda jego linia to jeden tag. Dla każdego tagu wyliczona jest suma wszystkich otagowanych nim zadań.
# 4. Nie musisz pisać testów, ale podziel program na funkcje tak, aby każda z nich robiła tylko jedną rzecz.

import click
import csv
from typing import Dict, List, Tuple


class Entry:
    def __init__(self, description: str, time: int, tags: List[str]):
        self.description = description
        self.time = time
        self.tags = tags

    def __str__(self):
        return f"description: {self.description}, time: {self.time}, tags: {self.tags}"
    
    def __repr__(self):
        return f"Entry({self.description!r}, {self.time!r}, {self.tags})" 
    
    def __eq__(self, other):
        return self.id == other.id \
               and self.description == other.description and self.time == other.time \
               and self.tags == other.tags 


def create_Entry_from_dict(row: Dict[str, str]) -> Entry:
    """Maps input rows/lines as dictionary (originally from csv file) to Entry object
      and returns it
    """
    return Entry(description = row['desc'], time = int(row['time']), tags = row['tags'].split())


def read_todos_from_csv(path: str) -> List[Entry]:
    """Reads csv rows and converts rows to objects of Entry class.
    Adds objects to a list of entries and returns it

    Args:
        path (string): path to the csv containing entry records
    """
    with open(path, encoding='utf-8') as stream:
        reader = csv.DictReader(stream)  
        entries = [create_Entry_from_dict(row) for row in reader]
    return entries


def sum_time_per_tag(entries: List[Entry], tag: str) -> Tuple[int, str] :
    """For given list of entries and a tag, 
    returns tuple of: (total execution time for tag, this tag)
    """
    total_time_per_tag = tuple()
    execution_times_per_tag = [entry.time for entry in entries for entry_tag in entry.tags if entry_tag == tag]
    total_time_per_tag = sum(execution_times_per_tag), tag
    return total_time_per_tag


# Alternative 1 - optimal (as per performance) version of print_report using list comprehension
def print_report(entries: List[Entry]) -> None:
    """ For given list of entries, prints report of total time per tag and this tag"""
    checked_tag = []
    results = []

    print ("TOTAL_TIME TAG")

    [(results.append(sum_time_per_tag(entries, tag)),checked_tag.append(tag) ) \
     for entry in entries for tag in entry.tags if tag not in checked_tag] 
    
    [print(f"{item[0]:>10d} {item[1]:<20}") for item in results]    


# Alternative 2 - less consize but more readable (and optimal as per performance) version of print report
# def print_report(entries: List[Entry]) -> None:
#     """ For given list of entries, prints report of total time per tag and this tag"""
#     checked_tag = []
#     results = []
    
#     print ("TOTAL_TIME TAG")
#     for entry in entries:
#         for tag in entry.tags:
#             if tag in checked_tag:
#                 continue
#             else:
#                 checked_tag.append(tag)
#                 results.append(sum_time_per_tag(entries, tag))
#     [print(f"{item[0]:>10d} {item[1]:<20}") for item in results]
    

# Alternative 3 - not optimal but readable version of print_report
# def print_report(entries: List[Entry]) -> None:
#     """ For given list of entries, prints report of total time per tag and this tag"""
#     print ("TOTAL_TIME TAG")
#     execution_times_per_tag = [sum_time_per_tag(entries, tag) for entry in entries for tag in entry.tags]
#     results = set(execution_times_per_tag)
#     [print(f"{item[0]:>10d} {item[1]:<20}") for item in results]


@click.command()
@click.argument('path_to_file') # python M06/solutions/M06L14_projekt.py M06/solutions/track.csv
def main(path_to_file: str) -> None:
    entries  = read_todos_from_csv(path_to_file) 
    print_report(entries)


if __name__ == "__main__":
    main()
