import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import base64

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Makarand Parkhi", page_icon=":man:", layout="wide")


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
lottie_coding1 = load_lottieurl("https://lottie.host/4aa91426-c8f4-4d9a-a147-4efc1d7316a0/hJVlutDzzz.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")
img_user = Image.open("images/makarand.jfif")
img_winpoint = Image.open("images/winpoint.png")

# with st.sidebar:
selected = option_menu(
    menu_title=None,
    options=['Home', 'Winpoint', 'Blogs', 'Connect'],
    icons=['house', 'people', 'newspaper', 'envelope'],  # From Bootstrap icons
    default_index=0,
    orientation='horizontal'
)

if (selected == 'Home'):
    
    # ---- HEADER SECTION ----
    with st.container():
        left_column, right_column = st.columns((1.5, 1))
        with left_column:
            st.subheader("Hi, I am Makarand :wave: ")
            st.title("A Leader & Entrepreneur")
            st.write(
                "Who led and managed WinPoint Learning Center (WinPoint) – A Training and Consulting company – founded in 2012 with a dream to impact people's career lives and to contribute to the transformative initiatives of the corporate. My vision for WinPoint (an EdTech company), for B2C segment, was to inspire people worldwide to envision a great career and to help them accomplish career goals at any stage of their professional lives, and for B2B segment, it was to empower enterprise customers to achieve their goals and objectives by improving performance of their employees in the key result areas. Over the last ten years, I have developed an expertise in running an entrepreneurial startup focused on learning & early career development."
            )
            st.write("[My LinkedIn >](https://www.linkedin.com/in/makarand-parkhi-34a09717//)")
        with right_column:
            st.image(img_user)

    # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((2, 1))
        with left_column:
            st.header("Professional Summary")
            st.write("##")
            st.write(
                """
                - Over 20 years of experience of working within Bid & Proposal, Pursuit, Sales Support, and Presales Management including 12 years with customers from the global markets (UK, Europe, NA, APAC, ME) in the outsourcing/offshoring focused on the IT Services and IT Consulting industry
                - Extensive experience in bid project management (1m - 50m dollar pursuits) across Education, Telecom, T & T, Utilities etc based on a deep understanding of the bid process; strong exposure to different phases in the business development lifecycle including market identification, account planning, opportunity assessment, opportunity planning, proposal planning, proposal development, and negotiation & post-submittal activity
                - Knowledge of building and managing Proposal Centre of Excellence (PCoE) promoting a winning culture
                - Expertise in working in close collaboration with the large bid team (20-25 people), sales/opportunity managers, and senior leadership resulting in successful completion of proposals with high levels of engagement and improved team performance
                - Significant experience of working at a leadership level (12+ years); ability to engage, inspire, advise, and coach the proposal team by constructively challenging them around strategy, win theme & value proposition
                - Considerable experience with training, mentoring, & coaching people
                - Great skills in strategic planning, critical thinking, proposal development and management, project management, communication, collaboration, relationship management, time management, decision making, persuasion, and influencing

                If this sounds interesting to you, feel free to contact me
                """
            )
            st.write("[Winpoint >](http://winpointlc.com/)")
            st.write("[Facebook >](https://www.facebook.com/makarand.parkhi.7)")
        with right_column:
            st_lottie(lottie_coding1, height=300, key="coding1")

if (selected == 'Winpoint'):

    st.title("Winpoint: Pursuit of Knowledge")
    st.write("---")
    # ---- HEADER SECTION ----
    with st.container():
        left_column, right_column = st.columns((1.5, 1))
        with left_column:
            st.subheader("About:")
            st.write(
                "WinPoint is a ‘Training and Consulting’ company founded in 2012 with a dream to impact people’s career lives and to contribute to the transformative initiatives of the corporate. We started this enterprise after collectively working in the corporate for 38 years including stints across global markets at a leadership level."
            )
            st.write("[Winpoint >](http://winpointlc.com/)")
        with right_column:
            st.image(img_winpoint)

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