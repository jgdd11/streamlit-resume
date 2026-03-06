import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📄 Interactive Resume")

st.header("John Dion")
st.write("Aspiring Data Scientist | Sports Analytics | Machine Learning")

st.write("""
Welcome to my interactive resume. Use the widgets to explore my skills,
experience, and projects.
""")

# -------------------------
# Interactive Widget 1
# -------------------------
st.sidebar.header("Filters")

experience_years = st.sidebar.slider(
    "Minimum Years of Experience",
    0, 10, 2
)

# -------------------------
# Skills Table
# -------------------------
st.header("💻 Skills")

skills = pd.DataFrame({
    "Skill": ["Python", "SQL", "Machine Learning", "Data Visualization", "Streamlit"],
    "Proficiency (%)": [90, 85, 80, 85, 75]
})

st.table(skills)

# -------------------------
# Chart
# -------------------------
st.header("📊 Skill Proficiency Chart")

fig, ax = plt.subplots()
ax.bar(skills["Skill"], skills["Proficiency (%)"])
ax.set_ylabel("Proficiency (%)")
ax.set_title("Skill Levels")

st.pyplot(fig)

# -------------------------
# Interactive Widget 2
# -------------------------
st.header("📁 Projects")

projects = {
    "Hockey Tracking Analytics": "Built models using player tracking data to analyze zone entries.",
    "Reinforcement Learning Hockey Strategy": "Used supervised Q-learning to evaluate offensive decisions.",
    "Sports Data Dashboard": "Created interactive dashboards to visualize player performance."
}

selected_project = st.selectbox(
    "Select a Project",
    list(projects.keys())
)

st.write(projects[selected_project])

# -------------------------
# Interactive Widget 3
# -------------------------
st.header("💼 Work Experience")

experience = pd.DataFrame({
    "Company": ["Sports Analytics Lab", "Data Science Internship", "Research Assistant"],
    "Role": ["Analytics Researcher", "Data Analyst Intern", "Sports Data Analyst"],
    "Years Experience": [2, 1, 1]
})

if st.checkbox("Show Work Experience"):
    filtered_exp = experience[experience["Years Experience"] >= experience_years]
    st.dataframe(filtered_exp)

# -------------------------
# Education Table
# -------------------------
st.header("🎓 Education")

education = pd.DataFrame({
    "Institution": ["University"],
    "Degree": ["BSc Data Science"],
    "Year": ["2026"]
})

st.table(education)

st.write("📧 Contact: johnguydion@email.com")