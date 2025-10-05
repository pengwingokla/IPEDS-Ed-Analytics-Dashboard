
  
    

create or replace transient table IPEDS.TRANSFORM_DIMENSIONS.dim_chrtstat
    
    
    
    as (select cast(code as number) as chrtstat_code, label as chrtstat_label
from IPEDS.TRANSFORM_SEEDS_GRADUATION.chrtstat_code
    )
;


  