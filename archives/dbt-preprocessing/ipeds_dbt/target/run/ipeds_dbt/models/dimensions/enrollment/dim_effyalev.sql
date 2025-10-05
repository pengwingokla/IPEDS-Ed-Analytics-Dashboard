
  
    

create or replace transient table IPEDS.TRANSFORM_DIMENSIONS.dim_effyalev
    
    
    
    as (select cast(code as number) as effyalev_code, label as effyalev_label
from IPEDS.TRANSFORM_SEEDS_ENROLLMENT.effyalev_code
    )
;


  