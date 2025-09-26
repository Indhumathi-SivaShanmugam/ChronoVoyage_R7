import streamlit as st
import base64

# --- Helper Function for Image Background ---
def get_base64_image(image_path):
    """Encodes an image to a base64 string for use in CSS."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Encode the background image
image_base64 = get_base64_image("vintage_bg.png")

# --- Custom CSS for Elegant Retro-Futuristic Vibe ---
custom_css = f"""
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Oswald:wght@400;700&family=Orbitron:wght@400;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {{
    background: url("data:image/jpeg;base64,{image_base64}") no-repeat center center fixed;
    background-size: cover;
    color: #000000;
}}

/* Main title styling - Transparent */
h1.title {{
    font-family: 'Playfair Display', serif;
    font-size: 4rem;
    color: #dfcba2;
    text-align: center;
    text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
    background: transparent !important;
    border: none !important;
    margin-bottom: 0.2rem;
    padding: 0;
}}

/* Tagline styling - smaller and elegant */
h3.tagline {{
    font-family: 'Orbitron', sans-serif;
    font-size: 1.4rem;
    color: #000000;
    text-align: center;
    margin-top: 0;
    margin-bottom: 3rem;
    font-weight: 400;
    letter-spacing: 1px;
}}

/* Center the main content */
.main .block-container {{
    max-width: 800px;
    padding-top: 2rem;
}}

/* Elegant container for all sections */
.custom-container {{
    /* Even duller - closer to gray */
    background: rgba(190, 175, 145, 0.1) !important; !important;
    border: 1px solid rgba(223, 203, 162, 0.5) !important;
    border-radius: 15px;
    padding: 2.5rem !important;
    margin: 2rem auto !important;
    backdrop-filter: blur(8px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    max-width: 600px;
}}

.container-title {{
    font-family: 'Orbitron', sans-serif !important;
    font-size: 1.8rem !important;
    color: #dfcba2 !important;
    text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
    text-align: center !important;
    margin-bottom: 1.5rem !important;
}}

/* Input styling inside container */
.input-wrapper {{
    text-align: center;
    margin: 0 auto;
    max-width: 400px;
}}

.stTextInput > div > div {{
    background-color: rgba(255, 255, 255, 0.9) !important;
    border: 2px solid #dfcba2 !important;
    border-radius: 25px !important;
    padding: 10px 20px !important;
    display: flex !important;
    align-items: center !important;
    min-height: 50px !important;
}}

.stTextInput > div > div > input {{
    background-color: transparent !important;
    border: none !important;
    color: #000000 !important;
    font-family: 'Orbitron', sans-serif !important;
    font-size: 1.1rem !important;
    text-align: center !important;
    letter-spacing: 1px;
    padding: 0 !important;
    margin: 0 !important;
    line-height: normal !important;
    height: auto !important;
    vertical-align: middle !important;
}}

.stTextInput > div > div > input::placeholder {{
    color: #666666 !important;
    font-style: italic;
    line-height: normal !important;
    vertical-align: middle !important;
}}

/* Question text styling */
.question-text {{
    font-family: 'Playfair Display', serif !important;
    font-size: 1.8rem !important;
    color: #000000 !important;
    text-align: center !important;
    line-height: 1.6 !important;
    margin-bottom: 0 !important;
    padding: 1rem !important;
}}

/* Notes section styling */
.notes-title {{
    font-family: 'Orbitron', sans-serif !important;
    font-size: 1.5rem !important;
    color: #dfcba2 !important;
    text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
    text-align: left !important;
    margin-bottom: 1rem !important;
    border-bottom: 2px solid rgba(223, 203, 162, 0.5);
    padding-bottom: 0.5rem;
}}

.notes-content {{
    font-family: 'Oswald', sans-serif !important;
    font-size: 1.1rem !important;
    color: #000000 !important;
    line-height: 1.6 !important;
    text-align: left !important;
    padding: 1rem !important;
}}

.notes-content ul {{
    text-align: left !important;
    margin-left: 1rem !important;
    padding-left: 1rem !important;
}}

.notes-content li {{
    text-align: left !important;
    margin-bottom: 0.5rem !important;
}}

/* Remove all default Streamlit styling */
.stMarkdown {{
    background: transparent !important;
    margin: 0 !important;
    padding: 0 !important;
}}

.stMarkdown > div {{
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    margin: 0 !important;
    padding: 0 !important;
}}

/* Hide Streamlit headers and labels */
.stTextInput label {{
    display: none !important;
}}

/* Remove gaps between elements */
div[data-testid="stVerticalBlock"] {{
    gap: 0rem !important;
}}

/* Hide Streamlit's default footer and other elements */
footer {{ visibility: hidden; }}
.stDeployButton {{ display: none; }}
#MainMenu {{ visibility: hidden; }}
"""

# Inject custom CSS
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# Define the question sets
question_sets = {
    "SET 1": {
        "question": "In which year was the idea of a global ___________ for sharing i__________ first proposed?",
        "notes": """
        <ul style="text-align: left; margin-left: 1rem; padding-left: 1rem;">
        <li>Strictly Enter your Team name properly as the question varies according to each team.</li>
        <li>Each blank hides  critical keywords.</li>
        <li>Only exact phrasing leads to the right year.</li>
        <li>The ___ are not to scale , treat them just as a fill up entirely .</li>
         <li>Think about historic milestones in science and technology.</li>
        <li>Tune your words like a radio — precision is everything.</li>
        </ul>
        """
    },
    "SET 2": {
        "question": "In which year was the first __________ Engine concept, a m____________ c__________machine, introduced?",
         "notes": """
        <ul style="text-align: left; margin-left: 1rem; padding-left: 1rem;">
        <li>Strictly Enter your Team name properly as the question varies according to each team.</li>
        <li>Each blank hides  critical keywords.</li>
        <li>Only exact phrasing leads to the right year.</li>
        <li>The ___ are not to scale , treat them just as a fill up entirely .</li>
         <li>Think about historic milestones in science and technology.</li>
        <li>Tune your words like a radio — precision is everything.</li>
        </ul>
        """
    },

    "SET 3": {
        "question": "In which year was the first ________ by Apple, a revolutionary s_________, announced to the public?",
         "notes": """
        <ul style="text-align: left; margin-left: 1rem; padding-left: 1rem;">
        <li>Strictly Enter your Team name properly as the question varies according to each team.</li>
        <li>Each blank hides  critical keywords.</li>
        <li>Only exact phrasing leads to the right year.</li>
        <li>The ___ are not to scale , treat them just as a fill up entirely .</li>
         <li>Think about historic milestones in science and technology.</li>
        <li>Tune your words like a radio — precision is everything.</li>
        </ul>
        """
},
}

# --- Streamlit App Layout ---

# Title and Tagline
st.markdown("<h1 class='title'>Round 7 - Signals through Air</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='tagline'>The wireless age begins — invisible waves carry the last pieces of the mystery.</h3>", unsafe_allow_html=True)


# Input Section - Using HTML to properly contain everything
input_html = f"""
<div class="custom-container">
    <div class="container-title">Enter Your Team Name</div>
    <div class="input-wrapper">
        <!-- Input will be placed here -->
    </div>
</div>
"""

st.markdown(input_html, unsafe_allow_html=True)

# Place the input inside the container using columns to maintain structure
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    team_name = st.text_input(
        "", 
        placeholder="TEAM NAME in  ALL CAPS",
        key="team_input",
        label_visibility="collapsed"
    )

# Display question and notes based on team name
if team_name:
    team_name_lower = team_name.strip().lower()
    
    # Check if the entered team name exists in our question sets (case-insensitive)
    found_team = next((key for key in question_sets if key.lower() == team_name_lower), None)

    if found_team:
        # Display the question in an elegant container
        question_html = f"""
        <div class="custom-container">
            <div class="notes-title">QUESTION:</div>
            <div class="question-text">{question_sets[found_team]['question']}</div>
        </div>
        """
        st.markdown(question_html, unsafe_allow_html=True)
        
        # Display the notes in an elegant container with left alignment
        notes_html = f"""
        <div class="custom-container">
            <div class="notes-title">Keep in Mind:</div>
            <div class="notes-content">{question_sets[found_team]['notes']}</div>
        </div>
        """
        st.markdown(notes_html, unsafe_allow_html=True)
    else:
        st.error("Set not found. Please check the spelling and try again. Valid sets are: SET 1, SET 2, SET 3")