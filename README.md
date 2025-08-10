🏎️📊Predicting Podium Finishes in Formula 1 

Data wrangling, logistic regression, and Tableau storytelling to uncover how qualifying positions shape race outcomes.

📌 Overview
This project explores the relationship between qualifying position and race success in Formula 1, combining Python-based machine learning with interactive Tableau visualizations.
Using historical race data, I applied logistic regression to predict podium finishes, and built a two-slide Tableau Story to visualize trends, outliers, and driver overperformance.

🔍 Key Features
Data Wrangling & Cleaning: Merged multiple CSV datasets (results, qualifying, drivers, standings) using pandas and NumPy.

Machine Learning: Implemented a logistic regression model in Python to predict podium finishes based on qualifying position.

Visualization: Designed an interactive Tableau Story highlighting:

Yearly podium rates by qualifying position

Correlation between starting grid position and position changes

Storytelling: Annotated key findings, such as P1 starters being 3× more likely to podium than other positions.

🛠️ Tech Stack
Python (pandas, NumPy, scikit-learn)

Tableau Public (interactive storytelling)

📊 Results & Insights
P1 starters are over 3× more likely to finish on the podium than any other position.

Higher qualifying positions correlate strongly with minimal grid position changes during races.

Certain drivers consistently outperform their starting grid, highlighting strategic race execution.

📂 Repository Structure
bash
Copy
Edit
├── data/                # Raw and cleaned datasets  
├── notebooks/           # Jupyter notebooks for data analysis & ML  
├── tableau_story/       # Tableau workbook (.twbx)  
├── README.md            # Project overview (this file)  
└── requirements.txt     # Python dependencies  

View the Tableau Story via the public link.

📈 Tableau Story Preview
https://public.tableau.com/views/Formula1Analysis_2/Story1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link 

📬 Contact: 
Adi Pelled
📧 adi.pelled.ap@gmail.com
