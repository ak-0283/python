import streamlit as st
import random

# Page config
st.set_page_config(page_title="SGPA,CGPA to Percentage Converter", layout="centered")

# Custom Dark Theme CSS
dark_bg = """
<style>
/* Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #1e293b); /* dark navy → slate */
    color: #f8fafc !important; /* light text */
}

/* Header */
[data-testid="stHeader"] {
    background: linear-gradient(90deg, #1e3a8a, #3b82f6);
    color: white;
}

/* Title */
h1 {
    color: #38bdf8 !important; /* cyan */
    font-weight: bold;
}

/* Button styling */
.stButton>button {
    background-color: #3b82f6;
    color: white;
    border-radius: 8px;
    padding: 8px 16px;
    border: none;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #2563eb;
    color: white;
}

/* Alert boxes customization */
.stSuccess {
    background-color: #065f46 !important; /* dark green */
    color: #f0fdf4 !important; /* light green text */
    border-radius: 8px;
}
.stInfo {
    background-color: #1e3a8a !important; /* dark blue */
    color: #e0f2fe !important;
    border-radius: 8px;
}
.stWarning {
    background-color: #78350f !important; /* dark amber */
    color: #fef9c3 !important;
    border-radius: 8px;
}
.stError {
    background-color: #7f1d1d !important; /* dark red */
    color: #fee2e2 !important;
    border-radius: 8px;
}
</style>
"""
st.markdown(dark_bg, unsafe_allow_html=True)

# Title
st.title("🎓 SGPA & CGPA to Percentage Calculator")

# Select option
option = st.selectbox(
    'Select the conversion type:',
    ('SGPA to Percentage', 'CGPA to Percentage'))
st.write('👉 You selected:', option)

percentage = None

# Conversion logic using sliders
if option == 'SGPA to Percentage':
    sgpa = st.slider("Select your SGPA:", 0.0, 10.0, 5.0, 0.01)
    if st.button('Convert to Percentage'):
        percentage = (sgpa - 0.75) * 10
        st.success(f'🎯 Your Percentage is: {percentage:.2f}%')

else:
    cgpa = st.slider("Select your CGPA:", 0.0, 10.0, 5.0, 0.01)
    if st.button('Convert to Percentage'):
        percentage = (cgpa - 0.75) * 10
        st.success(f'🎯 Your Percentage is: {percentage:.2f}%')

# Motivational quotes (dark theme with color-coded boxes)
if percentage is not None:
    if percentage < 50:
        quotes = [
            "Don't worry, success is a journey, not a race! 🚀",
            "Failures are the stepping stones to success. Keep pushing! 💪",
            "Your efforts matter more than numbers. Keep going! 🌟"
        ]
        st.error(random.choice(quotes))

    elif 50 <= percentage < 70:
        quotes = [
            "Good job! Keep striving for excellence! 🌠",
            "Consistency is the key to improvement. You're on the right path! 🔑",
            "Every day is a chance to get better. Keep it up! 🌱"
        ]
        st.warning(random.choice(quotes))

    elif 70 <= percentage < 85:
        quotes = [
            "Great work! You’re shining bright! ✨",
            "Excellence is not an act but a habit. Keep the momentum going! 🔥",
            "Proud of your dedication! 💯"
        ]
        st.info(random.choice(quotes))

    else:
        quotes = [
            "Outstanding! You're a true inspiration! 🏆",
            "Excellence achieved! The sky is the limit! 🚀",
            "Your hard work is clearly paying off! 🎉"
        ]
        st.success(random.choice(quotes))
