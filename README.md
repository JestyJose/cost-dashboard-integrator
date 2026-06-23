# Cost Dashboard Integrator

## Objective
Generate AWS cost dashboard JSON from PostgreSQL data.

## Requirements
- Python
- PostgreSQL
- psycopg2-binary

## Installation

pip install -r requirements.txt

## Run

python app.py

## Tables Used
- aws_resources
- aws_costs
- top_cost_resources

## Output
Generates output.json containing aggregated AWS cost data.

## Example JSON Output

```json
{
  "submitted_by": "jestyjose@mulearn",
  "services": {
    "EC2": {
      "total_cost": 125.50,
      "resources": [
        {
          "resource_id": 1,
          "resource_name": "web-server",
          "cost": 75.50
        }
      ]
    }
  }
}
```

## Implementation

This project connects to a PostgreSQL database using psycopg2. It queries data from aws_resources, aws_costs, and top_cost_resources tables, aggregates cost information by AWS service type, and generates a structured JSON output for frontend dashboard integration.

## Submitted By
jestyjose@mulearn
