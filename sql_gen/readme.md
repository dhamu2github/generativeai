# SQL Query Generator

A Python application that generates MySQL-compatible SQL queries from natural language text using the Groq LLM API. The application connects to a MySQL database, retrieves the schema information, and generates appropriate SQL queries based on user prompts.

## Features

- Natural language to SQL query conversion
- Automatic database schema retrieval
- Secure MySQL database connection handling
- Integration with Groq's LLM API
- Query execution capabilities

## Prerequisites

- Python 3.7+
- MySQL Server
- Groq API access

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dhamu2github/generativeai.git
cd sql_gen
```

2. Install required dependencies:
```bash
pip install mysql-connector-python groq
```

3. Set up environment variables:
```bash
export GROQ_API_KEY='your_groq_api_key_here'
```

## Configuration

Update the database configuration in `database_utils.py`:

```python
# MySQL connection details
db_config = {
    'host': 'localhost',       # Change if not on localhost
    'user': 'foodmart',         # Replace with your MySQL username
    'password': 'foodmart@123', # Replace with your MySQL password
    'database': 'FOODMART'      # Replace with your MySQL database name
}
```

## Project Structure

```
sql-query-generator/
├── sql_gen_app.py        # Main application entry point
├── model_utils.py        # LLM integration and query generation
└── database_utils.py     # Database connection and operations
```

### File Descriptions

- **sql_gen_app.py**: Main application script that orchestrates the connection to MySQL, schema retrieval, and query generation
- **model_utils.py**: Handles interaction with the Groq API and SQL query generation
- **database_utils.py**: Contains utilities for MySQL database operations

## Usage

1. Ensure your MySQL server is running and accessible with the configured credentials.

2. Run the application:
```bash
python sql_gen_app.py
```

3. The application will:
   - Connect to the specified MySQL database
   - Retrieve the database schema
   - Generate an SQL query based on the provided text prompt
   - Execute the query (if uncommented in the code)

## Example

```python
# Example text prompt
text_prompt = "List top 5 products from the product table and join with table inventory_fact_1998 and get warehouse sales"

# Generated SQL query will be displayed in the console
```

## Function Reference

### Database Utilities (`database_utils.py`)

- `connect_to_mysql()`: Establishes connection to MySQL database
- `get_db_schema(connection)`: Retrieves and formats database schema information
- `execute_sql_query(connection, sql_query)`: Executes the generated SQL query

### Model Utilities (`model_utils.py`)

- `generate_sql_query(text_prompt, schema_info, model_name)`: Generates SQL query from natural language using Groq API

## Environment Variables

- `GROQ_API_KEY`: Your Groq API key for accessing the LLM service

## Error Handling

The application includes error handling for:
- Database connection failures
- Schema retrieval errors
- Query generation failures
- Query execution errors

## Security Considerations

- Database credentials should be stored securely
- API keys should be managed through environment variables
- Input validation is recommended before query execution
- Connection closing is handled automatically

## Limitations

- Requires active internet connection for Groq API access
- Query generation accuracy depends on the LLM model
- Limited to MySQL syntax
- Schema retrieval may be slow for large databases


