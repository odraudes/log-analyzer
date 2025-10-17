import re
import csv
import yaml
from pathlib import Path

# Cargar configuración
with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

log_file = Path("examples/sample-log.txt")
report_file = Path(config["report_file"])

results = []

# Leer logs
with open(log_file, "r") as f:
    lines = f.readlines()

# Aplicar reglas
for pattern_name, pattern_info in config["patterns"].items():
    regex = re.compile(pattern_info["regex"])
    level = pattern_info["level"]
    for line in lines:
        match = regex.search(line)
        if match:
            results.append([pattern_name, *match.groups(), level, line.strip()])

# Guardar reporte
with open(report_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Pattern", "User", "IP", "Level", "Log line"])
    writer.writerows(results)

print(f"[✅] Reporte generado en {report_file}")
