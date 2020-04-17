
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score+=1
    print('vowel score is:',score)
    return score
   

no_of_words = str(input("Enter no of words: "))
words = input("Enter the word ,in which yu want check vowel score: ").split()

print(score_words(words))