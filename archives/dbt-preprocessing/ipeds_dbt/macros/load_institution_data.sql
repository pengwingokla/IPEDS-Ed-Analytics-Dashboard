{% macro load_institution_data() %}
    -- This macro can be used to load institution data from external sources
    -- or to perform data quality checks on the institution_info seed
    
    {% set query %}
        SELECT 
            COUNT(*) as total_institutions,
            COUNT(DISTINCT unitid) as unique_unitids,
            COUNT(DISTINCT state_abbr) as unique_states,
            COUNT(DISTINCT city) as unique_cities
        FROM {{ ref('institution_info_all') }}
    {% endset %}
    
    {% set results = run_query(query) %}
    
    {% if execute %}
        {% set row = results.rows[0] %}
        {{ log("Institution data summary:", info=true) }}
        {{ log("Total institutions: " ~ row[0], info=true) }}
        {{ log("Unique unitids: " ~ row[1], info=true) }}
        {{ log("Unique states: " ~ row[2], info=true) }}
        {{ log("Unique cities: " ~ row[3], info=true) }}
    {% endif %}
    
{% endmacro %}
