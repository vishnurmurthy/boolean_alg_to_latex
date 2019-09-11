import sys

vars = []
latex_dict = {
    'or':'\\vee',
    'and':'\\wedge',
    'not':'\\neg',
    'xor':'\\otimes',
    'then':'\\rightarrow',
    'implies':'\\rightarrow',
    'iff':'\\iff',
    '(':'(',
    ')':')',
    '-\\textgreater':'\\rightarrow',
    '&':'&',
    '\\textasciicircum':'\\wedge',
    '':''

}

while (True):
    x = input("Input variables or type 111 to finish. Remove variable by typing --1: ")
    if x=='111':
        break
    if x=='--1' in x:
        vars = vars[:-1]
        print("Removed")
    else:
        vars.append(x)
for x in vars:
    latex_dict.update( {str(x) : '\\textit{' + str(x) + '}'} )

print("Variables: ", ", ".join(vars))

while (True):
    statement = input("Input boolean statement in English: ")
    statement = statement.split(" ")
    print()

    for expression in statement:
        if expression in latex_dict:
            print(latex_dict[expression], end = ' ')
        elif '(' in expression or ')' in expression:
            words_list = [""]
            for letter in expression:
                if letter=="(":
                    words_list.append(letter)
                elif letter==")":
                    words_list.append(letter)
                else:
                    if (words_list[-1] in '()'):
                        words_list.append("")
                    words_list[-1]+=letter
            for word in words_list:
                print(latex_dict[word], end = ' ')
        else:
            print(expression, end = ' ')

    print()
    print()
