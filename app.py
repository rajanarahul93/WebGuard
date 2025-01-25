from flask import Flask, render_template, request
from scanner import crawl_website, detect_sql_injection, detect_xss

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form.get('url')
    links = crawl_website(url)
    sql_injection_result = detect_sql_injection(url)
    xss_result = detect_xss(url)

    return render_template(
        'index.html',
        url=url,
        links=links,
        sql_injection_result=sql_injection_result,
        xss_result=xss_result,
    )

if __name__ == "__main__":
    app.run(debug=True)
