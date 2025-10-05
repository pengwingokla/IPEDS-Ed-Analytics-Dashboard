
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select city
from IPEDS.TRANSFORM_DIMENSIONS.dim_institution
where city is null



  
  
      
    ) dbt_internal_test