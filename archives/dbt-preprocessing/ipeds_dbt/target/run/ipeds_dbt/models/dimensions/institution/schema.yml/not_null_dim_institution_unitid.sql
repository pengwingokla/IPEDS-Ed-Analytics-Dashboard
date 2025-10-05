
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select unitid
from IPEDS.TRANSFORM_DIMENSIONS.dim_institution
where unitid is null



  
  
      
    ) dbt_internal_test