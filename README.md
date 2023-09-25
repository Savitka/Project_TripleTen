# Project_TripleTen

# URL of my app on Render
https://project-tripleten.onrender.com/

# Running a file locally
Use git to clone project’s git repository to your local machine
call command in terminal: 'streamlit run puth\app.py'

# Loaded Libraries
- streamlit,
- pandas,
- plotly.express

# Exploratory Data Analysis
The directory 'notebooks' contains a file 'EDA.ipynb' with exploratory data analysis:
- dataset information
- checking for empty data
- checking for duplicates
- data grouping by bodystyle
- average price for bodystyle
  Cchart: pie, histogram

# methods in file app.py
- pd.read_csv() - reads the file
- st.checkbox() - show or hide data
- st.table() - Display a static table
- st.write() - displays text
- px.bar(df, x='x', y='y') - creates a histogram
- px.scatter(df, x='x', y='y', color='color') - create scatter plot,
- st.plotly_chart() - Display an interactive Plotly chart
