import streamlit as st
import streamlit as st
import mysql.connector
import pandas as pd
from tabulate import tabulate


#connection to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database="project"
)

mycursor = mydb.cursor()

with st.sidebar:
    st.title(":red [Red bus project]")
    st.header("Skill take away")
    st.caption("Python Selenium")
    st.caption("SQL")
    st.caption("Streamlit")

# Display all bus data 
st.header("All state bus details")

mycursor.execute("SELECT buslink, route, busname, bustype, boardingtime, droppingtime, busrating, busid FROM all_states1")
data = mycursor.fetchall()
df = pd.DataFrame(data, columns=[i[0] for i in mycursor.description])
st.dataframe(df)

# Route filter
route_input = st.text_input("Enter the route name to filter results")

if st.button("Search by Route", key="search_route"):
    if route_input:
        query = "SELECT buslink, route, busname, bustype, boardingtime, droppingtime, busrating, busid FROM all_states1 WHERE route = %s"
        mycursor.execute(query, (route_input,))
        data = mycursor.fetchall()

        if data:
            df = pd.DataFrame(data, columns=[i[0] for i in mycursor.description])
            st.dataframe(df)
        else:
            st.write("No buses found for this route.")
    else:
        st.write("Please enter a route name.")

# Bustype filter
bustype_input = st.text_input("Enter the bus type to filter results")

if st.button("Search by Bus Type", key="search_bustype"):
    if bustype_input:
        query = "SELECT buslink, route, busname, bustype, boardingtime, droppingtime, busrating, busid FROM all_states1 WHERE bustype = %s"
        mycursor.execute(query, (bustype_input,))
        data = mycursor.fetchall()

        if data:
            df = pd.DataFrame(data, columns=[i[0] for i in mycursor.description])
            st.dataframe(df)
        else:
            st.write("No buses found for this bus type.")
    else:
        st.write("Please enter a bus type.")

#busrating filter
busrating_input = st.text_input("Enter the bus rating to filter results")

if st.button("Search by Bus Rating", key="search_busrating"):
    if busrating_input:
        query = "SELECT buslink, route, busname, bustype, boardingtime, droppingtime, busrating, busid FROM all_states1 WHERE busrating = %s"
        mycursor.execute(query, (busrating_input,))
        data = mycursor.fetchall()

        if data:
            df = pd.DataFrame(data, columns=[i[0] for i in mycursor.description])
            st.dataframe(df)
        else:
            st.write("No buses found for this bus rating.")
    else:
        st.write("Please enter a bus rating.")


question = ("1.Why should I use Selenium for scraping instead of other methods?",
           "2.Can Selenium automate clicking on next page buttons or pagination controls?",
           "3.Should I create an SQL table using Python code for this project?",
            "4. Should I use mysql,  sqlite or Postgresql?",
            "5.How do I handle errors and exceptions in Selenium scraping?",
            "6.Can I use other libraries besides Selenium for web scraping?",
            "7.How do we handle changes in the website’s structure?",
            "8.What are the ethical considerations when scraping data from websites like Redbus?",
            "9.How can I deploy the Streamlit application for this project?",
            "10.How to navigate to the next page using Selenium?")

question = st.selectbox("Select Questions",question)
st.write("Selected Question:", question)

if question == "1.Why should I use Selenium for scraping instead of other methods?":

  Answer1 = '''Selenium code is easier to write compared to other languages, and it easily fetches data.'''
  st.write(Answer1)

elif question == "2.Can Selenium automate clicking on next page buttons or pagination controls?":
  Answer2 = '''I wrote the code for the pagination container and next page button '''
  st.write(Answer2)

elif question =='''3.Should I create an SQL table using Python code for this project?''':
  Answer3 = '''My Python code converts the data to a DataFrame, stores it in SQL (using XAMPP), and then creates the table'''
  st.write(Answer3)

elif question == '''4.Should I use mysql,  sqlite or Postgresql?''':
  Answer4 = '''I use XAMMP'''
  st.write(Answer4)

elif question == '''5.How do I handle errors and exceptions in Selenium scraping?''':
  Answer5 = '''I use Python code using try-except blocks'''
  st.write(Answer5)

elif question == '''6.Can I use other libraries besides Selenium for web scraping?''':
  Answer6 = '''I use BeautifulSoup HTML content '''
  st.write(Answer6)

elif question == '''7.How do we handle changes in the website’s structure?''':
  Answer7 = '''Using CSS selectors, XPath ,class name,Tag namre '''
  st.write(Answer7)

elif question == '''8.What are the ethical considerations when scraping data from websites like Redbus?''':
  Answer8 = '''Handle data privacy and security responsibly.'''
  st.write(Answer8)

elif question =='''9.How can I deploy the Streamlit application for this project?''':
  Answer9 ='''I refer to https://docs.streamlit.io/get-started/installation'''
  st.write(Answer9)

elif question == '''10.How to navigate to the next page using Selenium?''':
  Answer10 = '''https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html'''
  st.write(Answer10)

mydb.close()




