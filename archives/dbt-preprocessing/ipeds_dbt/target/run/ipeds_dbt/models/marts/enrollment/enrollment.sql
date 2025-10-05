
  
    

create or replace transient table IPEDS.TRANSFORM_MARTS.enrollment
    
    
    
    as (select * from (
            

  -- All available enrollment years



  

  

  

  

  


with base as (
  
    

        (
            select
                cast('IPEDS.TRANSFORM_STAGING.stage__enrollment2019' as TEXT) as _dbt_source_relation,

                
                    cast("INSTITUTION_ID" as NUMBER(38,0)) as "INSTITUTION_ID" ,
                    cast("SURVEY_YEAR" as NUMBER(4,0)) as "SURVEY_YEAR" ,
                    cast("STUDENT_LEVEL_AND_DEGREE_STATUS" as character varying(16777216)) as "STUDENT_LEVEL_AND_DEGREE_STATUS" ,
                    cast("UNDERGRADUATE_GRADUATE_LEVEL" as character varying(16777216)) as "UNDERGRADUATE_GRADUATE_LEVEL" ,
                    cast("ORIGINAL_LEVEL_OF_STUDY" as character varying(16777216)) as "ORIGINAL_LEVEL_OF_STUDY" ,
                    cast("GRAND_TOTAL" as character varying(16777216)) as "GRAND_TOTAL" ,
                    cast("GRAND_TOTAL_MEN" as character varying(16777216)) as "GRAND_TOTAL_MEN" ,
                    cast("GRAND_TOTAL_WOMEN" as character varying(16777216)) as "GRAND_TOTAL_WOMEN" ,
                    cast("AMERICAN_INDIAN_TOTAL" as character varying(16777216)) as "AMERICAN_INDIAN_TOTAL" ,
                    cast("ASIAN_TOTAL" as character varying(16777216)) as "ASIAN_TOTAL" ,
                    cast("BLACK_AFRICAN_AMERICAN_TOTAL" as character varying(16777216)) as "BLACK_AFRICAN_AMERICAN_TOTAL" ,
                    cast("HISPANIC_LATINO_TOTAL" as character varying(16777216)) as "HISPANIC_LATINO_TOTAL" ,
                    cast("NATIVE_HAWAIIAN_PACIFIC_ISLANDER_TOTAL" as character varying(16777216)) as "NATIVE_HAWAIIAN_PACIFIC_ISLANDER_TOTAL" ,
                    cast("WHITE_TOTAL" as character varying(16777216)) as "WHITE_TOTAL" ,
                    cast("TWO_OR_MORE_RACES_TOTAL" as character varying(16777216)) as "TWO_OR_MORE_RACES_TOTAL" ,
                    cast("RACE_ETHNICITY_UNKNOWN_TOTAL" as character varying(16777216)) as "RACE_ETHNICITY_UNKNOWN_TOTAL" ,
                    cast("US_NONRESIDENT_TOTAL" as character varying(16777216)) as "US_NONRESIDENT_TOTAL" 

            from IPEDS.TRANSFORM_STAGING.stage__enrollment2019

            
        )

        union all
        

        (
            select
                cast('IPEDS.TRANSFORM_STAGING.stage__enrollment2020' as TEXT) as _dbt_source_relation,

                
                    cast("INSTITUTION_ID" as NUMBER(38,0)) as "INSTITUTION_ID" ,
                    cast("SURVEY_YEAR" as NUMBER(4,0)) as "SURVEY_YEAR" ,
                    cast("STUDENT_LEVEL_AND_DEGREE_STATUS" as character varying(16777216)) as "STUDENT_LEVEL_AND_DEGREE_STATUS" ,
                    cast("UNDERGRADUATE_GRADUATE_LEVEL" as character varying(16777216)) as "UNDERGRADUATE_GRADUATE_LEVEL" ,
                    cast("ORIGINAL_LEVEL_OF_STUDY" as character varying(16777216)) as "ORIGINAL_LEVEL_OF_STUDY" ,
                    cast("GRAND_TOTAL" as character varying(16777216)) as "GRAND_TOTAL" ,
                    cast("GRAND_TOTAL_MEN" as character varying(16777216)) as "GRAND_TOTAL_MEN" ,
                    cast("GRAND_TOTAL_WOMEN" as character varying(16777216)) as "GRAND_TOTAL_WOMEN" ,
                    cast("AMERICAN_INDIAN_TOTAL" as character varying(16777216)) as "AMERICAN_INDIAN_TOTAL" ,
                    cast("ASIAN_TOTAL" as character varying(16777216)) as "ASIAN_TOTAL" ,
                    cast("BLACK_AFRICAN_AMERICAN_TOTAL" as character varying(16777216)) as "BLACK_AFRICAN_AMERICAN_TOTAL" ,
                    cast("HISPANIC_LATINO_TOTAL" as character varying(16777216)) as "HISPANIC_LATINO_TOTAL" ,
                    cast("NATIVE_HAWAIIAN_PACIFIC_ISLANDER_TOTAL" as character varying(16777216)) as "NATIVE_HAWAIIAN_PACIFIC_ISLANDER_TOTAL" ,
                    cast("WHITE_TOTAL" as character varying(16777216)) as "WHITE_TOTAL" ,
                    cast("TWO_OR_MORE_RACES_TOTAL" as character varying(16777216)) as "TWO_OR_MORE_RACES_TOTAL" ,
                    cast("RACE_ETHNICITY_UNKNOWN_TOTAL" as character varying(16777216)) as "RACE_ETHNICITY_UNKNOWN_TOTAL" ,
                    cast("US_NONRESIDENT_TOTAL" as character varying(16777216)) as "US_NONRESIDENT_TOTAL" 

            from IPEDS.TRANSFORM_STAGING.stage__enrollment2020

            
        )

        union all
        

        (
            select
                cast('IPEDS.TRANSFORM_STAGING.stage__enrollment2021' as TEXT) as _dbt_source_relation,

                
                    cast("INSTITUTION_ID" as NUMBER(38,0)) as "INSTITUTION_ID" ,
                    cast("SURVEY_YEAR" as NUMBER(4,0)) as "SURVEY_YEAR" ,
                    cast("STUDENT_LEVEL_AND_DEGREE_STATUS" as character varying(16777216)) as "STUDENT_LEVEL_AND_DEGREE_STATUS" ,
                    cast("UNDERGRADUATE_GRADUATE_LEVEL" as character varying(16777216)) as "UNDERGRADUATE_GRADUATE_LEVEL" ,
                    cast("ORIGINAL_LEVEL_OF_STUDY" as character varying(16777216)) as "ORIGINAL_LEVEL_OF_STUDY" ,
                    cast("GRAND_TOTAL" as character varying(16777216)) as "GRAND_TOTAL" ,
                    cast("GRAND_TOTAL_MEN" as character varying(16777216)) as "GRAND_TOTAL_MEN" ,
                    cast("GRAND_TOTAL_WOMEN" as character varying(16777216)) as "GRAND_TOTAL_WOMEN" ,
                    cast("AMERICAN_INDIAN_TOTAL" as character varying(16777216)) as "AMERICAN_INDIAN_TOTAL" ,
                    cast("ASIAN_TOTAL" as character varying(16777216)) as "ASIAN_TOTAL" ,
                    cast("BLACK_AFRICAN_AMERICAN_TOTAL" as character varying(16777216)) as "BLACK_AFRICAN_AMERICAN_TOTAL" ,
                    cast("HISPANIC_LATINO_TOTAL" as character varying(16777216)) as "HISPANIC_LATINO_TOTAL" ,
                    cast("NATIVE_HAWAIIAN_PACIFIC_ISLANDER_TOTAL" as character varying(16777216)) as "NATIVE_HAWAIIAN_PACIFIC_ISLANDER_TOTAL" ,
                    cast("WHITE_TOTAL" as character varying(16777216)) as "WHITE_TOTAL" ,
                    cast("TWO_OR_MORE_RACES_TOTAL" as character varying(16777216)) as "TWO_OR_MORE_RACES_TOTAL" ,
                    cast("RACE_ETHNICITY_UNKNOWN_TOTAL" as character varying(16777216)) as "RACE_ETHNICITY_UNKNOWN_TOTAL" ,
                    cast("US_NONRESIDENT_TOTAL" as character varying(16777216)) as "US_NONRESIDENT_TOTAL" 

            from IPEDS.TRANSFORM_STAGING.stage__enrollment2021

            
        )

        union all
        

        (
            select
                cast('IPEDS.TRANSFORM_STAGING.stage__enrollment2022' as TEXT) as _dbt_source_relation,

                
                    cast("INSTITUTION_ID" as NUMBER(38,0)) as "INSTITUTION_ID" ,
                    cast("SURVEY_YEAR" as NUMBER(4,0)) as "SURVEY_YEAR" ,
                    cast("STUDENT_LEVEL_AND_DEGREE_STATUS" as character varying(16777216)) as "STUDENT_LEVEL_AND_DEGREE_STATUS" ,
                    cast("UNDERGRADUATE_GRADUATE_LEVEL" as character varying(16777216)) as "UNDERGRADUATE_GRADUATE_LEVEL" ,
                    cast("ORIGINAL_LEVEL_OF_STUDY" as character varying(16777216)) as "ORIGINAL_LEVEL_OF_STUDY" ,
                    cast("GRAND_TOTAL" as character varying(16777216)) as "GRAND_TOTAL" ,
                    cast("GRAND_TOTAL_MEN" as character varying(16777216)) as "GRAND_TOTAL_MEN" ,
                    cast("GRAND_TOTAL_WOMEN" as character varying(16777216)) as "GRAND_TOTAL_WOMEN" ,
                    cast("AMERICAN_INDIAN_TOTAL" as character varying(16777216)) as "AMERICAN_INDIAN_TOTAL" ,
                    cast("ASIAN_TOTAL" as character varying(16777216)) as "ASIAN_TOTAL" ,
                    cast("BLACK_AFRICAN_AMERICAN_TOTAL" as character varying(16777216)) as "BLACK_AFRICAN_AMERICAN_TOTAL" ,
                    cast("HISPANIC_LATINO_TOTAL" as character varying(16777216)) as "HISPANIC_LATINO_TOTAL" ,
                    cast("NATIVE_HAWAIIAN_PACIFIC_ISLANDER_TOTAL" as character varying(16777216)) as "NATIVE_HAWAIIAN_PACIFIC_ISLANDER_TOTAL" ,
                    cast("WHITE_TOTAL" as character varying(16777216)) as "WHITE_TOTAL" ,
                    cast("TWO_OR_MORE_RACES_TOTAL" as character varying(16777216)) as "TWO_OR_MORE_RACES_TOTAL" ,
                    cast("RACE_ETHNICITY_UNKNOWN_TOTAL" as character varying(16777216)) as "RACE_ETHNICITY_UNKNOWN_TOTAL" ,
                    cast("US_NONRESIDENT_TOTAL" as character varying(16777216)) as "US_NONRESIDENT_TOTAL" 

            from IPEDS.TRANSFORM_STAGING.stage__enrollment2022

            
        )

        union all
        

        (
            select
                cast('IPEDS.TRANSFORM_STAGING.stage__enrollment2023' as TEXT) as _dbt_source_relation,

                
                    cast("INSTITUTION_ID" as NUMBER(38,0)) as "INSTITUTION_ID" ,
                    cast("SURVEY_YEAR" as NUMBER(4,0)) as "SURVEY_YEAR" ,
                    cast("STUDENT_LEVEL_AND_DEGREE_STATUS" as character varying(16777216)) as "STUDENT_LEVEL_AND_DEGREE_STATUS" ,
                    cast("UNDERGRADUATE_GRADUATE_LEVEL" as character varying(16777216)) as "UNDERGRADUATE_GRADUATE_LEVEL" ,
                    cast("ORIGINAL_LEVEL_OF_STUDY" as character varying(16777216)) as "ORIGINAL_LEVEL_OF_STUDY" ,
                    cast("GRAND_TOTAL" as character varying(16777216)) as "GRAND_TOTAL" ,
                    cast("GRAND_TOTAL_MEN" as character varying(16777216)) as "GRAND_TOTAL_MEN" ,
                    cast("GRAND_TOTAL_WOMEN" as character varying(16777216)) as "GRAND_TOTAL_WOMEN" ,
                    cast("AMERICAN_INDIAN_TOTAL" as character varying(16777216)) as "AMERICAN_INDIAN_TOTAL" ,
                    cast("ASIAN_TOTAL" as character varying(16777216)) as "ASIAN_TOTAL" ,
                    cast("BLACK_AFRICAN_AMERICAN_TOTAL" as character varying(16777216)) as "BLACK_AFRICAN_AMERICAN_TOTAL" ,
                    cast("HISPANIC_LATINO_TOTAL" as character varying(16777216)) as "HISPANIC_LATINO_TOTAL" ,
                    cast("NATIVE_HAWAIIAN_PACIFIC_ISLANDER_TOTAL" as character varying(16777216)) as "NATIVE_HAWAIIAN_PACIFIC_ISLANDER_TOTAL" ,
                    cast("WHITE_TOTAL" as character varying(16777216)) as "WHITE_TOTAL" ,
                    cast("TWO_OR_MORE_RACES_TOTAL" as character varying(16777216)) as "TWO_OR_MORE_RACES_TOTAL" ,
                    cast("RACE_ETHNICITY_UNKNOWN_TOTAL" as character varying(16777216)) as "RACE_ETHNICITY_UNKNOWN_TOTAL" ,
                    cast("US_NONRESIDENT_TOTAL" as character varying(16777216)) as "US_NONRESIDENT_TOTAL" 

            from IPEDS.TRANSFORM_STAGING.stage__enrollment2023

            
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
  -- Student level information
  ela.effyalev_label as student_level_and_degree_status,
  el.effylev_label as undergraduate_graduate_level,
  ls.lstudy_label as original_level_of_study,
  -- Enrollment counts
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
left join IPEDS.TRANSFORM_DIMENSIONS.dim_institution i on b.institution_id = i.unitid
left join IPEDS.TRANSFORM_DIMENSIONS.dim_effyalev ela on b.student_level_and_degree_status = ela.effyalev_code
left join IPEDS.TRANSFORM_DIMENSIONS.dim_effylev  el  on b.undergraduate_graduate_level = el.effylev_code
left join IPEDS.TRANSFORM_DIMENSIONS.dim_lstudy   ls  on b.original_level_of_study = ls.lstudy_code
        )
        order by (
            institution_id, survey_year
        )
    )
;

alter table IPEDS.TRANSFORM_MARTS.enrollment cluster by (institution_id, survey_year);
  