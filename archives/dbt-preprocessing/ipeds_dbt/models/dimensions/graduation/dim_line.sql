select trim(code) as line_code, label as line_label
from {{ ref('line_code') }}