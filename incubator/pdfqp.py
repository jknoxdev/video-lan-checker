import PyPDF2
import sqlite3
import csv
import os

class PDFQuestionParser:
    def __init__(self, pdf_path, database_name):
        self.pdf_path = pdf_path
        self.database_name = database_name
        self.qa_data = []

    def extract_qa_from_pdf(self):
        with open(self.pdf_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            num_pages = pdf_reader.numPages
            current_question = ""
            current_answers = {}
            current_answer_prefix = ""
            
            for page_num in range(num_pages):
                page = pdf_reader.getPage(page_num)
                text = page.extractText()
                lines = text.split('\n')
                for line in lines:
                    if line.startswith("QUESTION:"):
                        if current_question:
                            self.qa_data.append((current_question, current_answers))
                            current_question = line[10:].strip()
                            current_answers = {}
                        elif current_question and line.startswith("Answer:"):
                            current_answer_prefix = line[7:8]
                            current_answer = line[9:].strip()
                            current_answers[current_answer_prefix] = current_answer
                        elif current_answer_prefix and line.startswith(current_answer_prefix):
                            current_answer += " " + line.strip()
                            
                    if current_question:
                        self.qa_data.append((current_question, current_answers))
                    
    def create_database(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        question TEXT,
        answer_a TEXT,
        answer_b TEXT,
        answer_c TEXT,
        answer_d TEXT
        )
        """)
        
        conn.commit()
        conn.close()
                                        
    def insert_qa_into_database(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
                                            
        for question, answers in self.qa_data:
            cursor.execute(
                "INSERT INTO questions (question, answer_a, answer_b, answer_c, answer_d) VALUES (?, ?, ?, ?, ?)",
                (question, answers.get("a", ""), answers.get("b", ""), answers.get("c", ""), answers.get("d", ""))
            )
            
            conn.commit()
            conn.close()
                                                
    def export_database_to_csv(self, csv_file_path):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM questions")
        rows = cursor.fetchall()
        
        conn.close()
        
        with open(csv_file_path, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["ID", "Question", "Answer A", "Answer B", "Answer C", "Answer D"])
            
            for row in rows:
                csv_writer.writerow(row)
        
    def display_qa(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM questions")
        rows = cursor.fetchall()
        
        conn.close()
        
        for row in rows:
            _, question, answer_a, answer_b, answer_c, answer_d = row
            print("Question:", question)
            print("Answers:")
            print("A. ", answer_a)
            print("B. ", answer_b)
            print("C. ", answer_c)
            print("D. ", answer_d)
            input("Press Enter to continue...")

    def run(self):
        while True:
            print("Menu:")
            print("1. Extract and store QA from PDF")
            print("2. Count items in the database and store count in a file")
            print("3. Export database to CSV")
            print("4. Display QA from the database")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.extract_qa_from_pdf()
                self.create_database()
                self.insert_qa_into_database()
                print("Questions and answers extracted and stored in the database.")
            elif choice == "2":
                # Implementation for counting items and storing count
            elif choice == "3":
                csv_file_path = input("Enter the path for the CSV export: ")
                csv_file_path = os.path.normpath(csv_file_path)
                self.export_database_to_csv(csv_file_path)
                print(f"Database exported to '{csv_file_path}'.")
            elif choice == "4":
                self.display_qa()
            elif choice == "5":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please choose again.")
                
# -------------------------------------------------------------------
#  main
# -------------------------------------------------------------------
def main():
    print("PDF Parsing and Scanning Application")

    pdf_path = input("Enter the path to the PDF file: ")
    pdf_path = os.path.normpath(pdf_path)
    if not os.path.exists(pdf_path):
        print("Error: The provided PDF file does not exist.")
        return

    database_name = "qa_database.db"

    parser = PDFQuestionParser(pdf_path, database_name)

    if os.path.exists(database_name):
        database_size = os.path.getsize(database_name)
        print(f"Database '{database_name}' found, size: {database_size} bytes")
    else:
        print("No database found. Proceeding to application.")

    parser.run()

if __name__ == "__main__":
    main()
