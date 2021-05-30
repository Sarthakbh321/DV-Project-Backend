# TODO: To initialize a useful setup for data warehousing.
# TODO: To fetch data from the CSV file and store each type in different containers.
# TODO: To make getters for various features and modules

import pandas as pandas

class FetchData:
    def __init__(self, activation = False):
        self.activation = activation
        self.check_datafile_type()

    def check_datafile_type(self):
        pass
        # datatype = self.data_type
        # continue from the datatype method

    def fetch_data_from_file(self):
        column_list = ["sl_no", "gender", "ssc_p", "ssc_b", "hsc_p", "hsc_b", "hsc_s", "degree_p", "degree_t", "workexp", "etest_p", "specialisation", "mba_p", "status", "salary"]
        # opening the csv file to fetch data
        datafile = pandas.read_csv("codebase\datasets\dataset.csv",
                                   usecols=column_list)
        # print(datafile["sl_no"])
        self.serial_number = datafile["sl_no"]
        self.gender_list = datafile["gender"]
        self.number_of_males = len(datafile[datafile.gender == 'M'])
        # print(self.number_of_males)
        self.number_of_females = len(datafile[datafile.gender == 'F'])
        self.secondary_school_percentage = datafile["ssc_p"]
        self.secondary_school_board = datafile["ssc_b"]
        self.number_of_central_board_secondary = len(datafile[datafile.ssc_b == "Central"])
        self.number_of_other_board_secondary = len(datafile[datafile.ssc_b == "Others"])
        self.high_school_percentage = datafile["hsc_p"]
        self.high_school_board = datafile["hsc_b"]
        self.number_of_central_board_high = len(datafile[datafile.hsc_b == "Central"])
        self.number_of_other_board_high = len(datafile[datafile.hsc_b == "Others"])
        self.high_school_subjects = datafile["hsc_s"]
        self.high_school_arts = len(datafile[datafile.hsc_s == "Arts"])
        self.high_school_science = len(datafile[datafile.hsc_s == "Science"])
        self.high_school_commerce = len(datafile[datafile.hsc_s == "Commerce"])
        self.college_degree = datafile["degree_t"]
        self.number_of_commerce_management_degree = len(datafile[datafile.degree_t == "Comm&Mgmt"])
        self.number_of_science_tech_degree = len(datafile[datafile.degree_t == "Sci&Tech"])
        self.number_of_other_degree = len(datafile[datafile.degree_t == "Others"])
        self.college_marks = datafile["degree_p"]
        self.work_experience = datafile["workexp"]
        self.number_of_no_workexp = len(datafile[datafile.workexp == "No"])
        self.number_of_yes_workexp = len(datafile[datafile.workexp == "Yes"])
        self.emp_test_percentage = datafile["etest_p"]
        self.students_specialization = datafile["specialisation"]
        self.number_of_mkt_hr_spec = len(datafile[datafile.specialisation == "Mkt&HR"])
        self.number_of_mkt_fin_spec = len(datafile[datafile.specialisation == "Mkt&Fin"])
        self.mba_percentage = datafile["mba_p"]
        self.student_placement_status = datafile["status"]
        self.number_of_student_placed = len(datafile[datafile.status == "Placed"])
        self.number_of_student_not_placed = len(datafile[datafile.status == "Not Placed"])
        self.salary_index = datafile["salary"]

    '''
    Now as the datafile is fetched with various methods
    we need getters for every function method which can be used later
    by other modules.
  '''

    def get_serial_numbers(self):
        self.fetch_data_from_file()
        return self.serial_number

    def get_gender_list(self):
        self.fetch_data_from_file()
        return self.gender_list

    def get_number_of_males(self):
        self.fetch_data_from_file()
        return self.number_of_males

    def get_number_of_females(self):
        self.fetch_data_from_file()
        return self.number_of_females

    def get_secondary_school_percentage_list(self):
        self.fetch_data_from_file()
        return self.secondary_school_percentage

    def get_number_of_central_board_in_secondary_school(self):
        self.fetch_data_from_file()
        return self.number_of_central_board_secondary

    def get_number_of_other_boards_in_secondary_school(self):
        self.fetch_data_from_file()
        return self.number_of_other_board_secondary

    def get_high_school_percentage_list(self):
        self.fetch_data_from_file()
        return self.high_school_percentage

    def get_number_of_central_board_in_high_school(self):
        self.fetch_data_from_file()
        return self.number_of_central_board_high

    def get_number_of_other_boards_in_high_school(self):
        self.fetch_data_from_file()
        return self.number_of_other_board_high

    def get_high_school_subjects(self):
        self.fetch_data_from_file()
        return self.high_school_subjects

    def get_number_of_arts_in_high_school(self):
        self.fetch_data_from_file()
        return self.high_school_arts

    def get_number_of_commerce_in_high_school(self):
        self.fetch_data_from_file()
        return self.high_school_commerce

    def get_number_of_science_in_high_school(self):
        self.fetch_data_from_file()
        return self.high_school_science

    def get_college_degree_list(self):
        self.fetch_data_from_file()
        return self.college_degree

    def get_number_of_commerce_management_degree(self):
        self.fetch_data_from_file()
        return self.number_of_commerce_management_degree

    def get_number_of_science_tech_degree(self):
        self.fetch_data_from_file()
        return self.number_of_science_tech_degree

    def get_number_of_other_degree(self):
        self.fetch_data_from_file()
        return self.number_of_other_degree

    def get_college_marks_list(self):
        self.fetch_data_from_file()
        return self.college_marks

    def get_work_experience_list(self):
        self.fetch_data_from_file()
        return self.work_experience

    def get_number_of_no_work_experience(self):
        self.fetch_data_from_file()
        return self.number_of_no_workexp

    def get_number_of_yes_work_experience(self):
        self.fetch_data_from_file()
        return self.number_of_yes_workexp

    def get_students_specialization_list(self):
        self.fetch_data_from_file()
        return self.students_specialization

    def get_students_spec_in_mkt_hr(self):
        self.fetch_data_from_file()
        return self.number_of_mkt_hr_spec

    def get_students_spec_in_mkt_fin(self):
        self.fetch_data_from_file()
        return self.number_of_mkt_fin_spec

    def get_mba_percentage_list(self):
        self.fetch_data_from_file()
        return self.mba_percentage

    def get_student_placement_status_list(self):
        self.fetch_data_from_file()
        return self.student_placement_status

    def get_number_of_placed_students(self):
        self.fetch_data_from_file()
        return self.number_of_student_placed

    def get_number_of_non_placed_students(self):
        self.fetch_data_from_file()
        return self.number_of_student_not_placed

    def get_salary_index_list(self):
        return self.salary_index
