# Creating dataset sample  
# Author: Anchif

reaction_time <- data.frame(
  group = c("control","control","control","control","control","treatment",
            "treatment","treatment","treatment", "treatment"),
  reaction_time = c(340, 350, 355, 365, 345,310, 315, 320, 300, 330))

write.csv(reaction_time, "reaction_time.csv", row.names = FALSE)
