# Simple Threat Modeling Simulation
systems = [
    {"name": "Web App", "impact": 5, "likelihood": 4},
    {"name": "Database", "impact": 5, "likelihood": 3},
    {"name": "API Gateway", "impact": 4, "likelihood": 2},
]

print("Threat Modeling Simulation\n")
for system in systems:
    risk_score = system["impact"] * system["likelihood"]
    print(f"{system['name']} -> Risk Score: {risk_score}")

print("\nHigh risk systems need mitigation!")
