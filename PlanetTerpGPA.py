import requests
import json

dictGrade = {'A+':4.0, 'A': 4.0, 'A-':3.7, 'B+':3.3, 'B': 3.0, 'B-':2.7, 'C+':2.3, 'C': 2.0, 'C-':1.7, 'D+':1.3, 'D': 1.0, 'D-':0.7, 'F': 0.0, 'W': 0.0} 
course_name = input("What is the course name? ")
num = 0
den = 0
professors = []

grade_data = requests.get('https://api.planetterp.com/v1/grades?course=' + course_name).json()
if 'error' in grade_data and grade_data['error'] == "course not found":
    print ("Error: Course not found.")
else:
    for course_grade_data in grade_data:
        for key in dictGrade:
            num = num + dictGrade[key] * course_grade_data[key]
            den = den + course_grade_data[key] * 1.0
    print("Average GPA for " + course_name + " is " + str(round(num/den, 2)))
    choice = input("Looking for the best professor. Do you want to consider ratings for the specific course only? (Type 'Yes' or 'No') ")
    print("Loading...")
    prof_data = requests.get('https://api.planetterp.com/v1/course?name=' + course_name).json()
    if 'error' in prof_data and prof_data['error'] == "course not found":
        print ("Error: Course not found.")
    else:
        prof_rate = []
        for course_prof_data in prof_data['professors']:
            prof = course_prof_data.split()
            query = ""
            i = 0
            for word in prof:
                query = query + word
                if i != len(prof) - 1:
                    query = query + "%20"
                    i = i + 1

            review_data = requests.get('https://api.planetterp.com/v1/professor?name=' + query + "&reviews=true").json()
            if 'error' in review_data and review_data['error'] == "professor not found":
                print ("Error: Course not found.")
            else:
                sum = 0
                count = 0
                #print(link)
                for review in review_data['reviews']:
                    if review['course'] != None: 
                        if choice.lower() == 'yes': 
                            if review['course'].lower() == course_name.lower(): 
                                sum = (sum + review['rating']) * 1.0
                                count = (count + 1) * 1.0
                        else:
                            sum = (sum + review['rating']) * 1.0
                            count = (count + 1) * 1.0

                if (count != 0):
                    #print("Average rating for " + course_prof_data + " is " + str(sum/count))
                    prof_rate.append({"Professor" : course_prof_data, "Rating" : round(sum/count, 2), "Count" : count})
        
        prof_rate = sorted(prof_rate, key = lambda i: (i['Rating'], i['Count']), reverse=True)
        result = ""
        for best in prof_rate:
            if best['Rating'] == prof_rate[0]['Rating'] and best['Count'] == prof_rate[0]['Count']:
                result = result + best['Professor'] + ", "

        if (len(prof_rate) != 0):    
            print ("The professor with the best rating for " + course_name.upper() + " is " + result + "with an average rating of " + str(prof_rate[0]['Rating'])) 
        else:
            print("No reviews found")







    
