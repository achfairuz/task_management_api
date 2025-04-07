# Task Management API - FastAPI

A **Task Management** application built with **FastAPI** using **JWT Bearer Token** authentication. Only admin users have access to create categories; aside from category creation, token authentication is not required.

---

## 📁 Folder Structure

```
.
├── auth/
│   └── auth.py
├── models/
│   └── models.py
├── routes/
│   ├── auth_routes.py
│   ├── category.py
│   └── task.py
├── schema/
│   ├── schema_user.py
│   ├── schema_category.py
│   └── schema_task.py
├── alembic/
├── main.py
├── alembic.ini
├── requirements.txt
└── .env
```

---

## ⚙️ Features

| Module      | Features                                                                                                                |
| ----------- | ----------------------------------------------------------------------------------------------------------------------- |
| 🔐 Auth     | - Login and Register (default role: `user`)                                                                             |
| 👥 Role     | - Admin role must be manually set in the database                                                                       |
| 📂 Category | - `GET /categories` for all users<br>- `POST /categories` for admin only                                                |
| ✅ Task     | - CRUD Tasks: `GET`, `POST`, `PUT`, `DELETE`<br>- `GET` by ID<br>- `GET` by `category_id` or `status` (with pagination) |

---

## 🔐 Authentication

- Only **admin** users receive a JWT Bearer Token.
- This token is required to access the `POST /categories` endpoint.

---

## 🔓 Open Endpoints

- `POST /register` - Registers a new user (default role: user)
- `POST /login` - Logs in the user

Use `application/x-www-form-urlencoded` for body:

```
username: your_username
password: your_password
```

---

## 🔐 Protected Endpoints

- **Swagger UI**: Click “Authorize” and enter the token.
- **Postman**:
  1. Login via `/login`
  2. Copy the token from the response (admin only)
  3. On `POST /categories`, go to **Authorization tab**
  4. Set type to **Bearer Token** and paste the token

---

## 📆 Endpoints Summary

### 🔸 Auth

```
POST /register
POST /login
```

### 🔸 Category (JSON)

```
GET /categories
POST /categories  # admin only
```

### 🔸 Task (JSON)

```
GET /tasks
GET /tasks/{task_id}
GET /tasks/filter?category_id=1
GET /tasks/filter?status=done
POST /tasks
PUT /tasks/{task_id}
DELETE /tasks/{task_id}
```

Pagination sample:

```
http://127.0.0.1:8000/tasks/filter?status=to-do&category_id=17&page=1&per_page=10
```

---

## 📘 Swagger UI

Swagger is available at:

```
http://localhost:8000/docs
```

Public Postman Collection:

[Postman Workspace](https://www.postman.com/quirkly/workspace/task-management-api)

---

## 🚀 Getting Started

```bash
# 1. Activate virtual environment
venv\Scripts\activate

# 2. Install requirements
pip install -r requirements.txt

# 3. Alembic migrations (if not initialized)
alembic init alembic

# 4. Create & apply migration
alembic revision --autogenerate -m "initial"
alembic upgrade head

# 5. Run the app
uvicorn main:app --reload
```

---

## ⚠️ Notes

- If bcrypt version error occurs:

```bash
pip install bcrypt==3.2.0 passlib==1.7.4
```

---

## 🛠 Technologies

- FastAPI
- SQLAlchemy
- Alembic
- JWT (via `jose`)
- PostgreSQL
- Swagger UI

---

# 🇮🇩 Task Management API - Bahasa Indonesia

Aplikasi **Manajemen Tugas** dengan **FastAPI** dan autentikasi **JWT Bearer Token**. Hanya admin yang bisa membuat kategori. Endpoint lainnya tidak memerlukan token.

## 📁 Struktur Folder

(Sama seperti di atas)

## ⚙️ Fitur

| Modul       | Fitur                                                                                                                                  |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 🔐 Auth     | - Login dan Register (role default: `user`)                                                                                            |
| 👥 Role     | - Role admin harus diatur manual di database                                                                                           |
| 📂 Category | - `GET /categories` untuk semua user<br>- `POST /categories` hanya untuk admin                                                         |
| ✅ Task     | - CRUD task: `GET`, `POST`, `PUT`, `DELETE`<br>- `GET` berdasarkan ID<br>- Filter berdasarkan kategori atau status (dengan pagination) |

## 🔐 Autentikasi

- Hanya user dengan role admin yang mendapatkan JWT Token
- Token diperlukan untuk mengakses `POST /categories`

## 🔓 Endpoint Terbuka

- `POST /register` – daftar user baru (role: user)
- `POST /login` – login (admin akan menerima token)

Gunakan `application/x-www-form-urlencoded`:

```
username: str
password: str
```

## 🔐 Endpoint Terproteksi

- **Swagger UI**: klik "Authorize", masukkan token.
- **Postman**:
  1. Login ke `/login`
  2. Copy token dari response (jika admin)
  3. Pada endpoint `POST /categories`, buka tab Authorization
  4. Pilih **Bearer Token**, lalu paste token

## 📘 Swagger

Swagger UI dapat diakses melalui:

```
http://localhost:8000/docs
```

Postman Workspace Publik:

[Postman Workspace](https://www.postman.com/quirkly/workspace/task-management-api)

## 🚀 Menjalankan Project

```bash
venv\Scripts\activate
pip install -r requirements.txt
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
uvicorn main:app --reload
```

## 🛠 Teknologi

- FastAPI
- SQLAlchemy
- Alembic
- JWT (dengan jose)
- PostgreSQL
- Swagger UI
