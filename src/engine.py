from utils import start_browser
from modules import data_hint_extract
from context import context as ctx

def start(module, target):
    start_browser.start_browser()

    print("Scraping, please wait... (If you receive an error, try again!)\n")
    
    if module == "data_hint_extract":
        numbers, emails = data_hint_extract.data_hint_extract(target)
        print(numbers, emails)
    else:
        return
    
    ctx.BROWSER.close()
    ctx.PLAYWRIGTH.stop()