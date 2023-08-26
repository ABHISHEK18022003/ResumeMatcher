# RESUME MATCHER
* Resume Matcher is a Web App, which when provided with the resume and a job description, shows how similar both of these are.
* Technology Stack Used: HTML, CSS, Python

Term Frequency-Inverse Document Frequency (TF-IDF) approach is used to measure the similarity between job descriptions. The generated cosine similarity matrix helps identify similar jobs.

jobs_US.head().transpose(): This command displays a transposed view of the first few records in the 'jobs_US' dataset, providing an initial insight into the data's structure.

jobs_US_base_line = jobs_US.iloc[0:10000,0:8]: Here, a subset of the 'jobs_US' dataset is created, including the first 10,000 rows and the first 8 columns. This subset serves as the basis for the analysis, ensuring manageable data volume.

jobs_US_base_line['Title'] = jobs_US_base_line['Title'].fillna(''): The 'Title' column is filled with empty strings for missing values, ensuring consistency in subsequent operations.

jobs_US_base_line['Description'] =jobs_US_base_line['Description'].fillna(''): Similarly, missing values in the 'Description' column are filled with empty strings.

jobs_US_base_line['Description'] = jobs_US_base_line['Title'] + jobs_US_base_line['Description']: 
The 'Description' column is augmented by concatenating the 'Title' and 'Description' columns. This combines both textual attributes into a single string for better context representation.

tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english'): 
The TfidfVectorizer is employed to convert the combined text data into a numerical representation, considering both single words and word pairs (bigrams). Stop words in English are also excluded.

tfidf_matrix = tf.fit_transform(jobs_US_base_line['Description']): 
The transformed data is stored in the 'tfidf_matrix', representing the text's TF-IDF values.

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix): The cosine similarity between job descriptions is calculated using the TF-IDF matrix. This similarity matrix quantifies the resemblance between job descriptions.

jobs_US_base_line = jobs_US_base_line.reset_index(): The dataframe's index is reset to allow for easy retrieval of job titles and indices.

indices = pd.Series (jobs_US_base_line.index, index= jobs_US_base_line['Title']): 
A Series is created with job titles as the index and corresponding indices as values. This serves as a lookup table for job titles and their corresponding indices.

The 'get_recommendations' function suggests similar jobs based on a given job title. For instance, a job titled 'SAP Business Analyst / WM' would yield recommendations such as 'SAP FI/CO Business Consultant', 'SAP FI/CO Business Analyst', and more.  

