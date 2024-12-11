calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    print(len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    return string_lower in (item.lower() for item in list_to_search)

string_info('Carrot')
print(is_contains('CaRRot', ["carrot", 'labrodour', 'want']))
string_info('TanGo')
print(calls)