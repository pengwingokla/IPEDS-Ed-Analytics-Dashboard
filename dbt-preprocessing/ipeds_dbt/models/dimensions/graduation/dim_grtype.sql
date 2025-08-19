select cast(code as number) as grtype_code, label as grtype_label
from {{ ref('grtype_code') }}