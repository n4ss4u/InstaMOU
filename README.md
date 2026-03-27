# InstaMOU

InstaMOU is an OSINT-oriented tool designed to extract publicly accessible information from Instagram through modular and automated techniques.

InstaMOU is built around a modular architecture that allows the integration of multiple data extraction techniques focused on Instagram. Each module is responsible for a specific task

---

## Modules

InstaMOU uses a module-based system. Each module performs a specific type of extraction or enumeration.

- data_hint_extract → Extracts masked email/phone hints from the password recovery flow
- (more modules coming soon)

---

## 🚀 Getting Started

- ```git clone https://github.com/n4ss4u/InstaMOU```
- ```cd InstaMOU```
- ```pip install -r requirements.txt```
- ```playwright install chromium```
- ```python instamou.py [MODULE] [USERNAME]```

---

> [!WARNING]
> This tool is intended for educational and research purposes only. Do not use InstaMOU for unauthorized access, abuse, or any activity that violates laws or platform terms of service.