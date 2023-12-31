def black_box(user_input: str) -> str:
    strings = user_input.split(' ')
    output = ''

    for word in strings:
        if len(word) <= 2:
            output += word + ' '
        else:
            output += word[0] + str(len(word) - 2) + word[-1] + ' '

    return output


# Check if it works:
print(black_box('internationalization'))
print(black_box('localization'))
print(black_box('Hello world !'))
print(black_box('98 99 100 101 1062'))
print(black_box('(codin) + (game) = (codingame)'))