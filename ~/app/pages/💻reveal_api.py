import requests
import streamlit as st
from PIL import Image
import json

image = Image.open('image2.png')
st.image(image)

st.title("Reveal Endpoint")

st.write("Cost: 2 credits / successful request.")
st.write("Deanonymize an IPv4 address and associate the Company behind the IPv4 address.")

api_endpoint = 'https://nubela.co/proxycurl/api/reveal/company'

api_key = st.text_input('ENTER YOUR API KEY')
role = st.text_input('ENTER USER COMPANY ROLE')
ip = st.text_input('ENTER USER IPV4 ADDRESS')

if st.button('Get Data'):
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
        'role_contact_number': 'include',
        'role_personal_email': 'include',
        'role': role,
        'ip': ip,
    }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

    st.write(response.json())
    
    jsonFile = open("response.json", "w")
    #jsonFile.write(jsonString)
    jsonFile.close()

    if st.button('Convert To Csv File'):
        with open('response.json', 'r') as f:
            data = json.load(f)
            df = pd.json_normalize(data)
            df.to_csv('reveal_company.csv', encoding='utf-8', index=False)
            df = pd.DataFrame(df)
            file_name = "reveal_company.csv"
            file_path = f"./{file_name}"
            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                      data=df,
                      file_name=file_name,
                      key='download_df')
