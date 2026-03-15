def spam():
    print("Spam!")
    pass
    
def caesar():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = 5
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    
    # Example usage
    message = "hello"
    encoded = message.translate(translation_table)
    print(encoded)  # Outputs: mjqqt

# Call the function once, outside the function body
caesar()
