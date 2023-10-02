from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QListWidgetItem
from PySide6.QtGui import QShortcut, QKeySequence


from datas import save_task_in_json, get_tasks_from_json, delete_task_from_json, clear_json_list


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TO DO LIST")
        self.resize(400, 600)

        self.create_widgets()
        self.setup_layouts()
        self.setup_connections()
        self.setup_shortcuts()
        self.populate_lw_tasks()
    
    
    def create_widgets(self):
        self.central_area = QWidget() 
        self.setCentralWidget(self.central_area)

        self.le_add_task = QLineEdit()
        self.le_add_task.setPlaceholderText("ex : faire les courses...")
        self.btn_add_task = QPushButton("Ajouter une tâche")
        self.btn_remove_task = QPushButton("Supprimer une tâche")
        self.lw_tasks = QListWidget()
        self.btn_clear_tasks_list = QPushButton("Vider la liste")

    def setup_layouts(self):
        layout = QVBoxLayout(self.central_area)
        layout.addWidget(self.le_add_task)
        layout.addWidget(self.btn_add_task)
        layout.addWidget(self.btn_remove_task)
        layout.addWidget(self.lw_tasks)
        layout.addWidget(self.btn_clear_tasks_list)
        
    def setup_connections(self):
        self.btn_add_task.clicked.connect(self.add_task)
        self.btn_remove_task.clicked.connect(self.remove_task)
        self.btn_clear_tasks_list.clicked.connect(self.clear_list)
       
    def setup_shortcuts(self):
        QShortcut(QKeySequence(Qt.Key_Return), self.le_add_task, self.add_task)
        QShortcut(QKeySequence(Qt.Key_Delete), self.lw_tasks, self.remove_task)

    def add_task(self):
        task = self.le_add_task.text()
        if task:
            item = QListWidgetItem(task)
            item.task = task
            save_task_in_json(item.task)
            self.lw_tasks.addItem(item)
            self.le_add_task.clear()

    def remove_task(self):
        item = self.lw_tasks.currentItem()
        if item:
            delete_task_from_json(item.task)
            self.lw_tasks.takeItem(self.lw_tasks.row(item))

    def populate_lw_tasks(self):
        tasks =  get_tasks_from_json()
        for task in tasks:
            item = QListWidgetItem(task)
            item.task = task
            self.lw_tasks.addItem(item)

    def clear_list(self):
        clear_json_list()
        self.lw_tasks.clear()
        

    


        

