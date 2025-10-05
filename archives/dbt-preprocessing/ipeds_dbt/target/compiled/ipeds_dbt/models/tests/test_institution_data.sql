-- Test to verify institution data is properly populated
-- This will help us confirm that the institution_name, city, and state are no longer null

with enrollment_check as (
  select 
    count(*) as total_enrollment_records,
    count(institution_name) as enrollment_records_with_name,
    count(city) as enrollment_records_with_city,
    count(state_abbr) as enrollment_records_with_state
  from IPEDS.TRANSFORM_MARTS.enrollment
),

graduation_check as (
  select 
    count(*) as total_graduation_records,
    count(institution_name) as graduation_records_with_name,
    count(city) as graduation_records_with_city,
    count(state_abbr) as graduation_records_with_state
  from IPEDS.TRANSFORM_MARTS.graduation
),

sample_data as (
  select 
    institution_id,
    institution_name,
    city,
    state_abbr,
    survey_year
  from IPEDS.TRANSFORM_MARTS.enrollment
  where institution_name is not null
  limit 5
)

select 
  e.total_enrollment_records,
  e.enrollment_records_with_name,
  e.enrollment_records_with_city,
  e.enrollment_records_with_state,
  g.total_graduation_records,
  g.graduation_records_with_name,
  g.graduation_records_with_city,
  g.graduation_records_with_state
from enrollment_check e
cross join graduation_check g

union all

select 
  institution_id as total_enrollment_records,
  case when institution_name is not null then 1 else 0 end as enrollment_records_with_name,
  case when city is not null then 1 else 0 end as enrollment_records_with_city,
  case when state_abbr is not null then 1 else 0 end as enrollment_records_with_state,
  survey_year as total_graduation_records,
  null as graduation_records_with_name,
  null as graduation_records_with_city,
  null as graduation_records_with_state
from sample_data