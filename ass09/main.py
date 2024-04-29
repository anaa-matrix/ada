



#shwetakakade2921
#Pap29d6uA7RWVmMC
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QMessageBox, QTableWidget, QTableWidgetItem, QDesktopWidget
# from pymongo import MongoClient
# from bson.objectid import ObjectId

# class LibraryManagementApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()

#         # MongoDB setup
#         self.client = MongoClient('mongodb://localhost:27017')
#         self.db = self.client['library']
#         self.collection = self.db['books']

#     def init_ui(self):
#         self.setWindowTitle('Library Management System')
#         self.resize(800, 600)
#         self.center_window()

#         self.label_operation = QLabel('Select CRUD Operation:')
#         self.btn_add_book = QPushButton('Add Book')
#         self.btn_view_books = QPushButton('View Books')
#         self.btn_update = QPushButton('Update')
#         self.btn_delete = QPushButton('Delete')

#         self.btn_add_book.clicked.connect(lambda: self.perform_operation('Add Book'))
#         self.btn_view_books.clicked.connect(lambda: self.perform_operation('View Books'))
#         self.btn_update.clicked.connect(lambda: self.perform_operation('Update'))
#         self.btn_delete.clicked.connect(lambda: self.perform_operation('Delete'))

#         self.label_title = QLabel('Title:')
#         self.label_author = QLabel('Author:')
#         self.label_year = QLabel('Year:')
#         self.label_result = QLabel()

#         self.input_title = QLineEdit()
#         self.input_author = QLineEdit()
#         self.input_year = QLineEdit()

#         self.result_display = QTableWidget()
#         self.result_display.setColumnCount(3)
#         self.result_display.setHorizontalHeaderLabels(['Title', 'Author', 'Year'])

#         self.result_display.horizontalHeader().setStretchLastSection(True)
#         self.result_display.verticalHeader().setVisible(False)

#         self.layout_operation = QVBoxLayout()
#         self.layout_operation.addWidget(self.label_operation)
#         self.layout_operation.addWidget(self.btn_add_book)
#         self.layout_operation.addWidget(self.btn_view_books)
#         self.layout_operation.addWidget(self.btn_update)
#         self.layout_operation.addWidget(self.btn_delete)

#         self.layout_form = QVBoxLayout()
#         self.layout_form.addWidget(self.label_title)
#         self.layout_form.addWidget(self.input_title)
#         self.layout_form.addWidget(self.label_author)
#         self.layout_form.addWidget(self.input_author)
#         self.layout_form.addWidget(self.label_year)
#         self.layout_form.addWidget(self.input_year)
#         self.layout_form.addWidget(self.label_result)

#         self.layout_input = QHBoxLayout()
#         self.layout_input.addLayout(self.layout_form)
#         self.layout_input.addWidget(self.result_display)

#         self.layout_main = QVBoxLayout()
#         self.layout_main.addLayout(self.layout_operation)
#         self.layout_main.addLayout(self.layout_input)

#         self.setLayout(self.layout_main)

#     def perform_operation(self, operation):
#         if operation == 'Add Book':
#             self.add_book()
#         elif operation == 'View Books':
#             self.view_books()
#         elif operation == 'Update':
#             self.update_book()
#         elif operation == 'Delete':
#             self.delete_book()

#     def add_book(self):
#         title = self.input_title.text()
#         author = self.input_author.text()
#         year = self.input_year.text()

#         if title and author and year:
#             existing_book = self.collection.find_one({'title': title, 'author': author, 'year': year})
#             if existing_book:
#                 QMessageBox.warning(self, 'Warning', 'This book already exists.')
#             else:
#                 document = {'title': title, 'author': author, 'year': year}
#                 self.collection.insert_one(document)
#                 self.show_prompt('Book added successfully.')
#                 self.clear_input_fields()
#         else:
#             self.show_prompt('Please enter all fields.')

#     def view_books(self):
#         books = self.collection.find()
#         self.result_display.setRowCount(0)
#         for row, book in enumerate(books):
#             self.result_display.insertRow(row)
#             self.result_display.setItem(row, 0, QTableWidgetItem(book['title']))
#             self.result_display.setItem(row, 1, QTableWidgetItem(book['author']))
#             self.result_display.setItem(row, 2, QTableWidgetItem(book['year']))

#     def update_book(self):
#         title = self.input_title.text()
#         author = self.input_author.text()
#         year = self.input_year.text()

#         if title:
#             book = self.collection.find_one({'title': title})
#             if book:
#                 self.collection.update_one({'_id': ObjectId(book['_id'])}, {'$set': {'author': author, 'year': year}})
#                 self.show_prompt('Book updated successfully.')
#                 self.clear_input_fields()
#             else:
#                 self.show_prompt('Book not found.')
#         else:
#             self.show_prompt('Please enter title.')

#     def delete_book(self):
#         title = self.input_title.text()

#         if title:
#             book = self.collection.find_one({'title': title})
#             if book:
#                 self.collection.delete_one({'_id': ObjectId(book['_id'])})
#                 self.show_prompt('Book deleted successfully.')
#                 self.clear_input_fields()
#             else:
#                 self.show_prompt('Book not found.')
#         else:
#             self.show_prompt('Please enter title.')

#     def clear_input_fields(self):
#         self.input_title.clear()
#         self.input_author.clear()
#         self.input_year.clear()

#     def show_prompt(self, message):
#         QMessageBox.information(self, 'Info', message)

#     def center_window(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = LibraryManagementApp()
#     window.show()
#     sys.exit(app.exec_())



# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QMessageBox, QTableWidget, QTableWidgetItem, QDesktopWidget
# from pymongo import MongoClient
# from bson.objectid import ObjectId

# class LibraryManagementApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()

#         # MongoDB setup
#         self.client = MongoClient('mongodb://localhost:27017')
#         self.db = self.client['library']
#         self.collection = self.db['books']

#     def init_ui(self):
#         self.setWindowTitle('Library Management System')
#         self.resize(800, 600)
#         self.center_window()

#         self.setStyleSheet('''
#             QWidget {
#                 background-color: #f0f0f0; /* Set background color for the main window */
#             }
#             QLabel {
#                 background-color: #d3d3d3; /* Set background color for labels */
#             }
#             QLineEdit {
#                 background-color: #ffffff; /* Set background color for line edits */
#             }
#             QPushButton {
#                 background-color: #4caf50; /* Set background color for buttons */
#                 color: white; /* Set text color for buttons */
#             }
#             QTableWidget {
#                 background-color: #ffffff; /* Set background color for table widget */
#             }
#         ''')

#         self.label_operation = QLabel('Select CRUD Operation:')
#         self.btn_add_book = QPushButton('Add Book')
#         self.btn_view_books = QPushButton('View Books')
#         self.btn_update = QPushButton('Update')
#         self.btn_delete = QPushButton('Delete')

#         self.btn_add_book.clicked.connect(lambda: self.perform_operation('Add Book'))
#         self.btn_view_books.clicked.connect(lambda: self.perform_operation('View Books'))
#         self.btn_update.clicked.connect(lambda: self.perform_operation('Update'))
#         self.btn_delete.clicked.connect(lambda: self.perform_operation('Delete'))

#         self.label_title = QLabel('Title:')
#         self.label_author = QLabel('Author:')
#         self.label_year = QLabel('Year:')
#         self.label_result = QLabel()

#         self.input_title = QLineEdit()
#         self.input_author = QLineEdit()
#         self.input_year = QLineEdit()

#         self.result_display = QTableWidget()
#         self.result_display.setColumnCount(3)
#         self.result_display.setHorizontalHeaderLabels(['Title', 'Author', 'Year'])

#         self.result_display.horizontalHeader().setStretchLastSection(True)
#         self.result_display.verticalHeader().setVisible(False)

#         self.layout_operation = QVBoxLayout()
#         self.layout_operation.addWidget(self.label_operation)
#         self.layout_operation.addWidget(self.btn_add_book)
#         self.layout_operation.addWidget(self.btn_view_books)
#         self.layout_operation.addWidget(self.btn_update)
#         self.layout_operation.addWidget(self.btn_delete)

#         self.layout_form = QVBoxLayout()
#         self.layout_form.addWidget(self.label_title)
#         self.layout_form.addWidget(self.input_title)
#         self.layout_form.addWidget(self.label_author)
#         self.layout_form.addWidget(self.input_author)
#         self.layout_form.addWidget(self.label_year)
#         self.layout_form.addWidget(self.input_year)
#         self.layout_form.addWidget(self.label_result)

#         self.layout_input = QHBoxLayout()
#         self.layout_input.addLayout(self.layout_form)
#         self.layout_input.addWidget(self.result_display)

#         self.layout_main = QVBoxLayout()
#         self.layout_main.addLayout(self.layout_operation)
#         self.layout_main.addLayout(self.layout_input)

#         self.setLayout(self.layout_main)

#     def perform_operation(self, operation):
#         if operation == 'Add Book':
#             self.add_book()
#         elif operation == 'View Books':
#             self.view_books()
#         elif operation == 'Update':
#             self.update_book()
#         elif operation == 'Delete':
#             self.delete_book()

#     def add_book(self):
#         title = self.input_title.text()
#         author = self.input_author.text()
#         year = self.input_year.text()

#         if title and author and year:
#             existing_book = self.collection.find_one({'title': title, 'author': author, 'year': year})
#             if existing_book:
#                 QMessageBox.warning(self, 'Warning', 'This book already exists.')
#             else:
#                 document = {'title': title, 'author': author, 'year': year}
#                 self.collection.insert_one(document)
#                 self.show_prompt('Book added successfully.')
#                 self.clear_input_fields()
#         else:
#             self.show_prompt('Please enter all fields.')

#     def view_books(self):
#         books = self.collection.find()
#         self.result_display.setRowCount(0)
#         for row, book in enumerate(books):
#             self.result_display.insertRow(row)
#             self.result_display.setItem(row, 0, QTableWidgetItem(book['title']))
#             self.result_display.setItem(row, 1, QTableWidgetItem(book['author']))
#             self.result_display.setItem(row, 2, QTableWidgetItem(book['year']))

#     def update_book(self):
#         title = self.input_title.text()
#         author = self.input_author.text()
#         year = self.input_year.text()

#         if title:
#             book = self.collection.find_one({'title': title})
#             if book:
#                 self.collection.update_one({'_id': ObjectId(book['_id'])}, {'$set': {'author': author, 'year': year}})
#                 self.show_prompt('Book updated successfully.')
#                 self.clear_input_fields()
#             else:
#                 self.show_prompt('Book not found.')
#         else:
#             self.show_prompt('Please enter title.')

#     def delete_book(self):
#         title = self.input_title.text()

#         if title:
#             book = self.collection.find_one({'title': title})
#             if book:
#                 self.collection.delete_one({'_id': ObjectId(book['_id'])})
#                 self.show_prompt('Book deleted successfully.')
#                 self.clear_input_fields()
#             else:
#                 self.show_prompt('Book not found.')
#         else:
#             self.show_prompt('Please enter title.')

#     def clear_input_fields(self):
#         self.input_title.clear()
#         self.input_author.clear()
#         self.input_year.clear()

#     def show_prompt(self, message):
#         QMessageBox.information(self, 'Info', message)

#     def center_window(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = LibraryManagementApp()
#     window.show()
#     sys.exit(app.exec_())





import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QMessageBox, QTableWidget, QTableWidgetItem, QDesktopWidget
from pymongo import MongoClient
from bson.objectid import ObjectId

class LibraryManagementApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        # MongoDB setup
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['library']
        self.collection = self.db['books']

    def init_ui(self):
        self.setWindowTitle('Library Management System')
        self.resize(800, 600)
        self.center_window()

        self.setStyleSheet('''
            QWidget {
                background-color: #F5DEB3; /* Background color */
            }
            QLabel {
                font-weight: bold; /* Bold text */
            }
            QLineEdit, QTextEdit {
                background-color: #FFFFFF; /* White background for input fields */
            }
            QPushButton {
                background-color: #D3D3D3; /* Gray background for buttons */
                color: #000000; /* Black text color for buttons */
            }
            QTableWidget {
                background-color: #FFF9F0; /* Gray background for table */
            }
        ''')

        self.label_operation = QLabel('Select CRUD Operation:')
        self.btn_add_book = QPushButton('Add Book')
        self.btn_view_books = QPushButton('View Books')
        self.btn_update = QPushButton('Update')
        self.btn_delete = QPushButton('Delete')

        self.btn_add_book.clicked.connect(lambda: self.perform_operation('Add Book'))
        self.btn_view_books.clicked.connect(lambda: self.perform_operation('View Books'))
        self.btn_update.clicked.connect(lambda: self.perform_operation('Update'))
        self.btn_delete.clicked.connect(lambda: self.perform_operation('Delete'))

        self.label_title = QLabel('Title:')
        self.label_author = QLabel('Author:')
        self.label_year = QLabel('Year:')
        self.label_result = QLabel()

        self.input_title = QLineEdit()
        self.input_author = QLineEdit()
        self.input_year = QLineEdit()

        self.result_display = QTableWidget()
        self.result_display.setColumnCount(3)
        self.result_display.setHorizontalHeaderLabels(['Title', 'Author', 'Year'])

        self.result_display.horizontalHeader().setStretchLastSection(True)
        self.result_display.verticalHeader().setVisible(False)

        self.layout_operation = QVBoxLayout()
        self.layout_operation.addWidget(self.label_operation)
        self.layout_operation.addWidget(self.btn_add_book)
        self.layout_operation.addWidget(self.btn_view_books)
        self.layout_operation.addWidget(self.btn_update)
        self.layout_operation.addWidget(self.btn_delete)

        self.layout_form = QVBoxLayout()
        self.layout_form.addWidget(self.label_title)
        self.layout_form.addWidget(self.input_title)
        self.layout_form.addWidget(self.label_author)
        self.layout_form.addWidget(self.input_author)
        self.layout_form.addWidget(self.label_year)
        self.layout_form.addWidget(self.input_year)
        self.layout_form.addWidget(self.label_result)

        self.layout_input = QHBoxLayout()
        self.layout_input.addLayout(self.layout_form)
        self.layout_input.addWidget(self.result_display)

        self.layout_main = QVBoxLayout()
        self.layout_main.addLayout(self.layout_operation)
        self.layout_main.addLayout(self.layout_input)

        self.setLayout(self.layout_main)

    def perform_operation(self, operation):
        if operation == 'Add Book':
            self.add_book()
        elif operation == 'View Books':
            self.view_books()
        elif operation == 'Update':
            self.update_book()
        elif operation == 'Delete':
            self.delete_book()

    def add_book(self):
        title = self.input_title.text()
        author = self.input_author.text()
        year = self.input_year.text()

        if title and author and year:
            existing_book = self.collection.find_one({'title': title, 'author': author, 'year': year})
            if existing_book:
                QMessageBox.warning(self, 'Warning', 'This book already exists.')
            else:
                document = {'title': title, 'author': author, 'year': year}
                self.collection.insert_one(document)
                self.show_prompt('Book added successfully.')
                self.clear_input_fields()
        else:
            self.show_prompt('Please enter all fields.')

    def view_books(self):
        books = self.collection.find()
        self.result_display.setRowCount(0)
        for row, book in enumerate(books):
            self.result_display.insertRow(row)
            self.result_display.setItem(row, 0, QTableWidgetItem(book['title']))
            self.result_display.setItem(row, 1, QTableWidgetItem(book['author']))
            self.result_display.setItem(row, 2, QTableWidgetItem(book['year']))

    def update_book(self):
        title = self.input_title.text()
        author = self.input_author.text()
        year = self.input_year.text()

        if title:
            book = self.collection.find_one({'title': title})
            if book:
                self.collection.update_one({'_id': ObjectId(book['_id'])}, {'$set': {'author': author, 'year': year}})
                self.show_prompt('Book updated successfully.')
                self.clear_input_fields()
            else:
                self.show_prompt('Book not found.')
        else:
            self.show_prompt('Please enter title.')

    def delete_book(self):
        title = self.input_title.text()

        if title:
            book = self.collection.find_one({'title': title})
            if book:
                self.collection.delete_one({'_id': ObjectId(book['_id'])})
                self.show_prompt('Book deleted successfully.')
                self.clear_input_fields()
            else:
                self.show_prompt('Book not found.')
        else:
            self.show_prompt('Please enter title.')

    def clear_input_fields(self):
        self.input_title.clear()
        self.input_author.clear()
        self.input_year.clear()

    def show_prompt(self, message):
        QMessageBox.information(self, 'Info', message)

    def center_window(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LibraryManagementApp()
    window.show()
    sys.exit(app.exec_())
