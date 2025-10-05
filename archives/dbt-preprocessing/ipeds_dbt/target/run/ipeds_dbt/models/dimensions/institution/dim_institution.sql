
  
    

create or replace transient table IPEDS.TRANSFORM_DIMENSIONS.dim_institution
    
    
    
    as (

SELECT 
    unitid,
    institution_name,
    city,
    state_abbr
FROM IPEDS.TRANSFORM_SEEDS_INSTITUTION.institution_info_all
    )
;


  