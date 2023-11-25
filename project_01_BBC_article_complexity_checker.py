### 🔴 Projekt

# Napisz dla BBC program sprawdzający złożoność artykułów i wpisów, dzięki czemu 
# pracę dziennikarzy będzie można sparametryzować i automatycznie ustalić, czy 
# piszą teksty proste i łatwe w zrozumieniu. 
# Policz jaka jest średnia długość słów i wyświetl rezultat.

# Podpowiedzi:

# words = len(text.split())  # liczba słów

# a = 9
# b = 3
# division = a / b
# print(division)

# Aby policzyć średnią długość słowa, możesz bazować na liczbie wszystkich 
# znaków oraz liczbie słów.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Rozwiązanie:

# Poproś użytkownika o podanie tekstu do analizy
textToBeAnalyzed = input("Podaj/wklej tekst do zanalizowania: ")

# oblicz liczbę wszystkich znaków w tekście
totalTextLength = len(textToBeAnalyzed)

# oblicz liczbę słów w podanym tekście
numberOfWords = len(textToBeAnalyzed.split()) 

# oblicz średnią długość wyrazu według wzoru: średnia długość wyrazu to:
# całkowita liczba znaków w tekście, pomniejszona o ilość spacji (liczba słów - 1)
# podzielona przez ilość słów w tekście
meanWordLength = (totalTextLength - (numberOfWords - 1)) / numberOfWords
print("Średnia długość słów w tekście to:", meanWordLength)

# można się pokusić o kategrozyację złożoności tekstu budując przedziały 
# na podstawie średniej długości wyrazu, na przykład: 
# do 5 znaków - niska
# 6 - 9 znaków - średnia
# 10 i więcej znaków - wysoka
# i zaimplementować tę logikę jako funkcje
def calculateMeanWordLength(textToBeAnalyzed):
    totalTextLength = len(textToBeAnalyzed)
    numberOfWords = len(textToBeAnalyzed.split()) 
    meanWordLength = (totalTextLength - (numberOfWords - 1)) / numberOfWords
    return meanWordLength


def calculateTextComplexity(meanWordLength):
    if meanWordLength <= 5: 
        return 'niska'
    elif meanWordLength > 5 and meanWordLength < 10:
        return 'średnia'
    else:
        return 'wysoka'

# testy
# niska złożoność
textToBeAnalyzed = 'Ala ma kota. A Ela ma rysia.'
meanWordLength = calculateMeanWordLength(textToBeAnalyzed)
print("Test 1. Średnia długość wyrazu w tekście to:", meanWordLength)
print("Test 1. Obliczona złożoność jest {}.".format(calculateTextComplexity(meanWordLength)))

# średnia złożoność
textToBeAnalyzed = 'Podejrzewam, że to średnia złożoność.'
meanWordLength = calculateMeanWordLength(textToBeAnalyzed)
print("Test 2. Średnia długość wyrazu w tekście to:", meanWordLength)
print("Test 2. Obliczona złożoność jest {}.".format(calculateTextComplexity(meanWordLength)))

# wysoka złożoność
textToBeAnalyzed = 'Onomatopeiczność pompatycznej różnorodności zalesienia amazońskiego.'
meanWordLength = calculateMeanWordLength(textToBeAnalyzed)
print("Test 3. Średnia długość wyrazu w tekście to:", meanWordLength)
print("Test 3. Obliczona złożoność jest {}.".format(calculateTextComplexity(meanWordLength)))

# dłuższy tekst - credit: https://www.bbc.com/sport/football/66551395
textToBeAnalyzed = r"""England captain Harry Kane scored and set up a goal on his Bundesliga debut as champions Bayern Munich recorded a thumping win at Werder Bremen.
Kane swept a low right-footed effort past home goalkeeper Jiri Pavlenka from 15 yards to double Bayern's lead.
He had earlier assisted the first of Leroy Sane's two goals with a deft clip over the top inside four minutes.
Mathys Tel rounded off a comfortable victory for Thomas Tuchel's side late on.
"I was a little bit nervous and excited to play the game of course," Kane told broadcaster DAZN after the match.
"We started well with a goal in the first few minutes. For sure there were a few butterflies, but as always when I get on the pitch, instinct takes over."
It was a fine evening for Bayern and the club's record signing Kane, who arrived in Bavaria to great fanfare but had a disappointing start with a 3-0 defeat to RB Leipzig in the German Super Cup.
Billed as the man to finally fill Robert Lewandowski's boots over a year on from the prolific Poland striker's switch to Barcelona, Kane expertly laid on the first goal for Sane.
His quick thinking sent the former Manchester City winger racing clear to roll a low effort into the bottom left corner.
A much-improved Bremen threatened after the break, but Kane dispatched the visitors' second goal of the night, collecting Alphonso Davies' precise pass before picking his spot and placing a low shot into the bottom left corner.
With Kane struggling with cramp, Bayern made several changes.
Substitute Thomas Muller teed up Sane's second goal before Kane\'s replacement, French teenager Tel, drove in a late fourth."""
meanWordLength = calculateMeanWordLength(textToBeAnalyzed)
print("Test 4. Średnia długość wyrazu w tekście to:", meanWordLength)
print("Test 4. Obliczona złożoność jest {}.".format(calculateTextComplexity(meanWordLength)))
