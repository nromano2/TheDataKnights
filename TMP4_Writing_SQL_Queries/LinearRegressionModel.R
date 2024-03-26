#Reading in Country Rentals.csv file created from Python File
df <- read.csv("Individual_Rentals.csv")

#Creating Linear Regression Model
RentalModel <- lm(total_spent ~ num_rentals, data = df)

#Rental Model Summary
summary(RentalModel)

#Scatterplot
plot(df$num_rentals, df$total_spent)
title("Scatterplot Overlayed with Model Line")
abline(RentalModel)

#Residual Plots
plot(RentalModel$residuals,
     main = "Rental Model Residuals",
     ylab = "Residuals")
abline(h=0)

#Normal Quantile Line
qqnorm(RentalModel$residuals)
qqline(RentalModel$residuals)
