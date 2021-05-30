'''
  # TODO: To fetch the genders and placement index from the fetching module
  # TODO: To generate graphs according to the dataset
'''

# from fetch_data import FetchData as FetchData
import clean_data as FetchData
from matplotlib import pyplot as plt

class SubjectWisePlacementAnalysis:
  def __init__(self, activation = False):
    self.activation = activation
  
  def generateGraph(self):
    # activation of the fetchData object which will inherit the properties 
    # FetchData class method
    fetchData = FetchData.FetchData(True)
    
    subject_list = fetchData.get_high_school_subjects()
    print(subject_list)
    placement_status_list = fetchData.get_student_placement_status_list()
    science_students = []
    commerce_students = []
    arts_students = []
    
    for count in range(len(subject_list)):
      if subject_list[count] == 'Science': science_students.append(subject_list[count])
      elif subject_list[count] == "Commerce": commerce_students.append(subject_list[count])
      elif subject_list[count] == "Arts": arts_students.append(subject_list[count])
      else: continue
    
    # subject wise placed students
    science_placed = 0
    commerce_placed = 0
    arts_placed = 0
    
    # subject wise not-placed students
    science_not_placed = 0
    commerce_not_placed = 0
    arts_not_placed = 0
    
    # computing number of placed students - subject wise
    for count in range(len(placement_status_list)):
      if placement_status_list[count] == "Placed" and "Placed" in placement_status_list[count]:
        if subject_list[count] == "Science" and "Science" in subject_list[count]:
          science_placed += 1
        elif subject_list[count] == "Commerce" and "Commerce" in subject_list[count]:
          commerce_placed += 1
        elif subject_list[count] == "Arts" and "Arts" in subject_list[count]:
          arts_placed += 1
      elif placement_status_list[count] == "Not Placed" and "Not Placed" in placement_status_list[count]:
        if subject_list[count] == "Science" and "Science" in subject_list[count]:
          science_not_placed += 1
        elif subject_list[count] == "Commerce" and "Commerce" in subject_list[count]:
          commerce_not_placed += 1
        elif subject_list[count] == "Arts" and "Arts" in subject_list[count]:
          arts_not_placed += 1
          
    plt.plot(science_students)
    plt.plot(commerce_students)
    plt.plot(arts_students)
    plt.title("Subject wise Index")
    plt.legend(["Science", "Commerce", "Arts"])
    plt.xlabel("No. of Students")
    plt.ylabel("Subject")
    plt.show()
    
    # plt.plot()
  
# if __name__ == '__main__':
#   subjectWisePlacementAnalysis = SubjectWisePlacementAnalysis()
#   subjectWisePlacementAnalysis.generateGraph()
#
#