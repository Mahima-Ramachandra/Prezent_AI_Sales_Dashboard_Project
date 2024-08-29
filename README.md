Sales Dashboard Project
Overview
This repository contains a Tableau dashboard for analyzing sales performance across different regions, products, and channels. It includes scripts for data generation, processing, and API testing, as well as the final Tableau workbook and output files.
Repository Structure

**workbooks/: **Contains the Tableau workbook file for customer sales analysis
**scripts/:** Python scripts for data processing and API testing
**OutputFiles/:** Generated sample data and Tableau workbook files
**textFile/:** Assessment question

Key Files

**/myScript_dataprocessing.py:**

Main script for sample data generation
Includes exchange rate calculation
Converts sales amount and saves in Parquet format


/Exchange_rate_api.py:

Used to test the exchange rate API and its data
Preliminary script before integration into main processing


/Sample_data_generation.py:

Sample data generation script provided by Prezent.ai


/Data_insights_assesment.txt:

Contains the questions and requirements for the data insights assessment


OutputFiles/:

Contains generated sample data (CSV files)
**Includes the final Parquet file with processed data**
**Stores Tableau workbook files for sales analysis**


/sales_analysis.twb:

Tableau workbook file containing the sales analysis dashboard



Setup and Usage

Clone this repository
Install required Python libraries: pandas, requests, pyarrow
Run myScript_dataprocessing.py to generate and process data
Open the Tableau workbook in OutputFiles/ to view the sales analysis

Data Processing Workflow

Exchange rates are fetched using the tested API (see Exchange_rate_api.py)
Sample data is generated , Sales data is processed and converted using myScript_dataprocessing.py
Final output is saved in Parquet format in the OutputFiles/ directory
Tableau workbook uses this processed data for analysis and visualization

Tableau Dashboard
The Tableau dashboard in sales_analysis.twb provides insights on:

Overall sales performance
Regional sales breakdown
Product performance analysis
Customer segmentation
Year-over-year growth trends

Refer to the workbook for interactive visualizations and detailed insights.
Assessment Questions
For the specific questions and requirements of this project, refer to Data_insights_assesment.txt

License
This project is licensed under the MIT License - see the LICENSE.md file for details.
