import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def remove_adjectives_verbs_adverbs_prepositions(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    
    # Perform part-of-speech tagging
    tagged_words = pos_tag(words)
    
    # Filter out adjectives, verbs, adverbs, and prepositions
    filtered_words = [word for word, tag in tagged_words if tag not in ['JJ', 'JJR', 'JJS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'RB', 'RBR', 'RBS', 'IN']]
    
    # Join the filtered words back into a sentence
    filtered_sentence = ' '.join(filtered_words)
    
    return filtered_sentence

# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
filtered_sentence = remove_adjectives_verbs_adverbs_prepositions(sentence)
print(filtered_sentence)
