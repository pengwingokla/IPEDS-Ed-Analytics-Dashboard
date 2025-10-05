
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    chrtstat_code as unique_field,
    count(*) as n_records

from IPEDS.TRANSFORM_DIMENSIONS.dim_chrtstat
where chrtstat_code is not null
group by chrtstat_code
having count(*) > 1



  
  
      
    ) dbt_internal_test