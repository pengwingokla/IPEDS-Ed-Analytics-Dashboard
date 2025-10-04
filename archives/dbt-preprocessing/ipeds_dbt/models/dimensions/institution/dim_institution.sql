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
    state_abbr
FROM {{ ref('institution_info_all') }}
