import streamlit as st
import numpy as np
import pandas as pd

# Page content
st.markdown(" <center>  <h1> Crop recommendation </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

st.markdown(''' <center>  <h6>
    This application predicts the crop type according to the type of soil </center> </h6> ''', unsafe_allow_html=True)

# the path of a photo provided from the path of this file
st.image('crops.jpg')


