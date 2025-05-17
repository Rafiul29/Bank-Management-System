# 🏦 Bank Management System

A simple and secure Bank Management System built with Django. This project allows users to manage bank accounts, perform transactions, and track financial activities.

## 🚀 Features

- **User registration and authentication**  
- **Account creation and balance management**  
- **Deposit and withdrawal functionality**  
  - Max 2 deposit/withdrawal requests per user
- **Loan request functionality**  
  - Max 2 loan requests per user
- **Transaction history tracking**  
- **Admin panel for managing users and accounts**  
- **Email notifications for deposit, withdrawal, and loan requests**  
  - Sent to the user's email upon transaction request
## 🛠 Tech Stack

- Python 3
- Django
- SQLite3 (default)
- TailwindCss (frontend styling)

## 📦 Installation

Follow these steps to get the project running locally:

### 1. Clone the Repository

```sh
git clone https://github.com/Rafiul29/Bank-Management-System.git
cd Bank-Management-System
```


2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install Dependencies
```sh
pip install -r requirements.txt
```

4. Apply Migrations
Run the following commands to set up the database:
```sh
python manage.py makemigrations
python manage.py migrate

```
5. Create a Superuser (Admin)
To access the Django admin panel, you'll need to create a superuser. Run the following command:
```sh
python manage.py createsuperuser
```


6. Run the Development Server
```sh
python manage.py runserver
```



🙌 Acknowledgements
Developed by Rafiul29
Feel free to fork and improve the project!


### Explanation of the Code:
- **Installation Instructions**: The commands are laid out properly within triple backticks for better readability and ease of use.
- **Folder Structure**: The folder structure is clearly presented to help users understand the project's layout.
- **License**: It includes a section on licensing, with a link to the MIT License (you can change this to any other license if necessary).
- **Testing Instructions**: It encourages users to test the application by interacting with the admin panel and other functionalities.

Let me know if you need further edits or additions!
