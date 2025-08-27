# Student Performance Dataset – Exploratory Data Analysis

This project explores a synthetic dataset of student performance (200 rows × 9 columns) using Python and Excel.  
The goal was to practice a real-world data science workflow: data cleaning, descriptive statistics, correlation analysis, and group comparisons.

## Steps Performed
- Checked dataset shape, column data types, and missing values  
- Generated summary statistics (mean, std, min, max, quartiles)  
- Explored variable distributions (histograms and descriptive stats)  
- Converted categorical variables into numerical form to enable correlation analysis  
- Computed correlation matrix to identify relationships with final grades (G3)  
- Compared performance by gender and by school

## Key Findings
- **No missing data** — dataset was clean from the start  
- **Final grades (G3)** center around ~9.5 (0–19 range)  
- **Weak positive correlation** between study time (0.15) and G3  
- **School MS students slightly outperform GP students** on average  
- **Male students show higher average final grades than female students**  
- **Failures and absences** show little relationship with grades

## Next Steps
This analysis could be extended with:
- Additional visualizations (boxplots, scatterplots)  
- Simple regression or machine learning models to predict G3  
- Statistical testing to check if group differences are significant

---

**Note:** This dataset is synthetic and was used purely for learning purposes.  
