{{ config(materialized='table') }}

with src as (
    select * from {{ source('raw_ipeds','GRAD2020') }}
)

{{ stg_grad_select(2020) }}
from src
