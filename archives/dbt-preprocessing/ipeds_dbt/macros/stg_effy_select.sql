{% macro stage_enrollment(year) %}
    select
        cast(UNITID as integer) as institution_id,
        {{ year }} as survey_year,
        {% if year == 2019 %}
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
        {% else %}
        -- 2020+ columns
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
        {% endif %}
    from src
{% endmacro %}
