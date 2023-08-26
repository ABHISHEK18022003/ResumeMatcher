import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def match_predict(resumeFileObj,job_desc):
    resumeReader = PyPDF2.PdfFileReader(resumeFileObj)
    resumeObj = resumeReader.getPage(0) 
    resume=resumeObj.extractText() 
    text=[resume,job_desc]
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)
    match_percentage = cosine_similarity(count_matrix)[0][1] * 100
    match_percentage = round(match_percentage,2)
    return(match_percentage)
