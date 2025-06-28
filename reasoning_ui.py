import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QTextEdit, QMessageBox
)
from PyQt6.QtGui import QFont
import vertexai
from vertexai.preview import reasoning_engines

# Khởi tạo Vertex AI SDK
vertexai.init(project="vertex-ai-agent-demo-464303", location="us-central1")

# Khởi tạo Reasoning Engine đã tạo từ trước
REASONING_ENGINE_ID = "projects/446645608781/locations/us-central1/reasoningEngines/6023256638352261120"
reasoning_engine = reasoning_engines.ReasoningEngine(REASONING_ENGINE_ID)

class ReasoningApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertex AI Reasoning Agent")
        self.setGeometry(300, 200, 600, 400)

        layout = QVBoxLayout()

        self.label = QLabel("Enter two numbers (e.g. 2 5):")
        self.label.setFont(QFont("Arial", 12))
        layout.addWidget(self.label)

        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Arial", 12))
        layout.addWidget(self.input_field)

        self.submit_btn = QPushButton("Ask Reasoning Agent")
        self.submit_btn.clicked.connect(self.call_agent)
        layout.addWidget(self.submit_btn)

        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        self.result_area.setFont(QFont("Courier", 11))
        layout.addWidget(self.result_area)

        self.setLayout(layout)

    def call_agent(self):
        user_input = self.input_field.text().strip()
        try:
            parts = user_input.split()
            a = int(parts[0])
            b = int(parts[1])
        except Exception:
            QMessageBox.warning(self, "Input Error", "Please enter two integers separated by space (e.g. 3 4).")
            return

        try:
            response = reasoning_engine.query(a=a, b=b)
            self.result_area.setPlainText(response)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ReasoningApp()
    window.show()
    sys.exit(app.exec())
