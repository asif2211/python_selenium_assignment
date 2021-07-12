from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time
from selenium.common.exceptions import TimeoutException
import csv


class AeromexicoCheckinDesktopPagae():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "Python selenium Assignment"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def read_csv_file(self,questions,answers,correc_answers):

        # header = ['Questions', 'Answers', 'Correct Answers']
        files =  open("test_data_file_new.csv", "a")
        writer = csv.writer(files, delimiter='\t')
        # writer.writerow(header)
        for w in range(len(questions)):
            writer.writerow([questions[w],answers[w],correc_answers[w]])
        files.close()

    def google_sign_in_test_cases(self):

        wait = WebDriverWait(
            self.driver,
            1000

        )
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#headingText > span'))).text

        assert "Sign in" in element
        print(self.driver.title)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.Xb9hP > input')))
        element.clear()
        element.send_keys('m.asif@arbisoft.com')

        submit_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR
                                , '.VfPpkd-dgl2Hf-ppHlrf-sM5MNb  > button')))

        submit_btn.click()
        # validate password screen
        passwordAssertion = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                                        , '#password > div.aCsJod.oJeWuf > div > div.Xb9hP'))).text

        assert "Enter your password" in passwordAssertion

        print(self.driver.title)

        password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password > div input')))

        password.send_keys('D5!4Ftmp')

        password_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#passwordNext > div button')))

        password_btn.click()

    def page_title_test_case(self):

        wait = WebDriverWait(
            self.driver,
            1000

        )

        #  check title

        check_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR
            ,'.freebirdFormviewerViewHeaderTitle.exportFormTitle'))).text

        assert 'Automation Assessment' in check_title

    def required_error_test_cases(self):

        wait = WebDriverWait(
            self.driver,
            1000
        )

        submit_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR
                     , 'span[class*="ppsMaterialWizButtonPaperbuttonLabel"]')))
        submit_btn.click()

        print('button clicked for required fields')

        required_field_error_msg = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                                    , '.freebirdFormviewerComponentsQuestionBaseValidationError')))

        # get title of input fileds like Name *
        all_input_title = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
         , '.freebirdFormviewerComponentsQuestionBaseTitleDescContainer > div.freebirdFormviewerComponentsQuestionBaseTitle')))

        # interacting with input fileds
        # check required error msg

        for i in range(len(all_input_title)):

            print(all_input_title[i].text + required_field_error_msg[i].text)

        print('required error message noted')

    def check_Validation_With_negative_test_screen_one(self):

        wait = WebDriverWait(
            self.driver,
            10
        )

        email_value = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                            ,'.freebirdFormviewerViewNumberedItemContainer input')))

        print('-- negative test cases starts --')

        # check if all fields are empty then no button submitted
        for i in range(len(email_value)):

            if email_value[i].get_attribute("value") == "":

                print('please fill all answers')
            else:
                submit_Btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR
                                 ,'span[class*="ppsMaterialWizButtonPaperbuttonLabel"]')))
                submit_Btn.click()

        # get title of input fileds like Name *

        all_input_title = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                            ,     '.freebirdFormviewerComponentsQuestionBaseTitleDescContainer > div.freebirdFormviewerComponentsQuestionBaseTitle')))

        print("Page is ready!")

        print("Loading took too much time!")

        all_input_values = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR
                       ,   '.quantumWizTextinputPaperinputInputArea .quantumWizTextinputPaperinputInput')))
        time.sleep(.5)
        list_of_data = []
        answer_list = []
        for i in range(len(all_input_title)):
            print(all_input_title[i].text)
            list_of_data.append(all_input_title[i].text)

            if all_input_title[i].text == "CNIC *":
                all_input_values[i].send_keys('1234567890')

            else:
                print('Cnic is not exist')

            if all_input_title[i].text == "Name *":
                all_input_values[i].send_keys('asif')
            else:
                print('Name is not exist')

            if all_input_title[i].text == "Email *":
                all_input_values[i].send_keys('asifbsitgmail.com')
            else:
                print('Email is not exist')

            if all_input_title[i].text == "Phone Number *":
                all_input_values[i].send_keys('1234567890')
            else:
                print('Phone is not exist')

        # interacting with pattern varifications

        all_input_pattern_varifications = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                       , '.freebirdFormviewerComponentsQuestionBaseValidationError')))

        # check validation as expected
        time.sleep(.5)
        for i in range(len(all_input_title)):
            # self.append_dict_as_row(all_input_title[i])
            if all_input_title[i].text == "CNIC *":

                assert "Must match pattern" in all_input_pattern_varifications[i].text

                print(all_input_title[i].text + 'getting 13 digits')
                break
            if all_input_title[i].text == "Email *":

                assert "Must be a valid email" in all_input_pattern_varifications[i].text

                print(all_input_title[i].text + 'getting proper email pattern')

            if all_input_title[i].text == "Phone Number *":

                assert "Must match pattern" in all_input_pattern_varifications[i].text

                print(all_input_title[i].text + 'getting proper 11 digits')

            submit_Btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR
                                                                    ,
                                                                    'span[class*="ppsMaterialWizButtonPaperbuttonLabel"]')))
            submit_Btn.click()
        # empty fields
        for i in range(len(all_input_title)):
            all_input_values[i].clear()

        print('-- Negative test cases ends --')
    # CSV for this


    def positive_test_cases(self):
        wait = WebDriverWait(
            self.driver,
            50
        )

        required_field_error_msg = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                                    , '.freebirdFormviewerComponentsQuestionBaseValidationError')))

        # get title of input fileds like Name *

        all_input_title = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
         , '.freebirdFormviewerComponentsQuestionBaseTitleDescContainer > div.freebirdFormviewerComponentsQuestionBaseTitle')))
        # interacting with input fileds

        all_input_values = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                                        , '.quantumWizTextinputPaperinputInputArea input')))

        print('-- positive testcases starts -- ')
        answer_list = []
        question_list = []
        for i in range(len(all_input_title)):

            question_list.append((all_input_title[i].text))
            if all_input_title[i].text == "CNIC *":
                all_input_values[i].send_keys('3130125298621')

            if all_input_title[i].text == "Email *":
                all_input_values[i].send_keys('m.asif@arbisoft.com')

            if all_input_title[i].text == "Phone Number *":
                all_input_values[i].send_keys('12345612345')

            if all_input_title[i].text == "Name *":
                all_input_values[i].send_keys('Muhammad Asif')

            answer_list.append(all_input_title[i].get_attribute("value"))
        all_input_values = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                           ,    '.quantumWizTextinputPaperinputInputArea input')))

        answer_list = [x.get_attribute('value') for x in all_input_values]

        submit_Btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR
                     , 'span[class*="ppsMaterialWizButtonPaperbuttonLabel"]')))

        submit_Btn.click()
        correct_answers = []
        correct_answers = answer_list
        print('-- positive testcases starts ends page 1 --')
        # write file in csv formate
        header = ['Questions', 'Answers', 'Correct Answers']
        files = open("test_data_file_new.csv", "a")
        writer = csv.writer(files, delimiter=',')
        writer.writerow(header)
        for w in range(len(question_list)):
            writer.writerow([question_list[w], answer_list[w], correct_answers[w]])
        files.close()
        del files

    def check_required_field_test_screen_two(self):

            wait = WebDriverWait(
                self.driver,
                100
            )

            # check screen question title

            secreen_two_question_heading_verification = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR
                                                    ,  '.freebirdMaterialHeaderbannerPagebreakText')))

            assert  'Multiple type Questions' in secreen_two_question_heading_verification.text

            print('Multiple type Questions screen exist')

            # button clicked for check required error messages

            submit_Btn = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                         ,  'span[class*="appsMaterialWizButtonPaperbuttonLabel"]')))

            print('next button clicked')

            check_box = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                             , '.appsMaterialWizToggleRadiogroupOffRadio')))

            check_box_value = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                             , '.docssharedWizToggleLabeledLabelText')))

            question_element = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                              , '.freebirdFormviewerComponentsQuestionBaseTitle')))

            question_text_list = [list.text for list in question_element]
            questions_screen_two = []
            answers_screen_two = []
            for i in range(len(check_box_value)):

                if check_box_value[i].text == "Password":
                    check_box[i].click()
                    answers_screen_two.append((check_box_value[i].text))
                    logging.info('Password is selected as answer')

                if check_box_value[i].text == "Inspecting Elements":
                    check_box[i].click()
                    answers_screen_two.append((check_box_value[i].text))
                    logging.info('Inspecting Elements is selected as answer')
                    print('--- ending of page 2 ---')

            for text_index in range(len(question_text_list)):
                questions_screen_two.append(question_text_list[text_index])

            self.read_csv_file(questions_screen_two, answers_screen_two,answers_screen_two)
            submit_Btn[1].click()

    def check_required_field_test_screen_third(self):

            wait = WebDriverWait(
                self.driver,
                100
            )

            # check screen question title

            secreen_two_question_heading_verification = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR
            ,  '.freebirdMaterialHeaderbannerPagebreakText'))).text

            assert 'Checkboxes' in secreen_two_question_heading_verification

            print('Checkboxes screen exist')

            # button clicked for check required error messages

            submit_Btn = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                         ,  'span[class*="appsMaterialWizButtonPaperbuttonLabel"]')))

            print('next button clicked page 3')

            check_box = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                             , '.quantumWizTogglePapercheckboxInnerBox')))

            check_box_value = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                             , '.docssharedWizToggleLabeledLabelText')))
            question_element = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                                ,  '.freebirdFormviewerComponentsQuestionBaseTitle')))
            question_text_list = [list.text for list in question_element]
            questions_screen_third = []
            answers_screen_two = []
            value_of_third_ans = ""
            value_of_first_ans = ""
            value_of_second_ans = ""
            value_of_fourth_ans = ""
            for text_index in range(len(question_text_list)):
                if question_text_list[text_index] == "Select the two numbers that are not prime. *":
                    questions_screen_third.append(question_text_list[text_index])
                    for i in range(len(check_box_value)):

                        if check_box_value[i].text == "21":
                            check_box[i].click()
                            value_of_first_ans = check_box_value[i].text
                            logging.info('21 is selected as answer')

                        if check_box_value[i].text == "51":
                            check_box[i].click()
                            value_of_second_ans = check_box_value[i].text
                            logging.info('51 is selected as answer')

                if question_text_list[text_index] == "Select the correct answers *":
                    questions_screen_third.append(question_text_list[text_index])
                    for i in range(len(check_box_value)):

                        if check_box_value[i].text == "63/7 = 54/6":
                            value_of_third_ans = check_box_value[i].text
                            check_box[i].click()
                            logging.info('63/7 = 54/6 is selected as answer')

                        if check_box_value[i].text == "4*10 = 5*8":
                            value_of_fourth_ans = check_box_value[i].text
                            check_box[i].click()
                            logging.info('4*10 = 5*8 is selected as answer')

            answers_screen_two.append([value_of_first_ans, value_of_second_ans])
            answers_screen_two.append([value_of_third_ans, value_of_fourth_ans])
            print(answers_screen_two)
            submit_Btn[1].click()
            print('next button clicked page 3')

            self.read_csv_file(questions_screen_third, answers_screen_two,answers_screen_two)

    def check_required_field_test_screen_fourth(self):
        print("-- Starting of screen 4")
        logging.info('-- Starting of screen 4 ')
        wait = WebDriverWait(
            self.driver,
            10
        )

        submit_Btn = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR
                        ,'span[class*="appsMaterialWizButtonPaperbuttonLabel"]')))

        dropdown_element = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR
                              , '.quantumWizMenuPaperselectEl')))

        question_element = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR
                               , '.freebirdFormviewerComponentsQuestionBaseTitle')))

        questions_screen_fourth = []
        answers_screen_fourth = []
        correct_answers_fourth = []

        get_array = [x for x in dropdown_element]
        print(len(get_array))
        get_question_text = [x.text for x in question_element]

        for que_text in get_question_text:
            questions_screen_fourth.append(que_text)

        for line in get_array:
            time.sleep(1)
            line.click()
            dropdown_value_click = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                , '.exportSelectPopup .quantumWizMenuPaperselectOption[data-value="Lahore"]')))
            dropdown_value_click.click()
            answers_screen_fourth.append('Lahore')

        time.sleep(1)
        submit_Btn[1].click()
        print("-- end of screen 4")
        logging.info('-- Ending of screen 4 ')
        for shuffle_text in questions_screen_fourth:
            if shuffle_text == "Capital of Punjab *":
                correct_answers_fourth.append('Lahore')

            if shuffle_text == "Capital of Pakistan *":
                correct_answers_fourth.append('Islamabad')

        self.read_csv_file(questions_screen_fourth, answers_screen_fourth, correct_answers_fourth)

    def check_required_field_test_screen_fith(self):

        wait = WebDriverWait(
            self.driver,
            100
        )

        submit_Btn = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR
                         ,  '.freebirdFormviewerViewNavigationButtonsAndProgress .appsMaterialWizButtonPaperbuttonContent.exportButtonContent .appsMaterialWizButtonPaperbuttonLabel')))

        submit_Btn[1].click()

        print('button submitted')

        # test error messages
        file_text_test = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR
                          ,   '.freebirdFormviewerComponentsQuestionBaseValidationError')))

        for i in range(len(file_text_test)):
            print(file_text_test[i].text)
            if file_text_test[i].text == "This is a required question":

                error_message_text = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR
                                  , '.freebirdFormviewerComponentsQuestionBaseTitle.exportItemTitle')))
                print(error_message_text[i].text)
                print(file_text_test[i].text,error_message_text[i].text)
        time.sleep(2)
        # for pics file code
        title_text_element = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR
                              ,     '.freebirdFormviewerComponentsQuestionBaseTitle.exportItemTitle')))
        file_elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR
                                                                             , '.appsMaterialWizButtonEl')))
        title_text = [element.text for element in title_text_element]
        for text_index in range(len(title_text)):

            if title_text[text_index] == "Upload pdf file *" and text_index == 0:

                file_elements[text_index].click()

                print('element exist pdf')
                iframes_element = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR
                                                          , '.modal-dialog-content > iframe')))
                for iframe_element in iframes_element:

                    wait.until(EC.frame_to_be_available_and_switch_to_it(iframe_element.get_attribute('id')))
                    file_title_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                                                                      , '#picker\:ht')))
                    file_title_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                                                                      , '#\:6 > div')))
                    if file_title_element.text == "My Drive":
                        file_title_element.click()

                        select_file_pdf = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                          , '#\:11\.DoclistBlob\.0\.0BzYBeycVEeLHc3RhcnRlcl9maWxlX2Rhc2hlclYw\:label > div')))

                        if select_file_pdf:
                            select_file_pdf.click()
                            select_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                         , '#picker\:ap\:2')))
                            select_btn.click()

                            # print('pdf selected')

            if title_text[text_index] == "Upload pdf file *" and text_index == 1:
                file_elements_pdf = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR
                                               , '.appsMaterialWizButtonEl')))
                file_elements_pdf[text_index].click()
                print('element exist pdf')
                iframes_element = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR
                                                          , '.modal-dialog-content > iframe')))
                for iframe_element in iframes_element:

                    wait.until(EC.frame_to_be_available_and_switch_to_it(iframe_element.get_attribute('id')))
                    file_title_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                                                                      , '#picker\:ht')))
                    file_title_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                                                                      , '#\:6 > div')))
                    if file_title_element.text == "My Drive":
                        file_title_element.click()

                        select_file_pdf = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                          , '#\:11\.DoclistBlob\.0\.0BzYBeycVEeLHc3RhcnRlcl9maWxlX2Rhc2hlclYw\:label > div')))

                        if select_file_pdf:
                            select_file_pdf.click()
                            select_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                         , '#picker\:ap\:2')))
                            select_btn.click()

            if title_text[text_index] == "Upload Image File *" and text_index == 1:
                print('Upload Image File *')
                file_elements_img = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR
                                      , '.appsMaterialWizButtonEl')))
                file_elements_img[2].click()

                iframes_element = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR
                                                   ,    '.modal-dialog-content > iframe')))

                for iframe_element in iframes_element:

                    wait.until(EC.frame_to_be_available_and_switch_to_it(iframe_element.get_attribute('id')))
                    file_title_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                                                                      , '#picker\:ht')))
                    file_title_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                                                                      , '#\:6 > div')))
                    if file_title_element.text == "My Drive":
                        file_title_element.click()
                        select_file_pics = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                           ,  '#\:11\.docs\.0\.1Mpz-VWKxWDcgFc9ryNJ2aIuEzLzeMUul')))

                        if select_file_pics:
                            select_file_pics.click()
                            select_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                                , '#picker\:ap\:2')))

                            select_btn.click()

            if title_text[text_index] == "Upload Image File *" and text_index == 0:
                print('Upload Image File *')

                file_elements[text_index].click()

                iframes_element = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR
                                                   ,    '.modal-dialog-content > iframe')))

                for iframe_element in iframes_element:

                    wait.until(EC.frame_to_be_available_and_switch_to_it(iframe_element.get_attribute('id')))
                    file_title_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                                                                      , '#picker\:ht')))
                    file_title_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                                                                      , '#\:6 > div')))
                    if file_title_element.text == "My Drive":
                        file_title_element.click()
                        select_file_pics = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                           ,  '#\:11\.docs\.0\.1Mpz-VWKxWDcgFc9ryNJ2aIuEzLzeMUul')))

                        if select_file_pics:
                            select_file_pics.click()
                            select_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                                , '#picker\:ap\:2')))

                            select_btn.click()
                            print('more than 1 file can be uploaded and file size is equal to 1 MB')

            if title_text[text_index] == "Upload Image File *" and text_index == 1:
                print('Upload Image File *')

                file_elements[text_index].click()
                iframes_element = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR
                                    ,  '.modal-dialog-content > iframe')))

                for iframe_element in iframes_element:

                    wait.until(EC.frame_to_be_available_and_switch_to_it(iframe_element.get_attribute('id')))
                    file_title_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                                                   , '#picker\:ht')))
                    file_title_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                                                   , '#\:6 > div')))
                    if file_title_element.text == "My Drive":
                        file_title_element.click()
                        select_file_pics = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                                 ,  '#\:11\.docs\.0\.1Mpz-VWKxWDcgFc9ryNJ2aIuEzLzeMUul')))

                        if select_file_pics:
                            select_file_pics.click()
                            select_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR
                                                            , '#picker\:ap\:2')))

                            select_btn.click()
                            print('more than 1 file can be uploaded and file size is equal to 1 MB')

