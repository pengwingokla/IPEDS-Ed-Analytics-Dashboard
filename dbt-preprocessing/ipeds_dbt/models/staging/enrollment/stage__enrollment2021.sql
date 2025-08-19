with src as (
    select * from {{ source('raw_ipeds','EFFY2021') }}
)

{{ stage_enrollment(2021) }}
