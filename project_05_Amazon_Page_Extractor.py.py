# Napisz dla Amazona program, który automatycznie wyciąga wybrane informacje z wybranych stron internetowych, na przykład nazwy produktów ze stron Leroy Merlin. 
# Użytkownik podaje jedynie adres strony oraz ścieżkę xpath, którą może łatwo skopiować w przeglądarce.

# 1. Użyj biblioteki click, aby łatwiej było Ci odczytać url oraz xpath.

# 2. Podziel kod na funkcje tak, aby można było go łatwo testować.

# 3. Napisz kilka testów. Zacznij od tzw. happy path, tzn. najprostszego przypadku, a następnie przetestuj przypadki brzegowe.

# 4. Wyciągając z HTML tekst, usuń białe znaki z początku i końca (poszukaj odpowiedniej metody na stringach) oraz zamień znaki końca linii na spacje.

# 5. Wyświetl każdy znaleziony element HTML w osobnej linii.

# 6. Użyj docstringów, aby udokumentować Twój kod. Jakie informacje Twoim zdaniem warto tam zawrzeć?

# Hint: W razie problemów z cudzysłowami w XPATH pod Windows, możesz zamienić je na apostrofy, np.:
#     "//div[@id='wartosc']" 
# zamiast 
#     '//div[@id="wartosc"]'

# $ python M05/M05L20_projekt.py https://www.kaufland.pl/oferta/aktualny-tydzien/przeglad.category=01_Mi%C4%99so__Dr%C3%B3b__W%C4%99dliny.html /html/body/div[3]/main/div[1]/div/div/div[4]/div[2]/div[1]/div/div/div/div/div/a/div[1]/div[2]/h4/text()

import click
from lxml.html import fromstring
import requests

def get_elements_from_url(analyzed_url, x_path):
    """Gets HTML elements from a given internet site (analyzed_url)
    defined by given x-path(x_path) and returns     
    """
    content_values = []
    r = requests.get(analyzed_url)
    dom = fromstring(r.text)
    elements = dom.xpath(x_path)
    content_values = [clean_text_entry(element, ' ') for element in elements]
    print (content_values)

    return content_values


# 4. Wyciągając z HTML tekst, usuń białe znaki z początku i końca (poszukaj odpowiedniej metody na stringach) 
# oraz zamień znaki końca linii na spacje.
def clean_text_entry(text, target_character):
    """Replaces end of line sign with target_character
    for given text and trims the text by removing white spaces from the 
    beggining and the end of the text   
    """
    cleaned_text = ''
    cleaned_text = text.replace('\n', target_character)
    cleaned_text = cleaned_text.strip()

    return cleaned_text


def print_elements_separate_lines(list):
    for element in list:
        print(element)


# 1. Użyj biblioteki click, aby łatwiej było Ci odczytać url oraz xpath.
@click.command()
@click.argument('analyzed_url')
@click.argument('x-path')
def main(analyzed_url, x_path):
    """Gets and prints out information e.g. list of sold products 
    from a given internet site (analyzed_url) that is defined by given x-path(x_path)  
    Usage: python M05/M05L20_projekt.py url xpath 
    e.g. python M05/M05L20_projekt.py https://www.kaufland.pl/oferta/aktualny-tydzien/przeglad.category=01_Mi%C4%99so__Dr%C3%B3b__W%C4%99dliny.html /html/body/div[3]/main/div[1]/div/div/div[4]/div[2]/div[1]/div/div/div/div/div/a/div[1]/div[2]/h4/text()
    """
    elements = []
    elements = get_elements_from_url(analyzed_url, x_path)
    
    print_elements_separate_lines(elements)

if __name__ == "__main__":
    main()
