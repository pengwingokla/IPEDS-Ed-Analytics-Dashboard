with src as (
    select * from {{ source('raw_ipeds','EFFY2020') }}
)

{{ stage_enrollment(2020) }}
