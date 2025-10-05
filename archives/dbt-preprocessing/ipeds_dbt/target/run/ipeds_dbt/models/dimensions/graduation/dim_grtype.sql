
  
    

create or replace transient table IPEDS.TRANSFORM_DIMENSIONS.dim_grtype
    
    
    
    as (select cast(code as number) as grtype_code, label as grtype_label
from IPEDS.TRANSFORM_SEEDS_GRADUATION.grtype_code
    )
;


  