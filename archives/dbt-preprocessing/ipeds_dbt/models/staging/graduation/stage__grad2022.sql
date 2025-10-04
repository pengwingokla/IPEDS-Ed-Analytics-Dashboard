{{ config(materialized='table') }}

with src as (
    select * from {{ source('raw_ipeds','GRAD2022') }}
)

{{ stg_grad_select(2022) }}
from src
