# Project: Analyzing a Hypothetical Drug A clinical trial

# Author: Anchif

# 1. Load the Tidyverse to get read_csv
library(readr)

# 2. Read file : reaction_time.csv
my_data <- read.csv("C:/Users/ali/Desktop/R Projects/reaction_time.csv")

# 3. Check the data
my_data
summary(my_data)

# Run the Welch independent sample t_test
result <- t.test(reaction_time ~ group, data = my_data)

# Display result
print(result)

setwd("C:/Users/ali/Desktop/R Projects")

# Save result
capture.output( print(result), 
                file = "results/t_test_output.txt")