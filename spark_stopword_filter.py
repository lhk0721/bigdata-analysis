stopwords = [
    "the","a","an","and","or","but","if","because","as","until","while",
    "of","at","by","for","with","about","against","between","into","through",
    "during","before","after","above","below","to","from","up","down","in",
    "out","on","off","over","under","again","further","then","once","here",
    "there","when","where","why","how","all","any","both","each","few","more",
    "most","other","some","such","no","nor","not","only","own","same","so",
    "than","too","very","can","will","just","don","should","now","is","am",
    "are","was","were","be","been","being","do","does","did","have","has",
    "had","having","this","that","these","those","it","its","i","you","we",
    "they","me","him","her","us","them","my","your","our","their","what",
    "which","who","whom","whose",

    "이","그","저","것","거","수","등","들","및","또는","그리고","하지만",
    "그러나","그래서","때문에","위해","대한","같은","처럼","까지","부터",
    "로","으로","에게","에서","에는","이다","였다","아니다","합니다","하는",
    "하면","하지","하며","하면서","였다가","이다가","또","다시","곧","이미",
    "현재","지금","일때","경우","여기","거기","저기","무엇","누구","어디",
    "언제","어떻게","저는","나는","우리는","너는","너희는","그는","그녀는",
    "그것은","있다","없다","하다","된다","한다","됐다","된다","되고","하며",
    "했고","한다면","하는데","했다","합니다만","그리고나서","그럼에도",
    "그렇지만","정도","만큼","만","또한","아니라","거나","이며","이지만",
    "라도","만이라도","밖에","뿐","뿐이다","뿐만아니라",

    "는","은","는지","이라서","이라며","이라도","인데","인데도","인데요",
    "이다가","이었던","이었다","이었고","이어서","이라","이니","이니까",
    "이건","이게","이런","이러한","이러하다","저런","그런","그러한",
    "이렇다","저렇다","그렇다","이러니","그러니","저러니"
]

def main():
    myRdd_stop = (
        myRdd2.flatMap(
            lambda x: x.split()
        )
        .filter(
            lambda x: x not in stopwords
        )
    )
    for word in myRdd_stop.collect():
        print(word, end =' ')

if __name__ == '__main__':
    main()
