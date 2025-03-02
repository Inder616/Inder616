print( """
Welcome to the 
  ____                      _____ _       _             
 / ___|__ _ _ __ ___   ___ |  ___(_)_ __ | | __ _ _ __ 
| |   / _` | '_ ` _ \ / _ \| |_  | | '_ \| |/ _` | '__|
| |__| (_| | | | | | |  __/|  _| | | |_) | | (_| | |   
 \____\__,_|_| |_| |_|\___||_|   |_| .__/|_|\__,_|_|   
                                    |_|                
   ____      _       _  __ _           
  / ___|__ _| |_ ___| |/ _| |_   _ ___ 
 | |   / _` | __/ _ \ | |_| | | | / __|
 | |__| (_| | ||  __/ |  _| | |_| \__ \\
  \____\__,_|\__\___|_|_| |_|\__,_|___/
""")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
           'w', 'x', 'y', 'z']
def ceasar(text, shifts, encode_or_decode):
    decrypted_message = ""

    if encode_or_decode == "decode":
        shifts *= -1
    
    for letter in text: 
        if letter not in alphabet:
              decrypted_message += letter

        else:   
            position = alphabet.index(letter) + shifts
            position %= len(alphabet)
            decrypted_message += alphabet[position]
        

    print(f"Here is the {encode_or_decode}d result: {decrypted_message}")

should_continue = True

while should_continue :

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction not in ["encode" , "decode"]:
                print("Invalid input. Please enter 'encode' or 'decode'.")
                exit()
    message = input("Type your message: \n")
    shift = int(input("Enter the shift value (1-25): \n"))

    ceasar(text=message, shifts = shift, encode_or_decode = direction )

    choice = input("Do you want to encode/decode another message? (yes/no): \n").lower()
    if choice not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        exit()
    if choice == "no":
            should_continue = False
            print("Goodbye!")
             

       