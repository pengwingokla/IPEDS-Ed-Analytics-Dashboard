with src as (
    select * from {{ source('raw_ipeds','EFFY2022') }}
)

{{ stage_enrollment(2022) }}
