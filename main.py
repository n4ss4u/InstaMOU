from sys import argv

from src import engine

module = argv[1]
target = argv[2]

if module or target:
    engine.start(module, target)
else:
    print("Module or target empty. Try again!")