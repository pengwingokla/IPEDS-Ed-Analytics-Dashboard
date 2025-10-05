
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select lstudy_code
from IPEDS.TRANSFORM_DIMENSIONS.dim_lstudy
where lstudy_code is null



  
  
      
    ) dbt_internal_test