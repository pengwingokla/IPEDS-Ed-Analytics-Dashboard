





  

  

  

  


with base as (
  
    

        (
            select
                cast('IPEDS.TRANSFORM_STAGING.stage__grad2020' as TEXT) as _dbt_source_relation,

                
                    cast("SURVEY_YEAR" as NUMBER(4,0)) as "SURVEY_YEAR" ,
                    cast("INSTITUTION_ID" as NUMBER(38,0)) as "INSTITUTION_ID" ,
                    cast("GRTYPE_CODE" as character varying(16777216)) as "GRTYPE_CODE" ,
                    cast("CHRTSTAT_CODE" as character varying(16777216)) as "CHRTSTAT_CODE" ,
                    cast("SECTION_CODE" as character varying(16777216)) as "SECTION_CODE" ,
                    cast("COHORT_CODE" as character varying(16777216)) as "COHORT_CODE" ,
                    cast("LINE_CODE" as character varying(16777216)) as "LINE_CODE" ,
                    cast("GR_TOTAL_ALL" as NUMBER(38,0)) as "GR_TOTAL_ALL" ,
                    cast("GR_TOTAL_MALE" as NUMBER(38,0)) as "GR_TOTAL_MALE" ,
                    cast("GR_TOTAL_FEMALE" as NUMBER(38,0)) as "GR_TOTAL_FEMALE" ,
                    cast("GR_AI_AN_ALL" as NUMBER(38,0)) as "GR_AI_AN_ALL" ,
                    cast("GR_AI_AN_MALE" as NUMBER(38,0)) as "GR_AI_AN_MALE" ,
                    cast("GR_AI_AN_FEMALE" as NUMBER(38,0)) as "GR_AI_AN_FEMALE" ,
                    cast("GR_ASIAN_ALL" as NUMBER(38,0)) as "GR_ASIAN_ALL" ,
                    cast("GR_ASIAN_MALE" as NUMBER(38,0)) as "GR_ASIAN_MALE" ,
                    cast("GR_ASIAN_FEMALE" as NUMBER(38,0)) as "GR_ASIAN_FEMALE" ,
                    cast("GR_BLACK_ALL" as NUMBER(38,0)) as "GR_BLACK_ALL" ,
                    cast("GR_BLACK_MALE" as NUMBER(38,0)) as "GR_BLACK_MALE" ,
                    cast("GR_BLACK_FEMALE" as NUMBER(38,0)) as "GR_BLACK_FEMALE" ,
                    cast("GR_HISPANIC_ALL" as NUMBER(38,0)) as "GR_HISPANIC_ALL" ,
                    cast("GR_HISPANIC_MALE" as NUMBER(38,0)) as "GR_HISPANIC_MALE" ,
                    cast("GR_HISPANIC_FEMALE" as NUMBER(38,0)) as "GR_HISPANIC_FEMALE" ,
                    cast("GR_NHPI_ALL" as NUMBER(38,0)) as "GR_NHPI_ALL" ,
                    cast("GR_NHPI_MALE" as NUMBER(38,0)) as "GR_NHPI_MALE" ,
                    cast("GR_NHPI_FEMALE" as NUMBER(38,0)) as "GR_NHPI_FEMALE" ,
                    cast("GR_WHITE_ALL" as NUMBER(38,0)) as "GR_WHITE_ALL" ,
                    cast("GR_WHITE_MALE" as NUMBER(38,0)) as "GR_WHITE_MALE" ,
                    cast("GR_WHITE_FEMALE" as NUMBER(38,0)) as "GR_WHITE_FEMALE" ,
                    cast("GR_TWO_OR_MORE_ALL" as NUMBER(38,0)) as "GR_TWO_OR_MORE_ALL" ,
                    cast("GR_TWO_OR_MORE_MALE" as NUMBER(38,0)) as "GR_TWO_OR_MORE_MALE" ,
                    cast("GR_TWO_OR_MORE_FEMALE" as NUMBER(38,0)) as "GR_TWO_OR_MORE_FEMALE" ,
                    cast("GR_UNKNOWN_ALL" as NUMBER(38,0)) as "GR_UNKNOWN_ALL" ,
                    cast("GR_UNKNOWN_MALE" as NUMBER(38,0)) as "GR_UNKNOWN_MALE" ,
                    cast("GR_UNKNOWN_FEMALE" as NUMBER(38,0)) as "GR_UNKNOWN_FEMALE" ,
                    cast("GR_NONRESIDENT_ALL" as NUMBER(38,0)) as "GR_NONRESIDENT_ALL" ,
                    cast("GR_NONRESIDENT_MALE" as NUMBER(38,0)) as "GR_NONRESIDENT_MALE" ,
                    cast("GR_NONRESIDENT_FEMALE" as NUMBER(38,0)) as "GR_NONRESIDENT_FEMALE" 

            from IPEDS.TRANSFORM_STAGING.stage__grad2020

            
        )

        union all
        

        (
            select
                cast('IPEDS.TRANSFORM_STAGING.stage__grad2021' as TEXT) as _dbt_source_relation,

                
                    cast("SURVEY_YEAR" as NUMBER(4,0)) as "SURVEY_YEAR" ,
                    cast("INSTITUTION_ID" as NUMBER(38,0)) as "INSTITUTION_ID" ,
                    cast("GRTYPE_CODE" as character varying(16777216)) as "GRTYPE_CODE" ,
                    cast("CHRTSTAT_CODE" as character varying(16777216)) as "CHRTSTAT_CODE" ,
                    cast("SECTION_CODE" as character varying(16777216)) as "SECTION_CODE" ,
                    cast("COHORT_CODE" as character varying(16777216)) as "COHORT_CODE" ,
                    cast("LINE_CODE" as character varying(16777216)) as "LINE_CODE" ,
                    cast("GR_TOTAL_ALL" as NUMBER(38,0)) as "GR_TOTAL_ALL" ,
                    cast("GR_TOTAL_MALE" as NUMBER(38,0)) as "GR_TOTAL_MALE" ,
                    cast("GR_TOTAL_FEMALE" as NUMBER(38,0)) as "GR_TOTAL_FEMALE" ,
                    cast("GR_AI_AN_ALL" as NUMBER(38,0)) as "GR_AI_AN_ALL" ,
                    cast("GR_AI_AN_MALE" as NUMBER(38,0)) as "GR_AI_AN_MALE" ,
                    cast("GR_AI_AN_FEMALE" as NUMBER(38,0)) as "GR_AI_AN_FEMALE" ,
                    cast("GR_ASIAN_ALL" as NUMBER(38,0)) as "GR_ASIAN_ALL" ,
                    cast("GR_ASIAN_MALE" as NUMBER(38,0)) as "GR_ASIAN_MALE" ,
                    cast("GR_ASIAN_FEMALE" as NUMBER(38,0)) as "GR_ASIAN_FEMALE" ,
                    cast("GR_BLACK_ALL" as NUMBER(38,0)) as "GR_BLACK_ALL" ,
                    cast("GR_BLACK_MALE" as NUMBER(38,0)) as "GR_BLACK_MALE" ,
                    cast("GR_BLACK_FEMALE" as NUMBER(38,0)) as "GR_BLACK_FEMALE" ,
                    cast("GR_HISPANIC_ALL" as NUMBER(38,0)) as "GR_HISPANIC_ALL" ,
                    cast("GR_HISPANIC_MALE" as NUMBER(38,0)) as "GR_HISPANIC_MALE" ,
                    cast("GR_HISPANIC_FEMALE" as NUMBER(38,0)) as "GR_HISPANIC_FEMALE" ,
                    cast("GR_NHPI_ALL" as NUMBER(38,0)) as "GR_NHPI_ALL" ,
                    cast("GR_NHPI_MALE" as NUMBER(38,0)) as "GR_NHPI_MALE" ,
                    cast("GR_NHPI_FEMALE" as NUMBER(38,0)) as "GR_NHPI_FEMALE" ,
                    cast("GR_WHITE_ALL" as NUMBER(38,0)) as "GR_WHITE_ALL" ,
                    cast("GR_WHITE_MALE" as NUMBER(38,0)) as "GR_WHITE_MALE" ,
                    cast("GR_WHITE_FEMALE" as NUMBER(38,0)) as "GR_WHITE_FEMALE" ,
                    cast("GR_TWO_OR_MORE_ALL" as NUMBER(38,0)) as "GR_TWO_OR_MORE_ALL" ,
                    cast("GR_TWO_OR_MORE_MALE" as NUMBER(38,0)) as "GR_TWO_OR_MORE_MALE" ,
                    cast("GR_TWO_OR_MORE_FEMALE" as NUMBER(38,0)) as "GR_TWO_OR_MORE_FEMALE" ,
                    cast("GR_UNKNOWN_ALL" as NUMBER(38,0)) as "GR_UNKNOWN_ALL" ,
                    cast("GR_UNKNOWN_MALE" as NUMBER(38,0)) as "GR_UNKNOWN_MALE" ,
                    cast("GR_UNKNOWN_FEMALE" as NUMBER(38,0)) as "GR_UNKNOWN_FEMALE" ,
                    cast("GR_NONRESIDENT_ALL" as NUMBER(38,0)) as "GR_NONRESIDENT_ALL" ,
                    cast("GR_NONRESIDENT_MALE" as NUMBER(38,0)) as "GR_NONRESIDENT_MALE" ,
                    cast("GR_NONRESIDENT_FEMALE" as NUMBER(38,0)) as "GR_NONRESIDENT_FEMALE" 

            from IPEDS.TRANSFORM_STAGING.stage__grad2021

            
        )

        union all
        

        (
            select
                cast('IPEDS.TRANSFORM_STAGING.stage__grad2022' as TEXT) as _dbt_source_relation,

                
                    cast("SURVEY_YEAR" as NUMBER(4,0)) as "SURVEY_YEAR" ,
                    cast("INSTITUTION_ID" as NUMBER(38,0)) as "INSTITUTION_ID" ,
                    cast("GRTYPE_CODE" as character varying(16777216)) as "GRTYPE_CODE" ,
                    cast("CHRTSTAT_CODE" as character varying(16777216)) as "CHRTSTAT_CODE" ,
                    cast("SECTION_CODE" as character varying(16777216)) as "SECTION_CODE" ,
                    cast("COHORT_CODE" as character varying(16777216)) as "COHORT_CODE" ,
                    cast("LINE_CODE" as character varying(16777216)) as "LINE_CODE" ,
                    cast("GR_TOTAL_ALL" as NUMBER(38,0)) as "GR_TOTAL_ALL" ,
                    cast("GR_TOTAL_MALE" as NUMBER(38,0)) as "GR_TOTAL_MALE" ,
                    cast("GR_TOTAL_FEMALE" as NUMBER(38,0)) as "GR_TOTAL_FEMALE" ,
                    cast("GR_AI_AN_ALL" as NUMBER(38,0)) as "GR_AI_AN_ALL" ,
                    cast("GR_AI_AN_MALE" as NUMBER(38,0)) as "GR_AI_AN_MALE" ,
                    cast("GR_AI_AN_FEMALE" as NUMBER(38,0)) as "GR_AI_AN_FEMALE" ,
                    cast("GR_ASIAN_ALL" as NUMBER(38,0)) as "GR_ASIAN_ALL" ,
                    cast("GR_ASIAN_MALE" as NUMBER(38,0)) as "GR_ASIAN_MALE" ,
                    cast("GR_ASIAN_FEMALE" as NUMBER(38,0)) as "GR_ASIAN_FEMALE" ,
                    cast("GR_BLACK_ALL" as NUMBER(38,0)) as "GR_BLACK_ALL" ,
                    cast("GR_BLACK_MALE" as NUMBER(38,0)) as "GR_BLACK_MALE" ,
                    cast("GR_BLACK_FEMALE" as NUMBER(38,0)) as "GR_BLACK_FEMALE" ,
                    cast("GR_HISPANIC_ALL" as NUMBER(38,0)) as "GR_HISPANIC_ALL" ,
                    cast("GR_HISPANIC_MALE" as NUMBER(38,0)) as "GR_HISPANIC_MALE" ,
                    cast("GR_HISPANIC_FEMALE" as NUMBER(38,0)) as "GR_HISPANIC_FEMALE" ,
                    cast("GR_NHPI_ALL" as NUMBER(38,0)) as "GR_NHPI_ALL" ,
                    cast("GR_NHPI_MALE" as NUMBER(38,0)) as "GR_NHPI_MALE" ,
                    cast("GR_NHPI_FEMALE" as NUMBER(38,0)) as "GR_NHPI_FEMALE" ,
                    cast("GR_WHITE_ALL" as NUMBER(38,0)) as "GR_WHITE_ALL" ,
                    cast("GR_WHITE_MALE" as NUMBER(38,0)) as "GR_WHITE_MALE" ,
                    cast("GR_WHITE_FEMALE" as NUMBER(38,0)) as "GR_WHITE_FEMALE" ,
                    cast("GR_TWO_OR_MORE_ALL" as NUMBER(38,0)) as "GR_TWO_OR_MORE_ALL" ,
                    cast("GR_TWO_OR_MORE_MALE" as NUMBER(38,0)) as "GR_TWO_OR_MORE_MALE" ,
                    cast("GR_TWO_OR_MORE_FEMALE" as NUMBER(38,0)) as "GR_TWO_OR_MORE_FEMALE" ,
                    cast("GR_UNKNOWN_ALL" as NUMBER(38,0)) as "GR_UNKNOWN_ALL" ,
                    cast("GR_UNKNOWN_MALE" as NUMBER(38,0)) as "GR_UNKNOWN_MALE" ,
                    cast("GR_UNKNOWN_FEMALE" as NUMBER(38,0)) as "GR_UNKNOWN_FEMALE" ,
                    cast("GR_NONRESIDENT_ALL" as NUMBER(38,0)) as "GR_NONRESIDENT_ALL" ,
                    cast("GR_NONRESIDENT_MALE" as NUMBER(38,0)) as "GR_NONRESIDENT_MALE" ,
                    cast("GR_NONRESIDENT_FEMALE" as NUMBER(38,0)) as "GR_NONRESIDENT_FEMALE" 

            from IPEDS.TRANSFORM_STAGING.stage__grad2022

            
        )

        union all
        

        (
            select
                cast('IPEDS.TRANSFORM_STAGING.stage__grad2023' as TEXT) as _dbt_source_relation,

                
                    cast("SURVEY_YEAR" as NUMBER(4,0)) as "SURVEY_YEAR" ,
                    cast("INSTITUTION_ID" as NUMBER(38,0)) as "INSTITUTION_ID" ,
                    cast("GRTYPE_CODE" as character varying(16777216)) as "GRTYPE_CODE" ,
                    cast("CHRTSTAT_CODE" as character varying(16777216)) as "CHRTSTAT_CODE" ,
                    cast("SECTION_CODE" as character varying(16777216)) as "SECTION_CODE" ,
                    cast("COHORT_CODE" as character varying(16777216)) as "COHORT_CODE" ,
                    cast("LINE_CODE" as character varying(16777216)) as "LINE_CODE" ,
                    cast("GR_TOTAL_ALL" as NUMBER(38,0)) as "GR_TOTAL_ALL" ,
                    cast("GR_TOTAL_MALE" as NUMBER(38,0)) as "GR_TOTAL_MALE" ,
                    cast("GR_TOTAL_FEMALE" as NUMBER(38,0)) as "GR_TOTAL_FEMALE" ,
                    cast("GR_AI_AN_ALL" as NUMBER(38,0)) as "GR_AI_AN_ALL" ,
                    cast("GR_AI_AN_MALE" as NUMBER(38,0)) as "GR_AI_AN_MALE" ,
                    cast("GR_AI_AN_FEMALE" as NUMBER(38,0)) as "GR_AI_AN_FEMALE" ,
                    cast("GR_ASIAN_ALL" as NUMBER(38,0)) as "GR_ASIAN_ALL" ,
                    cast("GR_ASIAN_MALE" as NUMBER(38,0)) as "GR_ASIAN_MALE" ,
                    cast("GR_ASIAN_FEMALE" as NUMBER(38,0)) as "GR_ASIAN_FEMALE" ,
                    cast("GR_BLACK_ALL" as NUMBER(38,0)) as "GR_BLACK_ALL" ,
                    cast("GR_BLACK_MALE" as NUMBER(38,0)) as "GR_BLACK_MALE" ,
                    cast("GR_BLACK_FEMALE" as NUMBER(38,0)) as "GR_BLACK_FEMALE" ,
                    cast("GR_HISPANIC_ALL" as NUMBER(38,0)) as "GR_HISPANIC_ALL" ,
                    cast("GR_HISPANIC_MALE" as NUMBER(38,0)) as "GR_HISPANIC_MALE" ,
                    cast("GR_HISPANIC_FEMALE" as NUMBER(38,0)) as "GR_HISPANIC_FEMALE" ,
                    cast("GR_NHPI_ALL" as NUMBER(38,0)) as "GR_NHPI_ALL" ,
                    cast("GR_NHPI_MALE" as NUMBER(38,0)) as "GR_NHPI_MALE" ,
                    cast("GR_NHPI_FEMALE" as NUMBER(38,0)) as "GR_NHPI_FEMALE" ,
                    cast("GR_WHITE_ALL" as NUMBER(38,0)) as "GR_WHITE_ALL" ,
                    cast("GR_WHITE_MALE" as NUMBER(38,0)) as "GR_WHITE_MALE" ,
                    cast("GR_WHITE_FEMALE" as NUMBER(38,0)) as "GR_WHITE_FEMALE" ,
                    cast("GR_TWO_OR_MORE_ALL" as NUMBER(38,0)) as "GR_TWO_OR_MORE_ALL" ,
                    cast("GR_TWO_OR_MORE_MALE" as NUMBER(38,0)) as "GR_TWO_OR_MORE_MALE" ,
                    cast("GR_TWO_OR_MORE_FEMALE" as NUMBER(38,0)) as "GR_TWO_OR_MORE_FEMALE" ,
                    cast("GR_UNKNOWN_ALL" as NUMBER(38,0)) as "GR_UNKNOWN_ALL" ,
                    cast("GR_UNKNOWN_MALE" as NUMBER(38,0)) as "GR_UNKNOWN_MALE" ,
                    cast("GR_UNKNOWN_FEMALE" as NUMBER(38,0)) as "GR_UNKNOWN_FEMALE" ,
                    cast("GR_NONRESIDENT_ALL" as NUMBER(38,0)) as "GR_NONRESIDENT_ALL" ,
                    cast("GR_NONRESIDENT_MALE" as NUMBER(38,0)) as "GR_NONRESIDENT_MALE" ,
                    cast("GR_NONRESIDENT_FEMALE" as NUMBER(38,0)) as "GR_NONRESIDENT_FEMALE" 

            from IPEDS.TRANSFORM_STAGING.stage__grad2023

            
        )

          -- aligns columns by name across years
)

select
  b.institution_id,
  b.survey_year,
  -- Institution information
  i.institution_name,
  i.city,
  i.state_abbr,
  -- Graduation information
  g.grtype_label   as grad_type,
  c.chrtstat_label as grad_status,
  s.section_label  as section,
  h.cohort_label   as cohort,
  l.line_label     as line,
  -- Graduation counts
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
left join IPEDS.TRANSFORM_DIMENSIONS.dim_institution i on b.institution_id = i.unitid
left join IPEDS.TRANSFORM_DIMENSIONS.dim_grtype   g on b.grtype_code   = g.grtype_code
left join IPEDS.TRANSFORM_DIMENSIONS.dim_chrtstat c on b.chrtstat_code = c.chrtstat_code
left join IPEDS.TRANSFORM_DIMENSIONS.dim_section  s on b.section_code  = s.section_code
left join IPEDS.TRANSFORM_DIMENSIONS.dim_cohort   h on b.cohort_code   = h.cohort_code
left join IPEDS.TRANSFORM_DIMENSIONS.dim_line     l on b.line_code     = l.line_code