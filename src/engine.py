from utils import start_browser

from context import context as ctx

def start(module, target):
    start_browser.start_browser()

    if module == "data_hint_extract":
        ctx.PAGE.goto("https://www.instagram.com/accounts/password/reset/")
    else:
        return
    
    ctx.BROWSER.close()
    ctx.PLAYWRIGTH.stop()