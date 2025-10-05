
    
    

select
    institution_id as unique_field,
    count(*) as n_records

from IPEDS.TRANSFORM_MARTS.enrollment
where institution_id is not null
group by institution_id
having count(*) > 1


