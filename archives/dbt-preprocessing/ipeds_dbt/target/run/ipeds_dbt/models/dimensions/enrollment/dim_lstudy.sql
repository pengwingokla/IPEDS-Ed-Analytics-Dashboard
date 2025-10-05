
  
    

create or replace transient table IPEDS.TRANSFORM_DIMENSIONS.dim_lstudy
    
    
    
    as (select cast(code as number) as lstudy_code, label as lstudy_label
from IPEDS.TRANSFORM_SEEDS_ENROLLMENT.lstudy_code
    )
;


  