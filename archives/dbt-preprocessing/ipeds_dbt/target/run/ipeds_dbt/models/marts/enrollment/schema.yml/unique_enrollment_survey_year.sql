
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    survey_year as unique_field,
    count(*) as n_records

from IPEDS.TRANSFORM_MARTS.enrollment
where survey_year is not null
group by survey_year
having count(*) > 1



  
  
      
    ) dbt_internal_test