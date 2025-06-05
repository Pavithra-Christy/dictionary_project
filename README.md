# 📘 Django Dictionary App

A clean and responsive Django application that lets users search for word definitions, phonetics, and usage examples using the [Free Dictionary API](https://dictionaryapi.dev). All searches are logged in a MySQL database.

---

## 🚀 Features

- 🔍 **Search Words** – Instantly fetch definitions, parts of speech, and phonetics
- 🗃️ **Search Log** – Stores searched words with timestamps in MySQL
- 🌐 **External API** – Integrates with [dictionaryapi.dev](https://dictionaryapi.dev)
- 🔐 **Environment Variables** – Secure DB credentials using `.env`
- 📱 **Responsive UI** – Clean, readable HTML5-based design

---

## 🖼️ Screenshots

> Example:  
> ![Search Page](screenshots/search.png)

---

## 🛠️ Tech Stack

- **Backend:** Django 5.2.1  
- **Database:** MySQL  
- **API:** [dictionaryapi.dev](https://dictionaryapi.dev)  
- **Styling:** HTML5 + Basic CSS  
- **Environment:** python-dotenv  

---

## ⚙️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/dictionary_project.git
cd dictionary_project

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate   # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup environment variables
cp .env.example .env   # or manually create .env file

# 5. Run migrations
python manage.py makemigrations
python manage.py migrate

# 6. Start the development server
python manage.py runserver
````

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 📂 Folder Structure

```
dictionary_project/
│
├── dictionary_app/
│   ├── templates/
│   │   └── search.html
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── dictionary_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .env
├── manage.py
└── requirements.txt
```

---

## 📄 License

This project is for learning purposes.

---
