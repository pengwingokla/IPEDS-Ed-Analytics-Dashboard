select cast(code as number) as cohort_code, label as cohort_label
from {{ ref('cohort_code') }}