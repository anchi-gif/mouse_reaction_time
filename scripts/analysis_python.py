# Project: Analyzing a Hypothetical Drug A clinical trial

import pandas as pd
from scipy.stats import ttest_ind

# Import dataset
my_data = pd.read_csv("Desktop/R Projects/data/reaction_time.csv")

# Separate group
control = my_data[my_data["group"] == "control"]["reaction_time"]
treatment = my_data[my_data["group"] == "treatment"]["reaction_time"]

### Hyphothesis (H0): Drug A (treatment group) has no effect on reaction_time compared to control saline group.

# Welch independent sample t-test
t_stat, p_value = ttest_ind(control, treatment)

# Display result
print(f"Control Mean: {sum(control)/len(control):.1f} ms")
print(f"Treatment Mean: {sum(treatment)/len(treatment):.1f} ms")
print(f"t-statistic: {t_stat:.2f}")
print(f"p-value: {p_value:.5f}")

# Automatic decision
if p_value < 0.05:
    print("Decision: Significant difference! Reject H0.")
else:
    print("Decision: No significant difference found. We can't reject H0.")
