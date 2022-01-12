"""
@author: Ville Hytönen
@version: 12.1.2022
@state: In Development
TODO: make work with GUI
"""

from bs4 import BeautifulSoup
import requests
import csv
import dicdatabase


def getUrl():
    print('Give url')
    url = input('>')
    scrapeTranslations(url)


# Scrapes translations from given url and sends results to database
def scrapeTranslations(url):        
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')        
    
    search_bar = soup.find('div', class_='text_input_wrap')
    search_word = search_bar.input.attrs['value']
    #print(search_word)
    
    translations_table = soup.find('table', class_='translations')
    translations = translations_table.find_all('a')
    try:
        translations = translations_table.find_all('a')
        translation_text = ''
        for translation in translations:
            translation_text += translation.text + '. '
    
    except AttributeError:
        translation_text = None
    
    #print('Translations:')
    #print(translation_text)
    
    #print('Definitions:')
    definition_list = soup.find('div', class_='definitions')
    try:
        definitions = definition_list.find_all('li')
        definition_text = ''
        for definition in definitions:
            definition_text += definition.text + ' '
    
    # Prints "-" if there are no definitions
    except AttributeError:
        definition_text = None
    
    #print(definition_text)

    dicdatabase.add_one(search_word, translation_text, definition_text)



    

#note: rowid must be in quotes
#dicdatabase.delete_one('0')

dicdatabase.show_all()