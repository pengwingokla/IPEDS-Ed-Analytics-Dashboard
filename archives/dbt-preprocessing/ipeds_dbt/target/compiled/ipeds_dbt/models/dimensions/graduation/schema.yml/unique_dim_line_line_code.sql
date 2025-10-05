
    
    

select
    line_code as unique_field,
    count(*) as n_records

from IPEDS.TRANSFORM_DIMENSIONS.dim_line
where line_code is not null
group by line_code
having count(*) > 1


