# What it is

This repository provides trending and customized GitHub repositories based on user-defined filters.

# How to setup:

1. Create a separate virtual environment in your local system.
2. Activate the virtual environment.
3. Install the required packages:
```bash
pip install requirements.txt
```
4. Add your GitHub Personal Access Token in a .env file (or any custom file you prefer). Add this ACCESS_TOKEN in .env file with your access token.
5. Run the backend server using Uvicorn:
```bash
uvicorn main:app --port <port_number> --reload
```
6. Test the backend server with a sample cURL request:
   ```bash
   curl http://localhost:<port_number>/test-cors
   ```
7. For the UI, update the placeholder your_backend_url_endpoint with your local server endpoint, which should look like:```[http://localhost:<port_number>/repos]```.
8. Run the frontend using Live Server in VS Code.
9. Open the frontend in your browser, fill out the form, and get repository details as per your request.
10.If you face any issues with responses from the backend, check the CORS middleware settings in __main.py__

# Conclusion:
This small project helps you discover GitHub repositories based on custom filters. You can easily extend the backend by adding more query options to suit your needs.
# Sample Image
<img width="1199" height="916" alt="Screenshot 2025-08-26 161208" src="https://github.com/user-attachments/assets/3d006f10-5487-4a4b-92db-0e4dfebac901" />
