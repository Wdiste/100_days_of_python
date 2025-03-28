# this program will encode or decode a message using a shift cipher:

def cipher(process, message, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    output = []
    # determine process requested, shift accordingly
        # find index of letter in message
        # add the letter that is <shift> letters away to the output
    if process == "encrypt":
        for letter in message:
            if letter.isalpha():
                index = (alphabet.index(letter) + shift) % 26
                output.append(alphabet[index])
            else:
                output.append(letter)
    if process == "decrypt":
        for letter in message:
            if letter.isalpha():
                # print(f"letter = {letter}, index = {alphabet.index(letter) - shift + 26}")
                index = (alphabet.index(letter) - shift) % 26 
                output.append(alphabet[index])
            else:
                output.append(letter)
    print("".join(output))

cipher(input("Encrypt or decrypt?"), input("What is your secret message?"), int(input("How many numbers to shift?")))
