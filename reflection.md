# Reflection

Student Name:  jamie cole
Sudent Email:  jcole05@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

In this assignment, I deepened my understanding of data cleaning and merging across multiple sources. For example, I used apply(pl.extract_year_mdy) to extract the year from the timestamp, which helped organize survey responses by year. I also applied pl.clean_country_usa() to standardize country names, particularly dealing with various inputs for "United States." However, I encountered challenges while merging datasets. Specifically, using merge() to combine survey data with cost-of-living data by ['year', '_full_city'] and ['year', 'City'] required careful attention to alignment, and I struggled with cities that didn't match perfectly. The salary adjustment step, apply(lambda row: row["_annual_salary_cleaned"] * (100 / row['Cost of Living Index'])), sometimes led to errors when the data format wasn’t properly cleaned beforehand. One area where I need more practice with is handling complex joins across datasets with mismatched entries and ensuring data consistency across multiple columns before merging. I'll also focus on currency cleaning functions, as errors in the pl.clean_currency() function disrupted some calculations. 