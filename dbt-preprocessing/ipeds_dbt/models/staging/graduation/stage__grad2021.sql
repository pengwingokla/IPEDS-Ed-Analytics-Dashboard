{{ config(materialized='table') }}

with src as (
    select * from {{ source('raw_ipeds','GRAD2021') }}
)

{{ stg_grad_select(2021) }}
from src
