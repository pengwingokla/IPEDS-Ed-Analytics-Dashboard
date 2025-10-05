
  
    

create or replace transient table IPEDS.TRANSFORM_DIMENSIONS.dim_line
    
    
    
    as (select trim(code) as line_code, label as line_label
from IPEDS.TRANSFORM_SEEDS_GRADUATION.line_code
    )
;


  