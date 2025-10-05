
    
    

select
    grtype_code as unique_field,
    count(*) as n_records

from IPEDS.TRANSFORM_DIMENSIONS.dim_grtype
where grtype_code is not null
group by grtype_code
having count(*) > 1


