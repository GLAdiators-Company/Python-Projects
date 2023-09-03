def code(message):
    words = message.split(" ")
    r1 = 'E4f'
    r2 = 'gfs'
    for index,word in enumerate(words):
        if(len(word)>=3):
            word = r1 + word[1:] + word[0] + r2
            print(word,end=' ')
            
        else:
            word = word[::-1]
            print(word,end=' ')

def de_code(message):
    words = message.split(" ")
    for index,word in enumerate(words):
        if(len(word)>=3):
            word = word[3:-3] 
            word = word[len(word)-1] + word[0:-1]
            print(word,end=' ')
            
        else:
            word = word[::-1]
            print(word,end=' ')

op = int(input('[1] -> Code / [2] -> Decode : '))
message = input('Enter your message : ').strip()
match op:
    case 1:
        code(message)
    case 2:
        de_code(message)
    case _:
        print('Enter a valid operation')


    
        
    
    

