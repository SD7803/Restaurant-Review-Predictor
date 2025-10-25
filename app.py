#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

st.set_page_config(
    page_title="My App",
    page_icon=":smiley:",
    layout="wide",
    initial_sidebar_state="expanded"
)


import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib


# In[2]:


#st.set_page_config(layout="wide")
scaler=joblib.load("Scaler.pkl")


# In[3]:


st.title("Restaurant Rating Prediction App")
st.caption("This app helps you to predict a restaurants review class")
st.divider()


# In[4]:


averagecost=st.number_input("Please enter the estimated average cost for two",min_value=50,max_value=999999,value=1000,step=200)


# In[5]:


tablebooking=st.selectbox("Restaurant has table booking ?",["Yes","No"])


# In[6]:


onlinedelivery=st.selectbox("Restaurant has online booking ?",["Yes","No"])


# In[7]:


pricerange = st.selectbox("What is the price range (1 Cheapest, 4 Most expensive)", [1, 2, 3, 4])


# In[8]:


predictbutton=st.button("Predict the review!")


# In[9]:


st.divider()


# In[10]:


model=joblib.load("mlmodel.pkl")


# In[11]:


bookingstatus =1 if tablebooking =="Yes" else 0
deliverystatus=1 if onlinedelivery == "Yes" else 0


# In[12]:


values=[[averagecost,bookingstatus,deliverystatus,pricerange]]
my_X_values=np.array(values)
X=scaler.transform(my_X_values)


# In[13]:


if predictbutton:
    st.snow()
    prediction=model.predict(X)
    if prediction < 2.5:
        st.write("Poor")
    elif prediction < 3.5:
        st.write("Average")
    elif prediction < 4.0:
        st.write("Good")
    elif prediction < 4.5:
        st.write("Very Good")
    else:
        st.write("Excellent")
        









