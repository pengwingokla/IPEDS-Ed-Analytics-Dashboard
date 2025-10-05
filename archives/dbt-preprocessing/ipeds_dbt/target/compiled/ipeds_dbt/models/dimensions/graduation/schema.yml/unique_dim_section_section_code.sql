
    
    

select
    section_code as unique_field,
    count(*) as n_records

from IPEDS.TRANSFORM_DIMENSIONS.dim_section
where section_code is not null
group by section_code
having count(*) > 1


