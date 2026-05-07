{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6d6b5f38-ffc8-4d3e-815b-13410de266ef",
   "metadata": {},
   "source": [
    "# Project: Analyzing a Hypothetical Drug A clinical trial"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c3cfc41d-2184-4e80-90ef-5fd80c47a230",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from scipy.stats import ttest_ind"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "70a2a458-bd80-4b71-b7f8-d12e11beda49",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import dataset\n",
    "my_data = pd.read_csv(\"Desktop/R Projects/data/reaction_time.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e7e8c2aa-d33c-4759-9167-5599466ff86c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>group</th>\n",
       "      <th>reaction_time</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>control</td>\n",
       "      <td>340</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>control</td>\n",
       "      <td>350</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>control</td>\n",
       "      <td>355</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>control</td>\n",
       "      <td>365</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>control</td>\n",
       "      <td>345</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>treatment</td>\n",
       "      <td>310</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>treatment</td>\n",
       "      <td>315</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>treatment</td>\n",
       "      <td>320</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>treatment</td>\n",
       "      <td>300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>treatment</td>\n",
       "      <td>330</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       group  reaction_time\n",
       "0    control            340\n",
       "1    control            350\n",
       "2    control            355\n",
       "3    control            365\n",
       "4    control            345\n",
       "5  treatment            310\n",
       "6  treatment            315\n",
       "7  treatment            320\n",
       "8  treatment            300\n",
       "9  treatment            330"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "883eaf27-e08a-4b8e-8afd-21e5e89d5f75",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Separate group\n",
    "\n",
    "control = my_data[my_data[\"group\"] == \"control\"][\"reaction_time\"]\n",
    "treatment = my_data[my_data[\"group\"] == \"treatment\"][\"reaction_time\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "12c3110e-2f22-4c70-8f94-bdff6f4a636d",
   "metadata": {},
   "source": [
    "### Hyphothesis (H0): Drug A (treatment group) has no effect on reaction_time compared to control saline group."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "155ea819-8609-485b-88b7-65ad327abf27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Control Mean: 351.0 ms\n",
      "Treatment Mean: 315.0 ms\n",
      "t-statistic: 5.46\n",
      "p-value: 0.00060\n"
     ]
    }
   ],
   "source": [
    "# Welch independent sample t-test\n",
    "t_stat, p_value = ttest_ind(control, treatment)\n",
    "\n",
    "# Display result\n",
    "print(f\"Control Mean: {sum(control)/len(control):.1f} ms\")\n",
    "print(f\"Treatment Mean: {sum(treatment)/len(treatment):.1f} ms\")\n",
    "print(f\"t-statistic: {t_stat:.2f}\")\n",
    "print(f\"p-value: {p_value:.5f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00207dfd-fa8a-4f23-9d9d-91f25b875573",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Automatic decision\n",
    "\n",
    "if p-value < 0.05:\n",
    "    print(\"Decision: Significant difference! Reject H0.\")\n",
    "else:\n",
    "    print(\"Decision: No significant difference found. We can't reject H0.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
