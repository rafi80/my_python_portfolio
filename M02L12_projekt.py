# Jesteś konsultantem działającym dla Niebezpiecznika - polskiego lidera cyberbezpieczeństwa. Napisz program, który będzie dokonywał audytu bezpieczeństwa u klientów Niebezpiecznika - jesteś odpowiedzialny za moduł sprawdzający złożoność haseł i generujący raport z rekomendacjami. 
#
# 1. Poproś użytkownika o hasło, a następnie sprawdź, czy spełnia ono reguły bezpieczeństwa.
# 2. Hasło powinno mieć minimum jedną małą literę, jedną wielką literę i jeden znak specjalny.
# 3. Hasło nie może zawierać spacji!  (wewnętrzny wymóg klienta wynikający z ograniczeń ich systemu teleinformatycznego)
# 4. Hasło musi mieć minimum 8 znaków.
# 5. Jeśli hasło jest niepoprawne, wyświetl raport w punktach co należy zmienić.

# Hinty

# Używaj operatorów and oraz or do tworzenia bardziej złożonych warunków.
counter = 0
text = "ile liter lub cyfr ma ten napis? 1234"
for char in text:
    if char.isalpha() or char.isdigit():
        counter = counter + 1
print("Ten tekst ma", len(text), "znaków, w tym", counter, "liter i cyfr.")

# Możesz także negować przy pomocy not.
text = "ASdf"
if not text.islower():
    print("Nie wszystkie litery są małe!")
    
# Możesz łączyć not, or oraz and:
if text.isalpha() and not text.islower():
    print("Same litery i co najmniej jedna wielka litera.")
    
# Do porównania typu "większy lub równy" służy >=
x = 5
print(x >= 5)  # ==> True