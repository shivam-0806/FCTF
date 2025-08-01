from flask import Flask, request, make_response
import base64
import json

app = Flask(__name__)

@app.route('/')
def not_the_edible_kind():
    # Try to decode cookie
    cookie = request.cookies.get("session")
    flag = "pclub{c00kie_priv1leg3_escalat3d}"

    is_admin = False
    if cookie:
        try:
            decoded = base64.b64decode(cookie).decode()
            data = json.loads(decoded)
            is_admin = data.get("admin") == 1
        except Exception:
            pass  # silently ignore errors

    # Build HTML response
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Not the Edible Kind</title>
    <style>
        body {{
        margin: 0;
        height: 100vh;
        background: #000;
        color: #fff;
        font-family: Arial, sans-serif;
        display: flex;
        align-items: center;
        justify-content: center;
        }}

        .container {{
        text-align: center;
        max-width: 800px;
        padding: 40px;
        line-height: 1.6;
        }}

        h1 {{
        font-size: 2em;
        margin-bottom: 20px;
        }}

        p {{
        font-size: 1.2em;
        }}

        img {{
        margin-top: 30px;
        max-width: 100%;
        border: 2px solid #fff;
        }}
    </style>
    </head>
    <body>
    <div class="container">
        <h1>Not the Edible Kind</h1>
        <p>This cookie may not be sweet, but it's got a secret baked in.</p>
        {"<p><code>" + flag + "</code></p>" if is_admin else ""}
    </div>
    </body>
    </html>

    """

    # If no cookie, set one with admin: 0
    if not cookie:
        payload = base64.b64encode(json.dumps({"admin": 0}).encode()).decode()
        resp = make_response(html)
        resp.set_cookie("session", payload)
        return resp

    return html

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
