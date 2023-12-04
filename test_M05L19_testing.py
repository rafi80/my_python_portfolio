### 🔴 Testowanie automatyczne

# Do tej pory testowaliśmy programy manualnie (= ręcznie).

# Programy jest dużo łatwiej utrzymać, gdy dysponujemy zestawem testów AUTOMATYCZNYCH - czyli miniprogramów, które zastępują nas w ręcznym testowaniu.

# Te miniprogramy działają dużo szybciej i taniej od człowieka, a raz napisane można odpalać ile tylko dusza zapragnie. 

# Testy automatyczne odpalamy po każdej zmianie w kodzie. W ten sposób upewniamy się, że nie zepsuliśmy czegoś.

# Jeśli testy automatyczne nie wykryją żadnego defektu, to wciąż nie mamy gwarancji, że wszystko działa tak jak powinno.

# Testy nie służą udowodnieniu, że program działa poprawnie. Testy mają nam ułatwić i usprawnić znajdowanie tego, co popsuliśmy, gdy zmienialiśmy kod.

# Jest wiele frameworków do testowania. Najważniejsze to unittest (część standardowej biblioteki) oraz pytest (third-party, ale bardziej Pythonowy). My poznamy pytest. Trzeba go zainstalować:

# $ pip install pytest

# Następnie tworzymy osobny plik na testy (zawsze trzymamy w osobnych plikach testy oraz to, co jest testowane), koniecznie zaczynając od "test", np. "test_moj_modul.py" - jeśli chcemy, żeby zostały automatycznie wykryte przez pytest'a.

# W środku niego umieszczamy funkcje, które również zaczynają się od "test". Każda z nich będzie traktowana jako pojedynczy test:

# def test_method_lower():
#     text = "ASDF"
#     got = text.lower()
#     expected = "asdf"
#     assert got == expected
#     assert 2 + 2 == 5
    
# W środku używamy instrukcji assert do sprawdzenia warunków, które powinny być spełnione. Jeśli którykolwiek z nich nie jest spełniony, wówczas test jest NIEZALICZONY = czerwony = fail. W przeciwnym razie test PRZESZEDŁ = zielony = pass.

### 🔴 Ćwiczenie

# Napisz testy do `preprocess_review` - funkcji z ćwiczenia M05L08:

from M05L19_testing import preprocess_review

def test_function_preprocess_review():
    review = "Magdalena miała kotka Romchotka"
    got = preprocess_review(review)
    expected = ['magdalena', 'miała','kotka','romchotka']
    assert got == expected

def test_function_preprocess_review_2():
    review = "Magdalena miała kotka<br /> Romchotka"
    got = preprocess_review(review)
    expected = ['magdalena', 'miała','kotka','romchotka']
    assert got == expected