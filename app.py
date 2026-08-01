import streamlit as st
import random
from datetime import date
from streamlit.components.v1 import html as st_html

st.set_page_config(
    page_title="Will You Go On A Date With Me?",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,500;1,600&family=Nunito:wght@400;500;600;700;800&family=Great+Vibes&display=swap');
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(135deg, #fce7f3 0%, #f3e8ff 50%, #e0e7ff 100%);
        min-height: 100vh;
    }
    
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 520px !important;
    }
    
    .main-card, .date-card {
        background: #fffef9;
        border-radius: 20px;
        padding: 1.8rem 1.4rem;
        box-shadow: 0 15px 40px rgba(190, 24, 93, 0.12);
        max-width: 100%;
        margin: 0.5rem auto 1rem;
        text-align: center;
        border: 1px solid rgba(251, 207, 232, 0.6);
    }
    
    .small-label {
        font-family: 'Nunito', sans-serif;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        color: #be185d;
        text-transform: uppercase;
        margin-bottom: 0.6rem;
    }
    
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.85rem;
        font-weight: 700;
        color: #881337;
        line-height: 1.25;
        margin-bottom: 0.6rem;
    }
    
    .subtitle {
        font-family: 'Nunito', sans-serif;
        font-size: 0.9rem;
        color: #9f1239;
        opacity: 0.85;
        margin-bottom: 1.2rem;
        line-height: 1.5;
    }
    
    .meme-img {
        border-radius: 14px;
        border: 3px solid #fff;
        box-shadow: 0 6px 18px rgba(0,0,0,0.1);
        max-width: 180px;
        width: 70%;
        margin: 0 auto 0.4rem;
        display: block;
    }
    
    .stButton > button {
        font-family: 'Nunito', sans-serif !important;
        font-weight: 700 !important;
        border-radius: 9999px !important;
        padding: 0.65rem 1.4rem !important;
        font-size: 0.95rem !important;
        transition: all 0.25s ease !important;
        width: 100% !important;
    }
    
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #ec4899, #db2777) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 14px rgba(219, 39, 119, 0.4) !important;
    }
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) scale(1.02) !important;
        box-shadow: 0 6px 20px rgba(219, 39, 119, 0.5) !important;
    }
    
    .stButton > button[kind="secondary"] {
        background: white !important;
        color: #be185d !important;
        border: 2px solid #f9a8d4 !important;
    }
    
    .slang-msg {
        font-family: 'Nunito', sans-serif;
        font-size: 1.05rem;
        font-weight: 700;
        color: #be185d;
        background: #fdf2f8;
        border: 2px dashed #f9a8d4;
        border-radius: 14px;
        padding: 0.9rem 1rem;
        margin: 1rem 0;
        animation: shake 0.4s ease-in-out;
        text-align: center;
    }
    
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        20% { transform: translateX(-5px); }
        40% { transform: translateX(5px); }
        60% { transform: translateX(-3px); }
        80% { transform: translateX(3px); }
    }

    .envelope-closed {
        width: 240px;
        height: 155px;
        background: linear-gradient(145deg, #fce7f3, #fbcfe8);
        border-radius: 12px;
        margin: 1.5rem auto;
        position: relative;
        box-shadow: 0 12px 30px rgba(190, 24, 93, 0.25);
        border: 2px solid #f9a8d4;
    }
    .envelope-flap {
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 75px;
        background: linear-gradient(145deg, #f9a8d4, #f472b6);
        clip-path: polygon(0 0, 50% 70%, 100% 0);
        border-radius: 12px 12px 0 0;
    }
    .ribbon {
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        width: 60px; height: 60px;
        background: radial-gradient(circle, #be185d 30%, #9f1239 70%);
        border-radius: 50%;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        display: flex; align-items: center; justify-content: center;
        z-index: 5;
        font-size: 1.7rem;
    }
    .envelope-text {
        position: absolute;
        bottom: 14px;
        width: 100%;
        text-align: center;
        font-family: 'Nunito', sans-serif;
        font-size: 0.8rem;
        font-weight: 700;
        color: #9f1239;
    }

    @media (max-width: 480px) {
        .main-title { font-size: 1.65rem; }
        .meme-img { max-width: 150px; }
        .envelope-closed { width: 210px; height: 140px; }
        .block-container { padding-left: 0.7rem !important; padding-right: 0.7rem !important; }
    }
</style>
""", unsafe_allow_html=True)

# ==================== SESSION STATE ====================
if "frame" not in st.session_state:
    st.session_state.frame = 1
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0
if "wrong_attempts" not in st.session_state:
    st.session_state.wrong_attempts = 0
if "letter_opened" not in st.session_state:
    st.session_state.letter_opened = False

# ==================== FRAME 1: Question ====================
if st.session_state.frame == 1:
    st.markdown("""
    <div class="main-card">
        <div class="small-label">A Small Question</div>
        <div class="main-title">Will you go on<br>a date with me?</div>
        <div class="subtitle">Take your time. There is really only one right answer here.</div>
        <img class="meme-img" 
             src="https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif" 
             alt="Me waiting for you to press YES">
        <div style="font-family:'Nunito',sans-serif; font-size:0.75rem; color:#be185d; 
                    font-weight:700; margin-top:0.4rem; letter-spacing:0.04em;">
            ME WAITING FOR YOU TO PRESS YES
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)

    if st.button("💖 Yes, I'd love to!", use_container_width=True, type="primary", key="yes_btn"):
        st.session_state.frame = 2
        st.rerun()

    st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)

    # Runaway No button (works on mobile)
    no_labels = [
        "Nope", "No way", "Absolutely not", "Hmm... no", "Still no",
        "Nice try 😏", "You sure?", "Think again", "Really?", "Come on...",
        "The other one →", "Almost...", "Nope again", "I dare you", "Wrong button"
    ]
    current_label = no_labels[min(st.session_state.no_clicks, len(no_labels)-1)]

    runaway_html = f"""
    <div id="no-container" style="position:relative; height:70px; width:100%; margin:0 auto;">
        <button id="noBtn" 
            style="
                position: absolute;
                left: 50%;
                top: 10px;
                transform: translateX(-50%);
                font-family: Nunito, sans-serif;
                font-weight: 700;
                font-size: 0.95rem;
                padding: 0.65rem 1.6rem;
                border-radius: 9999px;
                background: white;
                color: #be185d;
                border: 2px solid #f9a8d4;
                box-shadow: 0 2px 8px rgba(0,0,0,0.06);
                cursor: pointer;
                transition: all 0.15s ease;
                white-space: nowrap;
                z-index: 10;
                -webkit-tap-highlight-color: transparent;
                user-select: none;
            ">
            {current_label}
        </button>
    </div>

    <script>
        const btn = document.getElementById('noBtn');
        const container = document.getElementById('no-container');
        let clicks = {st.session_state.no_clicks};
        const labels = {no_labels};

        function moveButton(e) {{
            if (e) {{
                e.preventDefault();
                e.stopPropagation();
            }}
            const containerRect = container.getBoundingClientRect();
            const btnRect = btn.getBoundingClientRect();
            const maxX = Math.max(10, containerRect.width - btnRect.width - 10);
            const maxY = Math.max(5, containerRect.height - btnRect.height - 5);
            let newX = Math.random() * maxX;
            let newY = Math.random() * maxY;
            const curLeft = parseFloat(btn.style.left) || containerRect.width / 2;
            if (Math.abs(newX - curLeft) < 40) {{
                newX = (newX + 80) % maxX;
            }}
            btn.style.left = newX + 'px';
            btn.style.top = newY + 'px';
            btn.style.transform = 'none';
            clicks = Math.min(clicks + 1, labels.length - 1);
            btn.innerText = labels[clicks];
        }}

        btn.addEventListener('mouseenter', moveButton);
        btn.addEventListener('click', function(e) {{
            e.preventDefault();
            moveButton(e);
        }});
        btn.addEventListener('touchstart', function(e) {{
            e.preventDefault();
            moveButton(e);
        }}, {{passive: false}});
        btn.addEventListener('touchmove', function(e) {{
            e.preventDefault();
        }}, {{passive: false}});
    </script>
    """
    st_html(runaway_html, height=80)

    st.markdown("""
    <p style="text-align:center; font-family:'Nunito',sans-serif; color:#be185d; 
              font-size:0.85rem; margin-top:0.8rem; opacity:0.9;">
        The No button runs away on purpose 😏<br>
        Just press the pink one 💕
    </p>
    """, unsafe_allow_html=True)

# ==================== FRAME 2: Date Picker ====================
elif st.session_state.frame == 2:
    st.markdown("""
    <div class="date-card">
        <div class="small-label">Wait a second...</div>
        <div class="main-title" style="font-size:1.65rem;">
            Oh shit I forgot<br>what day is today 😩
        </div>
        <div class="subtitle">
            Can u remind me?<br>
            (pick the correct date below)
        </div>
    </div>
    """, unsafe_allow_html=True)

    selected = st.date_input(
        "Select the date",
        value=None,
        min_value=date(2020, 1, 1),
        max_value=date(2030, 12, 31),
        format="DD/MM/YYYY",
        label_visibility="collapsed"
    )

    st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)

    if st.button("Confirm Date 📅", use_container_width=True, type="primary"):
        if selected is None:
            st.warning("Pick a date first silly 😤")
        elif selected.month == 8 and selected.day == 1:
            st.session_state.frame = 3
            st.session_state.letter_opened = False
            st.rerun()
        else:
            st.session_state.wrong_attempts += 1
            slang = [
                "Are you crazy?? 🤨",
                "Bruhhh... seriously? 😒",
                "I am hating u now 😤",
                "Choose correctly like this 👆",
                "Bro what day do you think it is? 💀",
                "Wrong. Try again before I get mad 🔥",
                "Nahhh this ain't it chief ✋",
                "Pick August 1st you absolute clown 🤡",
                "I'm about to un-date you 😭",
                "One more wrong and I'm blocking you 📵",
            ]
            msg = slang[min(st.session_state.wrong_attempts - 1, len(slang) - 1)]
            st.markdown(f'<div class="slang-msg">{msg}</div>', unsafe_allow_html=True)

    if st.session_state.wrong_attempts >= 3:
        st.markdown("""
        <p style="text-align:center; font-family:'Nunito',sans-serif; 
                  color:#be185d; font-size:0.8rem; margin-top:0.8rem;">
            💡 Hint: It's National Girlfriend Day... August 1 😉
        </p>
        """, unsafe_allow_html=True)

# ==================== FRAME 3: Letter ====================
elif st.session_state.frame == 3:

    if not st.session_state.letter_opened:
        st.markdown("""
        <div style="text-align:center; margin-top:0.5rem;">
            <div class="small-label">You got a letter</div>
            <div style="font-family:'Playfair Display',serif; font-size:1.4rem; 
                        font-weight:700; color:#881337; margin-bottom:0.3rem;">
                Something special is waiting...
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="envelope-closed">
            <div class="envelope-flap"></div>
            <div class="ribbon">🎀</div>
            <div class="envelope-text">TAP TO OPEN ✉️</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open the letter 💌", use_container_width=True, type="primary"):
            st.session_state.letter_opened = True
            st.rerun()

    else:
        # Scrollable letter - works on mobile
        letter_html = """
        <div style="
            background: #fffef9;
            border-radius: 16px;
            padding: 1.5rem 1.2rem;
            max-width: 100%;
            margin: 0 auto;
            box-shadow: 0 15px 40px rgba(190, 24, 93, 0.15);
            border: 1px solid #f9a8d4;
            font-family: Nunito, sans-serif;
            max-height: 70vh;
            overflow-y: auto;
            -webkit-overflow-scrolling: touch;
        ">
            <div style="
                font-family: 'Great Vibes', cursive;
                font-size: 2rem;
                color: #be185d;
                text-align: center;
                margin-bottom: 0.8rem;
            ">Happy Girlfriend Day 💕</div>
            
            <div style="text-align:center; font-size:1.2rem; margin:0.7rem 0; opacity:0.7;">✦ ✦ ✦</div>
            
            <div style="font-size:0.95rem; color:#4a1d2e; line-height:1.75; text-align:left;">
                <p style="margin-bottom:0.9rem;">Hey you,</p>
                
                <p style="margin-bottom:0.9rem;">
                    Till now we've been friends…  
                    laughing, talking, sharing random nonsense at odd hours.
                </p>
                
                <p style="margin-bottom:0.9rem;">
                    But today, on this special day, I want to say something real.
                </p>
                
                <p style="margin-bottom:0.9rem;">
                    I don't just want to stay friends.  
                    I want us to be something more —  
                    <strong>together, for real, till we're old and still arguing about who forgot the charger.</strong>
                </p>
                
                <p style="margin-bottom:0.9rem;">
                    So this is me officially asking…  
                    will you be my girlfriend?
                </p>
                
                <p style="margin-bottom:0.9rem;">
                    No pressure. Just honesty.  
                    And a whole lot of love ready for you.
                </p>
            </div>
            
            <div style="
                font-family: 'Great Vibes', cursive;
                font-size: 1.5rem;
                color: #be185d;
                text-align: right;
                margin-top: 1.1rem;
            ">Yours,</div>
            
            <div style="text-align:center; font-size:1.3rem; margin:0.8rem 0 0.3rem; opacity:0.7;">💖</div>
        </div>
        """
        st_html(letter_html, height=480)

        st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)

        if st.button("🎁 Surprise awaiting — Press me", use_container_width=True, type="primary"):
            st.session_state.frame = 4
            st.rerun()

# ==================== FRAME 4: Video (fullscreen + landscape + 180° on mobile) ====================
elif st.session_state.frame == 4:
    st.markdown("""
    <style>
        .stApp {
            background: #0a0a0a !important;
        }
        .block-container {
            padding-top: 0.3rem !important;
            padding-bottom: 0 !important;
            padding-left: 0.3rem !important;
            padding-right: 0.3rem !important;
            max-width: 100% !important;
        }
        video {
            width: 100% !important;
            max-height: 94vh !important;
            border-radius: 8px;
            object-fit: contain;
        }
        /* Rotate video 180° on mobile for better experience */
        @media (max-width: 768px) {
        video {
            position: fixed !important;
            top: 50% !important;
            left: 50% !important;
            # width: 100vh !important;   /* swapped */
            # height: 100vw !important;  /* swapped */
            max-width: none !important;
            max-height: none !important;
            transform: translate(-50%, -50%) rotate(90deg) !important;
            object-fit: cover !important;
            border-radius: 0 !important;
            z-index: 100;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Mobile landscape detection + prompt
    orientation_js = """
    <div id="rotate-msg" style="
        display: none;
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(10,10,10,0.95);
        z-index: 9999;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: white;
        font-family: Nunito, sans-serif;
        padding: 2rem;
    ">
        <div style="font-size: 3rem; margin-bottom: 1rem;">📱↩️</div>
        <div style="font-size: 1.3rem; font-weight: 700; margin-bottom: 0.5rem;">
            Please rotate your phone
        </div>
        <div style="font-size: 0.95rem; opacity: 0.8;">
            Turn to landscape for the best experience 💖
        </div>
    </div>

    <script>
        function isMobile() {
            return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)
                || (window.innerWidth <= 768);
        }

        function checkOrientation() {
            const msg = document.getElementById('rotate-msg');
            if (!msg) return;

            if (isMobile()) {
                if (screen.orientation && screen.orientation.lock) {
                    screen.orientation.lock('landscape').catch(function() {});
                }

                const isPortrait = window.innerHeight > window.innerWidth;
                if (isPortrait) {
                    msg.style.display = 'flex';
                } else {
                    msg.style.display = 'none';
                }
            }
        }

        checkOrientation();
        window.addEventListener('resize', checkOrientation);
        window.addEventListener('orientationchange', function() {
            setTimeout(checkOrientation, 200);
        });
    </script>
    """
    st_html(orientation_js, height=0)

    video_path = "special.mp4"

    try:
        st.video(video_path, autoplay=True, muted=False, loop=False)
    except Exception:
        st.error("Video not found! Place your MP4 as **special.mp4** next to app.py")

# Footer only on non-video frames
if st.session_state.frame != 4:
    st.markdown("""
    <div style="text-align:center; margin-top:2.5rem; font-family:'Nunito',sans-serif; 
                font-size:0.7rem; color:#a78bfa; opacity:0.7;">
        made with 💖 · just for you
    </div>
    """, unsafe_allow_html=True)