from context import context as ctx

def data_hint_extract(target):
    page = ctx.PAGE

    emails = []
    numbers = []

    page.goto("https://www.instagram.com/accounts/password/reset/")

    page.wait_for_selector('input[type="text"]', state='visible')
    input_box = page.locator('input[type="text"]').first
    input_box.click()
    page.keyboard.type(target, delay=40)
    page.keyboard.press('Enter')

    page.wait_for_selector('input[type="radio"][name="RecoveryOptions"]', timeout=15000)

    radios = page.locator('input[type="radio"][name="RecoveryOptions"]')

    count = radios.count()

    for i in range(count):
        radio = radios.nth(i)
        label = radio.locator("xpath=ancestor::label")

        text = label.inner_text().strip()
        lines = [l.strip() for l in text.splitlines() if l.strip()]

        if len(lines) >= 2:
            correlatable = lines[-1]

            if correlatable.startswith("Use your"):
                continue
            elif correlatable.startswith("+"):
                numbers.append(correlatable)
            elif "@" in correlatable:
                emails.append(correlatable)

    return numbers, emails