integer_list = [-3, -2, 1, 2, 3, 4, 5]
def square_odd(integer_list):
    return [(number if number % 2 == 0 else number * number) 
           for number in integer_list]

print(square_odd(integer_list))


from dahuffman import load_json
codec = load_json()

string_list = ['this', 'is', 'a', 'test']
string_list2 = ['this', 'new', 'words']

encoded_strings = {}
def encode_strings(string_list):
    encoded_strings.update({string_list[i] : codec.encode(string_list[i]) 
                            for i in range(0, len(string_list))})
    return encoded_strings

print(encode_strings(string_list))
print(encode_strings(string_list2))
