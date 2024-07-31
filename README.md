# MongoDB_Project
 Cloud Computing Project

## Overview
The purpose of this project is to create an adaptable database in MongoDB to store/catalog items with input through a user interface coded in Python.

### Goals
1. Wanted to understand and learn how MongoDB works and its benefits and drawbacks of using it over other databases.
2. Also wanted to understand the structure of MongoDB and database collections.

### Testbed and Software Tools
1. **MongoDB**: NoSQL database used to store and manage the catalog items.
2. **MongoDB Compass**: A graphical UI that helped to visualize and interact with the MongoDB database, making it easier to check on the data.
3. **Python**: Was the language used to work with the backend.
4. **Flask**: A framework for Python, I used it to create the web interface and API endpoints.
5. **VSCode (Visual Studio Code)**: IDE used for writing and managing the project's codebase.
6. **Postman**: This tool was really useful for testing the API endpoints to make sure that they work correctly, letting me do manual interfacing with the application's backend.
7. **PyMongo**: Python library for interacting with MongoDB, only used it to do the CRUD operations on the database in the Flask application.

### Functionalities of the Application
1. **Add Items**: Users can add new items to the catalog using a form on the web interface.
2. **View Items**: Users can view all current items in the catalog.
3. **Update Items**: Users can update existing items using an update form.
4. **Delete Items**: Users can delete existing items from the catalog.

### Setup and Running of Application

1. **Start MongoDB Server**: In a different terminal run
   mongod

2. **Create the Virtual Environment**:
python -m venv venv    

3. **Activate Virtual Environment**:
   .\venv\Scripts\Activate

4. **Install Required Packages**:
pip install -r requirements.txt

5. **Run Flask Application**:
   python app.py

### Verify the Data using MongoDB Compass:

1. Open MongoDB Compass
2. Connect to your MongoDB instance using mongodb://localhost:27017/ URI
3. Then go to the catalogDB database
4. Go to items
5. You should see changes from Postman in database here

### Testing with Postman

1. **GET all items**:
   - **Request Type**: GET
   - **URL**: `http://127.0.0.1:5000/items`
   - **Action**: Click "Send".
   - **Expected Result**: You should see a JSON array that has all of the items in the items collection

2. **POST a new item**:
   - **Request Type**: POST
   - **URL**: `http://127.0.0.1:5000/items`
   - **Body**: 
        json
     {
       "name": "item1",
       "description": "This is item 1"
     }
   - **Action**: Click "Send".
   - **Expected Result**: Adds a new item

3. **PUT to update an item**:
   - **Request Type**: PUT
   - **URL**: `http://127.0.0.1:5000/items`
   - **Body**:
        json
     {
       "query": {"name": "item1"},
       "new_values": {"description": "Updated description"}
     }
   - **Action**: Click "Send".
   - **Expected Result**: A JSON response showing that the item was updated

4. **DELETE an item**:
   - **Request Type**: DELETE
   - **URL**: `http://127.0.0.1:5000/items`
   - **Body**:
        json
     {
       "name": "item1"
     }
   - **Action**: Click "Send".
   - **Expected Result**: Should see that said item was deleted

5. **GET an item by name**:
   - **Request Type**: GET
   - **URL**: http://127.0.0.1:5000/items/<name>
   - **Action**: Click "Send"
   - **Expected Result**: You should see a JSON object of the item with the specified name

6. **Filter items by date range**:

   - **Request Type**: GET
   - **URL**: http://127.0.0.1:5000/items?start_date=<start_date>&end_date=<end_date>
   - **Action**: Click "Send"
   - **Expected Result**: You should see a JSON array of items that fall within the specified date range   

### Conclusion ###
This project helped me learn how to use MongoDB with Python to be able to perform CRUD (Create, Read, Update, Delete) operations. 
I was able to see firsthand the advantages of using a NoSQL database, such as flexibility and scalability.
Working on this project also gave me practical experience in managing a database through a simple web interface and RESTful APIs.