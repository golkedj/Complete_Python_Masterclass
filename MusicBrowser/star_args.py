def build_tuple(*args):
    return args

message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print(type(message_tuple))
print(message_tuple)

number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
print(type(number_tuple))
print(number_tuple)


def average_word_length(*args):
    sum = len(''.join(args))

    return sum // len(args)

average = average_word_length("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print("Average word length: {}".format(average))


def get_smallest_and_largest_words(*args):
    smallest_length = 0
    largest_length = 0
    for arg in args:
        if smallest_length is 0 and largest_length is 0:
            smallest_length = largest_length = len(arg)
        
        if smallest_length > len(arg):
            smallest_length = len(arg)

        if largest_length < len(arg):
            largest_length = len(arg)

    smallest = [word for word in args if len(word) is smallest_length]
    largest = [word for word in args if len(word) is largest_length]

    return (smallest, largest)

smallest, largest = get_smallest_and_largest_words("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print("Smallest word: ", smallest)
print("Largest word: ", largest)


def print_words_in_reverse_and_backwards(*args):
    reversed_words = args[::-1]
    reversed_words = [word[::-1] for word in reversed_words]
    print("reversed_words: {}".format(' '.join(reversed_words)))

print_words_in_reverse_and_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader")

words = ["hello", "planet", "earth", "take", "me", "to", "your", "leader"]
print("words:", words)
print("*words:", *words)