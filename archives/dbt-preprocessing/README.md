# IPEDS DBT Preprocessing

A dbt project for preprocessing and transforming IPEDS (Integrated Postsecondary Education Data System) data for enrollment and graduation analytics.

## Project Overview

This project uses dbt (data build tool) to transform raw IPEDS data into clean, structured datasets suitable for analysis and visualization. The project handles both enrollment and graduation data across multiple years.

## Project Structure

```
dbt-preprocessing/
├── ipeds_dbt/                 # Main dbt project
│   ├── models/                # Data transformation models
│   │   ├── staging/          # Initial data staging
│   │   ├── dimensions/       # Dimension tables
│   │   └── marts/            # Final presentation layer
│   ├── seeds/                # Lookup tables and code mappings
│   ├── macros/               # Reusable SQL macros
│   └── dbt_project.yml       # Project configuration
├── raw/                      # Raw data files
├── processed/                # Processed output files
└── commands.txt              # Common dbt commands
```

## Data Models

### Staging Layer
- **Enrollment**: Staged enrollment data for years 2019-2023
- **Graduation**: Staged graduation data for years 2020-2023

### Dimension Tables
- **Enrollment Dimensions**: `dim_effyalev`, `dim_effylev`, `dim_lstudy`
- **Graduation Dimensions**: `dim_chrtstat`, `dim_cohort`, `dim_grtype`, `dim_line`, `dim_section`

### Marts
- **Enrollment Mart**: Aggregated enrollment metrics
- **Graduation Mart**: Aggregated graduation metrics

## Prerequisites

- Python 3.7+
- dbt Core or dbt Cloud
- Access to IPEDS data sources

## Installation

1. Clone the repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Navigate to the dbt project directory:
   ```bash
   cd ipeds_dbt
   ```

4. Install dbt dependencies:
   ```bash
   dbt deps
   ```

## Usage

### Load Lookup Tables (Seeds)
```bash
# Load all seeds
dbt seed

# Load specific seed
dbt seed --select grtype_code
```

### Build Models
```bash
# Build all models
dbt run

# Build only staging models
dbt run --select staging

# Build specific staging model
dbt run --select staging.enrollment
```

### Run Tests
```bash
# Run all tests
dbt test

# Run tests for specific models
dbt test --select staging
```

### Generate Documentation
```bash
# Generate and serve documentation
dbt docs generate
dbt docs serve
```
To download csv locally, use SnowSQL:
```bash
snowsql -q "SELECT * FROM IPEDS.TRANSFORM_MARTS.enrollment" -o output_format=csv -o header=true -o output_file=enrollment-id.csv
```

Check profile info using:
```bash
cat ~/.dbt/profiles.yml
```
## Configuration

The project is configured in `dbt_project.yml` with:
- Separate schemas for staging, dimensions, and marts
- Custom seed configurations for lookup tables
- Variable definitions for graduation years

## Data Sources

The project expects IPEDS data files to be placed in the `raw/` directory. Ensure your data sources are properly configured in `models/sources/ipeds_sources.yml`.

## Contributing

1. Follow dbt best practices
2. Add appropriate tests for new models
3. Update documentation as needed
4. Ensure all models pass tests before committing
