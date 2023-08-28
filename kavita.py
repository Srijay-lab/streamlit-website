import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import base64

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Kavita's Space", page_icon=":man-woman-girl-boy:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding1 = load_lottieurl("https://lottie.host/e0fb34ee-b2db-463c-a4e9-8c4120f43462/jDkbh3hfkS.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")
img_kavita = Image.open("images/kavita.jpg")
img_safron = Image.open("images/safron_sample.png")

synclay_demo = open("images/synclay_demo.gif", "rb")

# with st.sidebar:
selected = option_menu(
    menu_title=None,
    options=['Home', 'Blogs', 'Travel', 'Connect'],
    icons=['house', 'book', 'airplane', 'envelope'],  # From Bootstrap icons
    # menu_icon='cast',
    default_index=0,
    orientation='horizontal'
)

if (selected == 'Home'):
    
    # ---- HEADER SECTION ----
    with st.container():
        left_column, right_column = st.columns((1.5, 1))
        with left_column:
            st.subheader("Hi, I am Kavita :wave: ")
            st.title("An Entrepreneur")
            st.write(
                "working with the vision of providing a transparent model in which matrimonial candidate would confirm matched profiles according to their choices before paying charges, helping him/her to select a perfect life partner."
            )
            st.write("[My LinkedIn >](https://www.linkedin.com/in/kavita-deshpande-6b0568166/)")
        with right_column:
            st.image(img_kavita)
            st.write("This snapshot was taken amidst my expedition to the land of Fire & Ice")

    # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((2, 1))
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
                """
                - I run the second largest Matrimonial Website called ReshimBandh in Maharashtra
                - I like to attend Sanskar Bharti programs
                - I take interest in Indian history
                - Reading is something I love and often find solace in books

                If this sounds interesting to you, feel free to contact me
                """
            )
            st.write("[Reshimbandh Website >](https://reshimbandh.com/dist/#/landing/about)")
            st.write("[Facebook >](https://www.facebook.com/kavita.deshpande.142)")
        with right_column:
            st_lottie(lottie_coding1, height=300, key="coding1")

if (selected == 'Connect'):
    # st.title(selected)

    # ---- CONTACT ----
    with st.container():
        # st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/deshpandesrijay@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
