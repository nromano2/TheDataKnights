#TMP4 - Writing SQL Queries
#Team: TheDataKnights
#Team Members: Nicholas Romano, Michael Zelaya
#DS-400 Data Science Senior Capstone

#Reading in Country Rentals.csv file created from Python File
df <- read.csv("Individual_Rentals.csv")

#Creating Linear Regression Model
RentalModel <- lm(total_spent ~ num_rentals, data = df)

#Rental Model Summary
summary(RentalModel)
#Model Function: -3.22174 + 4.32164(num_rentals)
#R-squared: 0.7581
#.7581 R-squared value indicates that the number of rentals explain roughly 75% of the variability in the total money spent by each individual

#Scatterplot
plot(df$num_rentals, df$total_spent)
title("Scatterplot Overlayed with Model Line")
abline(RentalModel)

#Residual Plots
plot(RentalModel$residuals,
     main = "Rental Model Residuals",
     ylab = "Residuals")
abline(h=0)

#The residuals from the model appear to be approxoimately normally distributed between [-40,40] with a mean around 0

#Normal Quantile Line
qqnorm(RentalModel$residuals)
qqline(RentalModel$residuals)

#The points of the normal quantile plot of the model indicate that the data is approximately normally distributed with most, if not all, the points lying on or near the line.

