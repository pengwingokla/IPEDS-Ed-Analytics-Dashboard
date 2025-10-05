
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select institution_name
from IPEDS.TRANSFORM_DIMENSIONS.dim_institution
where institution_name is null



  
  
      
    ) dbt_internal_test