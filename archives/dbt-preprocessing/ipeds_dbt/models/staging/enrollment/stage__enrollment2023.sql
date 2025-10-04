with src as (
    select * from {{ source('raw_ipeds','EFFY2023') }}
)

{{ stage_enrollment(2023) }}
