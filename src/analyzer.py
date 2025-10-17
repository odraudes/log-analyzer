import re
import csv

# Configuración básica
LOG_FILE = "examples/sample-log.txt"
REPORT_FILE = "reports/report.csv"

# Patrón de búsqueda: intentos fallidos de login
pattern = re.compile(r"Failed password for (\w+) from (\d+\.\d+\.\d+\.\d+)")

results = []

with open(LOG_FILE, "r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            user, ip = match.groups()
            results.append([user, ip, line.strip()])

# Guardar reporte
with open(REPORT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["User", "IP", "Log line"])
    writer.writerows(results)

print(f"Reporte generado en {REPORT_FILE}")
