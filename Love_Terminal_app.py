import streamlit as st
import random
from PIL import Image, ImageOps

st.set_page_config(page_title="Love Terminal", page_icon="💖", layout="centered")

# 23 compliment/media pairs
pairs = [
    ("My little angler fish. You are perfect just the way you are! :) 🐟",      "angler.jpg",         "image"),
    ("I will always take care of you and be there whenever you need me. 💖",      "careforyou.jpg",     "image"),
    ("I love seeing your outfits anything on you looks good...... or off 👀 👗",      "outfits.jpg",        "image"),
    ("My little chef. I love watching your kitchen endeavors can't wait for us to cook together. 😍","chef.jpg",           "image"),
    ("One of my favorite pictures together. You look so cute and I just want to always hold you just like I am here. 🧸",          "cutie.jpg",          "image"),
    ("I can watch you dance for hours on end and it makes me so happy. I can't wait to slow dance and do our wedding dances together. 💃","dance.mp4",    "video"),
    ("The fact that you have a good relationship with Alayna makes me so happy. Solidifies that fact that you are the one. 🫶",  "favgyals.jpg",        "image"),
    ("I still remember our first date like it was yesterday. It was never ending and every moment of it was precious to me and I love that we continue to make new memories together. 🌹","firstdate.JPEG","image"),
    ("You make every single good eats picture 100 times better. Everyone gonna be guessing which good eat im talking about!! 🍽️","goodeats.jpg","image"),
    ("That hand kiss? Yeah, I'm still thinking about it. I love kissing you everywhere and showing you how much I love you. 💋","handkiss.JPG","image"),
    ("Shahana you are so beautiful. I love you so much. 🔥","hot.JPG",           "image"),
    ("I could stay in that hug forever. You make me feel at peace and so comforted. 🤗",      "hugs.jpg",           "image"),
    ("Nothing beats laying together doing nothing on facetime just admiring each other. No matter the distance we have each others love.  💫","layingtogether.jpg","image"),
    ("Your smile is brighter than the stars. It makes me so happy seeing you happy. 💌","love.JPG",      "image"),
    ("This picture captures how enamored I am for you. Just looking at you lights up my whole world. You are PERFECT!",            "awe.jpg",        "image"),
    ("The ocean and night sky can't compare to your beauty. 🌊","pier.jpg",      "image"),
    ("The start of our journey together. Predate told us everything we needed to know about each other and I knew I was ready to be with you forever. 😂","predate.jpg","image"),
    ("You’re just effortlessly pretty even more than the most beautiful flower. ✨",        "pretty.jpg",         "image"),
    ("You have the most kissable lips. Can't resist fr 💋",        "pucker.JPG",         "image"),
    ("You make me feel so comfortable. You being in my arms makes me feel like im holding the whole world. You're all mine and im never letting you go. 😴",           "sleep.jpg",          "image"),
    ("Your beauty just wows me every time. I love pictures of you 😊",     "smile.jpg",          "image"),
    ("Even during tough times like studies we are there for each other and you make that look cute too. My little study buddy. 📚","studies.PNG",      "image"),
    ("My future doctorrrrr!! I love hearing about your work stories and keeping you company whenever. Seeing your little updates brings a smile to my face everytime. 📨","updates.jpg",    "image"),
]

# play background music
audio_file = open("background.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")

# Intro image
intro = ImageOps.exif_transpose(Image.open("us_together.JPG"))
st.image(intro, caption="❤️ Lahana ❤️", use_container_width=True)

# Initialize our shuffled queue on first run
if "queue" not in st.session_state:
    st.session_state.queue = pairs.copy()
    random.shuffle(st.session_state.queue)

st.title("💘 Welcome to the Love Terminal 💘")

name = st.text_input("What is your name, my love?", "")

if name:

    st.subheader(f"Hi {name} 🌹")

    # Surprise button
    if st.button("Click me for a surprise 💌"):

        if st.session_state.queue:
            # Pop one random pair from our queue
            compliment, media_path, media_type = st.session_state.queue.pop()

            st.success(compliment)

            # Display media
            if media_type == "image":
                img = Image.open(media_path)
                img = ImageOps.exif_transpose(img)
                st.image(img, caption="💕 Us", use_container_width=True)
            else:
                st.video(media_path)

        else:
            # Queue is empty
            st.balloons()
            st.markdown("### 🎉 All done! Hope you enjoyed every surprise. 🎉")
            st.write("I can't wait to continue making more memories with you and just being a part of your life. I love you so much and am so lucky to have you as my girlfriend ❤️")
            st.write("Thank you for being amazing! ❤️")

    # Secret‑code section stays the same
    secret = st.text_input("Type a secret code...")
    if secret.lower().strip() == "iloveyou":
        st.balloons()
        st.markdown("### 💖 Secret Message Unlocked 💖")
        st.info("SHAHANAAAAAAA!!!! Happy National Girlfriend's Day!!!!! I am the luckiest man in the world to be able to be with someone like you. I don't even know where to begin. Our journey is never ending and I love that we are with each other throughout our ups and downs. Being in your presence even on the phone makes me feel so comfortable and at peace. Even when im down or stressing seeing you instantly lifts my moods and just reminds me of how we have each other and thats all we need. Shahana I love you so much and you mean the world to me and I know for a fact that you are the one. There isn't a doubt in my mind about us being together. We are just meant to be. This summer has been long but talking to you every day made it go by so fast. The routine we created like waking up to each other in the morning and getting ready for the day. Making and eating meals together while yapping about life or random topics. Planning future dates and telling each other how much we love and miss each other. OH AND I CANT FORGET LOVE ISLAND. Watching shows and movies with you especially Love Island and Bollywood was some of the most fun I've had. I haven't been that invested in so long but something about you just makes everything perfect and I love it. Then us talking to each other at night in our sleepy voices saying goodnight and blowing kisses to each other makes me go to sleep happy and at peace every time. I think this summer was perfect and you were a big part of it Shahana being the best girlfriend in the world and all. Your company, your smile, your jokes, your beauty, everything about you is perfect in every way and I can't wait to spend the rest of my life with you and even after. Together till Jannah right!!!! I know this is just the beginning of our story and I can't wait to see how the next chapters unfold. I'm looking forward to finally being back at college knowing that you'll be there as well and that we have each other to lean on. I love you so much Shahana and I can't wait to see you again I miss youuuuu. Your Love, Labib ❤️")