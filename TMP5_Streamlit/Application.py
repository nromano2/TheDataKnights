""" 
Team Mini Project 5: Streamlit Web Application
Team: TheDataKnights
Team Members: Nick Romano, Michael Zelaya
DS-400 Data Science Sentior Capstone
Streamlit Wine Data Web Application
"""
#Importing Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

#Reading in red and white wine datasets. Have to use seperator keyword since the csv files have semicolon seperators
redWine_df = pd.read_csv("winequality-red.csv", sep=";")
whiteWine_df = pd.read_csv("winequality-white.csv", sep=";")

#Adding a color column
redWine_df.insert(0,"color","red")
whiteWine_df.insert(0,"color","white")

#Adding a underscore to the columns with spaces
redWine_df.rename(columns = {'fixed acidity':'fixed_acidity', 
                             'volatile acidity':'volatile_acidity', 
                             'citric acid':'citric_acid', 
                             'residual sugar':'residual_sugar', 
                             'free sulfur dioxide':'free_sulfur_dioxide', 
                             'total sulfur dioxide':'total_sulfur_dioxide'}, 
                  inplace=True)

whiteWine_df.rename(columns = {'fixed acidity':'fixed_acidity', 
                               'volatile acidity':'volatile_acidity', 
                               'citric acid':'citric_acid', 
                               'residual sugar':'residual_sugar',
                               'free sulfur dioxide':'free_sulfur_dioxide', 
                               'total sulfur dioxide':'total_sulfur_dioxide'}, 
                    inplace=True)

#Combining the two winequality datasets
combinedWine = pd.concat([redWine_df, whiteWine_df])

#Overall title of web application
st.title("Wine Quality Viewer")

#The following line assignes a variable name to one of the tabs for the diffferent pages that the user can select.
#Assigning a variable to each of the tabs enables us to use the with keyword to add elements to each tab
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["MetaData", "Data", "Color", "Quality", "Scatter", "Box", "Classification"])

with tab1: #Metadata Tab - creating a summary/descripton table of the data included in the dataset
#The followig code for the metadata tab creates a header for the tab. The creates a dictionary of the metaData information, which includes the column name, the variable role (feature/output), the type of variable, and the demogrphic, descripton, units, value_count and missing value count of each column. The metaData dictionary is then converted from a dictionary to a dataframe. Finally the dataframe is displayed to the application.
    
    st.header("Meta Data")
    
    metaData = {"name": ['color', 'fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',  'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality'],
                
                "role": ['feature', 'feature', 'feature', 'feature', 'feature', 'feature', 'feature', 'feature', 'feature', 'feature', 'feature', 'feature', 'output'],
                
                "type": ['Categorical, Nominal', 'Continous, Ratio', 'Continous, Ratio', 'Continous, Ratio', 'Continous, Ratio', 'Continous, Ratio', 'Continous, Ratio', 'Continous, Ratio', 'Continous, Ratio', 'Continous, Ratio', 'Continous, Ratio','Continous, Ratio', 'Categorocal, Ordinal'],
                
                "demographic": [None, None, None, None, None, None, None, None, None, None, None, None, None],
                
                "description": [None, None, None, None, None, None, None, None, None, None, None, None, None],
                
                "units": [None, None, None, None, None, None, None, None, None, None, None, None, None],
                
                "value_count": [len(combinedWine.color), len(combinedWine.fixed_acidity), len(combinedWine.volatile_acidity), len(combinedWine.citric_acid), len(combinedWine.residual_sugar), len(combinedWine.chlorides), len(combinedWine.free_sulfur_dioxide), len(combinedWine.total_sulfur_dioxide), len(combinedWine.density), len(combinedWine.pH), len(combinedWine.sulphates), len(combinedWine.alcohol), len(combinedWine.quality)],
                
                "missing_values": [combinedWine.color.isna().sum(), combinedWine.fixed_acidity.isna().sum(), combinedWine.volatile_acidity.isna().sum(), combinedWine.citric_acid.isna().sum(), combinedWine.residual_sugar.isna().sum(), combinedWine.chlorides.isna().sum(), combinedWine.free_sulfur_dioxide.isna().sum(), combinedWine.total_sulfur_dioxide.isna().sum(), combinedWine.density.isna().sum(), combinedWine.pH.isna().sum(), combinedWine.sulphates.isna().sum(), combinedWine.alcohol.isna().sum(), combinedWine.quality.isna().sum()]}

    metaDataFrame = pd.DataFrame(data=metaData)
    st.dataframe(metaDataFrame)

with tab2: #Dataset Viewer Tab - allows the user to see portions or all of the dataset
    
#The following code for the Dataset View tab creates the header for the page, then creates a selection list using the .radio method which allows the user to check one of the available options at a time and the section is stored under the DataSelection variable. 
    st.header("Data Set Veiwer")
    DataSelection = st.radio("Choose DataSet Veiw", ["Chemical", "Alcohol", "Quality", "All"])

#The If-elif-else statement displays the portion of the dataset that the user has selected to see. If user chooses chemical, the color and chemical-related columns will be displayed. If the user chooses Alcohol, the color and alcohol column will be displayed #If the user chooses Quality, then the color and qualiry columns will be displayed. #With 'All' being the only other selection, if all is selected the entire dataframe will be displayed
    if DataSelection == "Chemical":
        st.dataframe(combinedWine[['color', 'fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide',  'total_sulfur_dioxide', 'density', 'pH', 'sulphates']])

    elif DataSelection == "Alcohol":
        st.dataframe(combinedWine[['color', 'alcohol']])

    elif DataSelection == "Quality":
        st.dataframe(combinedWine[['color', 'quality']])

    else:
        st.dataframe(combinedWine)


with tab3:#Color Tab - Shows the distribution of red and white wine through a bar chart
    
#The following code sets the tab page header to Color Distribution, and creates a bar chart of the value coounts of the color column
    st.header("Color Distribution")
    st.bar_chart(combinedWine.color.value_counts())


with tab4: #Quality Tab - Shows the distribution of the number of wines per quality level
    st.header("Quality Distribution") #Page Header
    st.bar_chart(combinedWine.quality.value_counts()) #Creates a bar chart resembling a historgram for the quality distribution


with tab5: #Scatter Tab - Shows a scatterplot of two of the continuous variables that the user selects.
#The following code creates the header for the Scatter Tab page as 'Scatter Plots'.
    st.header("Scatter Plots")

#A checkbox list is created with the various continous variables for which the user can select from, which in turn are the selections that form the scatter plot. 
    fixed_acidity_scatter = st.checkbox('fixed_acidity') 
    volatile_acidity_scatter = st.checkbox('volatile_acidity')
    citric_acid_scatter = st.checkbox('citric_acid')
    residual_sugar_scatter = st.checkbox('residual_sugar')
    chlorides_scatter = st.checkbox('chlorides')
    free_sulfur_dioxide_scatter = st.checkbox('free_sulfur_dioxide')
    total_sulfur_dioxide_scatter = st.checkbox('total_sulfur_dioxide')
    density_scatter = st.checkbox('density')
    pH_scatter = st.checkbox('pH')
    sulphates_scatter = st.checkbox('sulphates')
    alcohol_scatter = st.checkbox('alcohol')

#The boxBooleans list stores the boolean value of whether or not a given checkbox has been checked or not. True if selected, otherwise False. This would allow us to know which checkboxes the user had selected.
    boxBooleans = [bool(fixed_acidity_scatter), 
                   bool(volatile_acidity_scatter), 
                   bool(citric_acid_scatter), 
                   bool(residual_sugar_scatter), 
                   bool(chlorides_scatter), 
                   bool(free_sulfur_dioxide_scatter), 
                   bool(total_sulfur_dioxide_scatter), 
                   bool(density_scatter), 
                   bool(pH_scatter), 
                   bool(sulphates_scatter), 
                   bool(alcohol_scatter)]

#The boxPositionDictionary contians the index positions of the continious variable columns within the boxBooleans list. This dictionary allows us to grab the text of the column name if the user ends up checking the columns corresponding box. 
    boxPositionDictionary = {0:'fixed_acidity', 
                             1:'volatile_acidity', 
                             2:'citric_acid', 
                             3:'residual_sugar', 
                             4:'chlorides', 
                             5:'free_sulfur_dioxide', 
                             6:'total_sulfur_dioxide', 
                             7:'density', 
                             8:'pH', 
                             9:'sulphates', 
                             10:'alcohol'}

#The if-else statement, ensures that the user selects exactly two checkboxes. It checks for two checked checkboxes by taking the sum of the boxBooleans list. If there are exactly 2 checkboxes selected it would sum to 2, since individual TRUE values sum to 1. If the sum is not 2, then we know that there are either 0-1 or 3-11 checkboxes are selected (in this scenario where more or less than 2 boxes are selected an error message appears). In the case where exactly 2 boxes are selected, np.where(boxBooleans) grabs the index positions of the TRUE values. Then x and y are used to search the string representation of the column name. Finally the scatter plot is formed. 
    if sum(boxBooleans) == 2:
        x, y = boxPositionDictionary.get(np.where(boxBooleans)[0][0]), boxPositionDictionary.get(np.where(boxBooleans)[0][1])
        st.scatter_chart(data=combinedWine, x=x,y=y)
        
    else:
        st.write(f"It seems that you have selected {sum(boxBooleans)} box(es). To create a scatterplot, exactly 2 boxes need to be selected.")


with tab6: #Boxplot tab - Provides a checklist of the continous variables and allows the user to select one to show its boxplot. 

#The following code creates the header for the Boxplot Tab page as 'Box Plots'.
    st.header("Box Plots")

#Then a checkbox list is created with the various continous variables for which the user can select from, which in turn forms a box plot. [NOTE: checkboxes with the same item names the checkboxes have to have different keys, that is why there are key parameters for each st.checkbox() methods.]
    fixed_acidity_box = st.checkbox('fixed_acidity', key = "fixed_acidity_boxplot_checkbox")
    volatile_acidity_box = st.checkbox('volatile_acidity', key = "volatile_acidity_boxplot_checkbox")
    citric_acid_box = st.checkbox('citric_acid', key = "citric_acid_boxplot_checkbox")
    residual_sugar_box = st.checkbox('residual_sugar', key = "residual_sugar_boxplot_checkbox")
    chlorides_box = st.checkbox('chlorides', key = "chlorides_boxplot_checkbox")
    free_sulfur_dioxide_box = st.checkbox('free_sulfur_dioxide', key = "free_sulfur_dioxide_boxplot_checkbox")
    total_sulfur_dioxide_box = st.checkbox('total_sulfur_dioxide', key = "total_sulfur_dioxide_boxplot_checkbox")
    density_box = st.checkbox('density', key = "density_boxplot_checkbox")
    pH_box = st.checkbox('pH', key = "pH_boxplot_checkbox")
    sulphates_box = st.checkbox('sulphates', key = "sulphates_boxplot_checkbox")
    alcohol_box = st.checkbox('alcohol', key = "alcohol_boxplot_checkbox")

#The boxBooleans list stores the boolean value of whether or not a given checkbox has been checked or not. True if selected, otherwise False. This would allow us to know which checkboxes the user had selected.
    boxplotBooleans = [bool(fixed_acidity_box), 
                       bool(volatile_acidity_box), 
                       bool(citric_acid_box), 
                       bool(residual_sugar_box), 
                       bool(chlorides_box), 
                       bool(free_sulfur_dioxide_box), 
                       bool(total_sulfur_dioxide_box), 
                       bool(density_box), bool(pH_box), 
                       bool(sulphates_box)]

#The boxPositionDictionary contians the index positions of the continious variable columns within the boxBooleans list. This dictionary allows us to grab the text of the column name if the user ends up checking the columns corresponding box.
    boxplotboxPositionDictionary = {0:'fixed_acidity', 
                                    1:'volatile_acidity', 
                                    2:'citric_acid', 
                                    3:'residual_sugar', 
                                    4:'chlorides', 
                                    5:'free_sulfur_dioxide', 
                                    6:'total_sulfur_dioxide', 
                                    7:'density', 
                                    8:'pH', 
                                    9:'sulphates', 
                                    10:'alcohol'}

#The if-else statement, ensures that the user selects exactly one checkbox. It checks for one checked checkbox by taking the sum of the boxBooleans list. If there are exactly 1 checkbox selected it would sum to 1, since individual TRUE values sum to 1. If the sum is not 1, then we know that there are either 0 or 2-11 checkboxes are selected (in this scenario where more or less than 1 box is selected an error message appears). In the case where exactly 1 box is selected, the feature variable grabs the index position of the TRUE value [np.where(boxBooleans)]. Then uses the index position to search the string representation of the column name. Finally the boxplot is formed. 
    if sum(boxplotBooleans) == 1:
        feature = boxplotboxPositionDictionary.get(np.where(boxplotBooleans)[0][0])
        
        fig, ax= plt.subplots()
        plt.boxplot(combinedWine[f'{feature}'])
        ax.set_title(f"{feature} boxplot")
        ax.set_xlabel(f"{feature}")
        ax.set_ylabel(f"{feature} values")
        st.pyplot(fig)
        
    else:
        st.write(f"It seems that you have selected {sum(boxplotBooleans)} boxes. To create a boxplot, exactly 1 box is needed to be selected.")

with tab7: #Classification Tab - Displays information about the random forest classifer model ran on the data

#Sets tab header to Random Forest Classifier Report
    st.header("Random Forest Classifier Report")

#Sets the independent variables to the continous features within the dataset and the dependent variable as the quality column
    x = combinedWine[['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 
                      'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol']]
    y = combinedWine.quality

#Train-Test Split of data at a 70-30 rate.
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=15)

#Creates, fits, and makes predictions using a random forest classifier model
    ClassifierModel = RandomForestClassifier(max_depth = 9, random_state=15)
    ClassifierModel.fit(X_train, y_train)
    y_pred = ClassifierModel.predict(X_test)

#Creates a classification report of the model
    report = pd.DataFrame(classification_report(y_test, y_pred, output_dict=True, zero_division=0)).T

#Subheaders for the classification report and feature importance visualization. Adds the classification report and freature importance bar chart
    st.subheader("Classification Report")
    st.dataframe(report)
    st.subheader("Random Forest Feature Importance Visualization")
    st.bar_chart(data=ClassifierModel.feature_importances_)