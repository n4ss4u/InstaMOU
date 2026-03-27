from playwright.sync_api import sync_playwright

from context import context as ctx

def start_browser():
    p = sync_playwright().start()

    browser = p.chromium.launch(
        headless=True, 
        args=[
            "--use-gl=swiftshader",
            "--enable-webgl",
            "--ignore-gpu-blocklist",
            "--disable-blink-features=AutomationControlled",
        ],
    )

    context = browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        viewport={"width": 1280, "height": 800},
    )

    page = context.new_page()

    page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
    """)

    
    ctx.PLAYWRIGTH = p
    ctx.BROWSER = browser
    ctx.CONTEXT = context
    ctx.PAGE = page

    return