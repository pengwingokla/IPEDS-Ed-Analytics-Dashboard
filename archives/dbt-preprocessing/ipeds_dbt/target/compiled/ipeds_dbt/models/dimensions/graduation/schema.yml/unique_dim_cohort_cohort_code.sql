
    
    

select
    cohort_code as unique_field,
    count(*) as n_records

from IPEDS.TRANSFORM_DIMENSIONS.dim_cohort
where cohort_code is not null
group by cohort_code
having count(*) > 1


