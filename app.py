from re import X
import streamlit as st 
import pandas as pd
import numpy as np
df = pd.read_csv("credit_default.csv", index_col=0)
df.head()
df3= df.groupby(df['age'])[['income', 'term']].mean()
df1 = df.groupby(df['income'])[['term','loan_amount']].mean()
df4 = df.groupby(df['gender'])[['property_value', 'credit_score', 'status']].mean()
st.header("Dashboard Inadimplência de Crédito")
#if st.sidebar.button("Escolha o Grafico"):
    #df3= pd.DataFrame(
     #   np.random.rand(20,3),
      #  columns=[ 'age','income', 'status']
    #)
    #st.bar_chart(df3)
    #st.line_chart(df3)
    
    
    
opcao= st.sidebar.multiselect(
    "SELECIONE A OPÇÃO",
    ('TIPO DE RENDA','GENERO','IDADE')
) 

if "TIPO DE RENDA" in opcao:
    st.line_chart(df1)
if "GENERO" in opcao:
    st.bar_chart(df4)
if "IDADE" in opcao:
    st.line_chart(df3)


        
        
        
        
        
        


