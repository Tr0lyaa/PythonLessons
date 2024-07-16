def all_variants(text):
    for length in range(len(text)):
        for start in range(len(text) - length):
            yield text[start:start + 1 + length]


a = all_variants("abc")
for i in a:
    print(i)
