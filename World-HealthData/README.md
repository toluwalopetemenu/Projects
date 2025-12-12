**Overview**
This dataset is from 10x Anlytics Hackathon, which I registered for but couldn’t fully participate in because of issues beyond my control. Although this analysis is a bit late, I did enjoy working through it as it’s one of the many things I am passionate about! Health. We will be exploring how to improve the health status of people in Africa.

**About the Dataset:** Our data comes in 6 datasets which contains the records of causes of death across various years and countries
1. Deaths across different age groups
2. Medical Doctor per 10,000 population
3. ISO 3166 country and continent codes list
4. World population
5. Health Expenditure (% of GDP)

Data cleaning process was done using python. I choose to work with python as I am currently on the women techsters fellowship with tech4dev, and I have been taken classes on it; this would serve as a means to also practice my learning. PowerBi, is a tool I have consistently tried to navigate my way for a while. Hence, I also choose to work with it for this analysis.

Detailed breakdown of how I cleaned, joined my dataset, and extracted the Africa Set as an excel file available in the file here

**Exploratory Data Analysis and Data Visualization**
The goal of this analysis is to provide solutions to the health challenges in Africa. This is open-ended; therefore, the first thing I will do is to define the health challenges in Africa: the top 3 challenges I found from an online search includes inadequate human resource, poor healthcare financing and poor leadership and management. This isn’t surprising as most African countries are considered low- and middle-income countries and do not invest in health care compared to developed countries.

But what does our data say? I will be answering the following questions:
1. What is the leading cause of death in Africa?
2. Which Country has the highest death rate recorded?
3. What is the distribution of Health Care personnel across the countries?
While I try to answer these questions, I will also share other interesting insights along the way, I believe you will find it as interesting as I did while working on this.

Keynote: Our dataset is quite large but for the sake of application and relevance to date, my analysis focuses on 2010–2019.

**Insight**
When it comes to healthcare, it is important to look at vulnerable Populations, this is because this set of people is more prone to morbidity(disease) and mortality(deaths) so we will be looking at the rate of death within this population. I narrowed my result to include the Top 5 countries with the highest death rates.
<img width="1045" height="543" alt="image" src="https://github.com/user-attachments/assets/299aa46d-8942-472f-9a95-6ba162ea1cf8" />

From figure 1 we see that Nigeria has the highest death rate for the vulnerable populations, there is also a wide margin in the Under 5 mortality rate when compared to other countries.

Question 2: What are the top leading causes of death in Africa? From my analysis, cardiovascular diseases are the leading cause of death with over 12 million five hundred and nineteen thousand two hundred and two attributed to it. Other leading causes also include HIV/AIDs, Lower Respiratory Disorder, Malaria and Neonatal Disorder.
<img width="649" height="89" alt="image" src="https://github.com/user-attachments/assets/838b449d-48bd-48df-88cb-e73752345d9a" />

I further decided to create a filter to focus on 3 of these diseases: Cardiovascular diseases, HIV/AIDs and Diarrheal diseases, the rationale behind choosing these diseases is they are largely influenced by lifestyle choices amongst other factors.

More analysis insight, including recommendation and conclusion available here: https://medium.com/@temenuoluwabusola/data-analysis-with-python-and-power-bi-27466f41fc0b
