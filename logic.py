def morz(ar):
    morzd = {'А': '• _ - •',
            'Б': '• - - -',
            'В': '• - -',
            'Г': '- - •',
            'Д': '- • •',
            'Е': '•',
            'Ё': '• • - • •',
            'Ж': '- - - •',
            'З': '- - • •',
            'И': '• •',
            'Й': '• - - -',
            'К': '- • -',
            'Л': '• - • •',
            'М': '- -',
            'Н': '- •',
            'О': '- - -',
            'П': '• - - •',
            'Р': '• - •',
            'С': '• • •',
            'Т': '-',
            'У': '• • -',
            'Ф': '• • - •',
            'Х': '• • • •',
            'Ц': '- • - •',
            'Ч': '- - - •',
            'Ш': '- - - -',
            'Щ': '- • • •',
            'Ъ': '• - - • -',
            'Ы': '- • - -',
            'Ь': '- • • -',
            'Э': '• • - • •',
            'Ю': '• • - -',
            'Я': '• - • -',
            '1': '. ----',
            '2': '..---',
            '3': '... --',
            '4': '.... -',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----',
            '.': '·–·–·–',
            ',': '–·–·–·',
            ':': '— – – –',
            '-': '— ···· —',
            '!': '·–·–·–',
            '?': '··––··',
            ' ': '...'
            }
    s = ''
    for i in range(len(ar)-1):
        s = s + morzd[ar[i].upper()] + '/'
    return s

def atbash(ar):
    result = ""
    for i in ar:
        if i.isalpha():
            if i.isupper():
                result += chr(1071 - ord(i) + 1040)
            else:
                result += chr(1103 - ord(i) + 1072)
        else:
            result += i
    return result

def cesar(ar):
    b=[]
    shag = 3
    cesar = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
             'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    for i in range(len(ar)):
        if ar[i].isalpha() and ar[i].isupper():
            ind = cesar.index(ar[i])
            b.append(cesar[(ind + shag) % len(cesar)])
        elif ar[i].isalpha() and ar[i].islower():
            ind = cesar.index(ar[i].upper())
            b.append(cesar[(ind + shag) % len(cesar)].lower())
        else:
            b.append(ar[i])
    return ''.join(b)