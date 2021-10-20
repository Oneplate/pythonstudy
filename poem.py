import random

verbs = ["are","is", "goes", "cooks", "shoots", "faints", "chews", "screams"]
nouns = ["bear", "lion", "mother", "baby", "sister", "car", "bicycle", "book"]
adverbs = ["handily", "sweetly", "sourly", "gingerly", "forcefully", "meekly"]
articles = ["a", "the", "that", "this"]

def simple_poem():
    for i in range(0,4):
        article = random.choice(articles)
        noun = random.choice(nouns)
        verb = random.choice(verbs)
        adverb = random.choice(adverbs)

        our_sentence = article+" "+noun+" "+verb+" "+adverb+"."
        our_sentence = our_sentence.capitalize()

        print("\t", our_sentence)

simple_poem()
