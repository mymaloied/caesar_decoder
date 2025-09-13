print("loading word database...")
import sys
try:
    import nltk
except ImportError:
    print("you haven`t installed requirements. Do it by: pip install -r requirements.txt")
    sys.exit()
nltk.download('words')
def decrypt_caesar(cipher):
    import string
    decrypted= []
    cipher = cipher.lower()
    alb = list(string.ascii_lowercase)
    original_cipher = list(cipher)
    for shift in range(len(alb)):
        cipher = original_cipher[:]  
        for el in range(len(cipher)):
            if cipher[el] in alb:  
                ltter_i = alb.index(cipher[el])
                res_i = ltter_i
                for a in range(shift):
                    if res_i == 0:
                        res_i = len(alb) - 1
                    else:
                        res_i -= 1
                cipher[el] = alb[res_i]
        decrypted.append(f"{''.join(cipher)}")
    return decrypted

def word_recognising(message):
    from nltk.corpus import words
    word_list = set(words.words())
    variants = dict()
    for variant in range(len(message)):
        words_message = message[variant].split()
        word_count = 0
        for word in words_message:
            if word in word_list:
                word_count += 1
        variants[variant] = word_count
    most_match = max(variants.values())
    if most_match == 0:
        return "no matches found"
    match_percentage = most_match / len(words_message)
    if match_percentage  <= 0.5: 
        return "too small match_percentage(under 50%)"
    matching_variant = message[max(variants, key=variants.get)]
    return matching_variant

cipher = input("Enter your cipher: ")
nltk.download('words')
private_message = decrypt_caesar(cipher)
while True:
    is_word_rec = input("Do you want to automatically find the most likely decryption?(Y/N) ")
    if is_word_rec == "Y" or is_word_rec == "y":
        fin = word_recognising(private_message)
        if fin == "no matches found" or fin == "too small match_percentage(under 50%)":
            print("error: ",fin)
            print("Decryption options: ")
            for stri in private_message:
                print(stri)
            break
        else:
            print(fin)
            break
    if is_word_rec == "N" or is_word_rec == "n":
        print("Decryption options: ")
        for stri in private_message:
            print(stri)
        break
    else:
        print("unknown input, try again")

