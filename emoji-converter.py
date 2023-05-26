def emoji_converter(x):
        y= x.split(' ')
        emojis = {'happy':"\U0001f600",
               'very happy':"\U0001F606",
              'lmao':"\U0001F923"}      
        for item in y:
            z =  emojis.get(item,item) +' ' # '' is space
        return z  


x= input('here-: ')             # note that we should never include input and output in def function
print(emoji_converter(x))