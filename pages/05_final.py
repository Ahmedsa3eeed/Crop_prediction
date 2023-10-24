import streamlit as st
import pandas as pd
import joblib

Inputs = joblib.load("Inputs.pkl")
model = joblib.load("model.pkl")

z3={'grapes': 0,
 'muskmelon': 1,
 'kidneybeans': 2,
 'jute': 3,
 'watermelon': 4,
 'orange': 5,
 'pigeonpeas': 6,
 'pomegranate': 7,
 'rice': 8,
 'coffee': 9,
 'mango': 10,
 'mothbeans': 11,
 'banana': 12,
 'coconut': 13,
 'lentil': 14,
 'apple': 15,
 'papaya': 16,
 'cotton': 17,
 'maize': 18,
 'blackgram': 19,
 'mungbean': 20,
 'chickpea': 21}

def prediction(Nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall):
    test_df=pd.DataFrame(columns=Inputs)
    test_df.at[0,'Nitrogen']=Nitrogen
    test_df.at[0,'phosphorus']=phosphorus
    test_df.at[0,'potassium']=potassium
    test_df.at[0,'temperature']=temperature
    test_df.at[0,'humidity']=humidity
    test_df.at[0,'ph']=ph
    test_df.at[0,'rainfall']=rainfall
    result=model.predict(test_df)[0]
    for i in z3.keys():
        if z3[i]==result:
            result_sh=i
            break 
    return result_sh

def main():
    st.title('Crop recommendation prediction')
    Nitrogen=float(st.number_input('Insert the amount of nitrogen in (in kg/ha) in soil'))
    phosphorus=float(st.number_input('Insert the amount for phosphorus in (in kg/ha) in soil'))
    potassium=float(st.number_input('Insert the amount of potassium in (in kg/ha) in soil'))
    temperature=float(st.number_input('Insert the average temperature in celsius'))
    humidity=float(st.number_input('Insert the average relative humidity in percent'))
    ph=float(st.number_input('Insert PH value of soil'))
    rainfall=float(st.number_input('Insert amount for rainfall in mm'))

    if st.button("predict"):
        result=prediction(Nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall)
        st.text(f'The crop will be {result}')


if __name__ == '__main__':
    main()
    
