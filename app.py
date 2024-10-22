import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

# Load the dataset
df = pd.read_excel("Heart Disease data.xlsx")

# Changing the column names to more readable form
df.columns = ['age', 'sex', 'chest_pain_type', 'rest_bp_syst', 'chol', 'fbs', 'rest_ecg', 'max_heart_rate',
     'exercise_induced_angina', 'old_peak', 'slope', 'vessels_colored', 'thal', 'target']
    
num_cols = ['age', 'old_peak', 'rest_bp_syst', 'chol', 'max_heart_rate']
cat_cols = ['sex', 'fbs', 'chest_pain_type', 'rest_ecg', 'exercise_induced_angina', 'slope', 'vessels_colored', 'thal', 'target']

for i in cat_cols:
  df[i] = df[i].astype(str)
    
# Univariate analysis    
def univariate_analysis(df):
    st.subheader("Univariate Analysis")
    
    select1 = st.selectbox("Display the report for", ("Numerical Columns", "Categorical Columns"))
    if select1 == 'Numerical Columns':
        summary = df[num_cols].describe().T
        summary.reset_index(inplace=True)
        summary['Skewness'] = summary['index'].map(lambda x: round(df[x].skew(),2))
        summary['Kurtosis'] = summary['index'].map(lambda x: round(df[x].kurt(),2))
    
        # Display summary statistics
        st.write(summary)
    
        # Display visualization
        t=1
        for i in num_cols:
            plt.subplot(3,2,t)
            sns.boxplot(df[i])
            t+=1
        plt.tight_layout()
        st.pyplot(plt)
        
    elif select1 == 'Categorical Columns':
        # Display summary
        description = df[cat_cols].describe()
        st.write(description)
        
        # Display visualization
        plt.figure(figsize=(15,8))
        t=1
        for i in cat_cols:
            plt.subplot(3,3,t)
            df[i].value_counts(normalize=True).plot(kind='pie', autopct='%.1f%%')
            plt.title(i)
            t+=1
        plt.tight_layout()
        st.pyplot(plt)
        
# Bivariate analysis
def bivariate_analysis(df):
    st.subheader("Bivariate Analysis")
    
    select2 = st.selectbox("Display the report for", ("Numerical Columns", "Categorical Columns", "Target vs Numerical Columns"))
    
    if select2 == 'Numerical Columns':
        plt.figure(figsize=(10,5))
        sns.heatmap(df[num_cols].corr(), annot=True, cmap='Greens')
        st.pyplot(plt)
        
    elif select2 == 'Categorical Columns': 
        plt.figure(figsize=(15,8))
        t=1
        for i in cat_cols:
            if i != 'target':
                plt.subplot(3,3,t)
                sns.countplot(data=df, x=i, hue='target')
                plt.title(i)
                t+=1
        plt.tight_layout()
        st.pyplot(plt)
    
    elif select2 == 'Target vs Numerical Columns':
        plt.figure(figsize=(10,5))
        t=1
        for i in num_cols:
            plt.subplot(3,2,t)
            sns.boxplot(data= df, y=i, hue='target')
            plt.title(i)
            t+=1
        plt.tight_layout()
        st.pyplot(plt)  
        

# Insights
def overall_insights():
    st.subheader("Overall Insights")
    st.write("Summary of the entire dataset:")
    
        # Display patient demographics
    st.markdown("### Patient Demographics")
    st.markdown("- The average age of patients is **54 years**, with a minimum of **29 years** and a maximum of **77 years**.")
    st.markdown("- Approximately **70%** of patients are labeled as **sex 1**, likely indicating males.")
    
    # Display clinical measurements
    st.markdown("### Clinical Measurements")
    st.markdown("- The average resting blood pressure is **131 mmHg**, with a maximum of **200 mmHg**, indicating the presence of outliers.")
    st.markdown("- The average maximum heart rate achieved is approximately **150 bpm**, ranging from **71 to 202 bpm**.")
    st.markdown("- Serum cholesterol levels reach as high as **564 mg/dL**, with a mean of **246 mg/dL**, showing outliers and mild skewness.")
    st.markdown("- Fasting blood sugar levels are greater than **120 mg/dL** in about **85%** of the patients.")

    # Display angina and ECG findings
    st.markdown("### Angina and ECG Findings")
    st.markdown("- **49%** of patients experience typical angina, while only **8%** present with asymptomatic chest pain.")
    st.markdown("- Only **1.5%** have resting ECG results classified as **category 2**.")
    st.markdown("- **33%** of patients experience exercise-induced angina.")
    st.markdown("- Majority of heart disease patients belong to **resting ECG category 1**, indicating ST-T wave abnormalities.")

    # Display thalassemia and heart disease insights
    st.markdown("### Thalassemia and Heart Disease")
    st.markdown("- Most patients fall into **categories 2 and 3** for thalassemia.")
    st.markdown("- **51%** of the patients are diagnosed with heart disease.")
    st.markdown("- Three-fourths of heart disease patients do not experience exercise-induced angina.")
    st.markdown("- Most heart patients have **zero major vessels colored** in fluoroscopy; an increase in heart disease count is observed in those with **four vessels colored**.")
    st.markdown("- Type **2 thalassemia** patients have a higher incidence of heart disease.")

    # Display correlation and additional insights
    st.markdown("### Correlation and Insights")
    st.markdown("- Mild positive correlations are observed between age and systolic blood pressure, cholesterol levels, and ST depression.")
    st.markdown("- About **2/3** of female patients have heart disease.")
    st.markdown("- Males with heart disease show higher fasting blood sugar levels compared to females.")
    st.markdown("- Most heart disease patients experience chest pain type **2** (non-anginal pain).")
    st.markdown("- The maximum **old peak** (ST depression) for heart disease patients is **4.2 mV**.")
    st.markdown("- The average maximum heart rate achieved for heart patients is **158 bpm**.")
    st.markdown("- Higher cholesterol levels are found in heart disease patients, with a maximum of **564 mg/dL**.")
        
    
    
st.set_page_config(page_title='EDA Dashboard', layout='wide', page_icon='🔍')

st.title("Welcome to my EDA Dashboard !")
st.subheader("Exploring Data Insights with Visualizations !")
st.write("This dashboard summarizes the EDA on heart disease data.")

type = st.selectbox("Select the required analysis", ("Univariate Analysis", "Bivariate Analysis", "Overall Insights"))

if type == 'Univariate Analysis':
    univariate_analysis(df)
elif type == 'Bivariate Analysis':
    bivariate_analysis(df)
elif type == 'Overall Insights':
    overall_insights()

    