# IPEDS dbt Integration 

This project models IPEDS (Integrated Postsecondary Education Data System) data using dbt on Snowflake.
It transforms raw annual survey tables (graduation, enrollment, etc.) into well-structured, analysis-ready marts.

## Sources

Raw IPEDS data is loaded into Snowflake under:
* Database: IPEDS
* Schema: RAW
* Tables: GRAD2020, GRAD2021, GRAD2022, GRAD2023, …

Example declaration (`models/sources/ipeds_sources.yml`):
```yaml
sources:
  - name: raw_ipeds
    database: IPEDS
    schema: RAW
    tables:
      - name: GRAD2020
      - name: GRAD2021
      - name: GRAD2022
      - name: GRAD2023
```

## Models
1. Staging (stage__gradYYYY)

OBrings in raw data from RAW.GRADYYYY. Applies light cleaning and adds a survey_year column.

2. Dimensions

Lookup tables that map survey codes → human-readable labels.

Examples: `dim_cohort`, `dim_grtype`, `dim_section`.

3. Marts

Combine staging and dimensions for analytics.

Example: `models/marts/graduation.sql` unions multiple years of graduation data and enriches with dimension labels.

## Usage
Install dependencies
```bash
dbt deps
```
Run all models
```bash
dbt run
dbt run --select stage__grad2023
```
Test models
```bash
dbt test
```

---
*Uyen Nguyen*