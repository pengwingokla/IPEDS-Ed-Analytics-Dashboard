
  
    

create or replace transient table IPEDS.TRANSFORM.debug_institution
    
    
    
    as (-- Debug model to check institution data issues
with institution_check as (
  select 
    unitid,
    institution_name,
    city,
    state_abbr
  from IPEDS.TRANSFORM_DIMENSIONS.dim_institution
  where unitid = 233426
),

enrollment_check as (
  select 
    institution_id,
    survey_year,
    institution_name,
    city,
    state_abbr
  from IPEDS.TRANSFORM_MARTS.enrollment
  where institution_id = 233426
  limit 5
),

raw_check as (
  select 
    unitid,
    institution_name,
    city,
    state_abbr
  from IPEDS.TRANSFORM_SEEDS_INSTITUTION.institution_info
  where unitid = 233426
)

select 
  'institution_check' as source,
  unitid,
  institution_name,
  city,
  state_abbr
from institution_check

union all

select 
  'enrollment_check' as source,
  institution_id as unitid,
  institution_name,
  city,
  state_abbr
from enrollment_check

union all

select 
  'raw_check' as source,
  unitid,
  institution_name,
  city,
  state_abbr
from raw_check
    )
;


  