from textwrap import dedent

class Help:
    UG_ENROLLMENT_HEADCOUNT = dedent("""
        This stacked bar chart shows the total fall enrollment of undergraduate and graduate students at the selected institution over time. 
        Graduate students includes Masters/Non-matriculated Grad, Post-Baccalaureate Certificates, and Doctorates.
    """)
    GENERAL_AID_TYPE_COMPOSITION = dedent("""
        This graph displays the percentage of full-time, first-time undergraduate students who received financial aid at the selected institution over time. It compares two categories:

        • Any Aid: Percent of full-time first-time undergraduates awarded any loans to students or grant aid from federal, state/local government, or the institution.  
        • Grant Only: Percent of full-time first-time undergraduates awarded federal, state, local, or institutional grant aid
    """)
    TOT_AMT_AID_COMPOSITION = dedent("""
        Tracks the total dollars disbursed to full-time, first-time undergraduates by aid type each year.  
        • Total Grant Aid combines federal, state/local, and institutional grants.  
        • Other Federal Grant Aid is non-Pell federal grants. Loans are funds to be repaid; grant aid is not.  
        • Total Student Loans includes federal and private student loans.
    """)
    AID_TYPE_COMPOSITION = dedent("""
        This stacked bar chart shows the distribution of financial aid types among full-time first-time undergraduates.  
        Each bar represents the percentage of students awarded federal grant aid, state/local grant aid, institutional grant aid, Pell grants, and other federal grant aid, based on the following columns:  
        • Percent of full-time first-time undergraduates awarded federal grant aid  
        • Percent of full-time first-time undergraduates awarded state/local grant aid  
        • Percent of full-time first-time undergraduates awarded institutional grant aid  
        • Percent of full-time first-time undergraduates awarded Pell grants  
        • Percent of full-time first-time undergraduates awarded other federal grant aid  
    """)

__all__ = ["Help"]

