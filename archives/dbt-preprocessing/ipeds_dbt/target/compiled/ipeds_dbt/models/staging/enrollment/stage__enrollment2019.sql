with src as (
    select * from IPEDS.RAW.EFFY2019
)


    select
        cast(UNITID as integer) as institution_id,
        2019 as survey_year,
        
        -- 2019 columns (need to verify actual column names)
        null as student_level_and_degree_status,
        null as undergraduate_graduate_level,
        null as original_level_of_study,
        null as grand_total,
        null as grand_total_men,
        null as grand_total_women,
        null as american_indian_total,
        null as asian_total,
        null as black_african_american_total,
        null as hispanic_latino_total,
        null as native_hawaiian_pacific_islander_total,
        null as white_total,
        null as two_or_more_races_total,
        null as race_ethnicity_unknown_total,
        null as us_nonresident_total
        
    from src
