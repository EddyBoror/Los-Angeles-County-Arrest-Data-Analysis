# Los Angeles Crime Analysis

<img src="https://github.com/EddyBoror/Los-Angeles-County-Arrest-Data-Analysis/blob/main/Images/Los%20Angeles.jpg" width="900" height="350" />


# Project Overview

Analyzing and Visualizing Uncleaned Arrest Data from L.A. County

<br>

# Data Sources

Arrest Data: This analysis's primary dataset, "Arrest_2020.csv," contains information from January 2020 to November 2023. It's important to remember that, even if my analysis is predicated on historical data, the dataset is updated daily to guarantee that the most recent and pertinent insights are considered.
  - [Download here](https://data.lacity.org/Public-Safety/Arrest-Data-from-2020-to-Present/amvf-fr72/about_data)

<br>

# Tools

- Excel: Data Source
  - [Download here](https://data.lacity.org/Public-Safety/Arrest-Data-from-2020-to-Present/amvf-fr72/about_data)
- Microsoft SQL server: Data Exploration (Uncleaned Dataset)
- Python: Pandas, NumPy, Matplotlib/Seaborn for data cleaning and visualization.
- Jupyter Notebooks: Documenting analysis steps, cleaning, and creating initial     
  visualizations.
- Tableau: Building interactive dashboards for comprehensive data representation.

<br>

# Data Cleaning/ Preparation

In the initial data preparation phase, I performed the following tasks with Python:

1. Data loading and inspection.
2. Handling missing values.
3. Data cleaning and formatting.

<br>

# Exploratory Data Analysis

### Python Analysis
- Please check here for my cleaning, analysis, and visualization using [Python](https://github.com/EddyBoror/Los-Angeles-County-Arrest-Data-Analysis/blob/main/Final%20Cleaned%20Arrest%20Dataset.ipynb) libraries.

### Area Crime Analysis:

  - What are the top four races within each geographical total count charge area?

![image](https://github.com/EddyBoror/Los-Angeles-County-Arrest-Data-Analysis/assets/61037075/340158e8-92c2-45f1-a43a-f11447d377e4)

### Arrest Type Breakdown::
What are the differences in charge type counts between males and females in the dataset?

Male
![image](https://github.com/EddyBoror/Los-Angeles-County-Arrest-Data-Analysis/assets/61037075/449ea6ba-8372-4d05-8da3-82e24694c533)

- Insight: Male charge descriptions dominate the dataset, with seven types exceeding 10,000 counts, while for females, Aggravated Assault tops the chart at 8,217 instances.
- Actionable View: Target resources towards addressing prevalent charge types among males, especially those with counts surpassing 10,000 instances, through tailored interventions and enforcement strategies.

Female
![image](https://github.com/EddyBoror/Los-Angeles-County-Arrest-Data-Analysis/assets/61037075/5d853b26-4478-4907-ba98-fc614a16bda8)


How does the average age vary by gender from 2020 to 2023?

![image](https://github.com/EddyBoror/Los-Angeles-County-Arrest-Data-Analysis/assets/61037075/8c0f46eb-7f39-41a9-9890-ffbd41e2fc0d)

- Insight: The consistent average age of 35 for arrests from 2020 to 2023 highlights a stable demographic trend.

- Actionable View: LAPD could use this insight to tailor interventions and allocate resources effectively for this age group, potentially through targeted community engagement or preventive programs.

<br>

# Data Statistical Summary

- The dataset primarily consists of "BOOKING" entries, indicating that a significant portion of the records corresponds to booking-related activities.

- The dataset records 3,772 instances of the common arrest time, around 1:00 PM, indicating a concentrated period for law enforcement activity.

- The most common area for arrests is "Rampart," with 18,632 occurrences, indicating a higher concentration of law enforcement activities in this region.

- The dataset indicates a higher frequency of male persons involved in arrests due to the majority of males (202,282 occurrences). Furthermore, "H," which has been recorded 131,366 times, is the most often occurring descent code, suggesting a concentration of arrests involving people of Hispanic heritage.

# Conclusion Analysis

The analysis of this data can be helpful for both people in the community and law enforcement. For pedestrians, it gives insights into when and where arrests commonly happen, helping them make informed decisions about their safety. Understanding the patterns in arrests, like the higher frequency for males and individuals of Hispanic heritage, can also contribute to a better awareness of law enforcement interactions.

Law enforcement can use the data to find patterns in the locations, timeframes, and kinds of charges associated with arrests. This data allows resources to be allocated more effectively and total operational effectiveness can be raised. Law enforcement can improve its tactics and procedures by better understanding the most frequent charges and the typical outcomes of arrests. Ultimately, this data analysis encourages safety and openness by supporting a more knowledgeable and cooperative interaction between the community and law enforcement.
