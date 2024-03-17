from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGroupBox, QPushButton,
    QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QButtonGroup, QMessageBox
)
import random

class Question:
    def __init__(self, text, right_answer, wrong1, wrong2, wrong3):
        self.text = text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions = [
    Question('Какие ваши любимые фильмы?', 'Зачем?', 'А?', 'Что?', 'Да.'),
    Question('Как вы относитесь к здоровому образу жизни?', 'Нет.?', 'А?', 'Что?', 'Да.'),
    Question('Какие книги вы читаете?', 'Зачем?', 'ЪЫЪ', '6', 'Да.'),
    Question('Какие у вас планы на будущее?', 'Зачем?', 'А?', 'Естественно.', 'Да.'),
    Question('Какие музыкальные жанры вы предпочитаете?', 'Вот.', 'А?', 'че', 'Да.'),
    Question('Как вы проводите свободное время?', 'Зачем?', 'А?', 'Что?', 'Да.'),
    Question('Как вы считаете, что является самым важным в жизни?', '4?', 'А?', 'Что?', 'лываловы.'),
    Question('Какие путешествия вы уже совершили?', 'Октябрь', 'Почему?', 'Что?', 'Да.'),
    Question('Какие фильмы вы рекомендуете посмотреть?', 'Зачем?', 'А?', 'Да?', 'Да.'),
    Question('Что вы думаете о современном искусстве?', 'Конечно?', 'Меньше, чем 8', 'Что?', 'Да.'),
]

def is_checked():
    for rbtn in answers_btn:
        if rbtn.isChecked():
            return True
    return False


def show_result():
    if not is_checked():
        return

    btn.setText('Следующий вопрос')
    for rbtn in answers_btn:
        rbtn.setDisabled(True)
        if rbtn.isChecked():
            if rbtn.text() == answers_btn[0].text():
                rbtn.setStyleSheet('color: green;')
                main_win.score += 1 
            else:
                rbtn.setStyleSheet('color: red;')
                answers_btn[0].setStyleSheet('color: green;')
        


def show_quetion():
    next_quetion()
    btn.setText('Ответить')
    button_group.setExclusive(False)
    for rbtn in answers_btn:
        rbtn.setDisabled(False)
        rbtn.setChecked(False)
        rbtn.setStyleSheet('')
    button_group.setExclusive(True)


def start_test():
    if btn.text() == 'Ответить':
        show_result()
    else:
        show_quetion()

def ask(q: Question):
    question_text.setText(q.text)
    random.shuffle(answers_btn)
    answers_btn[0].setText(q.right_answer)
    answers_btn[1].setText(q.wrong1)
    answers_btn[2].setText(q.wrong2)
    answers_btn[3].setText(q.wrong3)

def next_quetion():
    if main_win.q_index == len(questions) - 1:
        main_win.q_index = -1
        random.shuffle(questions)
        show_score()
        main_win.score = 0

    main_win.q_index += 1
    q = questions[main_win.q_index]
    ask(q)

def show_score():
    percent = main_win.score / main_win.total * 100  
    percent = round(percent, 2)
    text = 'Короче\n'
    text += 'Ты норм ответил на ' + str(main_win.score) + ' из ' + str(main_win.total) + ' вопросов.\n'
    text += 'Процент правильных ответов: ' + str(percent) + '%.' 

    msg = QMessageBox()
    msg.setWindowTitle('Результат')
    msg.setText(text)
    msg.exec()


app = QApplication([])                          
main_win = QWidget()                            
main_win.setWindowTitle('MemoryCard')           
main_win.resize(640, 480)            
main_win.q_index = -1           

main_win.score = 0  # счетчик правильных ответов
main_win.total = len(questions)  # счетчик всего ответов
main_win.setStyleSheet('font-size: 30px;')


question_text = QLabel('Тут будет вопрос?')     
grp_box = QGroupBox('Варианты ответов')         
radio1 = QRadioButton('Нет')                    
radio2 = QRadioButton('Да')                     
radio3 = QRadioButton('Что')                    
radio4 = QRadioButton('Зачем?')                 
btn = QPushButton('Ответить') 

answers_btn = [radio1, radio2, radio3, radio4]


button_group = QButtonGroup()
button_group.addButton(radio1)
button_group.addButton(radio2)
button_group.addButton(radio3)
button_group.addButton(radio4)

main_layout = QVBoxLayout()
main_h1 = QHBoxLayout()
main_h2 = QHBoxLayout()
main_h3 = QHBoxLayout()
grp_layput = QHBoxLayout()
grp_v1 = QVBoxLayout()
grp_v2 = QVBoxLayout()


main_h1.addWidget(question_text, alignment=Qt.AlignCenter)
main_h2.addWidget(grp_box)
main_h3.addWidget(btn, alignment=Qt.AlignCenter)
main_layout.addLayout(main_h1)
main_layout.addLayout(main_h2)
main_layout.addLayout(main_h3)
grp_v1.addWidget(radio1)
grp_v1.addWidget(radio2)
grp_v2.addWidget(radio3)
grp_v2.addWidget(radio4)
grp_layput.addLayout(grp_v1)
grp_layput.addLayout(grp_v2)
grp_box.setLayout(grp_layput)
main_win.setLayout(main_layout)

btn.clicked.connect(start_test)

random.shuffle(questions)
next_quetion()

main_win.show()
app.exec()
