select cast(code as number) as lstudy_code, label as lstudy_label
from {{ ref('lstudy_code') }}