from json_processor import JsonProcessor

myJsonProcessor = JsonProcessor()

numbers = [2, 3, 5, 7, 11, 13]

myJsonProcessor.dump_json(numbers, "numbers.json")

print(myJsonProcessor.load_json("numbdders.json"))
