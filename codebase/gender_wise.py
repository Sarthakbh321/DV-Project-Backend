'''
  # TODO: To fetch the genders and placement index from the fetching module
  # TODO: To generate graphs according to the dataset
'''

# from codebase import FetchData as FetchData
from codebase.clean_data import FetchData as FetchData
from matplotlib import pyplot as plt
import io
import base64

class GenderWisePlacementAnalysis:
  def __init__(self, activation = False):
    self.activation = activation
    
  def generateGraph(self):
    fetchDataObject = FetchData(True)
    #  print(fetchDataObject.get_gender_list())
    #  print(fetchDataObject.get_student_placement_status_list())
    
    gender_list = fetchDataObject.get_gender_list()
    placement_status_list = fetchDataObject.get_student_placement_status_list()
    males = []
    females = []
    
    for i in range(len(gender_list)):
      if (gender_list[i] == 'M'): males.append(gender_list[i])
      else: females.append(gender_list[i])
    
    male_placement = 0
    female_placement = 0
    
    for count in range(len(placement_status_list)):
      if (gender_list[count] == 'M'): male_placement += 1
      else: female_placement += 1
    
    male_value = fetchDataObject.get_number_of_males()
    female_value = fetchDataObject.get_number_of_females()
    
    # plt.scatter(male_value)
    # plt.scatter(female_value)
    plt.scatter(male_placement, len(placement_status_list))
    plt.scatter(female_placement, len(placement_status_list))
    # plt.plot(male_placement)
    # plt.plot(female_placement)

    bytes = io.BytesIO()

    plt.savefig(bytes, format="jpg")
    bytes.seek(0)

    b64 = base64.b64encode(bytes.read()).decode("ascii")

    return b64


    
  
# if __name__ == "__main__":
#     genderWisePlacementAnalysis = GenderWisePlacementAnalysis(True)
#     genderWisePlacementAnalysis.generateGraph()