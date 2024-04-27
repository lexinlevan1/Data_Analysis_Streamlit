# ------ Importing Packages -------
import pandas as pd
import streamlit as st
import matplotlib as plt
import seaborn as sns

# ------ Configuring Main Page -------

st.set_page_config(page_title= 'Average Time Spent By A User On Social Media',
                   page_icon= ':bar_chart:',
                   layout = 'wide')

df = pd.read_csv('dummy_data.csv')

print(df.head(5))

st.title('Data Project 1:')
st.header('Average Time Spent By A User On Social Media')
st.write('by: Lexin Deang')
st.caption('Kaggle Dataset Link : https://www.kaggle.com/datasets/imyjoshua/average-time-spent-by-a-user-on-social-media')

# Replace 'Lifestlye' with Lifestyle due to misspelling
df.replace({'Lifestlye':'Lifestyle'}, inplace = True)


tab1, tab2 = st.tabs(['EDA', 'Visualization'])

# -------- Exploratory Data Analysis --------
with tab1:
    
    st.header('Exploratory Data Analysis')
    
    # ------ Sidebar Creation -------

    profession = st.sidebar.multiselect(
        'Select the profession:',
        options = df['profession'].unique(),
        default = df['profession'].unique()
    )

    location = st.sidebar.multiselect(
        'Select the location:',
        options = df['location'].unique(),
        default = df['location'].unique()
    )

    gender = st.sidebar.multiselect(
        'Select the gender:',
        options = df['gender'].unique(),
        default = df['gender'].unique()
    )

    interests = st.sidebar.multiselect(
        'Select the interests:',
        options = df['interests'].unique(),
        default = df['interests'].unique()
    )

    demographics = st.sidebar.multiselect(
        'Select the demographics:',
        options = df['demographics'].unique(),
        default = df['demographics'].unique()
    )
    # *** Selection ***
    query_multiline = '''
        profession == @profession &
        location == @location &
        gender == @gender &
        interests == @interests &
        demographics == @demographics
    '''

    query_multiline = query_multiline.replace('\n', '')

    # Customized Dataframe Based on selections
    df_selection = df.query(query_multiline)

    st.dataframe(df_selection)



# -------- Visualization --------
with tab2: 

    # ------ Main Page -------
    st.title(':bar_chart: Visualizations')
    st.markdown('###')
    
    profession_str = ', '.join(profession)
    location_str = ', '.join(location)
    gender_str = ', '.join(gender)
    interests_str = ', '.join(interests)
    demographics_str = ', '.join(demographics)
    
    st.markdown(f"""
                 The data refers to the professions of `{profession_str}`\
                     at `{location_str}` who are `{gender_str}`,\
                         who have interests in `{interests_str}`, \
                             under the demographics of\
                                 `{demographics_str}`. """)
            
    average_income = round(df_selection['income'].mean(),1)
    average_time_spent = round(df_selection['time_spent'].mean(), 1)
    total_home_owners = len(df_selection[df_selection['isHomeOwner'] == True])


    left_col, middle_col, right_col = st.columns(3)
    with left_col: 
        st.subheader(':dollar: Income Average')
        st.subheader(f'$ {average_income}')
    with middle_col: 
        st.subheader(':clock2: Average Time Spent')
        st.subheader(f'{average_time_spent} hours')
    with right_col: 
        st.subheader(':house: Homeowners')
        st.subheader(f'{total_home_owners} of {len(df_selection)}')
    
    # -------- Category (5) vs Quantitative Variables --------
    quantitative = st.sidebar.selectbox(
        'What Quantitative Variable do you want to compare each category with?',
        ('Age', 'Time_spent', 'Income'),
        index = 1,
        placeholder = 'Select Numerical Variable...'
    )
    
    st.header(':pushpin: Interactive Charts')
    col1, col2, col3 = st.columns(3)
    
    with col1: 
        
        # Profession vs. User Input
        st.write('\n')
        st.subheader(f'Profession vs. {quantitative}')
        profession_cond = df_selection['profession'].isin(profession)
        profession_df = df_selection[profession_cond]
        profession_df = round(profession_df.groupby('profession')[quantitative.lower()].mean(), 2)

        st.bar_chart(data = profession_df)
    
    with col2: 
        
        # Location vs. User Input
        st.write('\n')
        st.subheader(f'Location vs. {quantitative}')
        location_cond = df_selection['location'].isin(location)
        location_df = df_selection[location_cond]
        location_df = round(location_df.groupby('location')[quantitative.lower()].mean(), 2)
    
        st.bar_chart(data = location_df)
    
    with col3: 
        
        # Gender vs. User Input
        st.write('\n')
        st.subheader(f'Gender vs. {quantitative}')
        gender_cond = df_selection['gender'].isin(gender)
        gender_df = df_selection[gender_cond]
        gender_df = round(gender_df.groupby('gender')[quantitative.lower()].mean(), 2)
        
        st.bar_chart(data = gender_df)
    
    col1, col2 = st.columns(2)
    with col1: 
        
        # Interests vs. User Input
        st.write('\n')
        st.subheader(f'Interests vs. {quantitative}')
        interest_cond = df_selection['interests'].isin(interests)
        interest_df = df_selection[interest_cond]
        interest_df = round(interest_df.groupby('interests')[quantitative.lower()].mean(), 2)
        
        st.bar_chart(data = interest_df)
    with col2:
            
        # Demographics vs. User Input
        st.write('\n')
        st.subheader(f'Demographics vs. {quantitative}')
        demographics_cond = df_selection['demographics'].isin(demographics)
        demographics_df = df_selection[demographics_cond]
        demographics_df = round(demographics_df.groupby('demographics')[quantitative.lower()].mean(), 2)
        
        st.bar_chart(data = demographics_df)
        
        
    