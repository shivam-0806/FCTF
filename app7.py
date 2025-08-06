from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def behind_the_curtains():
    user_agent = request.headers.get('User-Agent', '')
    flag = "pclub{cur10us_br0wser_h34der}"
    
    # Check if the custom User-Agent is present
    if 'pclub_browser' in user_agent:
        message = f"<p>The flag can only be obtained by <code>pclub_browser.</code><br>{flag}</p>"
    else:
        message = "<p>The flag can only be obtained by <code>pclub_browser</code><br>No flag for you. Try peeking behind the curtain...</p>"

    # HTML response
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Behind the Curtains</title>
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

        code {{
        background: #222;
        padding: 2px 6px;
        border-radius: 4px;
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
        <h1>Behind The Curtains</h1>
        <p>{message}</code></p>
    </div>
    </body>
    </html>

    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
