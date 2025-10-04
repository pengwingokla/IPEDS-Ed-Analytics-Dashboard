select cast(code as number) as section_code, label as section_label
from {{ ref('section_code') }}