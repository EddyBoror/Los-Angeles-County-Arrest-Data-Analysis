# Portfolio Project

### Project Overview

Analyzing and Visualizing Uncleaned Arrest Data from L.A. County

### Data Sources

Arrest Data: The primary dataset used for this analysis is the "Arrest_2020.csv"

### Tools

- Excel: Data Source
  - [Download here](https://data.lacity.org/Public-Safety/Arrest-Data-from-2020-to-Present/amvf-fr72/about_data)
- Microsoft SQL server: Data Exploration (Uncleaned Dataset)
- Python: Pandas, NumPy, Matplotlib/Seaborn for data cleaning and visualization.
- Jupyter Notebooks: Documenting analysis steps, cleaning, and creating initial     
  visualizations.
- Tableau: Building interactive dashboards for comprehensive data representation.

### Data Cleaning/ Preparation

In the initial data preparation phase, I performed the following tasks with Python:

1. Data loading and inspection.
2. Handling missing values.
3. Data cleaning and formatting.

### Exploratory Data Analysis

Geospatial Crime Analysis:

  - Explore trends in arrest frequencies across diverse locations on a geographic map.

<img src="https://github.com/EddyBoror/Los-Angeles-County-Arrest-Data-Analysis/blob/main/Geo%20City.png" width="1000" height="700" />

Demographic Analysis:
  - Are certain age groups or genders more frequently involved in arrests?

Arrest Type Breakdown::
  - What is the distribution of arrest types (e.g., misdemeanor, felony) in the dataset?

<img src="https://github.com/EddyBoror/Los-Angeles-County-Arrest-Data-Analysis/blob/main/Gender%20Age%20Arrest.png" width="1000" height="700" />


### Data Statistical Summary

- The dataset primarily consists of "BOOKING" entries, indicating that a significant portion of the records corresponds to booking-related activities.

- The dataset records 3,772 instances of the common arrest time, around 1:00 PM, indicating a concentrated period for law enforcement activity.

- The most common area for arrests is "Rampart," with 18,632 occurrences, indicating a higher concentration of law enforcement activities in this region.

- The dataset indicates a higher frequency of male persons involved in arrests due to the majority of males (202,282 occurrences). Furthermore, "H," which has been recorded 131,366 times, is the most often occurring descent code, suggesting a concentration of arrests involving people of Hispanic heritage.



