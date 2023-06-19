import enchant

def check_english_words(sentence):
    dictionary = enchant.Dict("en_US")
    words = sentence.split()
    non_english_words = []
    
    for word in words:
        if not dictionary.check(word):
            non_english_words.append(word)
    
    return non_english_words

sentence = "Mini Dal Mature Chat Recipe"
non_english_words = check_english_words(sentence)
print("Non-English words:", non_english_words)
