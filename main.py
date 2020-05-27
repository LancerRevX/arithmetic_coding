from arithmetic_coding import encode, decode

def char_freqs(text):
    return {char: text.count(char) / len(text) for char in set(text)}

while True:
    text = input('Enter your text: ')
    freqs = char_freqs(text)
    code = encode(text, freqs)
    print('Code:', code)
    decoded = decode(code, len(text), freqs)
    print('Decoded:', decoded)
