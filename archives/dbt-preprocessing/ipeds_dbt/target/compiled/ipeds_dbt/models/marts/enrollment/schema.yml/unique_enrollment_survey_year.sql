
    
    

select
    survey_year as unique_field,
    count(*) as n_records

from IPEDS.TRANSFORM_MARTS.enrollment
where survey_year is not null
group by survey_year
having count(*) > 1


