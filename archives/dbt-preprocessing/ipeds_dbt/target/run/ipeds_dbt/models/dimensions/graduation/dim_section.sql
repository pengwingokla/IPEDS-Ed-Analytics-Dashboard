
  
    

create or replace transient table IPEDS.TRANSFORM_DIMENSIONS.dim_section
    
    
    
    as (select cast(code as number) as section_code, label as section_label
from IPEDS.TRANSFORM_SEEDS_GRADUATION.section_code
    )
;


  