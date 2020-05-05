# Project II


# Topic

Produce visualizations depicting  financial crime reported by casinos in the Southwest region of the U.S. by county to determine the risk level associated with different counties.


# Visualization ideals 

Novel JS dropdown menu/item
Interactive map
Heatmap
Choropleth map


# Dataset

Treasury’s Financial Crimes Enforcement Network (FinCEN) is our nation’s financial intelligence unit, which collects, analyzes, and disseminates financial intelligence, such as Suspicious Activity Reports (SARS) that track alleged illicit activity reported by financial institutions. Found at: https://www.fincen.gov/reports/sar-stats

U.S. Census provides geographic data by county that we implemented to generate our maps. 
https://www.census.gov/geographies

Rationale

Plotting U.S. Treasury SARs filtered by different states/counties on a heatmap will assist law enforcement, regulators, and other financial institutions that serve casinos to better understand the risk level of crime types experienced by different counties at various locations. For example, casinos situated along the California-Mexico border may be a higher risk for counterfeiting associated with foreign exchange thus bumping up their crime incidence reporting.


GitHub Link: https://github.com/kellertw/project_II.git

_____________________________________________________________________________________



Gathering Data [Tom]
Cleaning data (Pandas) + Joining tables [Genti]
 - CA
 - NV
 - UT
 - AZ
 - CO
 - NM
    - Dec 2014-Dec 2019
Placing Data into database (SQLite) [Suliat, (Tom assist)]
Create: 
 - HTML file [Ben]
 - JS- app.js (from Javascript Challenge)[Kat]
 - CSS - style.css [Tom]
 - Config file- map box api key
 - Bootstrap (from Web Design Challenge)[Kat]
 - READme file
Finding new JS library and coding  [Kat]
Presentation planning 

# About the data
Financial institutions are required to file reports with a bureau of the Treasury, known as the Financial Crimes Enforcement Network (FinCEN), and these reports are rich with data. Financial institutions are everywhere, so Census data was also leveraged to plot activity on a map.
There are so many types of financial institutions that offer different products – and opportunities for criminals to abuse the system. Casinos are often dramatized for financial crimes, so it makes sense that they must file reports with the Treasury.
What do casinos report? What are the most commonly observed “suspicious activities” in Las Vegas, Nevada? How does that activity differ in California, or other states in the Southwest United States?
 
# What is FinCEN?
FinCEN is a bureau of the Treasury Department. It is charged with safeguarding the financial system from illicit use, combating money laundering, and promoting national security through the strategic use of financial authorities and the collection, analysis, and dissemination of financial intelligence.
 
# Casinos are Financial Institutions?!
Yes, casinos are defined as financial institutions under the Bank Secrecy Act (a group of laws collected under Title 31 of the Code of Federal Regulations). Much like banks or money services businesses, a lot of cash flows through casinos. The reports filed with FinCEN allow regulators, law enforcement, and private industry to observe trends and patterns of financial activity. This information helps to safeguard the financial system from abuse.
What is Suspicious Activity in a Casino or Card Club?
Suspicious activities are unusual transactions and activities that appear to have no legitimate purpose. FinCEN has studied their data, and developed documents to provide “red flags” for casinos and card clubs, as well as other financial institutions.
