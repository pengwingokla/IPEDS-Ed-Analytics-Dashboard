select cast(code as number) as chrtstat_code, label as chrtstat_label
from {{ ref('chrtstat_code') }}