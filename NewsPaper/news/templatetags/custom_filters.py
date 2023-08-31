from django import template

register = template.Library()

bad_words = [
    'about',
    'tommorow',
    'some',
]

text = []
@register.filter()
def censor(text):
    list = text.split()
    censor_list = []
    for word in list:
        w = []
        if word in bad_words:
            censor_word = w[0] + '*'
            censor_list.append(word.replace(w, censor_word))
        else:
            censor_list.append(word)

    return censor_list

