select cast(code as number) as effyalev_code, label as effyalev_label
from {{ ref('effyalev_code') }}