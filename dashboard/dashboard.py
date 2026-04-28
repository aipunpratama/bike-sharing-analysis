import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. PAGE SETUP & CONFIGURATION
st.set_page_config(
    page_title="Bike Sharing Analytics",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded"
)

sns.set_theme(style="white")

# 2. LOAD DATA
current_dir = os.path.dirname(os.path.abspath(__file__))

@st.cache_data
def load_data():
    day_path = os.path.join(current_dir, "day_cleaned.csv")
    hour_path = os.path.join(current_dir, "hour_cleaned.csv")
    
    day_df = pd.read_csv(day_path)
    hour_df = pd.read_csv(hour_path)
    
    return day_df, hour_df

# 3. SIDEBAR
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2972/2972185.png", width=100)
    st.title("⚙️ Data Filters")
    st.markdown("Use the filters below to adjust the charts:")
    
    # Year Filter
    year_options = ["All Years"] + list(day_df['yr'].unique())
    selected_year = st.selectbox("📅 Select Year:", year_options)
    
    # Season Filter
    season_options = ["All Seasons"] + list(day_df['season'].unique())
    selected_season = st.selectbox("🍂 Select Season:", season_options)
    
    st.markdown("---")
    st.caption("© 2026 by Data Analyst")

# 4. DYNAMIC DATA PREPROCESSING
filtered_day = day_df.copy()
filtered_hour = hour_df.copy()

# Apply Year filter if not selecting "All Years"
if selected_year != "All Years":
    filtered_day = filtered_day[filtered_day['yr'] == selected_year]
    filtered_hour = filtered_hour[filtered_hour['yr'] == selected_year]

# Apply Season filter if not selecting "All Seasons"
if selected_season != "All Seasons":
    filtered_day = filtered_day[filtered_day['season'] == selected_season]
    filtered_hour = filtered_hour[filtered_hour['season'] == selected_season]

# 5. HEADER & METRICS
st.title("🚲 Interactive Bike Sharing Dashboard")
st.markdown("Explore bike rental data dynamically based on your selected filters.")

total_rentals = filtered_day['cnt'].sum()
total_casual = filtered_day['casual'].sum()
total_registered = filtered_day['registered'].sum()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Bike Rentals", value=f"{total_rentals:,}")
with col2:
    st.metric("Total Casual Users", value=f"{total_casual:,}")
with col3:
    st.metric("Total Registered Users", value=f"{total_registered:,}")

st.markdown("---")

# 6. DATA VISUALIZATION
tab1, tab2 = st.tabs(["🌤️ Weather Impact (Select Hour)", "📅 Day Type Comparison"])

# TAB 1: Business Question 1
with tab1:
    st.subheader(f"Weather Impact on Bike Rentals ({selected_year} - {selected_season})")
    
    unique_hours = list(filtered_hour['hour_category'].unique())
    hour_options = ["All Hours"] + unique_hours
    selected_hour = st.radio("⏳ Display data for:", hour_options, horizontal=True)

    q1_data = filtered_hour.copy()
    if selected_hour != "All Hours":
        q1_data = q1_data[q1_data['hour_category'] == selected_hour]

    if q1_data.empty:
        st.warning("⚠️ No data available for this filter combination.")
    else:
        q1_plot = q1_data.groupby(by='weathersit')['cnt'].sum().reset_index()

        fig_col1, text_col1 = st.columns((2, 1))
        with fig_col1:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(x='weathersit', y='cnt', data=q1_plot, palette='Blues_r', ax=ax)
            ax.set_title(f'Total Rentals by Weather ({selected_hour})', fontsize=14, fontweight='bold')
            ax.set_xlabel('Weather Condition', fontsize=12)
            ax.set_ylabel('Total Rentals', fontsize=12)
            st.pyplot(fig)
            
        with text_col1:
            st.info("**Interactive Insight:**")
            st.write("Try changing the **Hour Category** option above. You will see that during **Rush Hour**, the rental gap between clear and bad weather is much larger than during Non-Rush Hour.")

# TAB 2: Business Question 2 (Dynamic) 
with tab2:
    st.subheader(f"User Comparison: Working Day vs Holiday ({selected_year} - {selected_season})")
    
    weather_options = ["All Weather"] + list(filtered_day['weathersit'].unique())
    selected_weather_t2 = st.selectbox("🌤️ Select Weather Condition:", weather_options, key='weather_tab2')
    
    q2_data = filtered_day.copy()
    if selected_weather_t2 != "All Weather":
        q2_data = q2_data[q2_data['weathersit'] == selected_weather_t2]
    
    if q2_data.empty:
        st.warning("⚠️ No data available for this filter combination.")
    else:
        q2_result = q2_data.groupby(by='workingday').agg({
            'casual': 'sum',
            'registered': 'sum'
        }).reset_index()
        
        q2_melted = q2_result.melt(
            id_vars='workingday', 
            value_vars=['casual', 'registered'],
            var_name='User Type', 
            value_name='Total Users'
        )

        fig_col2, text_col2 = st.columns((2, 1))
        with fig_col2:
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            sns.barplot(
                x='workingday', 
                y='Total Users', 
                hue='User Type', 
                data=q2_melted, 
                palette=['#FFA07A', '#20B2AA'], 
                ax=ax2
            )
            ax2.set_title(f'Casual vs Registered Users ({selected_weather_t2})', fontsize=14, fontweight='bold')
            ax2.set_xlabel('Day Type', fontsize=12)
            ax2.set_ylabel('Total Users', fontsize=12)
            st.pyplot(fig2)

        with text_col2:
            st.success("**Interactive Insight:**")
            st.write("""
            Try changing the **Weather Condition** option to *Light Rain/Snow* or *Severe Weather*. 
            
            You will notice an interesting pattern: in bad weather, **Casual** users (usually active on holidays) almost disappear, leaving mostly **Registered** users who still ride due to daily mobility needs.
            """)
