
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  





with validation_errors as (

    select
        institution_id, survey_year, student_level_and_degree_status, undergraduate_graduate_level, original_level_of_study
    from IPEDS.TRANSFORM_MARTS.enrollment
    group by institution_id, survey_year, student_level_and_degree_status, undergraduate_graduate_level, original_level_of_study
    having count(*) > 1

)

select *
from validation_errors



  
  
      
    ) dbt_internal_test