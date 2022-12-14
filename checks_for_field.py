import time
from pywinauto.application import Application
from pywinauto import keyboard


def input_field_check(collection):
    '''this function allows you to check what error is caused by entering a certain amount of a certain character in the input field'''

    app = Application().start(cmd_line=u'"C:\\Users\\User\\Desktop\\TestQA1.exe" ')
    main_window = app.TForm1
    main_window.wait('ready')

    input_field = main_window.Edit
    window = app.Dialog
    button_ok = window[u'\u041e\u041a']


    input_field.click()
    file_name = f"logs/input_field_check_log_{time.strftime('%Y-%m-%d_%H-%M')}.txt"

    with open(file_name, mode='w', encoding='utf-8') as log:
        print(f"Testing input field with {collection} collection\n", file=log, sep="\n")
        for number in collection:
            for i in range(1, 230):
                keyboard.send_keys(number)

            text = window.Static2.texts()
            print(f"Error {text} showed after {len(input_field.texts()[0])} '{number}' symbols", file=log, sep="\n")
            # time.sleep(0.3)
            button_ok.click()
            time.sleep(0.2)
            input_field.click()
            time.sleep(0.2)
            input_field.double_click()
            # keyboard.send_keys('^a^c')
            time.sleep(0.2)
            keyboard.send_keys('{DELETE}')
            time.sleep(0.1)
            input_field.double_click()
            time.sleep(0.1)
            keyboard.send_keys('{DELETE}')

    log.close()
    time.sleep(3)
    app.kill()


def number_buttons_check():
    """this check determines if an error is shown when each button is pressed once, in order from 1 to 9"""

    app = Application().start(cmd_line=u'"C:\\Users\\User\\Desktop\\TestQA1.exe" ')
    main_window = app.TForm1
    main_window.wait('ready')

    window = app.Dialog
    button_ok = window[u'\u041e\u041a']

    button1 = main_window[u'1']
    button2 = main_window[u'2']
    button3 = main_window[u'3']
    button4 = main_window[u'4']
    button5 = main_window[u'5']
    button6 = main_window[u'6']
    button7 = main_window[u'7']
    button8 = main_window[u'8']
    button9 = main_window[u'9']

    buttons_list = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
    file_name = f"logs/click_button_once_in_order_log_{time.strftime('%Y-%m-%d_%H-%M')}.txt"
    with open(file_name, mode='w', encoding='utf-8') as log:
        print(f"Testing buttons in order with a single click\n\n", file=log, sep="\n")
        for elem in buttons_list:
            if elem != button9:
                elem.click()
                try:
                    text = window.Static2.texts()
                    print(f"Error {text} showed after 1 click(s)  on {buttons_list.index(elem) + 1} button", file=log, sep="\n")
                    button_ok.click()
                finally:
                    continue
            else:
                elem.click()
                for i in range(3):
                    try:
                        text = window.Static2.texts()
                        print(f"Error {text} showed after 1 click  on {buttons_list.index(elem) + 1} button", file=log, sep="\n")
                        button_ok.click()
                    finally:
                        continue
    log.close()
    time.sleep(5)
    app.kill()
