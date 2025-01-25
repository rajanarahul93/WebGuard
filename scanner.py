import requests
from bs4 import BeautifulSoup

def crawl_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            return links
        else:
            return []
    except Exception as e:
        print(f"Error occurred while crawling: {e}")
        return []

def detect_sql_injection(url):
    payload = "' OR '1'='1"
    test_url = f"{url}?id={payload}"
    try:
        response = requests.get(test_url)
        if "error" in response.text.lower() or "mysql" in response.text.lower():
            return "Potential SQL Injection vulnerability found!"
        else:
            return "No SQL Injection vulnerability detected."
    except Exception as e:
        return f"Error during SQL injection detection: {e}"

def detect_xss(url):
    xss_payload = "<script>alert('XSS')</script>"
    test_url = f"{url}?q={xss_payload}"
    try:
        response = requests.get(test_url)
        if xss_payload in response.text:
            return "Potential XSS vulnerability found!"
        else:
            return "No XSS vulnerability detected."
    except Exception as e:
        return f"Error during XSS detection: {e}"
