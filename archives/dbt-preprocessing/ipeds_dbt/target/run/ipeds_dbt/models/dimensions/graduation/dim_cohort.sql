
  
    

create or replace transient table IPEDS.TRANSFORM_DIMENSIONS.dim_cohort
    
    
    
    as (select cast(code as number) as cohort_code, label as cohort_label
from IPEDS.TRANSFORM_SEEDS_GRADUATION.cohort_code
    )
;


  