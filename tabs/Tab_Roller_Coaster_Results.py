import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
        data_path = "data/coaster_db.csv"
        temps_df = pd.read_csv(data_path, low_memory=False) 
        return temps_df 

def show():
        st.subheader("🔍 Data Analysis")
        st.write("Exploration of the Roller Coaster dataset using Python.")

        df = load_data()
        
        
        st.markdown("""
                        ---
                        ### Describing the dataset
                        """)
        st.write(df.describe())
        
        
        

        st.markdown("""
                        ---
                        ### Seleciting only relevant columns from the dataset
                        
                        ```python
                        # You can do below or just drop columns

                        df = df[['coaster_name', 
                        # 'Length', 'Speed', 
                        'Location', 'Status', 
                        # 'Opening date',
                        # 'Type',
                        'Manufacturer', 
                        # 'Height restriction', 'Model', 'Height',
                        # 'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
                        # 'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
                        # 'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
                        # 'Track layout', 'Fastrack available', 'Soft opening date.1',
                        # 'Closing date', 
                        # 'Opened', 
                        # 'Replaced by', 'Website',
                        # 'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
                        # 'Single rider line available', 'Restraint Style',
                        # 'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
                        'year_introduced', 'latitude', 'longitude', 'Type_Main',
                        'opening_date_clean', 
                        # 'speed1', 'speed2', 'speed1_value', 'speed1_unit',
                        'speed_mph', 
                        # 'height_value', 'height_unit', 
                        'height_ft',
                        'Inversions_clean', 'Gforce_clean']].copy() #Copy makes python know its brand new dataframe and not just reference to old one
                        
                        ```
                        """)
        
        df = df[['coaster_name', 
                        # 'Length', 'Speed', 
                        'Location', 'Status', 
                        # 'Opening date',
                        # 'Type',
                        'Manufacturer', 
                        # 'Height restriction', 'Model', 'Height',
                        # 'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
                        # 'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
                        # 'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
                        # 'Track layout', 'Fastrack available', 'Soft opening date.1',
                        # 'Closing date', 
                        # 'Opened', 
                        # 'Replaced by', 'Website',
                        # 'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
                        # 'Single rider line available', 'Restraint Style',
                        # 'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
                        'year_introduced', 'latitude', 'longitude', 'Type_Main',
                        'opening_date_clean', 
                        # 'speed1', 'speed2', 'speed1_value', 'speed1_unit',
                        'speed_mph', 
                        # 'height_value', 'height_unit', 
                        'height_ft',
                        'Inversions_clean', 'Gforce_clean']].copy()
        
        st.markdown("""
                        ---
                        ### Converting column 'opening_date_time' to datetime format
                        
                        ```python
                        df['opening_date_clean'] = pd.to_datetime(df['opening_date_clean'])
                        ```
                        """)
        
        df['opening_date_clean'] = pd.to_datetime(df['opening_date_clean'])
        
        
        st.markdown("""
                        ---
                        ### Renaming column

                        """)
        
        df = df.rename(columns={'coaster_name':'Coaster_Name',
                        'year_introduced': 'Year_Introduced',
                        'latitude': 'Latitude',
                        'longitude': 'Longitude',
                        'opening_date_clean': 'Opening_Date',
                        'speed_mph': 'Speed_mph',
                        'height_ft': 'Height_ft',
                        'Inversions_clean': 'Inversions',
                        'Gforce_clean': 'Gforce'})
        st.write(df)

        st.markdown("""
                        ---
                        ### Sum of columns
                        """)
        
        st.write(df.isna().sum())
        
        

        st.markdown("""
                        ---
                        ### Check for duplicates in column 'Coaster_Name'
                        """)
        st.write(df.loc[df.duplicated(subset=['Coaster_Name'])])
        
        
        st.markdown("""
                        ---
                        ### Checking an example duplicate
                        """) 
        st.write(df.query('Coaster_Name=="Crystal Beach Cyclone"'))
        
        
        st.markdown("""
                        ---
                        ### Removing duplicates
                        
                        ```python
                        df = df.loc[~df.duplicated(subset=['Coaster_Name', 'Location', 'Opening_Date'])]\
                        .reset_index(drop=True).copy()  
                        ```
                        """)
        df = df.loc[~df.duplicated(subset=['Coaster_Name', 'Location', 'Opening_Date'])]\
        .reset_index(drop=True).copy()    
        
        
        
        st.markdown("""
                        ---
                        ### Feature understanding (AKA Univariate Analysis)
                        """)
        st.write(df['Year_Introduced'].value_counts())   
        
        
        st.markdown("""
                        ---
                        ### Count of coasters introduced by year
                        """)

        ax = df['Year_Introduced'].value_counts().head(10).plot(
        kind='barh',
        title='Top Years Coasters Introduced',
        figsize= (10,5)
        )

        ax.set_ylabel('Year Introduced')
        ax.set_xlabel('Count')

        st.pyplot(plt.gcf())
        plt.clf()
        
        
        
        st.markdown("""
                        ---
                        ### Distribution of the speed of roller coasters
                        """)
        
        ax = df['Speed_mph'].plot(
        kind='hist',
        bins=20,
        title='Coaster Speed (mph)',
        figsize= (10,5)
        )

        ax.set_xlabel('Speed (mph)')

        st.pyplot(plt.gcf())
        plt.clf()
        
        
        st.markdown("""
                        ---
                        ### Distribution of the speed of roller coasters
                        """)
        
        ax = df['Speed_mph'].plot(
        kind='kde',
        title='Coaster Speed (mph)',
        figsize= (10,5)
        )

        ax.set_xlabel('Speed (mph)')

        st.pyplot(plt.gcf())
        plt.clf()
        
        
        st.markdown("""
                        ---
                        ### Coaster Speed vs Height
                        """)
        
        df.plot(kind='scatter', 
        x='Speed_mph', 
        y='Height_ft',
        title = 'Coaster Speed vs Height',
        figsize= (10,5))

        st.pyplot(plt.gcf())
        plt.clf()
        
        
        st.markdown("""
                        ---
                        ### Coaster Speed vs Height
                        """)
        
        plt.figure(figsize=(10, 5))
        
        sns.scatterplot(
        x='Speed_mph', 
        y='Height_ft',
        hue = 'Year_Introduced',
        data = df)

        st.pyplot(plt.gcf())
        plt.clf()


        st.markdown("""
                        ---
                        ### Pairplot of features
                        """)
        
        sns.pairplot(data=df, 
        vars=['Year_Introduced', 'Speed_mph', 'Height_ft', 'Inversions', 'Gforce'],
        hue= 'Type_Main',
        height=1.5,
        aspect=1.5)

        st.pyplot(plt.gcf())
        plt.clf()
        
        
        st.markdown("""
                        ---
                        ### Correlation between the features
                        """)
        
        df_corr = df[['Year_Introduced', 'Speed_mph', 'Height_ft', 'Inversions', 'Gforce']].dropna().corr()
        
        plt.figure(figsize=(10, 5))
        
        sns.heatmap(df_corr, annot= True)

        st.pyplot(plt.gcf())
        plt.clf()