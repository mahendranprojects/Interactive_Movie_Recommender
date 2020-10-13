import streamlit as st
from recommender import recommender

st.set_option("deprecation.showfileUploaderEncoding", False)

st.markdown('<style>body{color: black ; text-align: center;}</style>',unsafe_allow_html=True)

st.title("MOVIE RECOMMENDER")
st.write("")
st.header("Content Based Recommender System")
st.subheader("The system recommends movies on the basis  the movies liked by user and the ratings for the movies")
st.write("")
st.write("")
st.write("Enter movie names and rating (both likes and dislikes) in the side panel to build your profile.")
st.write("")
st.write("")
st.write("")

st.sidebar.markdown("")

userLikes=[]
n=st.sidebar.number_input("How many movies do you want to enter?",value=0)
i=0
while i<n:
    movies={}
    movie=st.sidebar.text_input("Movie Title",key=i)
    rating=st.sidebar.slider("Rating",min_value=0.01,max_value=5.01,key=i)
    movies["title"]=movie.lower()
    movies["rating"]=rating
    userLikes.append(movies)
    i+=1

st.sidebar.markdown("")
st.sidebar.markdown("")
year=st.sidebar.text_input("Do you want movies after a specific year, if yes, mention the year?",value=1900)
noOfMovies=st.sidebar.number_input("How many movies do you want?",value=10)

if st.sidebar.button("Press for Recommendations",key=1):
    recommended=recommender(userLikes,year,noOfMovies)
    st.write(recommended)
