from textwrap import dedent

class Introduction:
    DATA_SOURCE_INFO = dedent("""
       **Data Source**  
       Integrated Postsecondary Education Data System (IPEDS)  
       Official dataset maintained by the National Center for Education Statistics (NCES), providing annual data on U.S. higher-education institutions.
       (Publicly available dataset reporting U.S. higher education institutional data)

        **Hosting & Data Access**  
        The raw IPEDS tables were preprocessed and combined into analysis-ready datasets covering domains such as Admissions, Enrollment, Graduation, and Financial Aid.
        The curated dataset is publicly hosted on Hugging Face Datasets under the repositories:  
        • `chloecodes/IPEDS_CUSTOM`  
        • `chloecodes/IPEDS_ADMISSION`  
        • `chloecodes/IPEDS_GRADUATION`  
        • `chloecodes/IPEDS_SFA`.
        
    """)

__all__ = ["Introduction"]