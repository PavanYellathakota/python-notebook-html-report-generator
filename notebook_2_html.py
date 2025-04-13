# %% [markdown]
# # Convert your whole Notebook code into single page webpage with charts and Interpretations.

# %%
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Updated dataset
df = pd.DataFrame({
    "startup": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"],
    "revenue": [6.5, 8.2, 4.8, 7.1, 9.5, 3.8, 10.2, 7.9, 8.6, 6.3, 5.9, 11.4, 4.2, 9.8, 7.4],
    "profit": [2.8, 3.9, 1.9, 3.0, 4.5, 1.4, 5.1, 3.7, 4.2, 2.9, 2.3, 5.8, 1.6, 4.9, 3.3],
    "sector": ["Fintech", "Health", "Fintech", "EduTech", "Health", "EduTech", "Fintech", "Retail", "Retail", "Health", 
               "AI", "Fintech", "EduTech", "Retail", "AI"],
    "region": ["US", "Europe", "Asia", "Asia", "US", "Europe", "Asia", "US", "Europe", "Asia", 
               "US", "Europe", "Asia", "US", "Europe"],
    "employees": [60, 150, 40, 90, 120, 50, 250, 180, 100, 70, 80, 300, 35, 200, 110],
    "funding_stage": ["Series A", "Seed", "Series B", "Series A", "Series B", "Seed", "Series A", "Series A", 
                      "Seed", "Series B", "Series A", "Series C", "Seed", "Series B", "Series A"],
    "growth": [18, 28, 15, 20, 35, 12, 40, 25, 30, 16, 22, 45, 10, 38, 24],
    "founded_year": [2018, 2020, 2019, 2017, 2016, 2021, 2015, 2018, 2019, 2020, 
                     2017, 2014, 2022, 2016, 2018],
    "customer_count": [5000, 12000, 3000, 8000, 15000, 2000, 25000, 10000, 9000, 4000, 
                      6000, 30000, 1500, 20000, 7000],
    "market_share": [5.2, 8.1, 3.4, 6.5, 10.3, 2.8, 12.7, 7.9, 6.8, 4.5, 
                     5.9, 15.4, 2.1, 11.2, 6.3]
})

# Bar Chart: Revenue by Startup
bar_fig = px.bar(df, x="startup", y="revenue", color="sector", title="Revenue by Startup")
bar_html = pio.to_html(bar_fig, include_plotlyjs=False, full_html=False)

# Pie Chart: Sector Distribution
pie_fig = px.pie(df, names="sector", title="Sector Distribution")
pie_html = pio.to_html(pie_fig, include_plotlyjs=False, full_html=False)

# Template HTML with insights
with open("startup_analysis_web.html", "w") as f:
    f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Startup Analysis Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {{
            font-family: Arial;
            margin: 2rem;
            background-color: #f9f9f9;
        }}
        .section {{
            background: white;
            padding: 20px;
            margin-bottom: 40px;
            border-radius: 12px;
            box-shadow: 0 0 8px rgba(0,0,0,0.05);
        }}
        h2 {{ color: #333; }}
        pre {{
            background: #eee;
            padding: 10px;
            border-radius: 8px;
            overflow-x: auto;
        }}
    </style>
</head>
<body>

<div class="section">
    <h2>Python Code</h2>
    <pre>
import pandas as pd
import plotly.express as px
df = pd.DataFrame({{
    "startup": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"],
    "revenue": [6.5, 8.2, 4.8, 7.1, 9.5, 3.8, 10.2, 7.9, 8.6, 6.3, 5.9, 11.4, 4.2, 9.8, 7.4],
    "sector": ["Fintech", "Health", "Fintech", "EduTech", "Health", "EduTech", "Fintech", "Retail", "Retail", "Health", 
               "AI", "Fintech", "EduTech", "Retail", "AI"],
    ...
}})
bar_fig = px.bar(df, x="startup", y="revenue", color="sector", title="Revenue by Startup")
pie_fig = px.pie(df, names="sector", title="Sector Distribution")
    </pre>

    <h2>Bar Chart: Revenue by Startup</h2>
    {bar_html}

    <h3>Interpretation</h3>
    <p>
        From the bar chart, we observe that <b>Startup L</b> and <b>Startup G</b> have the highest revenues, exceeding $10M. 
        Fintech and Health sectors show strong performance, with multiple startups generating significant revenue.
    </p>
</div>

<div class="section">
    <h2>Pie Chart: Sector Distribution</h2>
    {pie_html}

    <h3>Interpretation</h3>
    <p>
        The pie chart indicates that Fintech holds the largest share of startups (26.7%), followed by Health and Retail. 
        This suggests a strong market presence for Fintech-driven innovation.
    </p>
</div>

</body>
</html>
""")


