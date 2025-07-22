# 🔍 Secure Code Review – Vulnerability Report

**Project Name**: Vulnerable Python CLI Application  
**Intern Name**: Anshika Raj  
**Internship Program**: CodeAlpha – Cyber Security Virtual Internship  
**Task**: Task 3 – Secure Coding Review  
**Duration**: 20th June 2025 – 20th July 2025

---

## 📄 Overview
This document provides a detailed vulnerability assessment of a Python-based CLI application developed as part of Task 3 for the CodeAlpha Cyber Security Internship. The purpose of this review is to identify common coding flaws that can lead to security breaches and to recommend appropriate mitigation strategies.

---

## 📁 Application Reviewed
**File**: `vulnerable_app/app.py`

---

## ⚠️ Identified Vulnerabilities

### 1. Hardcoded Credentials
- **Code Snippet**:
  ```python
  if username == "admin" and password == "admin123":
  ```
- **Risk**: Storing credentials directly in code exposes them to anyone with access to the source.
- **Recommendation**: Store credentials securely using environment variables or a secrets manager.

---

### 2. Insecure Password Input
- **Code Snippet**:
  ```python
  password = input("Enter password: ")
  ```
- **Risk**: `input()` displays password on the screen.
- **Recommendation**: Use `getpass.getpass()` to securely accept password input.

---

### 3. Command Injection
- **Code Snippet**:
  ```python
  os.system(command)
  ```
- **Risk**: Executes arbitrary system commands. Vulnerable to command injection.
- **Recommendation**: Avoid `os.system()`. Use `subprocess.run()` with strict input validation.

---

### 4. Use of `eval()` Function
- **Code Snippet**:
  ```python
  print(eval(expression))
  ```
- **Risk**: Evaluates arbitrary Python code input by the user. High risk of code execution.
- **Recommendation**: Remove use of `eval()`. If parsing is required, use `ast.literal_eval()` for safer evaluation.

---

### 5. Silent Exception Handling
- **Code Snippet**:
  ```python
  except:
      pass
  ```
- **Risk**: Suppresses all runtime errors, making debugging and monitoring difficult.
- **Recommendation**: Catch specific exceptions and log errors appropriately.

---

## 🛠️ Tools Used
- **Bandit (Python Security Linter)**
  - Command: `bandit -r vulnerable_app/`
  - **Findings**:
    - High: Use of `eval()` and `os.system()`
    - Medium: Hardcoded passwords

---

## ✅ Conclusion
The reviewed application contains multiple critical security vulnerabilities that must be addressed to ensure safe deployment. By implementing the recommended changes, the application can be significantly hardened against common cyber threats.

---

## 👩‍💻 Performed By
**Anshika Raj**  
Cyber Security Intern  
CodeAlpha | June–July 2025

---

## 📌 Notes
This project and report are submitted as part of the Task 3 requirements for the CodeAlpha Cyber Security Internship Program. This report was created for educational purposes only.
