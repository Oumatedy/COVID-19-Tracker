# COVID-19 Global Data Tracker

This project provides a comprehensive, data-driven analysis of the COVID-19 pandemic using global data from Our World in Data. The notebook explores trends in cases, deaths, and vaccinations, and investigates how demographic and socioeconomic factors have influenced pandemic outcomes across countries and continents.

<img src="https://www.internationalairportreview.com/wp-content/uploads/ICAO-11.jpg" width="600">

From [International Airport Review - Updated Economic Impact Analysis COVID-19 (ICAO)](https://www.internationalairportreview.com/news/149655/updated-economic-impact-analysis-covid-19-icao/)
## Features
- **Interactive Dashboard:** Launch `dashboard.py` with Streamlit to explore and compare COVID-19 trends by country, date range, and metric. Includes multi-country comparison, summary statistics, and data download.
- **Data Import & Cleaning:** Loads and preprocesses the latest COVID-19 dataset, handling missing values and anomalies for robust analysis.
- **Exploratory Data Analysis (EDA):** Visualizes time trends, regional comparisons, and key metrics using Python libraries (pandas, matplotlib, seaborn, plotly).
- **Geographical & Demographic Analysis:** Compares pandemic impact by continent and country, and explores the role of age, population density, and GDP per capita.
- **Statistical & Regression Analysis:** Includes correlation matrices and regression models to uncover relationships between COVID-19 outcomes and factors like GDP, age, and vaccination rates.
- **Narrative Insights & Recommendations:** Presents findings with clear markdown explanations, actionable insights, and policy recommendations.

## Objectives
1. Import, clean, and preprocess global COVID-19 data for robust analysis.
2. Analyze and visualize time trends in cases, deaths, and vaccinations across countries and continents.
3. Compare key COVID-19 metrics between countries and regions, highlighting disparities and patterns.
4. Apply statistical and regression analysis to explore relationships between pandemic outcomes and demographic or socioeconomic factors.
5. Communicate findings through clear visualizations, narrative insights, and actionable recommendations in a well-structured notebook.

## Tools and Libraries
- **Python**: Primary programming language.
- **Pandas**: Data manipulation and analysis.
- **Plotly/Matplotlib/Seaborn**: Interactive and static visualizations.
- **Jupyter Notebook**: Development environment for code and analysis.
- **Scikit-learn**: Statistical analysis and correlation calculations (optional).

## How to Use
1. **Clone or download this repository.**
2. **Ensure you have Python 3.x and the following libraries installed:**
   - pandas
   - numpy
   - matplotlib
   - seaborn
   - plotly
   - scikit-learn
   - streamlit
3. **To launch the interactive dashboard:**
   - Open a terminal in the project folder and run:
     ```cmd
     streamlit run dashboard.py
     ```
   - Use the sidebar to select countries, date range, and metrics. Download filtered data as needed.
4. **To run the analysis notebook:**
   - Open `index.ipynb` in VS Code or Jupyter Notebook.
   - Run the notebook cells sequentially to reproduce the analysis and visualizations.
   - **Note:** If `index.ipynb` is too large to view on GitHub, please download the file and open it locally using Jupyter Notebook or VS Code for the best experience.

## Data Source
- [Our World in Data: COVID-19 Dataset](https://github.com/owid/covid-19-data)

## Project Structure
- `dashboard.py` — Interactive Streamlit dashboard for COVID-19 data exploration
- `index.ipynb` — Main analysis notebook
- `owid-covid-data.csv` — COVID-19 dataset (downloaded from Our World in Data)
- `README.md` — Project overview and instructions
- `LICENSE` — License information

### **Key Insights**

- `Mortality Rate Disparities`: Countries with older populations or limited healthcare infrastructure exhibited higher death rates.

- `Vaccination Equity`: High-income nations had significantly faster vaccine rollout rates compared to low-income regions.

- `Socioeconomic Impact`: GDP per capita correlated strongly with vaccination coverage, highlighting systemic inequities.

- `Population Density`: Densely populated areas experienced faster initial spread but lower long-term fatality rates due to earlier immunity.

### **Reflections**

- *Data Challenges*: Missing or inconsistent reporting from certain regions required careful imputation.

- *Policy Implications*: The analysis underscores the need for global cooperation in resource allocation during health crises.

- *Future Work*: Expanding the analysis to include post-pandemic recovery metrics (e.g., economic rebound, long COVID prevalence).

## License
This project is licensed under the MIT License.

## Acknowledgments
- Our World in Data for providing open-access COVID-19 data
- The global scientific and public health community for ongoing research and response efforts

**Image Credit**: [International Airport Review - Updated Economic Impact Analysis COVID-19 (ICAO)](https://www.internationalairportreview.com/news/149655/updated-economic-impact-analysis-covid-19-icao/)
