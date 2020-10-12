from dahuffman import load_json
import json

def square_odd(integer_list):
    return [(number if number % 2 == 0 else number * number) 
           for number in integer_list]

codec = load_json()
encoded_strings = {}

def encode_strings(string_list):
    encoded_strings.update({string_list[i] : codec.encode(string_list[i]) 
                            for i in range(0, len(string_list))})
    return encoded_strings

def decode_string(word):
    try:
        return list(encoded_strings.keys())[list(encoded_strings.values()).index(word)]
    except:
        print("User Error: This code does not match any previously encoded string.")


integer_list = [-3, -2, 1, 2, 3, 4, 5]
print(square_odd(integer_list))

string_list = ['this', 'is', 'a', 'test']
string_list2 = ['this', 'new', 'words']

print(encode_strings(string_list))
print(encode_strings(string_list2))

decode_this = b'\xd9'

print(decode_string(decode_this))

json.dump(encoded_strings, 'temp')

# >>> n.rpc.string_encoder.encode_strings(['this', 'is', 'a', 'test'])
# >>> n.rpc.string_encoder.peek()
