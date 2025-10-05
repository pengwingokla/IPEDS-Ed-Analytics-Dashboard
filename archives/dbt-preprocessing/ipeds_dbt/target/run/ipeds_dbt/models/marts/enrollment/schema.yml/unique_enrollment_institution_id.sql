
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    institution_id as unique_field,
    count(*) as n_records

from IPEDS.TRANSFORM_MARTS.enrollment
where institution_id is not null
group by institution_id
having count(*) > 1



  
  
      
    ) dbt_internal_test