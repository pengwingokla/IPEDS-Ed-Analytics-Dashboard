
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select state_abbr
from IPEDS.TRANSFORM_DIMENSIONS.dim_institution
where state_abbr is null



  
  
      
    ) dbt_internal_test