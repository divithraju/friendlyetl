# FriendlyETL

A beginner-friendly and customizable Python ETL (Extract, Transform, Load) package designed for fast and efficient data workflows. Built using Pandas and compatible with files and databases, this package helps you automate your ETL pipelines with just a few lines of code.
url= https://github.com/divithraju
linkedin= https://www.linkedin.com/in/divithraju/
## 🔧 Features

- ✅ Extract data from CSV, Excel, JSON, or databases (MySQL)  
- ✅ Clean and transform datasets using common operations  
- ✅ Load data to CSV or back into MySQL databases  
- ✅ Modular and easy to extend for your own workflows  
- ✅ Designed for beginners, students, and professionals alike  

## 🗂 Project Structure

friendlyetl/
├── friendlyetl/
│ ├── init.py
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
├── setup.py
├── README.md
└── dist/


## 🚀 Installation

Install the package from your local build:

```bash
pip install dist/friendlyetl-0.0.1-py3-none-any.whl

import friendlyetl as fetl

# Extract data from CSV
df = fetl.extract_data('input/sales.csv')

# Transform data
clean_df = fetl.clean_data(df)

# Load to MySQL
fetl.load_to_mysql(clean_df, db_name="sales_db", table_name="clean_sales")

 ## Dependencies
Python 3.6+

pandas

sqlalchemy

mysql-connector-python (if using MySQL)

Install all dependencies:

pip install -r requirements.txt
👤 Author
Divith Raju
Built with ❤️ to simplify ETL pipelines.
🔗 GitHub

📜 License
This project is licensed under the MIT License. See LICENSE file for more information.