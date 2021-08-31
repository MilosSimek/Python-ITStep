def change_latters(word):
    samohlasky ="aeiou"
    add_at_the_end = "way"
    add_seccond_at_the_end = "ay"
    if word[0] in samohlasky:
        return("{0}{1}".format(word, add_at_the_end))
    else:
        return("{0}{1}{2}".format(word[1:],word[0],add_seccond_at_the_end))


def sentense(sentense):
    text = sentense.split()
    new_text = []
    for i in text:
        new_text.append(change_latters(i))
    return ' '.join(new_text)

    



print(sentense("Mama ma maso"))
input()
        