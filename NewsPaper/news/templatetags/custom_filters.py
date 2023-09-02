from django import template

register = template.Library()

bad_words = [
    'about',
    'tomorrow',
    'some',
]

@register.filter()
def censor(value):
    text = value.split()
    for i, word in enumerate(text):
        if word in bad_words:
            text[i] = word[0] + '***'
    return ' '.join(text)


