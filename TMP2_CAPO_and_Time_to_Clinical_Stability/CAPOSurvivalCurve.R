library(survival)
df <- read.csv(file.choose())

SurvivalCurve <- survfit(Surv(df$TCS, df$Stability_Reached)~0)
plot(SurvivalCurve,
     main = "CAPO Survival Curve",
     xlab = "Time to Clinical Stability (Days)",
     ylab = "Survival Proability")
