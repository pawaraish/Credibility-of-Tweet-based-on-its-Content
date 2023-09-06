from nltk.stem import WordNetLemmatizer
word_lst = []
def stemmer(file):
    stm_lst = []
    stm = PorterStemmer()
    f = open(file,'r')
    for l in f:
        word_lst.append(1)
        w = stm.stem(str(l.strip()))
        stm_1st.append(w)
        return stm_lst
    stm_lst = stemmer('Hello I am a programmer')
    for i in range(len(word_lst)):
        print(word_lst[i]+"-->"+stm_lst[i])