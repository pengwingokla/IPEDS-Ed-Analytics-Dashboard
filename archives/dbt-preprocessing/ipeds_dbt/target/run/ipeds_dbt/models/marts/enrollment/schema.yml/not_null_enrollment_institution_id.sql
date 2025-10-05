
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select institution_id
from IPEDS.TRANSFORM_MARTS.enrollment
where institution_id is null



  
  
      
    ) dbt_internal_test