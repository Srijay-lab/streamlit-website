import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import base64

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Srijay's Space", page_icon=":tiger:", layout="wide")

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
lottie_coding1 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")
img_srijay = Image.open("images/srijay.jpg")
img_safron = Image.open("images/safron_sample.png")
img_diffusion = Image.open("images/diffusion.png")

synclay_demo = open("images/synclay_demo.gif", "rb")

selected = option_menu(
    menu_title=None,
    options=['Home', 'Research Exhibitions', 'Publications', 'Connect'],
    icons=['house', 'book', 'journal-code', 'envelope'],  # From Bootstrap icons
    # menu_icon='cast',
    default_index=0,
    orientation='horizontal'
)

if(selected == 'Home'):

    # ---- HEADER SECTION ----
    with st.container():
        left_column, right_column = st.columns((1.5,1))
        with left_column:
            st.subheader("Honored Visitor, welcome to My Space! :smile:")
            st.subheader("I am Srijay :wave: ")
            st.title("A Machine Learning Scientist")
            st.write(
                "with a proven track record of over 5 years in machine learning, deep learning, and computer vision, focusing on pioneering advancements in this field. During my tenure at the University of Warwick, I spearheaded the development of computer-vision based solutions in the domain of computational pathology and implemented cutting-edge Generative AI algorithms for tissue image generation. The results of this work were published in top-tier conferences and journals. As a Data Scientist at Microsoft, I collaborated with the Bing Ads team to improve the information retrieval performance of sponsored search by developing novel NLP techniques. My internship at Amazon further strengthened my software development skills. I am adept at learning quickly, adapting to changing circumstances, and working both independently and collaboratively."
            )
            st.write("[My LinkedIn >](https://www.linkedin.com/in/srijay-deshpande-6933b061/)")
            st.write("[My CV >](https://github.com/Srijay/streamlit-website/blob/main/Srijay_CV.pdf/)")
        with right_column:
            st.image(img_srijay)
            st.write("This snapshot was taken amidst my expedition to the land of Fire & Ice")

    # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((2,1))
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
                """
                - I train Machine Learning models/ Large Language Models on Large Datasets
                - I enjoy Competitive Coding and find programming accompanied by a cup of coffee quite delightful
                - I love to explore different parts of the world
                - During leisure, I like to engage in a game of Lawn Tennis
                - Reading is something I love and often find solace in books
    
                If this sounds interesting to you, feel free to contact me.
                """
            )
        with right_column:
            st_lottie(lottie_coding1, height=300, key="coding1")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Significant Experiences from My Journey")
            st.write("##")
            st.write(
                """
                - Currently I am Research Fellow at the University of Warwick
                - During my PhD, I focused on Generative AI for Computational Pathology, creating new deep generative models to generate realistic tissue images
                - My tenure as a Data Scientist at Microsoft saw me making valuable contributions to the realm of Bing Ads Retrieval
                - Throughout my masters at IIT-Bombay, I engaged in diverse projects centered around Natural Language Processing
                - While interning at Amazon, I garnered extensive proficiency in Java and Ruby on Rails
                - During my undergraduation at NIT-Nagpur, I gained proficiency in Computer Languages and Oracle Database
                """
            )
            st.write("[Warwick Profile >](https://warwick.ac.uk/fac/sci/dcs/people/u1958717/)")
        with right_column:
            st.markdown("![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmJrZzh4dGFudTQxNnBnaHBmMHl3YzIwMHhwa3R6ZWV2a29rNDg5eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LR4UZ731tZVkFDhOhu/giphy.gif)")

if (selected == 'Research Exhibitions'):

    st.title("Major Research Projects & Demos")

    # ---- PROJECTS ----
    with st.container():
        st.write("---")
        st.write("##")
        st.subheader("SAFRON: Stitching Across the Frontier Network for Generating Colorectal Cancer Histology Images")
        st.image(img_safron)

    with st.container():
        st.write(
            """
            A novel framework called SAFRON (Stitching Across the FROntier Network) to construct realistic, large high-resolution tissue images conditioned on input tissue component masks. We have used the proposed framework for generating, to the best of our knowledge, the largest-sized synthetic histology images to date (up to 11K × 8K pixels).
            """
        )
        
        st.write("[Try Demo >](https://huggingface.co/spaces/srijaydeshpande/SAFRON)")
        st.write("[Code >](https://github.com/Srijay/SAFRON/)")
        st.write("[Publication URL >](https://www.sciencedirect.com/science/article/abs/pii/S1361841521003820/)")
        st.write("[Project Website >](https://warwick.ac.uk/fac/cross_fac/tia/projects/safron//)")

    st.write("---")
    st.write("##")

    with st.container():
        st.write("---")
        st.write("##")
        st.subheader("Latent Diffusion Model + Pix2pixHD based Annotated Colon Cancer Image Generation")
        st.image(img_diffusion)

    with st.container():
        st.write(
            """
            A latent diffusion based model to create annotated colon cancer histology images.
            """
        )
        
        st.write("[Try Demo >](https://huggingface.co/spaces/srijaydeshpande/DiffusionGenerator)")
        st.write("[Publication URL >](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/12933/129330H/Synthesis-of-annotated-colon-cancer-tissue-images-from-gland-layout/10.1117/12.3006927.short)")

    st.write("---")
    st.write("##")

    with st.container():
            st.subheader("SynCLay: Interactive Synthesis of Histology Images from Bespoke Cellular Layouts")
            contents = synclay_demo.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            synclay_demo.close()
            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}"  width="900" height="450" alt="cat gif">',
                unsafe_allow_html=True,
            )
    with st.container():
            st.write(
                """
                An interactive framework called SynCLay (Synthesis from Cellular Layouts) that can construct realistic and high-quality histology images from user-defined cellular layouts along with annotated cellular boundaries. Tissue image generation based on bespoke cellular layouts through the proposed framework allows users to generate different histological patterns from arbitrary topological arrangement of different types of cells.
                """
            )
            st.write("[Code >](https://github.com/Srijay/SynCLay-Framework)")
            st.write("[Publication URL >](https://arxiv.org/abs/2212.13780/)")

if (selected == 'Publications'):

    st.title("Major Publications")
    # ---- PROJECTS ----
    with st.container():
        st.write("---")
        st.write("##")
        st.write("Deshpande, Srijay, Fayyaz Minhas, Simon Graham, and Nasir Rajpoot. “SAFRON: Stitching across the frontier network for generating colorectal cancer histology images.” Medical image analysis 77 (2022): 102337.")
        st.write("[Publication URL >](https://www.sciencedirect.com/science/article/abs/pii/S1361841521003820)")
        st.write("##")
        st.write("Deshpande, Srijay, Muhammad Dawood, Fayyaz Minhas, and Nasir Rajpoot. “SynCLay: Interactive Synthesis of Histology Images from Bespoke Cellular Layouts.”(Accepted in Medical image analysis (2023)).")
        st.write("[Publication URL >](https://arxiv.org/abs/2305.05006)")
        st.write("##")
        st.write("Pocock, Johnathan, Simon Graham, Quoc Dang Vu, Mostafa Jahanifar, Sri- jay Deshpande, Giorgos Hadjigeorghiou, Adam Shephard et al. “TIATool- box as an end-to-end library for advanced tissue image analytics.” Communi- cations medicine 2, no. 1 (2022): 120.")
        st.write("[Publication URL >](https://www.nature.com/articles/s43856-022-00186-5)")
        st.write("##")
        st.write("Deshpande, Srijay, Violeta Kovacheva, Fayyaz Minhas, and Nasir Rajpoot. “Generative models for synthesis of colorectal cancer histology images.” In Biomedical Image Synthesis and Simulation, pp. 491-516. Academic Press, 2022")
        st.write("[Publication URL >](https://www.sciencedirect.com/science/article/abs/pii/B9780128243497000293)")
        st.write("##")
        st.write("Thakare, Atul, Srijay Deshpande, Amit Kshirsagar, and Parag Deshpande. Mining Query Plans for Finding Candidate Queries and Sub-Queries for Materialized Views in BI Systems Without Cube Generation. Computing & Informatics 38, no. 2 (2019).")
        st.write("[Publication URL >](https://www.cai.sk/ojs/index.php/cai/article/download/2019_2_473/961/03)")
        st.write("##")
        st.write("Bhushan, Alka, Umesh Bellur, Kuldeep Sharma, Srijay Deshpande, and Nandlal L. Sarda. Mining swarm patterns in sliding windows over moving object data streams. In Proceedings of the 25th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, pp. 1-4. 2017.")
        st.write("[Publication URL >](https://dl.acm.org/doi/abs/10.1145/3139958.3139988)")

if(selected == 'Connect'):

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
