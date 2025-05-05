import streamlit as st

st.markdown("---")
st.markdown("<h3 style='text-align: center;'>Meet Our Team</h3>", unsafe_allow_html=True)

team = [
    {
        "name": "Hadi Mostafa Shaheen",
        "role": "Team Leader",
        "linkedin": r"https://www.linkedin.com/in/hadi-shaheen-06387431b/",
        "image": r"Hadi.jpeg",
        "whatsapp_link":r"https://wa.me/+0201556043211"
    },
    {
        "name": "Mohamed Salah Sarhan",
        "role": "Machine Learning Engineer",
        "linkedin": r"https://www.linkedin.com/in/mohamed-salah-b5b70a298/",
        "image": r"Salah.jpg",
        "whatsapp_link":r"https://wa.me/+201223012460"
    },
    {
        "name": "Mosa Mohamed HossamEldeen",
        "role": "Data Preprocessing Specialist",
        "linkedin": r"https://linkedin.com/in/mosa-placeholderhttps://www.linkedin.com/in/mosa-mohamed-28bbba299/",
        "image": r"Mosa.jpg",
        "whatsapp_link":r"https://wa.me/+0201281030671"
    },
    {
        "name": "Mariem Osama Esmael",
        "role": "Dashboard & Visualization Designer",
        "linkedin": r"https://www.linkedin.com/in/mariam-ismaeil-071417266/",
        "image": r"Mariem.jpg",
        "whatsapp_link":r"https://wa.me/+201201411435"        
    },
    {
        "name": "Nagwa Hamada Atia Khedr",
        "role": "Data Collection & Feature Engineering",
        "linkedin": r"https://www.linkedin.com/in/nagwa-hamada-2b141a339/",
        "image": r"Nagwa.jpg",
        "whatsapp_link":r"https://wa.me/+201005897982"
    },
]

# تقسيم الأعمدة
cols = st.columns(5)

for col, member in zip(cols, team):
    with col:
        st.image(member["image"], width=120)
        st.markdown(f"**{member['name']}**", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size: 14px; color: gray;'>{member['role']}</div>", unsafe_allow_html=True)
        st.markdown(f"[LinkedIn]({member['linkedin']})", unsafe_allow_html=True)
        st.markdown(f"[WhatsApp]({member['whatsapp_link']})",unsafe_allow_html=True)
