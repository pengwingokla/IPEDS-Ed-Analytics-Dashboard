
    
    

select
    effylev_code as unique_field,
    count(*) as n_records

from IPEDS.TRANSFORM_DIMENSIONS.dim_effylev
where effylev_code is not null
group by effylev_code
having count(*) > 1


