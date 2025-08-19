{% macro stage_enrollment(year) %}
    select
        UNITID as institution_id,
        {{ year }} as survey_year,
        EFFYALEV as student_level_and_degree_status,
        EFFYLEV as undergraduate_graduate_level,
        LSTUDY as original_level_of_study,
        EFYTOTLT as grand_total,
        EFYTOTLM as grand_total_men,
        EFYTOTLW as grand_total_women,
        EFYAIANT as american_indian_total,
        EFYASIAT as asian_total,
        EFYBKAAT as black_african_american_total,
        EFYHISPT as hispanic_latino_total,
        EFYNHPIT as native_hawaiian_pacific_islander_total,
        EFYWHITT as white_total,
        EFY2MORT as two_or_more_races_total,
        EFYUNKNT as race_ethnicity_unknown_total,
        EFYNRALT as us_nonresident_total
    from src
{% endmacro %}
