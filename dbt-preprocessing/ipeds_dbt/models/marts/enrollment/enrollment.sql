{{ config(materialized='table', cluster_by=['institution_id','survey_year']) }}

{% set years = [2023] %}  -- Add more years as enrollment staging models are created

{% set rels = [] %}
{% for y in years %}
  {% do rels.append( ref('stage__enrollment' ~ y) ) %}
{% endfor %}

with base as (
  {{ dbt_utils.union_relations(rels) }}  -- aligns columns by name across years
)

select
  b.institution_id,
  b.survey_year,
  ela.effyalev_label as student_level_and_degree_status,
  el.effylev_label as undergraduate_graduate_level,
  ls.lstudy_label as original_level_of_study,
  b.grand_total,
  b.grand_total_men,
  b.grand_total_women,
  b.american_indian_total,
  b.asian_total,
  b.black_african_american_total,
  b.hispanic_latino_total,
  b.native_hawaiian_pacific_islander_total,
  b.white_total,
  b.two_or_more_races_total,
  b.race_ethnicity_unknown_total,
  b.us_nonresident_total
from base b
left join {{ ref('dim_effyalev') }} ela on b.student_level_and_degree_status = ela.effyalev_code
left join {{ ref('dim_effylev') }}  el  on b.undergraduate_graduate_level = el.effylev_code
left join {{ ref('dim_lstudy') }}   ls  on b.original_level_of_study = ls.lstudy_code