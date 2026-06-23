import psycopg2
import json
from config import DB_CONFIG

conn = psycopg2.connect(**DB_CONFIG)
cursor = conn.cursor()

# Query data
cursor.execute("""
SELECT
    r.resource_id,
    r.resource_name,
    r.service_type,
    c.cost_amount,
    c.billing_month
FROM aws_resources r
JOIN aws_costs c
ON r.resource_id = c.resource_id
""")

rows = cursor.fetchall()

dashboard = {
    "submitted_by": "jestyjose@mulearn",
    "services": {}
}

for row in rows:
    resource_id, resource_name, service_type, cost, billing_month = row

    if service_type not in dashboard["services"]:
        dashboard["services"][service_type] = {
            "total_cost": 0,
            "resources": []
        }

    dashboard["services"][service_type]["total_cost"] += float(cost)

    dashboard["services"][service_type]["resources"].append({
        "resource_id": resource_id,
        "resource_name": resource_name,
        "cost": float(cost),
        "billing_month": billing_month
    })

with open("output.json", "w") as f:
    json.dump(dashboard, f, indent=4)

print(json.dumps(dashboard, indent=4))

cursor.close()
conn.close()
