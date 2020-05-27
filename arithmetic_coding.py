def encode(text: str, freqs: dict) -> float:
    start = (end := 0.0)
    freqs = freqs.copy()
    for char in freqs:
        freqs[char] = (end, end + freqs[char])
        end = freqs[char][1]
    for char in text:
        length = end - start
        start += length * freqs[char][0]
        end -= length - length * freqs[char][1]
    return start + (end - start) / 2


def decode(code: float, char_count: int, freqs: dict) -> str:
    i = 0.0
    freqs = freqs.copy()
    for char in freqs:
        freqs[char] = (i, i + freqs[char])
        i = freqs[char][1]
    text = ''
    for _ in range(char_count):
        for char in freqs:
            if freqs[char][0] <= code <= freqs[char][1]:
                text += char
                length = freqs[char][1] - freqs[char][0]
                code = (code - freqs[char][0]) / length
                break
    return text

