# Import our Pkgs
import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as sns
from PIL import Image,ImageFilter,ImageEnhance


def main():

	# Title and Subheader
	st.title("Iris Dataset EDA App")
	st.subheader("EDA Web App with Streamlit ")

	DATA_URL = ('https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv')

	@st.cache(persist=True, show_spinner=True)
	def load_data():
	    data = pd.read_csv(DATA_URL)
	    data.columns = ('sepal_length','sepal_width','petal_length','petal_width','species')
	    # lowercase = lambda x: str(x).lower()
	    # data.rename(lowercase, axis='columns', inplace=True)
	    # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
	    return data

	# Create a text element and let the reader know the data is loading.
	data_load_state = st.text('Loading data...')
	# Load 10,000 rows of data into the dataframe.
	data = load_data()
	# Notify the reader that the data was successfully loaded.
	data_load_state.text('Loading data...Completed!')


	# Show Dataset
	# if st.checkbox("Preview DataFrame: Head or Tail"):
		
	#	if st.button("Head"):
	#		st.write(data.head())
	#	if st.button("Tail"):
	#		st.write(data.tail())

	# Show Entire Dataframe
	if st.checkbox("View DataFrame"):
		st.dataframe(data)

			# Show Description
	if st.checkbox("View All Column Names"):
		st.text("Columns:")
		st.write(data.columns)

	# Dimensions - Radio Buttonss
	# data_dim = st.radio('Check the dimensions of the dataframe',('Rows','Columns'))
	# if data_dim == 'Rows':
	#	st.write("There are", len(data), "Rows in the dataset")
	# if data_dim == 'Columns':
	#	st.write("There are", data.shape[1], "Columns in the dataset")


	if st.checkbox("Show Summary of Dataset"):
		st.write(data.describe())
		st.write("There are", len(data), "rows and",data.shape[1], "columns in the dataset")


	# Selection

	if st.checkbox("View Single Column's Data"):

		species_option = st.selectbox('Select Columns',('sepal_length','sepal_width','petal_length','petal_width','species'))
		if species_option == 'sepal_length':
			st.write(data['sepal_length'])
		elif species_option == 'sepal_width':
			st.write(data['sepal_width'])
		elif species_option == 'petal_length':
			st.write(data['petal_length'])
		elif species_option == 'petal_width':
			st.write(data['petal_width'])
		elif species_option == 'species':
			st.write(data['species'])
		else:
			st.write("Select A Column")

	# Show Plots
	if st.checkbox("Show Plots"):
		st.write("_"*10)
		data.plot(kind='scatter', x='sepal_length', y='sepal_width')
		st.pyplot()
		st.write("---------------- 2D Scatter Plot of Sepal_length vs Sepal_width for all the Species ---------------- ")
		st.write("_"*10)
		st.write(sns.pairplot(data, hue="species", size=3))
		# Use Matplotlib to render seaborn
		st.pyplot()
		st.write("---------------- Pairplot of different species ----------------")
		st.write("_"*10)

		
		v_counts = data.groupby('species')
		st.bar_chart(v_counts)
		st.write("---------------- Bar Plot of Groups or Counts ----------------")
		st.write("_"*10)


	# Iris Image Manipulation
	@st.cache
	def load_image(img):
		im =Image.open(os.path.join(img))
		return im

	# Image Type
	if st.checkbox("Show/Hide Images"):

		species_type = st.radio('Have a look at the images of different Iris Species!',('Setosa','Versicolor','Virginica'))

		if species_type == 'Setosa':
			st.text("Showing Setosa Species")
			my_image = load_image('images/setosa.png')
		elif species_type == 'Versicolor':
			st.text("Showing Versicolor Species")
			my_image = load_image('images/versicolor.png')
		elif species_type == 'Virginica':
			st.text("Showing Virginica Species")
			my_image = load_image('images/virginica.png')

		if st.checkbox("Enhance Image"):

			enh = ImageEnhance.Contrast(my_image)
			num = st.slider("Contrast",1.0,2.0)
			img_width = st.slider("Zoom in the Image (Set Image Width in Pixels)",300,700)
			st.image(enh.enhance(num),width=img_width)
		else:
			img_width = 300
			num = 1.2
			enh = ImageEnhance.Contrast(my_image)
			st.image(enh.enhance(num),width=img_width)


	# About

	if st.button("About App"):
		st.subheader("Iris Dataset EDA App - Developed by Deepankar Kotnala")
		st.text("Built with Streamlit")


if __name__ == "__main__":
    main()


