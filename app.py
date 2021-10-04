import pandas as pd  
import numpy as np
import pickle
import streamlit as st

pickle_in = open("tddmodel.pkl","rb")
model =pickle.load(pickle_in)

pickle_in_enc = open("encoder.pickle", "rb")
encoder = pickle.load(pickle_in_enc)

def welcome():
    return "Welcome All"


def main():
    #st.title("Thyroid Disease Prediction")
    #st.image("image.jpg", width = 700)
    html_temp = """
    <div style="background-color:Green;padding:10px">
    <h2 style="color:white;text-align:center;">Thyroid Disease Classification ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    age = st.number_input("Age")
    
    sex = st.selectbox('Sex', ["male","female"])
    
    on_thyroxine = st.selectbox("On_thyroxine", ["yes", "no"])
    
    on_antithyroid_medication = st.selectbox("On_antithyroid_medication", ["yes", "no"])
    
    goitre = st.selectbox("Goitre", ["yes", "no"])
    
    hypopituitary = st.selectbox("Hypopituitary", ["yes", "no"])
    
    psych = st.selectbox("Psychological_symptoms", ["yes", "no"])
    
    tsh = st.number_input("Thyroid Stimulating Hormone")
    
    #t3 = st.slider('T3 Measure', 0.0, 11.0, (0.0, 11.0))
    t3 = st.number_input("T3 Measure")
    
    #tt4 = st.slider('Total T4 Measure', 2.0, 430.0, (2.0, 430.0))
    tt4 = st.number_input("Total T4 Measure")
    
    #t4u = st.slider('T4U Measure', 0.0, 2.0, (0.0, 2.0))
    t4u = st.number_input("T4U Measure")
    
    #fti = st.slider('Free Thyroxine Index Measure', 2.0, 395.0, (2.0, 395.0))
    fti = st.number_input("Free Thyroxine Index Measure")
    
    
    if st.button('Predict Class'):
        
        if sex == 'male':
            sex = 1
        else:
            sex = 0

        if on_thyroxine == 'yes':
            on_thyroxine = 1    
        else:
            on_thyroxine = 0
        
        if on_antithyroid_medication == "yes" :
            on_antithyroid_medication = 1
        else:
            on_antithyroid_medication = 0
        
        if goitre == "yes":
            goitre = 1
        else:
            goitre = 0   
        
        if hypopituitary == "yes":
            hypopituitary = 1
        else:
            hypopituitary = 0
        
        if psych == "yes":
            psych = 1
        else:
            psych = 0           
        
        #t3 = t3[1]
        
        #tt4 = tt4[1]
        
        #t4u = t4u[1]
        
        #fti = fti[1]
        
        query = [age,sex,on_thyroxine,on_antithyroid_medication,goitre,hypopituitary,psych,tsh,t3,tt4,t4u,fti]
    
        predicted_class = int(model.predict([query])[0])
    
        actual_class = encoder.inverse_transform([predicted_class])[0]

        st.success(actual_class)
        
        
    

         
    
    if st.button("About Author"):
               st.text("Name : Upendra Kumar") 
               st.text("Email : upendra.kumar48762@gmail.com") 
               st.text("Oragnization : Data Science Student at iNeuron.ai")
               st.text("Project is the part of Data Science Internship at iNeuron.ai")  

        
if __name__=='__main__':
    main()

    




