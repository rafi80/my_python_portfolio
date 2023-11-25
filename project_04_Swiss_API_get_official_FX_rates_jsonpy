# Pomóż szwajcarskiemu bankowi HSBC tworząc aplikację, która odczytuje i analizuje dane z Narodowego Banku Polskiego (NBP) udostępnione przez API i podaje ile była warta wskazana waluta we wskazanym dniu.

# Dzięki Tobie HSBC będzie mógł poprawnie wystawiać w Polsce faktury w walucie obcej - przepisy wymagają, aby kwoty na takich fakturach przeliczać na złotówki wg kursów NBP z określonych dni.

# 1. Zapoznaj się z opisem API: http://api.nbp.pl.
#    1. Ustal jak wygląda URL, pod którym znajdziesz kurs danej waluty z danego dnia?
#    2. W jakim formacie musi być data?
#    3. Co trzeba zmienić w URLu, aby otrzymać odpowiedź w JSONie zamiast XMLu?
# 2. Tabele kursów są publikowane tylko w dni robocze. Przeczytaj w dokumentacji co się stanie, gdy zapytasz o kurs z weekendu lub innego dnia wolnego od pracy?
# 3. Twój program przyjmuje walutę oraz datę jako dwa argumenty wiersza poleceń. Jeśli jednak nie zostaną podane, wówczas poproś użytkownika o podanie tych dwóch informacji przy pomocy funkcji input.

import sys

import requests
from dateutil import parser

print("KALKULATOR WALUT")

CURRENCY_CODES = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG',
                  'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 
                  'BOB', 'BOV', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 
                  'CDF', 'CHE', 'CHF', 'CHW', 'CLF', 'CLP', 'CNY', 'COP', 'COU', 
                  'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 
                  'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GHS', 
                  'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HTG', 'HUF', 
                  'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 
                  'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 
                  'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 
                  'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 
                  'MXV', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 
                  'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 
                  'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 
                  'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SVC', 
                  'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 
                  'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'USN', 'UYI', 'UYU', 'UYW', 
                  'UZS', 'VED', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 
                  'XBA', 'XBB', 'XBC', 'XBD', 'XCD', 'XDR', 'XOF', 'XPD', 'XPF', 
                  'XPT', 'XSU', 'XTS', 'XUA', 'XXX', 'YER', 'ZAR', 'ZMW', 'ZWL']

ISO8601_DATE_FORMAT = "%Y-%m-%d"

PRINT_OUT_DATE_FORMAT = "%d/%m/%Y"


# get the currency and date parameters, try get it from system parameter, 
# if not available, read from user prompt
try:
    currency = sys.argv[1]
except IndexError:
    currency = input("Podaj walutę: ")
currency = currency.upper()


try:
    rate_date = sys.argv[2]
except IndexError:
    rate_date = input("Podaj datę: ")

# NBP API requires currency ISO in ISO 4215 three letter foramat 
# and date in ISO 8601, YYYY-MM-DD format. 
# Currency will be covered by a constant CURRENCY_CODES and date be using
# the dateutilparser library

if currency.upper() not in CURRENCY_CODES:
    print("Nieprawidłowy kod waluty")
    sys.exit(1)

# convert date to ISO 8601 format
try:
    converted_datetime =  parser.parse(rate_date)
    yearfirst = False
except ValueError:
    print("Invalid date format")
    sys.exit(1)

iso8601_date = converted_datetime.strftime(ISO8601_DATE_FORMAT)

# convert date to print out format
print_out_format_date = converted_datetime.strftime(PRINT_OUT_DATE_FORMAT)

# construct API URL to get NBP currency table in json format
# the URL format is:
# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{date}/?format=json
# We use  middle exchange rates, which is table a: 
# http://api.nbp.pl/api/exchangerates/rates/a/{code}/{date}/?format=json 

URL = "http://api.nbp.pl/api/exchangerates/rates/a/" + currency + "/" + iso8601_date +"/?format=json" 

# send request, get table and extract the exchange rate
response = requests.get(URL)

if response.status_code == 404:
    print("Brak Danych")
    sys.exit(2)
if not response.ok:
    print("Unexpected server response")
    sys.exit(3)

# get response and print out the solution
table = response.json()

try:
    exchange_rate = table['rates'][0]['mid']
except (ValueError, KeyError) as e:
    print("Invalid server respons Danych")
    sys.exit(4)

print("1", currency, "=", exchange_rate,"PLN w dniu", print_out_format_date)
