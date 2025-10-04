{{ config(materialized='table') }}

with src as (
    select * from {{ source('raw_ipeds','GRAD2023') }}
)

{{ stg_grad_select(2023) }}
from src
