# Architecture Primer

## What You'll Learn
- How web applications work
- Client vs Server architecture
- The Request/Response lifecycle
- How data flows through a web app

---

## 1. Client vs Server

### The Big Picture

Think of a restaurant:
- **Client** (you, the customer) = Web Browser
- **Server** (kitchen) = Your Python Application
- **Request** (your order) = HTTP Request
- **Response** (your meal) = HTTP Response

```
┌─────────────┐                          ┌─────────────┐
│   Browser   │  ────── Request ──────>  │   Server    │
│  (Client)   │                          │  (Python)   │
│             │  <───── Response ──────  │             │
└─────────────┘                          └─────────────┘
```

### Client (Frontend)
**What it does:**
- Displays web pages (HTML)
- Handles styling (CSS)
- Adds interactivity (JavaScript)
- Sends requests to server
- Receives and displays responses

**Where it runs:** In the user's web browser

**Example:** When you type a URL and press Enter, your browser (client) sends a request.

### Server (Backend)
**What it does:**
- Receives requests from clients
- Processes business logic
- Interacts with databases
- Sends responses back to clients

**Where it runs:** On a remote computer (or your local machine during development)

**Example:** Your Flask/FastAPI app receives the request, fetches data from SQLite, and sends HTML back.

---

## 2. Request/Response Lifecycle

### Step-by-Step Breakdown

Let's trace what happens when you visit `http://localhost:5000/notes`:

```
1. User Action
   └─> User types URL in browser and presses Enter

2. Browser (Client)
   └─> Creates HTTP GET request
   └─> Sends to http://localhost:5000/notes

3. Server (Flask/FastAPI)
   └─> Receives request
   └─> Routes to correct function: @app.route('/notes')
   └─> Function runs (might query database)
   └─> Generates HTML response
   └─> Sends response back to browser

4. Browser (Client)
   └─> Receives HTML response
   └─> Renders page for user to see
```

### HTTP Methods

Different types of requests for different actions:

| Method | Purpose | Example |
|--------|---------|---------|
| **GET** | Retrieve data | Show list of notes |
| **POST** | Create new data | Submit a new note form |
| **PUT** | Update existing data | Edit a note |
| **DELETE** | Remove data | Delete a note |

### Example Request

When you submit a form:
```http
POST /notes HTTP/1.1
Host: localhost:5000
Content-Type: application/x-www-form-urlencoded

title=My+Note&content=This+is+my+note
```

### Example Response

Server sends back:
```http
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head><title>Notes</title></head>
<body><h1>Note created!</h1></body>
</html>
```

---

## 3. How Data Flows Through a Web App

### The Full Journey

```
┌──────────────────────────────────────────────────────────────┐
│                    WEB APPLICATION                            │
│                                                               │
│  ┌─────────┐      ┌─────────┐      ┌──────────┐            │
│  │ Browser │ ───> │  Flask  │ ───> │ SQLite   │            │
│  │ (HTML/  │      │ (Python │      │ Database │            │
│  │  CSS)   │      │  Code)  │      │          │            │
│  │         │ <─── │         │ <─── │          │            │
│  └─────────┘      └─────────┘      └──────────┘            │
│    Frontend         Backend          Storage                │
└──────────────────────────────────────────────────────────────┘
```

### Detailed Example: Creating a Note

**1. User Action (Frontend)**
```html
<!-- User sees this form -->
<form action="/notes" method="POST">
    <input type="text" name="title" placeholder="Note title">
    <textarea name="content" placeholder="Note content"></textarea>
    <button type="submit">Save Note</button>
</form>
```

**2. Request Sent**
- User clicks "Save Note"
- Browser sends POST request to `/notes` with form data
- Data travels over network to server

**3. Server Processes (Backend)**
```python
# Flask receives the request
@app.route('/notes', methods=['POST'])
def create_note():
    # Extract data from request
    title = request.form['title']
    content = request.form['content']
    
    # Validate data
    if not title or not content:
        return "Error: Both fields required", 400
    
    # Save to database
    db.execute(
        "INSERT INTO notes (title, content) VALUES (?, ?)",
        (title, content)
    )
    
    # Return response
    return redirect('/notes')
```

**4. Database Interaction**
```sql
-- SQLite stores the data
INSERT INTO notes (title, content, created_at) 
VALUES ('My Note', 'This is my note', '2024-01-15 10:30:00');
```

**5. Response Sent Back**
- Server sends redirect response
- Browser automatically requests `/notes` (GET)
- Server queries database for all notes
- Server renders HTML with note list
- Browser displays updated page

---

## 4. Web App Components

### Frontend (What Users See)
```html
<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>Welcome!</h1>
    <form action="/submit" method="POST">
        <input type="text" name="data">
        <button>Submit</button>
    </form>
</body>
</html>
```

### Backend (Python Logic)
```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']
    # Process data
    return "Success!"
```

### Database (Data Storage)
```sql
-- SQLite stores persistent data
CREATE TABLE notes (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 5. Key Concepts to Remember

### Stateless Protocol
- HTTP is stateless - each request is independent
- Server doesn't remember previous requests
- We use **sessions** and **cookies** to maintain state

### Routing
- Maps URLs to Python functions
- `/` → home page
- `/notes` → notes list
- `/notes/5` → specific note with ID 5

### Templates
- HTML files with placeholders
- Server fills in dynamic data
- Separates presentation from logic

### Static Files
- CSS, JavaScript, images
- Don't change per request
- Served directly without processing

---

## 6. Mini Exercise

Let's trace what happens for: `http://localhost:5000/hello?name=Alice`

**Question:** What are the steps?

<details>
<summary>Click to see answer</summary>

1. **User Action:** User types URL in browser
2. **HTTP Request:** Browser sends GET request to `/hello` with query parameter `name=Alice`
3. **Server Routing:** Flask matches `/hello` route
4. **Handler Function:** 
   ```python
   @app.route('/hello')
   def hello():
       name = request.args.get('name', 'World')
       return f"<h1>Hello, {name}!</h1>"
   ```
5. **Response Generated:** HTML string `<h1>Hello, Alice!</h1>`
6. **Response Sent:** Server sends 200 OK with HTML
7. **Browser Renders:** User sees "Hello, Alice!" on screen

</details>

---

## 7. Practice Problems

Ready to test your understanding? Complete the **[Practice Problems](./practice-problems.md)** to verify your knowledge!

**What you'll work on:**
- Trace request/response journeys through the system
- Design RESTful URL structures
- Debug common architectural issues

These exercises help solidify web architecture concepts.

---

## 8. Ready for Projects?

Now that you understand:
- ✅ Client vs Server roles
- ✅ Request/Response cycle
- ✅ Data flow through an app
- ✅ Key web components

You're ready to build your first project!

**Next:** [Notes App](../../projects/02-notes-app/) - Build a CRUD application

---

## 9. Quick Reference

### HTTP Status Codes
- `200 OK` - Success
- `201 Created` - Resource created
- `400 Bad Request` - Invalid client request
- `404 Not Found` - Resource doesn't exist
- `500 Internal Server Error` - Server error

### Common Headers
- `Content-Type: text/html` - Response contains HTML
- `Content-Type: application/json` - Response contains JSON
- `Location: /notes` - Redirect to this URL

### URL Parts
```
http://localhost:5000/notes/5?sort=date#top
│      │         │    │      │       │
scheme   host    port  path  query  fragment
```
