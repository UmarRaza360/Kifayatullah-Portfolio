import streamlit as st

# Page Configuration
st.set_page_config(page_title="Kifayatullah | Portfolio", layout="centered")

# Header Section
st.title("Kifayatullah")
st.subheader("Digital Marketing Specialist")
st.write("📧 kifayatstd@gmail.com | 📞 +92198633044 | [LinkedIn](#)")
st.divider()

# About Me
st.header("The Beginning")
st.write("""
I'm Kifayatullah, a results-driven Digital Marketing Specialist focused on helping businesses grow online through SEO, social media marketing, paid advertising, and creative digital strategies. I combine data-driven insights with creativity to build campaigns that increase visibility, engagement, and business growth.
""")

# Education Section
st.header("My Studies")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**FSC in Computer Science**")
    st.write("Government College Peshawar")
    st.write("*(2025 - 2026)*")
with col2:
    st.write("**DIT - Diploma in IT**")
    st.write("Sher Asghar Institute")
    st.write("*(2025 - 2026)*")
with col3:
    st.write("**E-commerce & Digital Marketing**")
    st.write("Bano Qabil Peshawar")
    st.write("*(2026)*")

st.divider()

# Capabilities
st.header("Personal Capabilities")
st.markdown("""
* **Communication Skills:** Strong ability to share ideas clearly and build professional relationships.
* **Leadership & Teamwork:** Capable of working independently and contributing positively within a team.
* **Creative Problem Solving:** Ability to analyze challenges and develop innovative solutions.
* **Time Management:** Skilled at prioritizing tasks and meeting deadlines effectively.
""")

st.divider()

# Experience
st.header("Career Experience")
st.markdown("""
* **Shopify E-commerce Management:** Managed Shopify store setup, product listings, inventory updates, and order processing to ensure smooth online operations.
* **Digital Marketing Campaigns:** Planned and executed paid advertising campaigns, tracked performance, and optimized strategies to increase reach and sales.
* **Content Creation & Branding:** Created engaging promotional content, social media creatives, and marketing materials using design tools and AI platforms.
* **SEO & Social Media Management:** Applied basic SEO techniques and managed social media activities to improve brand visibility and customer engagement.
""")

st.divider()

# Projects
st.header("Project Showcase")
st.subheader("Pharmapedia.pk")
st.write("""
Pharmapedia is a healthcare-focused digital platform designed to provide accessible and organized pharmaceutical information. 

* **Creative Project:** Worked on creating a professional digital presence focusing on creative design, content presentation, and user-friendly communication.
* **Design Concept:** Based on a modern healthcare identity, using clean visuals, structured layouts, and informative content to build credibility and connect with users.
""")

st.divider()
st.caption("Thanks for Your Attention. Let's connect and build something great!")
