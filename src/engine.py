from utils import start_browser

def start(module, target):
    p, browser, context, page = start_browser.start_browser()

    if module == "data_hint_extract":
        page.goto("https://www.instagram.com/accounts/password/reset/")
    else:
        return
    
    browser.close()
    p.stop()