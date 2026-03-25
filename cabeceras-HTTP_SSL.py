#!/usr/bin/env python3

import requests
import sys

# Colores tipo SOC
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def check_header(headers, header_name):
    return header_name.lower() in (h.lower() for h in headers.keys())

def print_result(status, message):
    if status == "OK":
        print(f"{GREEN}[OK]{RESET} {message}")
    elif status == "FAIL":
        print(f"{RED}[FAIL]{RESET} {message}")
    elif status == "WARN":
        print(f"{YELLOW}[WARN]{RESET} {message}")

def analyze_headers(url):
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers

        print(f"\n{BLUE}🔍 Analizando:{RESET} {url}")
        print("-" * 50)

        # Checks principales
        checks = {
            "Strict-Transport-Security": "HSTS",
            "Content-Security-Policy": "CSP",
            "X-Frame-Options": "Clickjacking Protection",
            "X-Content-Type-Options": "MIME Sniffing Protection",
            "X-XSS-Protection": "XSS Protection (legacy)",
            "Referrer-Policy": "Referrer Policy",
            "Permissions-Policy": "Permissions Policy"
        }

        score = 0

        for header, desc in checks.items():
            if check_header(headers, header):
                print_result("OK", desc)
                score += 1
            else:
                print_result("FAIL", desc)

        print("-" * 50)
        print(f"{BLUE}🧠 Fingerprinting:{RESET}")

        # Server header
        if "Server" in headers:
            print_result("WARN", f"Server: {headers.get('Server')}")
        else:
            print_result("OK", "Server header oculto")

        # X-Powered-By
        if "X-Powered-By" in headers:
            print_result("WARN", f"X-Powered-By: {headers.get('X-Powered-By')}")
        else:
            print_result("OK", "X-Powered-By oculto")

        print("-" * 50)

        # Score final
        total = len(checks)
        percentage = (score / total) * 100

        print(f"{BLUE}📊 Score de Seguridad:{RESET} {score}/{total} ({percentage:.0f}%)")

        if percentage == 100:
            print(f"{GREEN}Nivel: A+ (Excelente){RESET}")
        elif percentage >= 80:
            print(f"{GREEN}Nivel: A (Bueno){RESET}")
        elif percentage >= 60:
            print(f"{YELLOW}Nivel: B (Aceptable){RESET}")
        else:
            print(f"{RED}Nivel: C o menor (Mejorar urgente){RESET}")

    except requests.exceptions.RequestException as e:
        print(f"{RED}[ERROR]{RESET} No se pudo conectar: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: python3 headers_check.py https://example.com")
        sys.exit(1)

    url = sys.argv[1]

    if not url.startswith("http"):
        url = "https://" + url

    analyze_headers(url)
