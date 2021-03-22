import textwrap



def text_wrap(text,width,font):

    phrases = textwrap.wrap(text,width)

    texts = []
    WHITE = (255,255,255)
    for phrase in phrases:
        text = font.render(phrase,True,WHITE)
        texts.append(text)

    return texts







