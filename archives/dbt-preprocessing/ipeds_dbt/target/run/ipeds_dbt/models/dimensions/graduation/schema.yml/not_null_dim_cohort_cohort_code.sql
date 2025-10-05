
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select cohort_code
from IPEDS.TRANSFORM_DIMENSIONS.dim_cohort
where cohort_code is null



  
  
      
    ) dbt_internal_test