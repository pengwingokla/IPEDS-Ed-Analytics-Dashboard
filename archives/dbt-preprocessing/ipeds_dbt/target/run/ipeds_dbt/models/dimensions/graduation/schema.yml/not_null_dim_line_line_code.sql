
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select line_code
from IPEDS.TRANSFORM_DIMENSIONS.dim_line
where line_code is null



  
  
      
    ) dbt_internal_test