#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Smartwatch Data Analysis using Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from plotly import graph_objs as go


# In[7]:


data = pd.read_csv("C:\\Users\\Asus\\OneDrive\\Desktop\\smartwatch\\dataset\\dailyActivity_merged.csv")
print(data.head())


# In[8]:


#a look at whether this dataset has any null values or not
print(data.isnull().sum())


# In[9]:


#Let’s have a look at the information about columns in the dataset
print(data.info())


# In[43]:


#chaging datatype of  activitydate
data["ActivityDate"] = pd.to_datetime(data["ActivityDate"], format="%m/%d/%Y")
print(data.info())


# In[10]:


data["TotalMinutes"] = data["VeryActiveMinutes"] + data["FairlyActiveMinutes"] + data["LightlyActiveMinutes"] + data["SedentaryMinutes"]
print(data["TotalMinutes"].sample(5))


# In[11]:


print(data.describe())


# In[12]:


#the relationship between calories burned and the total steps walkel in a day
figure = px.scatter(data_frame = data, x="Calories",
                    y="TotalSteps", size="VeryActiveMinutes", 
                    trendline="ols", 
                    title="Relationship between Calories & Total Steps")
figure.show()


# In[16]:


#The average total number of active minutes in a day
label = ["Very Active Minutes", "Fairly Active Minutes", 
         "Lightly Active Minutes", "Inactive Minutes"]
counts = data[["VeryActiveMinutes", "FairlyActiveMinutes", 
               "LightlyActiveMinutes", "SedentaryMinutes"]].mean()
colors = ['gold','green', "Sapphire", "purple"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Total Active Minutes')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[19]:


data["ActivityDate"] = pd.to_datetime(data["ActivityDate"])
data["Day"] = data["ActivityDate"].dt.day_name()
print(data["Day"].head())


# In[20]:


#the very active , fairly active and lightly active minutes on each day of the week
fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["Day"],
    y=data["VeryActiveMinutes"],
    name='Very Active',
    marker_color='purple'
))
fig.add_trace(go.Bar(
    x=data["Day"],
    y=data["FairlyActiveMinutes"],
    name='Fairly Active',
    marker_color='green'
))
fig.add_trace(go.Bar(
    x=data["Day"],
    y=data["LightlyActiveMinutes"],
    name='Lightly Active',
    marker_color='pink'
))
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()


# In[21]:


#number of inactive minutes on each day of the week
day = data["Day"].value_counts()
label = day.index
counts = data["SedentaryMinutes"]
colors = ['#1E1F26','lightgreen', "pink", "blue", "skyblue", "cyan", "purple"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Inactive Minutes Daily')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[22]:


# the number of Calories on each day of week
calories = data["Day"].value_counts()
label = calories.index
counts = data["Calories"]
colors = ['#2A5084','#4C5F76', "#F7A851", "tone", "#697217", "tint", "shade"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Calories Burned Daily')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[ ]:


#tuesday is one of the most active days for all individuals in thr dataset, as the highest of calories were burned on tuesdays

