with src as (
    select * from {{ source('raw_ipeds','EFFY2019') }}
)

{{ stage_enrollment(2019) }}
