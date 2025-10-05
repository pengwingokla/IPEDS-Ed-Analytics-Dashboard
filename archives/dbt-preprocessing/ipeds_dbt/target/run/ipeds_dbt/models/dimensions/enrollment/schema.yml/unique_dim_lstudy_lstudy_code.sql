
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    lstudy_code as unique_field,
    count(*) as n_records

from IPEDS.TRANSFORM_DIMENSIONS.dim_lstudy
where lstudy_code is not null
group by lstudy_code
having count(*) > 1



  
  
      
    ) dbt_internal_test