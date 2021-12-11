import streamlit as st


import io
import os
import yaml

from PIL import Image

from predict import load_model , get_prediction

from confirm_button_hack import cache_on_button_press



st.set_page_config(layout = "wide")

st.write("password")

root_password = 'password'


def main():
    st.title("Mask Classificatino Demo")

    with open("config.yaml") as f:
        config = yaml.load(f , load = yaml.FullLoader)

    model = load_model()

    model.eval()


    uploaded_file = st.file_uploader("Choose image plase" , type["jpg" , "jpeg" , "png"])


    if uploaded_file :
        image_bytes = uploaded_file.getvalue()

        image = Image.open(io.BytesIO(image_bytes))

        st.image(image, caption('Uploadede Imasge'))

        st.write("Classifiying  don distraction me")

        _,y_hat = get_prediction(model, image_bytes)

        label = config['classes'][y_hat.item()]

        st.write(f'label is {label}')


# @cache_on_button_press('Authenticate')
# def authenticate(password) ->bool :
#     print(type(password))
#     return password == root_password

# password  = st.text_input('password' , type="password")


# if authenticate(password) :
#     st.success('you are authenticated')
#     main()

# else:
#     st.error('The password is invalid')

main()