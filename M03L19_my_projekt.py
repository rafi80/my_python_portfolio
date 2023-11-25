# Pomóż zespołowi Stanford AI Lab przeanalizować zbiór danych składający się z 50 tys. recenzji filmów, dzięki czemu będą mogli automatycznie określać sentyment nowych komentarzy i wypowiedzi w internecie. W szczególności zależy im, aby zidentyfikować te najbardziej pozytywne i negatywne wypowiedzi wśród milionów neutralnych komentarzy - dzięki temu będą mogli udostępnić te najbardziej pozytywne, a w przypadku tych najbardziej negatywnych będą mogli zareagować i odpowiedzieć zanim taki komentarz dotrze do szerszego grona.

# 1. Wszystkie pliki znajdują się w katalogu M03/data/aclImdb/train. 
# W podkatalogu "pos" znajdują się pozytywne komentarze, tzn. minimum 7/10. 
# W podkatalogu "neg" znajdują się negatywne komentarze, czyli te 6/10, 5/10 i niżej. 
# Każda recenzja to osobny plik.
# 2. W recenzjach znajdują się fragmenty HTML - "<br />" oznaczający znak końca linii. 
# Takie fragmenty zastąp spacją.
# 3. Wczytaj wszystkie pozytywne i negatywne recenzje do dwóch osobnych zmiennych. 
# Będzie łatwiej, jeśli każdą recenzję będziesz reprezentować nie jako string, tylko jako listę słów. 
# Tak więc każda z tych dwóch osobnych zmiennych będzie listą list.
# 4. Następnie poproś użytkownika, aby wpisał komentarz, którego sentyment chce wyliczyć. 
# Podziel ten komentarz na słowa.
# 5. Sentyment poszczególnych słów w tym komentarzu liczymy wg wzoru (positive-negative)/all_,
# gdzie positive to liczba pozytywnych recenzji, w których pojawiło się to słowo. 
# Negative to liczba negatywnych recenzji, w których pojawiło się to słowo. 
# Natomiast all_ to liczba wszystkich recenzji, w których pojawiło się to słowo. 
# Na przykład, jeśli dane słowo pojawia się w 5 pozytywnych i 5 negatywnych recenzjach, 
# to jego sentyment wynosi (5-5)/10 = 0.0. Jeśli dane słowo pojawia się w 9 pozytywnych
#  i 1 negatywnej recenzji, to jego sentyment wynosi (9-1)/10 = +0.8. 
# Jeśli dane słowo pojawia się w 90 pozytywnych i 10 negatywnych recenzjach, 
# to jego sentyment wynosi (90-10)/100 = +0.8, tak samo jak wcześniej. 
# Tak więc liczba zawsze jest z zakresu od -1.0 do +1.0. 
# 6. Sentyment całego tego komentarza to średnia arytmetyczna sentymentu wszystkich słów. 
# Tak więc wystarczy zsumować sentyment poszczególnych słów i następnie taką sumę 
# podzielić przez liczbę słów. W ten sposób sentyment całego komentarza też będzie z zakresu od -1.0 do +1.0.
# 7. Cały komentarz uznajemy za pozytywny, gdy jego sentyment jest > 0, a negatywny gdy jest < 0.

# 

import glob

# full path
# POSITIVE_REVIEWS_PATH = "M03\data\\aclImdb\\train\pos\\" 
# NEGATIVE_REVIEWS_PATH = "M03\data\\aclImdb\\train\\neg\\"

# test path (300 reviews)
POSITIVE_REVIEWS_PATH = "M03\data\\aclImdb\\my_test\pos\\"
NEGATIVE_REVIEWS_PATH = "M03\data\\aclImdb\\my_test\\neg\\"

# List of unwanted marks - punctuation marks and <br /> tag
MARKS_TO_REMOVE = ['.','?','!',',',':',';','/','-','_','(',')','{','}','[',']','\'','\"','...','/','@','#','$','€','%', '<br />']

# TO DO: consider performance tuning. It takes to long to read and clean 2500 reviews
def read_reviews(list_of_files):
    """ This function reads the content of all files containing reviews from a given list of files,
    splits a content of every file (using space as a separator) and adds words 
    to a list representing review. Then adds the list of words in a review 
    as an element to an outer list contatining all reviews.
    Then returns this list of lists [[word_1, word_2,..], [word_x, word_y,...], ...]. 
    """
    reviews = []
    content = ""
    file_counter = 0
    number_of_files = len(list_of_files)
    
    for file in list_of_files:
        file_counter += 1
        with open(file, encoding="UTF-8") as stream:
            print("Plik " + str(file_counter) + ' z ' + str(number_of_files) + " odczytany. \r", end="")
            content = stream.read()
        review = tokenize_content(content)
        reviews.append(review)
    print("")

    return reviews


def tokenize_content(content):
    """ This function reads a string and tokenizes content by splitting the 
    string using space as a separator, removes <br /> tags and punctuation marks
    from the content and stores the list of words as a list and returns it.
    """
    tokenized_content = []
    converted_text = ''
    lower_case = ''

    # 2. W recenzjach znajdują się fragmenty HTML - "<br />" oznaczający znak końca linii. 
    # Takie fragmenty zastąp spacją.
    # Usuwa również znaki interpunkcyjne, bo zakładamy, że nie mają sentymentu
    converted_text = remove_unwanted_marks(content, MARKS_TO_REMOVE)
    lower_case = converted_text.lower()

    # split content into list of words
    tokenized_content =  lower_case.split()

    return tokenized_content


def remove_unwanted_marks(text_to_convert, marks_to_remove):
    """ Removes unwanted tags (given as a list) from a given text
    and returnes cleaned text (str)
    """
    for mark in marks_to_remove:
        text_to_convert = text_to_convert.replace(mark, ' ')

    return text_to_convert


# 5. Sentyment poszczególnych słów w tym komentarzu liczymy wg wzoru (positive-negative)/all_,
# gdzie positive to liczba pozytywnych recenzji, w których pojawiło się to słowo. 
# Negative to liczba negatywnych recenzji, w których pojawiło się to słowo. 
# Natomiast all_ to liczba wszystkich recenzji, w których pojawiło się to słowo. 
# Na przykład, jeśli dane słowo pojawia się w 5 pozytywnych i 5 negatywnych recenzjach, 
# to jego sentyment wynosi (5-5)/10 = 0.0. Jeśli dane słowo pojawia się w 9 pozytywnych
#  i 1 negatywnej recenzji, to jego sentyment wynosi (9-1)/10 = +0.8. 
# Jeśli dane słowo pojawia się w 90 pozytywnych i 10 negatywnych recenzjach, 
# to jego sentyment wynosi (90-10)/100 = +0.8, tak samo jak wcześniej. 
# Tak więc liczba zawsze jest z zakresu od -1.0 do +1.0. 
def calculate_word_sentiment(review, positive_reviews, negative_reviews):
    """ Calculates sentiment of words in given review based on the list 
    of positive and negative reviews containing that word and returns a list 
    containing a pair(also list) of word and it's calculated sentiment
    """
    
    sentiments = []

    for word in review:
        positive = 0
        negative = 0
        sentiment = 0.0
        for positive_review in positive_reviews:
            for single_word in positive_review:
                if single_word == word:
                    positive+=1

        for negative_review in negative_reviews:
            for single_word in negative_review:
                if single_word == word:
                    negative+=1

        # number of all occurences o given word in any of reviews
        all_ = positive + negative
        
        if all_ != 0:
            sentiment = (positive-negative)/(positive+negative)
        else:
            # assuming neutral sentiment for not yet used words
            sentiment = 0.0
        sentiments.append([word, sentiment])

    return sentiments

# 6. Sentyment całego tego komentarza to średnia arytmetyczna sentymentu wszystkich słów. 
# 7. Cały komentarz uznajemy za pozytywny, gdy jego sentyment jest > 0, a negatywny gdy jest < 0.
# Zakładam, również, że sentyment = 0 jest pozytywny
def calculate_review_sentiment(sentiments):
    """ Calculates sentiment of a review based on a list of words from
    the review and their individual sentiment [word, sentiment] and returns 
    list cotaining that overall sentiment index (float) and it's textual 
    interpretation (text)
    """
    sum_of_individual_sentiments = 0.0
    overall_sentiment_index = 0.0
    text_overall_sentiment = ''

    for word, sentiment in sentiments:
        sum_of_individual_sentiments += sentiment
    
    if len(sentiments) > 0:
        overall_sentiment_index = sum_of_individual_sentiments/len(sentiments)
        if overall_sentiment_index >= 0:
            text_overall_sentiment = 'positive'
        else:
            text_overall_sentiment = 'negative'
        return [overall_sentiment_index, text_overall_sentiment]
    else:
        print("Nie mogę policzyć sentymentu dla pustego komentarza")


# 3. Wczytaj wszystkie pozytywne i negatywne recenzje do dwóch osobnych zmiennych. 
positive_reviews = []
negative_reviews = []

list_of_files_positive_reviews = glob.glob(POSITIVE_REVIEWS_PATH + '*.txt')
list_of_files_negative_reviews = glob.glob(NEGATIVE_REVIEWS_PATH + '*.txt')

print("Wczytuję bazę pozytywnych komentarzy.")
positive_reviews = read_reviews(list_of_files_positive_reviews)
print("Wczytuję bazę negatywnych komentarzy.")
negative_reviews = read_reviews(list_of_files_negative_reviews)

# keep this in a loop to prevent loading train reviews everytime we want to test a review sentiment
terminate = ''

while terminate != 'n':
    # 4. Następnie poproś użytkownika, aby wpisał komentarz, którego sentyment chce wyliczyć.
    examined_review = input("Podaj komentarz: ")
    # Podziel ten komentarz na słowa.
    tokenized_review = tokenize_content(examined_review)

    # calculate sentiment for every word in a given review and print it out
    sentiments = calculate_word_sentiment(tokenized_review, positive_reviews, negative_reviews)
    for word, sentiment in sentiments:
        print(word + " " + str(sentiment))

    # print out sentiment for the whole review
    overall_sentiment = calculate_review_sentiment(sentiments)
    try:
        index, sentiment_summary = overall_sentiment
        print("This sentence is " + sentiment_summary + ", sentiment = " + str(index))
    except:
        print("Coś poszło nie tak. Nie udało się policzyć sentymentu dla komentarza.")
    
    terminate = input("Czy chcesz sprawdzić kolejny komentarz? (t/n): ").lower()
print("Dziękujemy za użycie naszego programu!")

# TESTS -----------------------------------------------------------------------
# example of reviews to get tested: 
# This is a reason to watch movies. A fantastic display of performance skill. -positive
# This was a wonderful movie. -positive
# What a bad movie. I got bored. - negative
# try also an emtpty review - should return comment that sentiment cannot be calculated
# print(positive_reviews[10])