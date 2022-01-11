# translate-to-memory
Personal webscraping project to help learning vocabulary. Problem that I have is that I see a new word somewhere, translate it, forget it, see the same word, translate it again, forget it again.

Translate to Memory saves the words, translations and definitions using sanakirja.org as translator.

Consists of:
- Simple GUI that allows user to input a word and search translation for it using sanakirja.org
  - Six language presets:
    - english to finnish
    - swedish to finnish
    - german to finnish
    - and switched for all (finnish to x)  
- Webscraper for scraping words, translations and definitions 
  - Initiated by using the GUI
- Database for the scraped translations
