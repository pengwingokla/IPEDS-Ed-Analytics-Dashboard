
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select grtype_code
from IPEDS.TRANSFORM_DIMENSIONS.dim_grtype
where grtype_code is null



  
  
      
    ) dbt_internal_test