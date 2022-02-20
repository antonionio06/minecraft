import json
import re
def load_json(filename):
    with open(filename, 'r') as f:
        return json.loads(f.read())
def write_json(filename, dictionary, ):
    with open(filename, 'w+') as f:
        f.write(json.dumps(dictionary, separators=(",\n", ":")))
#this list was stolen from someone on ma pona, possibly Lipamanka, but i'm not sure
wordList = ["a", "akesi", "ala", "alasa", "ale", "anpa", "ante", "anu", "awen", "e", "en", "esun", "ijo", "ike", "ilo", "insa",
            "jaki", "jan", "jelo", "jo", "kala", "kalama", "kama", "kasi", "ken", "kepeken", "kili", "kiwen", "ko", "kon", "kule", "kulupu",
            "kute", "la", "lape", "laso", "lawa", "len", "lete", "li", "lili", "linja", "lipu", "loje", "lon", "luka", "lukin", "lupa",
            "ma", "mama", "mani", "meli", "mi", "mije", "moku", "moli", "monsi", "mu", "mun", "musi", "mute", "nanpa", "nasa", "nasin",
            "nena", "ni", "nimi", "noka", "o", "olin", "ona", "open", "pakala", "pali", "palisa", "pan", "pana", "pi", "pilin", "pimeja",
            "pini", "pipi", "poka", "poki", "pona", "pu", "sama", "seli", "selo", "seme", "sewi", "sijelo", "sike", "sin", "sina", "sinpin",
            "sitelen", "sona", "soweli", "suli", "suno", "supa", "suwi", "tan", "taso", "tawa", "telo", "tenpo", "toki", "tomo", "tu", "unpa",
            "uta", "utala", "walo", "wan", "waso", "wawa", "weka", "wile", "namako", "kin", "oko", "kipisi", "leko", "monsuta", "tonsi", "jasima",
            "kijetesantakalu", "soko", "meso", "epiku", "kokosila", "lanpan", "n", "misikeke", "ku", None, None, None, None, None, None, None,
            "[", "]", "_", None, None, None, None, None, None, None, None, None, None, None, None, None,
            "pake", "apeja", "majuna", "powe", None, None, None, None, None, None, None, None, None, None, None, None]
#I wanted to put words into cartoushes, and it kind of works, but i don't know how, and it tries to translate stuff like OpenGL so I cmmented it
'''
def acro(ch):
    print(ch)
    nimi = []
    for word in wordList:
        if word != None:
            if word[0]==ch.lower():
                nimi+=[word]
    if len(nimi)==0: return ch
    return chr(0xf1900+wordList.index(nimi[0]))
def cartushe(word):
    out=chr(0xf1990)
    for ch in word:
        out+=acro(ch)
        if ch!=word[0]: out+=chr(0xf1992)
    out+=chr(0xf1991)+chr(0xf1992)
    return out
'''
#This function replaces text with sitelen pona, but there are so many exceptions that I no longer know how any of this works
def t(txt):
    out=''
    spaces = re.split('\w+', txt)
    words = re.findall('\w+', txt)+['']
    for space, word in zip(spaces, words):
        space = space.replace(' ', '')
        #minecraft uses these symbols to mark, that they should be replaced by something
        if '%' in space or '$' in space:
            out+=space+word
            continue
        #minecraft sometimes uses ale and sometimes ali
        if word=="ali": word="ale"
        if word in wordList:
            out+=space+chr(0xF1900 + wordList.index(word))
        #proper names
        elif word.istitle():
            out+=space+word
        #capslocked words
        elif word.isupper():
            if word.lower() in wordList: out+=space+chr(0xF1900 + wordList.index(word.lower()))
            else: out+=space+word
        #sometimes else just happens :(
        else:
            out+=space+word
    return out

js = load_json("tok_default.json")
for k in js.keys():
    js[k] = t(js[k])
write_json("tok_sp.json", js)
