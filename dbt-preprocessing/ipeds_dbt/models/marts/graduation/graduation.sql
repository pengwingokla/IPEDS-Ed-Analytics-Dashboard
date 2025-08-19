{{ config(materialized='table', cluster_by=['institution_id','survey_year']) }}

{% set years = var('grad_years', []) %}

{% set rels = [] %}
{% for y in years %}
  {% do rels.append( ref('stage__grad' ~ y) ) %}
{% endfor %}

with base as (
  {{ dbt_utils.union_relations(rels) }}  -- aligns columns by name across years
)

select
  b.institution_id,
  b.survey_year,
  g.grtype_label   as grad_type,
  c.chrtstat_label as grad_status,
  s.section_label  as section,
  h.cohort_label   as cohort,
  l.line_label     as line,
  b.gr_total_all,  b.gr_total_male,  b.gr_total_female,
  b.gr_ai_an_all,  b.gr_ai_an_male,  b.gr_ai_an_female,
  b.gr_asian_all,  b.gr_asian_male,  b.gr_asian_female,
  b.gr_black_all,  b.gr_black_male,  b.gr_black_female,
  b.gr_hispanic_all, b.gr_hispanic_male, b.gr_hispanic_female,
  b.gr_nhpi_all,   b.gr_nhpi_male,   b.gr_nhpi_female,
  b.gr_white_all,  b.gr_white_male,  b.gr_white_female,
  b.gr_two_or_more_all, b.gr_two_or_more_male, b.gr_two_or_more_female,
  b.gr_unknown_all, b.gr_unknown_male, b.gr_unknown_female,
  b.gr_nonresident_all, b.gr_nonresident_male, b.gr_nonresident_female
from base b
left join {{ ref('dim_grtype') }}   g on b.grtype_code   = g.grtype_code
left join {{ ref('dim_chrtstat') }} c on b.chrtstat_code = c.chrtstat_code
left join {{ ref('dim_section') }}  s on b.section_code  = s.section_code
left join {{ ref('dim_cohort') }}   h on b.cohort_code   = h.cohort_code
left join {{ ref('dim_line') }}     l on b.line_code     = l.line_code
