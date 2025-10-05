
    
    

select
    unitid as unique_field,
    count(*) as n_records

from IPEDS.TRANSFORM_DIMENSIONS.dim_institution
where unitid is not null
group by unitid
having count(*) > 1


