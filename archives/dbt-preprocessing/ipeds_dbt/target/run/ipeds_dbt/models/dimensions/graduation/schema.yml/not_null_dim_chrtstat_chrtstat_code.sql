
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select chrtstat_code
from IPEDS.TRANSFORM_DIMENSIONS.dim_chrtstat
where chrtstat_code is null



  
  
      
    ) dbt_internal_test