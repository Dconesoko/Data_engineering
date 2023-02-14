-- Subquery to extract individual letters from the contents column in the google_file_store table
with base_table as (
  select 
    unnest(
      regexp_split_to_array(
        lower(words),  -- Convert each word to lowercase
        ''               -- Split each word into individual letters
      )
    ) as letter 
  from 
    (
      select 
        unnest(
          regexp_split_to_array(contents, ' ')  -- Split contents into words
        ) as words 
      from 
        google_file_store
    ) as A
), 

-- Subquery to select letters that are not equal to ',' or '.'
google_file_store_letters as (
  select 
    letter as char 
  from 
    base_table 
  where 
    letter not in (',', '.')  -- Ignore characters equal to ',' and '.'
), 

-- Subquery to merge the contents of two columns from the google_word_lists table into one column
merging_word_columns as (
  select 
    word 
  from 
    (
      select 
        words1 as word 
      from 
        google_word_lists 
      union all 
      select 
        words2 as word 
      from 
        google_word_lists
    ) as self
), 

-- Subquery to break down words into individual characters
words_field_to_char as (
  select 
    unnest(
      regexp_split_to_array(token, '')  -- Split words into individual characters
    ) as char 
  from 
    (
      select 
        unnest(
          string_to_array(word, ',')  -- Split words using comma separator
        ) as token 
      from 
        merging_word_columns
    ) as self
) 

-- Select the characters from both subqueries, count the occurrences, and return the top three
select 
  char, 
  count(*) 
from 
  (
    select 
      * 
    from 
      google_file_store_letters 
    union all 
    select 
      * 
    from 
      words_field_to_char
  ) as self 
group by 
  1 
order by 
  2 desc 
limit 
  3
