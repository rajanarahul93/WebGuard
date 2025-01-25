# 🌐 WebGuard: Vulnerability Scanner

**WebGuard** is a Python-powered web vulnerability scanner designed to identify potential security risks in web applications. This project demonstrates an understanding of **OWASP vulnerabilities**, including SQL Injection, Cross-Site Scripting (XSS), and other common threats, while offering an intuitive user interface.

---

## 🚀 Features
- **Automated Website Crawling**: Scans and collects all accessible links from the provided URL.
- **Vulnerability Detection**:
  - Detects potential **SQL Injection** vulnerabilities.
  - Identifies **Cross-Site Scripting (XSS)** risks.
- **Summary Reports**: Displays crawled links and vulnerabilities in a user-friendly format.
- **Customizable UI**: Built with Flask and styled with modern CSS for an intuitive experience.

---

## 📋 Requirements
To run this project, ensure the following dependencies are installed:

- Python 3.8+
- Flask
- Requests
- Beautiful Soup 4

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## 🛠️ Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/rajanarahul93/WebGuard.git
cd WebGuard
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Start the Flask server:
```bash
python app.py
```
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

### 4. Scan a Website
- Enter the URL of the website you wish to scan.
- Click on **Scan** to get a detailed report of vulnerabilities and crawled links.

---


## 🌟 How It Works
1. **Website Crawling**:
   - Uses Python's `requests` and `BeautifulSoup` libraries to extract all accessible links from the provided URL.
2. **Vulnerability Detection**:
   - Simulates potential SQL injection and XSS attacks to identify vulnerabilities.
3. **Reporting**:
   - Displays crawled links and vulnerabilities in a clear and concise format.

---

## ⚠️ Disclaimer
**WebGuard** is designed for educational purposes only. Ensure you have permission before scanning any website. Unauthorized scanning may violate local laws and regulations.

---

## 💡 Future Enhancements
- Add detection for **CSRF** and other vulnerabilities.
- Export results to a PDF or JSON file.
- Include an option for advanced scan modes.
- Enhance UI with additional frameworks like React or Bootstrap.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

---

## 👨‍💻 Author
**Your Name**  
- GitHub: [@rajanarahul93](https://github.com/rajanarahul93)  
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/vara-rahul-rajana)
