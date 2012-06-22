#Philip Afful Nunoo
print "Philip Afful Nunoo"

phrase = raw_input("Enter sentence to encrypt: ")
shift_value = int(input("Enter shift value: "))
encoded_phrase = ''

for c in phrase:
    letter = c    
    ascii_code = ord(letter)                    #converts letter to ascii
    
    if (ascii_code > 64 and ascii_code<91):     #if its a capital letter
        ascii_code = ascii_code + shift_value       
        if (ascii_code % 90 < 65):
           ascii_code = 65 + (ascii_code % 90)
        encoded_phrase = encoded_phrase + chr(ascii_code)
    elif(ascii_code > 96 and ascii_code<123):   #if its a small letter
        ascii_code = ascii_code + shift_value
        if (ascii_code % 122 < 97):
           ascii_code = 96 + (ascii_code % 122)
        encoded_phrase = encoded_phrase + chr(ascii_code)
    else:
        encoded_phrase = encoded_phrase + chr(ascii_code)

print "The encoded phrase is    : ", encoded_phrase
