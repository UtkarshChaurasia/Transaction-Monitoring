import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image 
def main():
    activities=['About','Monitoring System','Developers']
    option=st.sidebar.selectbox('Menu Bar:',activities)
    if option=='About':
        html_temp = """
        <div style = "background-color: yellow; padding: 10px;">
            <center><h1>ABOUT OUR PROJECT</h1></center>
        </div><br>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        st.title("What is Money Laundering?")
        image=Image.open('1.png')
        st.image(image,use_column_width=True)
        st.set_option('deprecation.showfileUploaderEncoding', False)#to remove error
        st.subheader('Money laundering is the illegal process of concealing the origins of money obtained illegally by passing it through a complex sequence of banking transfers or commercial transactions.')
        st.title('What is Transaction Monitoring?')
        st.subheader('Anti-money laundering (AML) transaction monitoring software allows banks and other financial institutions to monitor customer transactions on a daily basis or in real-time for risk.')
        st.subheader('By combining this information with analysis of customers’ historical information and account profile, the software can provide financial institutions with a “whole picture” analysis of a customer’s profile, risk levels, and predicted future activity, and can also generate reports and create alerts to suspicious activity')
        st.title('Our Product')
        st.subheader('Working of the product in a nutshell')
        image=Image.open('2.png')
        st.image(image,use_column_width=True)
        st.set_option('deprecation.showfileUploaderEncoding', False)#to remove error
        st.title('The future prospects ')
        st.subheader('With increasing crony capitalism and corruption due to the slightest of inefficiencies and people’s urges to make the most money in the shortest period of time, even not considering the legal implications, it is almost certain that we will see an increase in the amount of money being laundered in the global economy, without an interference by major players like financial institutions, consulting firms etc. ')
        st.subheader('To make our project self sustainable and ever adapting according to the market scenario, an integration of a simple Artificial neural network will be done to the model created, so that, as datasets become larger, the efficiency does not take a hit, and the model learns from itself, just like all of us. ')
    elif option=='Monitoring System':
        st.title("TRANSACTION MONITORING SYSTEM")
        image=Image.open('Magnify_Monitoring.jpg')
        st.image(image,use_column_width=True)
        st.set_option('deprecation.showfileUploaderEncoding', False)#to remove error
        st.subheader("Please Upload Your Dataset")
        df = pd.read_csv(st.file_uploader("Upload your dataset",type=['csv','xlsx','txt','json']))
        st.dataframe(df.head(10))
        st.success("Data Successfully loaded")
        model = pickle.load(open("final_model.pkl", "rb"))


        def preprocessData(dataFrame):
            #dataFrame = dataFrame.drop('step','nameOrig','nameDest'],axis = 1)
            dataFrame = dataFrame.drop(['step','nameOrig','nameDest'],axis=1)
            x_new = dataFrame
            x_new = pd.get_dummies(x_new)
            return x_new

        if st.button("Predict"):
            st.balloons()
            x_new = preprocessData(df)
            df['y_prednew'] = model.predict(x_new)
            df.to_csv('final_result.csv')

            st.title("Your Output is")
            st.dataframe(df)

                
            

if __name__=='__main__':
    main()
