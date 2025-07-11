# World Happiness Visualization Project

![World Happiness Map](https://github.com/itsmearafik/happiness_index_visualization/blob/main/happiness_visualization.png)  
*Interactive visualization of global happiness scores (2015-2019)*

## 📌 Overview

This project creates an animated choropleth map visualizing the World Happiness Report data from 2015-2019. The interactive visualization enables stakeholders to:

- Track happiness trends across 150+ countries
- Compare regional wellbeing metrics
- Identify correlations between economic/social factors and happiness
- Support data-driven policy decisions

## 🛠 Technical Implementation

### Data Pipeline Architecture

### Core Technologies

- **Python 3.8+**
- **Pandas** (Data wrangling/standardization)
- **Plotly Express** (Interactive visualization)
- **GeoJSON** (Geospatial mapping)

### Key Features

✔ **Dynamic Animation**: Year-by-year evolution of happiness scores  
✔ **Custom Color Scaling**: Intuitive plasma color scheme (low=purple → high=yellow)  
✔ **Country Name Resolution**: Automated normalization of 50+ geographic naming variants  
✔ **Responsive Design**: Adapts to desktop and mobile viewing  

## 💼 Business Value Proposition

This solution delivers actionable insights for:

**Government Agencies**  

- Benchmark quality of life metrics  
- Evaluate policy effectiveness over time  
- Identify regional wellbeing disparities  

**International Organizations**  

- Monitor UN Sustainable Development Goals (SDG 3: Good Health and Wellbeing)  
- Allocate humanitarian resources effectively  

**Corporate HR Teams**  

- Compare employee satisfaction with national baselines  
- Inform global workforce distribution strategies  

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas plotly
```

### Outputs

- Interactive HTML map (world_happiness.html)
- Cleaned CSV dataset

### 🧑‍💻 Professional Competencies Demonstrated

##### Data Engineering

- Built robust ETL pipeline handling 5 distinct data formats

- Implemented automated geographic name resolution

- Designed scalable data model for temporal analysis

##### Business Intelligence

- Translated raw data into executive-ready visualizations

- Developed intuitive metrics for cross-cultural comparison

- Created self-service analytics tool for non-technical users

##### Technical Communication

- Documented data normalization decisions

- Annotated visualization with clear legend and scales

- Structured code for maintainability

### 📊 Sample Insights

1. Nordic countries consistently rank highest (7.5+ scores)

2. Greatest 5-year improvement: Benin (+0.8 points)

3. Strong correlation between GDP and happiness (r=0.78)

### 📜 License

MIT License - Free for academic and commercial use with attribution

### 🤝 Contribution Guidelines

Contributions welcome! Please submit PRs for:

- Additional years of data

- Enhanced mobile responsiveness

- Alternative visualization modes

*"Measuring happiness is the first step toward improving it"*
