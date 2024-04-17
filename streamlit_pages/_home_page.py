import streamlit as st
from config import BANNER

def home_page():
    st.image(BANNER)
    st.write("""
        <style>
        .purple-text {
            color: #2d0042;
        }
        </style>
        ## <span class="purple-text">Introduction to Alzheimer's Disease </span>
        Alzheimer's disease (AD) is a progressive neurodegenerative disease. Though best known for its role in declining memory function, symptoms also include: difficulty thinking and reasoning, making judgements and decisions, and planning and performing familiar tasks. It may also cause alterations in personality and behavior. The cause of AD is not well understood. There is thought to be a significant hereditary component. For example, a variation of the APOE gene, APOE e4, increases risk of Alzheimer's disease.

        ## <span class="purple-text">Why Early Detection Matters </span>
        Early detection of Alzheimer's disease is paramount because it offers the best chance for effective treatment and improved quality of life. Identifying the condition at its onset allows for timely interventions, which can slow its progression and enable individuals and their families to plan for the future. Early detection also facilitates access to support services and clinical trials, fostering hope for more effective therapies in the fight against this devastating disease.

        ## <span class="purple-text">Purpose of the project </span>
        The purpose of this project proposal is to develop a machine learning model for the early prediction of Alzheimer's disease. Alzheimer's disease is a devastating neurodegenerative disorder that affects millions of individuals worldwide. Early detection is crucial for better patient care and the development of potential interventions. This project aims to leverage machine learning techniques to create a predictive model that can identify individuals at risk of Alzheimer's disease based on relevant data.
        
        <br>
                
        """, unsafe_allow_html=True)

    st.caption('Finished reading? Navigate to the `Prediction Page` to make some predictions')
