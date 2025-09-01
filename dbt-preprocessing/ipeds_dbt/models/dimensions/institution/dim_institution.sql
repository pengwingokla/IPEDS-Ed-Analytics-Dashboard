{{
  config(
    materialized='table',
    schema='DIMENSIONS'
  )
}}

SELECT 
    unitid,
    institution_name,
    city,
    state_abbr,
    -- Create a full address field
    CONCAT(city, ', ', state_abbr) as full_address,
    -- Add metadata
    CURRENT_TIMESTAMP as created_at,
    CURRENT_TIMESTAMP as updated_at
FROM {{ ref('institution_info') }}
