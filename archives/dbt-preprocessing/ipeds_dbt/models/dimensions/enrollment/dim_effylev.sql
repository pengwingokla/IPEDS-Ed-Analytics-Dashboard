select cast(code as number) as effylev_code, label as effylev_label
from {{ ref('effylev_code') }}