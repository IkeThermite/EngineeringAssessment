from dahuffman import load_json
import random
import string

def square_odd(integer_list):
    return [(number if number % 2 == 0 else number * number) 
           for number in integer_list]

codec = load_json()
encoded_strings = {}
lookup_strings = {}

def encode_strings(string_list):
    for i in range(0, len(string_list)):
        string_hash = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        lookup_strings.update({string_list[i] : string_hash})
        encoded_strings.update({string_hash : codec.encode(string_list[i])})
    return lookup_strings

def decode_string(string_hash):
    try:
        return list(lookup_strings.keys())[list(lookup_strings.values()).index(string_hash)]
    except:
        print("User Error: This code does not match any previously encoded string.")


integer_list = [-3, -2, 1, 2, 3, 4, 5]
print(square_odd(integer_list))

string_list = ['this', 'is', 'a', 'test', 'This is one very loooong string. Does it compress neatly?']
string_list2 = ['this', 'new', 'words']

print(encode_strings(string_list))
print(encode_strings(string_list2))

decode_this = b'\xd9'

# print(decode_string(decode_this))

#json.dump(encoded_strings, 'temp')

# n.rpc.engineering_assessment.square_odd([-4, -3, 1, 2, 3, 5, 10])
# n.rpc.engineering_assessment.encode_strings(['this', 'is', 'a', 'test'])
# n.rpc.engineering_assessment.peekAtEncodedStrings()
# n.rpc.engineering_assessment.peekAtStringHashes()
