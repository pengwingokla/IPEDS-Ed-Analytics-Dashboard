
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

with child as (
    select grad_type as from_field
    from IPEDS.TRANSFORM_MARTS.graduation
    where grad_type is not null
),

parent as (
    select grtype_code as to_field
    from IPEDS.TRANSFORM_DIMENSIONS.dim_grtype
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null



  
  
      
    ) dbt_internal_test