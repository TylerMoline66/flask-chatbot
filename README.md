````markdown
## Setup

1. **Initialize Python Shell**:
   If you're using Pipenv for managing dependencies, you can initialize a Python shell using the following command:
   ```bash
   python3 -m pipenv shell
   ```
````

2. **Install Dependencies**:
   Install project dependencies using Pipenv:

   ```bash
   pipenv install
   ```

3. **Configure MySQL**:
   Edit `app.py` to set your MySQL database configuration:

   ```python
   app.config['MYSQL_HOST'] = 'localhost'
   app.config['MYSQL_USER'] = 'your_username'
   app.config['MYSQL_PASSWORD'] = 'your_password'
   app.config['MYSQL_DB'] = 'your_database'
   ```

4. **Run the Flask App**:
   Start the Flask app using the following command:
   ```bash
   python app.py
   ```
   The app will run on `http://localhost:3000/`.

```

This will guide users to initialize a Python shell using Pipenv before installing dependencies and configuring the MySQL database.
```
