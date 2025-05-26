from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Welcome!</title>
  <style>
    body {
      background: #f2f2f2;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .card {
      background: white;
      padding: 2rem;
      border-radius: 1rem;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      text-align: center;
    }
    h1 {
      color: #333;
    }
    p {
      color: #666;
    }
    a {
      display: inline-block;
      margin-top: 1rem;
      color: #007BFF;
      text-decoration: none;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
    <a href="/about">About This App</a>
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, title="Welcome!", message="This is the new and improved version of the old website.")

@app.route("/about")
def about():
    return render_template_string(HTML_TEMPLATE, title="About", message="This app is built with Flask in a single file and styled with love.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
