# Dublin Urban Forest Analytics Platform

## Overview
The **Dublin Urban Forest Analytics Platform** is an advanced data-driven solution designed to analyze and visualize urban forest data for Dublin. The platform leverages Apache Spark for data processing and Streamlit for interactive visualization.

- Live Demo: [Dublin Urban Forest Analytics Dashboard](https://ritvikdubey27-dublin-urban-forest-analytics-srcdashboard-nvbytd.streamlit.app/)
- GitHub Repository: [Project Link](https://github.com/your-username/dublin-urban-forest-analytics)
- Dataset: [Kaggle](https://www.kaggle.com/datasets/mexwell/trees-in-dublin)

---

## Additional Key Features

- **Cloud Technology**: Leveraging Apache Spark for distributed data processing
- **Machine Learning Integration**: Predictive modeling for tree health and environmental impact
- **Scalable Architecture**: Designed to handle large urban forest datasets
- **Open-Source Collaboration**: Modular design encouraging community contributions

## Technology Stack
- **Data Processing**: Apache Spark
- **Programming Language**: Python
- **Visualization**: Streamlit, Plotly
- **Machine Learning**: PySpark MLlib
- **Geospatial Analysis**: GeoPandas, Folium

---

## Requirements

### System Requirements
- Python 3.9 or higher
- Java Development Kit (JDK) 8 or higher
- Apache Spark 3.5.0
- Git

### Python Package Dependencies
```bash
pip install -r requirements.txt
```

Contents of requirements.txt:
```
pyspark==3.5.0
pandas==2.1.3
numpy==1.26.2
streamlit==1.29.0
plotly==5.18.0
folium==0.15.0
streamlit-folium==0.15.0
matplotlib==3.8.2
seaborn==0.13.0
```

## Environment Setup

1. Install Java Development Kit:
```bash
# Windows
Download and install JDK from Oracle website

# Mac
brew install java
```

2. Set Environment Variables:
```bash
# Windows
set JAVA_HOME=C:\Program Files\Java\jdk1.8.0_xxx
set SPARK_HOME=C:\spark
set PATH=%PATH%;%SPARK_HOME%\bin

# Mac
export JAVA_HOME=$(/usr/libexec/java_home)
export SPARK_HOME=/usr/local/Cellar/apache-spark/3.5.0/libexec
export PATH=$PATH:$SPARK_HOME/bin
```

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/ritvikdubey27/dublin-urban-forest-analytics--platform
cd dublin-urban-forest-analytics-platform
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the data processing pipeline:
```bash
cd src
python data_processing.py
```

4. Launch the dashboard:
```bash
streamlit run dashboard.py
```

---

## Deployment
The application is deployed on Streamlit Cloud.

---
