
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select survey_year
from IPEDS.TRANSFORM_MARTS.enrollment
where survey_year is null



  
  
      
    ) dbt_internal_test