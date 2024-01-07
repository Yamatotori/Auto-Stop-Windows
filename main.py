import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QTimer
import os
import datetime

class ShutdownScheduler(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.shutdown_time = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_countdown)
        self.timer.start(1000)  # Met à jour toutes les secondes

    def initUI(self):
        self.setGeometry(300, 300, 700, 300)
        self.setWindowTitle('Planificateur d\'arrêt')
        self.setWindowIcon(QIcon('logo.png'))  # Remplacez 'path_to_your_icon.png' par le chemin de votre icône

        layout = QVBoxLayout()

        # Label pour le prochain arrêt
        self.label = QLabel('Prochain arrêt non programmé.', self)
        self.label.setFont(QFont('Arial', 12))
        layout.addWidget(self.label)

        h_layout = QHBoxLayout()

        # Champs de saisie Heures
        font = QFont('Arial', 12)
        self.hour_entry = QLineEdit(self)
        self.hour_entry.setFont(font)
        self.hour_entry.setPlaceholderText("Heures")
        h_layout.addWidget(self.hour_entry)

         # Champs de saisie Minutes
        self.min_entry = QLineEdit(self)
        self.min_entry.setFont(font)
        self.min_entry.setPlaceholderText("Minutes")
        h_layout.addWidget(self.min_entry)

        layout.addLayout(h_layout)

        # Bouton pour programmer l'arrêt
        self.shutdown_button = QPushButton('Programmer l\'arrêt', self)
        self.shutdown_button.clicked.connect(self.schedule_shutdown)
        self.shutdown_button.setStyleSheet("QPushButton { background-color: #0078D7; color: white; border-radius: 5px; font-size: 16px; padding: 10px; }"
                                           "QPushButton:hover { background-color: #0057B8; }")
        self.shutdown_button.setIcon(QIcon(QPixmap('plus_icon.png')))  # Remplacez 'plus_icon.png' par le chemin de votre icône "+"
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.shutdown_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)

        # Bouton pour annuler l'arrêt programmé
        self.cancel_button = QPushButton('Supprimer les arrêts programmés', self)
        self.cancel_button.clicked.connect(self.cancel_shutdown)
        self.cancel_button.setStyleSheet("QPushButton { background-color: #8B0000; color: white; border-radius: 5px; font-size: 16px; padding: 10px; margin: 40px }"
                                         "QPushButton:hover { background-color: #A52A2A; }")
        self.cancel_button.setIcon(QIcon(QPixmap('trash_icon.png')))  # Remplacez 'trash_icon.png' par le chemin de votre icône de poubelle
        cancel_button_layout = QHBoxLayout()
        cancel_button_layout.addStretch()
        cancel_button_layout.addWidget(self.cancel_button)
        cancel_button_layout.addStretch()
        layout.addLayout(cancel_button_layout)

        self.setLayout(layout)

    def schedule_shutdown(self):
        hours = int(self.hour_entry.text() or 0)
        minutes = int(self.min_entry.text() or 0)
        if 0 <= hours <= 999 and 0 <= minutes <= 60:
            total_seconds = hours * 3600 + minutes * 60
            if total_seconds > 0:
                os.system("shutdown /a")
                os.system(f"shutdown -s -t {total_seconds}")
                self.shutdown_time = datetime.datetime.now() + datetime.timedelta(seconds=total_seconds)
                self.update_countdown()
        else:
            QMessageBox.warning(self, "Erreur", "Valeurs hors limites.")

    def cancel_shutdown(self):
        os.system("shutdown /a")
        self.shutdown_time = None
        self.label.setText("Prochain arrêt non programmé.")
        QMessageBox.information(self, "Information", "Arrêts supprimés.")

    def update_countdown(self):
        if self.shutdown_time:
            remaining_time = self.shutdown_time - datetime.datetime.now()
            if remaining_time.total_seconds() > 0:
                hours, remainder = divmod(remaining_time.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.label.setText(f"Prochain arrêt programmé dans {hours} heures, {minutes} minutes et {seconds} secondes.")
            else:
                self.label.setText("Prochain arrêt non programmé.")
                self.shutdown_time = None

def main():
    app = QApplication(sys.argv)
    ex = ShutdownScheduler()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
