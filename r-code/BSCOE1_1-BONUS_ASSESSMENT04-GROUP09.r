library(readxl)
library(dplyr)

# NOTE: MATCH THE FILE PATH WITH THE SAMPLE DATA AND THE SOURCE CODE FOR IT TO WORK. THANK YOU.
SAMPLE_DATA <- read_excel("C:\\pup-viernes\\freshman-r\\data-analysis\\SAMPLE_DATA.xlsx")

# I. From SAMPLE_DATA, create a data with file name NEWDATA with the following conditions:
# 1. Randomly take 30% of the number of observations.

NEWDATA1 <- SAMPLE_DATA %>% sample_frac(0.3, replace=F)
  
# 2. Include only those students whose favorite color are either red, blue, or yellow.  
NEWDATA2 <- NEWDATA1 %>% filter(FAVORITE_COLOR %in% c('RED','YELLOW','BLUE'))



# 3. Select only of the following columns:
# Student Number
# Favorite Subject
# Grade in 4 subjects  
NEWDATA3 <- NEWDATA2 %>% select(-c(GENDER,AGE,HEIGHT,WEIGHT,FAVORITE_COLOR))


  
# 4. Rename all the column names so that the first letter is capitalized.   
NEWDATA4 <- NEWDATA3 %>%
 rename(Respondent_Number="RESPONDENT_NUMBER",
         Favorite_Subject="FAVORITE_SUBJECT",
         Grade_in_Math="GRADE_IN_MATH",
         Grade_in_Statistics_and_Probability="GRADE_IN_STATISTICS_AND_PROBABILITY",
         Grade_in_Science="GRADE_IN_SCIENCE",
         Grade_in_Media_and_Information_Literacy="GRADE_IN_MEDIA_AND_INFORMATION_LITERACY")


  
# 5. Create a new column and name it as Average. Calculate it as the average of the 4 subjects.  
 NEWDATA5 <- NEWDATA4 %>% 
 mutate(Average=(Grade_in_Math + Grade_in_Statistics_and_Probability + Grade_in_Science
                  + Grade_in_Media_and_Information_Literacy)/4)

# II. Summarize the data to find out the mean and standard deviation of the 'Average' column.
# Summarize the data according to favorite subject.
summary <- NEWDATA5 %>%
 group_by(Favorite_Subject) %>%
 summarise(mean(Average, na.rm=T), sd(Average, na.rm=T)) 


# Sample executed code in console.
if(F){"
> print(NEWDATA1)
# A tibble: 7 x 11
  RESPONDENT_NUMBER GENDER   AGE FAVORITE_SUBJECT FAVORITE_COLOR HEIGHT WEIGHT GRADE_IN_MATH
              <dbl> <chr>  <dbl> <chr>            <chr>           <dbl>  <dbl>         <dbl>
1                 8 MALE      19 SCIENCE          YELLOW            167     45            89
2                 2 FEMALE    19 SCIENCE          YELLOW            154     48            95
3                18 MALE      18 ENGLISH          BLUE              175     68            96
4                16 MALE      20 MATH             BLUE              174     49            92
5                10 FEMALE    19 ENGLISH          RED               162     54            93
6                 4 MALE      19 SCIENCE          BLUE              165     45            94
7                20 MALE      18 MATH             BLUE              176     58            92
# ... with 3 more variables: GRADE_IN_STATISTICS_AND_PROBABILITY <dbl>, GRADE_IN_SCIENCE <dbl>,
#   GRADE_IN_MEDIA_AND_INFORMATION_LITERACY <dbl>

> print(NEWDATA2)
# A tibble: 7 x 11
  RESPONDENT_NUMBER GENDER   AGE FAVORITE_SUBJECT FAVORITE_COLOR HEIGHT WEIGHT GRADE_IN_MATH
              <dbl> <chr>  <dbl> <chr>            <chr>           <dbl>  <dbl>         <dbl>
1                 8 MALE      19 SCIENCE          YELLOW            167     45            89
2                 2 FEMALE    19 SCIENCE          YELLOW            154     48            95
3                18 MALE      18 ENGLISH          BLUE              175     68            96
4                16 MALE      20 MATH             BLUE              174     49            92
5                10 FEMALE    19 ENGLISH          RED               162     54            93
6                 4 MALE      19 SCIENCE          BLUE              165     45            94
7                20 MALE      18 MATH             BLUE              176     58            92
# ... with 3 more variables: GRADE_IN_STATISTICS_AND_PROBABILITY <dbl>, GRADE_IN_SCIENCE <dbl>,
#   GRADE_IN_MEDIA_AND_INFORMATION_LITERACY <dbl>

> print(NEWDATA3)
# A tibble: 7 x 6
  RESPONDENT_NUMBER FAVORITE_SUBJECT GRADE_IN_MATH GRADE_IN_STATIST~ GRADE_IN_SCIENCE GRADE_IN_MEDIA_~
              <dbl> <chr>                    <dbl>             <dbl>            <dbl>            <dbl>
1                 8 SCIENCE                     89                89               88               89
2                 2 SCIENCE                     95                94               91               97
3                18 ENGLISH                     96                95               96               95
4                16 MATH                        92                94               93               92
5                10 ENGLISH                     93                94               94               93
6                 4 SCIENCE                     94                97               94               96
7                20 MATH                        92                95               90               94

> print(NEWDATA4)
# A tibble: 7 x 6
  Respondent_Number Favorite_Subject Grade_in_Math Grade_in_Statist~ Grade_in_Science Grade_in_Media_~
              <dbl> <chr>                    <dbl>             <dbl>            <dbl>            <dbl>
1                 8 SCIENCE                     89                89               88               89
2                 2 SCIENCE                     95                94               91               97
3                18 ENGLISH                     96                95               96               95
4                16 MATH                        92                94               93               92
5                10 ENGLISH                     93                94               94               93
6                 4 SCIENCE                     94                97               94               96
7                20 MATH                        92                95               90               94

> print(NEWDATA5)
# A tibble: 7 x 7
  Respondent_Number Favorite_Subject Grade_in_Math Grade_in_Statist~ Grade_in_Science Grade_in_Media_~
              <dbl> <chr>                    <dbl>             <dbl>            <dbl>            <dbl>
1                 8 SCIENCE                     89                89               88               89
2                 2 SCIENCE                     95                94               91               97
3                18 ENGLISH                     96                95               96               95
4                16 MATH                        92                94               93               92
5                10 ENGLISH                     93                94               94               93
6                 4 SCIENCE                     94                97               94               96
7                20 MATH                        92                95               90               94
# ... with 1 more variable: Average <dbl>

> print(summary)
# A tibble: 3 x 3
  Favorite_Subject `mean(Average, na.rm = T)` `sd(Average, na.rm = T)`
  <chr>                                 <dbl>                    <dbl>
1 ENGLISH                                94.5                     1.41
2 MATH                                   92.8                     0   
3 SCIENCE                                92.8                     3.5 

"}

