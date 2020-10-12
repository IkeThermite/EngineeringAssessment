from nameko.rpc import rpc
from dahuffman import load_json
import random
import string

class EngineeringAssessment:
    name = "engineering_assessment"
    encoded_strings = {}
    lookup_strings = {}
    codec = load_json()
    hash_alphabet = string.ascii_letters + string.digits
    
    @rpc
    def square_odd(self, integer_list):
        return [(number if number % 2 == 0 else number * number) 
               for number in integer_list]

    @rpc
    def encode_strings(self, string_list):
        for i in range(0, len(string_list)):
            string_hash = ''.join(random.choices(self.hash_alphabet, k=8))
            self.lookup_strings.update({string_list[i] : string_hash})
            self.encoded_strings.update({string_hash : self.codec.encode(string_list[i])})
        return self.lookup_strings      
    
    @rpc
    def decode_string(self, string_hash):
        try:
            return (list(self.lookup_strings.keys())[
                   list(self.lookup_strings.values()).index(string_hash)])
        except:
            print("User Error: This code does not match any previously encoded string.")

    @rpc
    def peek_encoded_strings(self):
        print(self.encoded_strings)
    
    @rpc
    def get_string_hashes(self):
        return self.lookup_strings