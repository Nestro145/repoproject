# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 06:59:10 2024

@author: eejeh
"""

import pandas as pd
file = pd.read_csv('C:/Users/eejeh/Desktop/Python_CSS_ project/movie_dataset_1.csv')
df = pd.DataFrame(file)
df.dropna(inplace=True)

#highest rated movie
highest_rated_movie = df.loc[df['Rating'].idxmax()]
print(highest_rated_movie)

#average revenue
average_revenue_of_all_movies = df["Revenue (Millions)"].mean()
print(average_revenue_of_all_movies)

#average revenue from 2015 to 2017
average_revenue_from_2015_to_2017 = df[(df['Year']>=2015)&(df['Year']<=2017)]
average_revenue_of_all_movies_15_17 = average_revenue_from_2015_to_2017["Revenue (Millions)"].mean()
print(average_revenue_of_all_movies_15_17)

#movies released in 2016
movie_releaed_in_2016 =  (file['Year']==2016).sum()
print(movie_releaed_in_2016)

#movies directed by Christopher Nolan

movies_directed_by_Christopher_Nolan = (file['Director']=='Christopher Nolan').sum()
print(movies_directed_by_Christopher_Nolan)

#movies_with_atleast_rating_of_8.0
movies_with_atleast_rating_8 = (file['Rating']>=8.0).sum()
print(movies_with_atleast_rating_8)

#median_of_movies_by_Christopher_Nolan
median_rating_Christopher_Nolan = file[file['Director']=='Christopher Nolan']['Rating'].median()
print(median_rating_Christopher_Nolan)

#Highest_average_rating
year_highest_average_rating = file.groupby('Year')['Rating'].mean().idxmax().max()
print(year_highest_average_rating)


#percentage_increase_of_movies_in 2006_t0_2016
#percentage_increase_in_number_of_movies_in_2006_t0_2016
Number_of_movies_2006 = len(file[file['Year']==2006])
Number_of_movies_2016 = len(file[file['Year']==2016])
percentage_increase_in_number_of_movies_in_2006_t0_2016 = (Number_of_movies_2016-Number_of_movies_2006)*100/Number_of_movies_2006
print(percentage_increase_in_number_of_movies_in_2006_t0_2016)

#most_common_actor
most_common_actor_df = df['Actors'].str.split(',', expand=True).stack().reset_index(level=1, drop=True).to_frame('Actor')
most_common_actor = most_common_actor_df['Actor'].mode().iloc[0]
print(most_common_actor)

#Unique genre
unique_genre = file['Genre'].str.split(',').explode().str.strip()
unique_genre_num = unique_genre.nunique()
print(unique_genre_num)

#correlation
numeric_cols = file.select_dtypes(include=['number']).columns

correlation_matrix = file[numeric_cols].corr()
                     