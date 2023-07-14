import streamlit as st
import pandas as pd

st.title("Garmy_Samb_ISE2")
st.write("TP_dashboard_tuto_streamlit!")

impressions = pd.read_csv('C:\Users\user\Desktop\SEMESTRE2_ISE2\MACHINE LEARNING 2\dashboard_tuto\impressions.csv')
clics = pd.read_csv('C:\Users\user\Desktop\SEMESTRE2_ISE2\MACHINE LEARNING 2\dashboard_tuto\clics.csv')
achats = pd.read_csv('C:\Users\user\Desktop\SEMESTRE2_ISE2\MACHINE LEARNING 2\dashboard_tuto\achats.csv')

fusion1 = pd.merge(impression,clics, on ='cookie_id')
fusion = pd.merge(fusion1,achats, on ='cookie_id')
fusion



@app.route('/api/donnees', methods=['GET'])
def donnees():
    return jsonify(fusion)
    
    
    
ca= fusion['price'].sum()
st.write(f"<span style='color:purple; font-size:60px;'>Chiffre d'affaires : {ca} € </span>", unsafe_allow_html=True)

st.subheader('Vente en fonction des campagnes')
hist= px.histogram(fusion, x = 'campaign_id', y= 'price')
st.plotly_chart(hist)


st.subheader('Age en fonction des produits')
box= px.box(fusion, x = 'product_id' , y= 'age')
st.plotly_chart(box)


st.subheader('Répartition des ventes en fonction du sexe')
colors = ['#808080', '#FFFF00'] 
pie = px.pie(fusion, values='price', names='gender', color_discrete_sequence=colors)
st.plotly_chart(pie)

st.subheader('Nuage de points des ventes en fonction des produits')
nuage = px.scatter(fusion, x='price', y='product_id')
st.plotly_chart(nuage)

  

if __name__ == '__dashboard_tuto__':
    app.run(debug=True)
