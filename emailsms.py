import streamlit as st  
import pickle 
import string 
from nltk.corpus import stopwords 
import nltk 
from nltk.stem import PorterStemmer 


ps = PorterStemmer()

import string
def transform_text(text) : 
    text = text.lower()
    text = nltk.word_tokenize(text)  #the text has come in the list
    y=[]
    for i in text: 
        if i.isalnum(): #special character are removed
            y.append(i)

    text = y[:] 
    y.clear() 
    for i in text : 
        if i not in stopwords.words('english') and i not in string.punctuation : 
            y.append(i)

    text = y[:]
    y.clear()
    for i in text : 
        y.append(ps.stem(i)) 



    return " ".join(y)



tfidf  = pickle.load(open('vectorization.pkl','rb')) 
model  = pickle.load(open('model.pkl' , 'rb')) #rb is read binary mode 

st.title("Email/Sms spam classifier")
input_msg = st.text_input("Enter the message")
if st.button("Predict" ):

    #preprocessing 
    transform_msg = transform_text(input_msg)

    #vectorization 
    vector_input = tfidf.transform([transform_msg])

    #predict 
    result = model.predict(vector_input)[0]

    #disply 
    if(result == 1) :
        st.header("Spam")
    else : 
        st.header(" Not Spam")
