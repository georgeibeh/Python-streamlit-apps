import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def financial_analysis():
    st.write("### Financial Analysis")
    st.write("Performing financial analysis...")
    display_multiple_charts()
    st.write("**Insight:** The financial health of the company appears stable based on current metrics.")

def financial_strategy():
    st.write("### Financial Strategy")
    st.write("Developing financial strategy...")
    display_multiple_charts()
    st.write("**Insight:** A diversified investment strategy is recommended for risk management.")

def risk_analysis():
    st.write("### Risk Analysis")
    st.write("Assessing risk factors...")
    display_multiple_charts()
    st.write("**Insight:** Market volatility is currently at a moderate level, requiring close monitoring.")

def predictive_analysis():
    st.write("### Predictive Analysis")
    st.write("Running predictive models...")
    display_multiple_charts()
    st.write("**Insight:** Future revenue projections indicate a steady growth trajectory.")

def about_us():
    st.write("### About Mustard IQ")
    st.write("Mustard IQ is a domain-specific expert tool designed for the Nigerian business landscape.")
    st.write("It leverages Artificial General Intelligence (AGI), financial modeling, and domain expertise to empower decision-makers.")

def homepage():
    st.write("### Welcome to Mustard IQ")
    st.write(
        "Mustard IQ is an AI-powered financial intelligence tool designed specifically for the Nigerian business landscape. "
        "It utilizes Artificial General Intelligence (AGI) concepts, financial modeling, and domain expertise "
        "to provide deep insights for decision-makers."
    )
    ai_agent_chat()

def footer():
    st.markdown("""
    <div style='background-color: #002b5c; padding: 15px; text-align: center; color: white; font-size: 14px;'>
        <b>Contact Information</b> | 📧 support@mustardiq.com | 📍 Lagos, Nigeria | 📞 +234 800 123 4567
    </div>
    """, unsafe_allow_html=True)

def ai_agent_chat():
    st.markdown("""
    <div style='position: fixed; bottom: 80px; right: 20px; background-color: #f0f2f6; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.2); width: 300px;'>
        <b>💬 AI Assistant</b>
        <p>Hello! How can I assist you with financial insights today?</p>
        <input type='text' placeholder='Type a message...' style='width: 100%; padding: 5px; border-radius: 5px; border: 1px solid #ccc;'>
    </div>
    """, unsafe_allow_html=True)

def display_multiple_charts():
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots()
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y, label='Revenue Growth')
        ax.legend()
        st.pyplot(fig)
    with col2:
        fig, ax = plt.subplots()
        categories = ['Stocks', 'Bonds', 'Real Estate', 'Crypto']
        values = [30, 40, 20, 10]
        ax.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
        ax.set_title("Investment Portfolio")
        st.pyplot(fig)
    col3, col4 = st.columns(2)
    with col3:
        fig, ax = plt.subplots()
        pie_labels = ['Q1', 'Q2', 'Q3', 'Q4']
        pie_values = [20, 30, 25, 25]
        ax.pie(pie_values, labels=pie_labels, autopct='%1.1f%%', colors=['blue', 'orange', 'green', 'red'])
        ax.set_title("Quarterly Revenue Distribution")
        st.pyplot(fig)
    with col4:
        fig, ax = plt.subplots()
        x = np.arange(1, 11)
        y = np.random.randint(10, 100, size=10)
        ax.scatter(x, y, color='purple')
        ax.set_title("Risk Exposure")
        st.pyplot(fig)

st.set_page_config(page_title="Mustard IQ", layout="wide")

st.markdown(
    """
    <style>
    .header {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #004d99;
        padding: 20px;
        background-color: #f0f2f6;
        border-bottom: 2px solid #004d99;
    }
    .stSidebar {
        background-color: #f8f9fa !important;
        padding: 20px;
        border-right: 2px solid #d1d1d1;
    }
    .main-content {
        padding: 30px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .footer {
        background-color: #002b5c;
        color: white;
        text-align: center;
        padding: 15px;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown("<div class='header'>📊 Mustard IQ - Financial Intelligence Hub</div>", unsafe_allow_html=True)

st.sidebar.title("📊 Mustard IQ")
st.sidebar.markdown("**A Professional Financial Tool**")

uploaded_file = st.sidebar.file_uploader("Upload a financial document", type=["pdf", "csv", "xlsx"])
if uploaded_file is not None:
    st.sidebar.success("File uploaded successfully!")
    # Placeholder for file processing

selected_category = st.sidebar.radio(
    "Navigation", 
    ["Home", "Financial Analysis", "Financial Strategy", "Risk Analysis", "Predictive Analysis", "About Us"],
    index=0
)

st.markdown("<div class='main-content'>", unsafe_allow_html=True)
if selected_category == "Home":
    homepage()
elif selected_category == "Financial Analysis":
    financial_analysis()
elif selected_category == "Financial Strategy":
    financial_strategy()
elif selected_category == "Risk Analysis":
    risk_analysis()
elif selected_category == "Predictive Analysis":
    predictive_analysis()
elif selected_category == "About Us":
    about_us()
st.markdown("</div>", unsafe_allow_html=True)

footer()
