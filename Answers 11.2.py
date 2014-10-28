__author__ = 'Nickolas'

transcript={'Fall 2013':[['MATH',151,1, 'Calculus 1'],['CHEM',105,1,'General Chemistry 1'],
                         ['ENGR',110,2,'Introduction to Engineering'],['ENGR',102,3,'Computer Aided Design'],
                         ['ENGL',101,1,'English 1'],['ENGR',160,1,'Freshman Seminar'],['HONR',200,1,'Critical Thinking']],
            'Spring 2014':[['MATH',152,2,'Calculus 2'],['ENGR',103,1,'MatLab'],['CHEM',106,2,'General Chemistry 2'],
                           ['ENGR',360,1,'Undergraduate Seminar'],['ENGR',116,21,'Renewable Exploration'],
                           ['ENGR',116,51,'Mechanical Exploration'],['PHYS',150,2,'Physics 1']],
            'Fall 2014':[['MATH',252,3,'Calculus 3'],['PHYS',151,2,'Physics 2'],['ENGR',110,1,'Technical Communications'],
                ['CSCI',156,1,'Intro to Computer Science'],['HONR',200,1,'Study of Monsters'],
                ['CEMS',210,1,'Properties and Structures of Materials'],['ENGR',360,1,'Engineering Seminar']],
            'Spring 2015':[['MATH',271,2,'Differential Equations'],['CEMS',215,1,'Microstructural'],['CEMS',216,1,'Bonding/Structure of Materials'],
                           ['CEMS',235,1,'Thermodynamics'],['CEMS',203,1,'Powder Processing'],['ENGR',360,1,'Engineering Seminar']]}

def courses():
    n=0
    for semester in transcript:
        print(semester)
        for course in transcript[semester]:
            g=","
            print('    ' + course[0]+g+str(course[1])+g+str(course[2])+g+course[3])
            n+=1

def find(transcript):
    x=input("course")
    for semester in transcript:
        for course in transcript[semester]:
            if course[0]==x:
                print(semester)
                break


courses()
find(transcript)