import os
import sqlite3
import PyPDF4

def create_database(database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        question_text TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_question_into_database(database_name, question_text):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO questions (question_text) VALUES (?)", (question_text,))
    
    conn.commit()
    conn.close()

def find_questions_in_directory(directory, database_name):
    pdf_files = [file for file in os.listdir(directory) if file.lower().endswith('.pdf')]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF4.PdfFileReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                text = pdf_reader.pages[page_num].extractText()
                print(".", end='', flush=True)
                if "QUESTION:" in text:
                    question_text = text.split("QUESTION:")[1].split("A.")[0].strip()
                    insert_question_into_database(database_name, question_text)
                    print("Q: " + question_text)
                    break

def main():
    data_directory = os.path.expanduser("~/data/src/parse/")
    database_name = "question_database.db"
    
    print(f"Checking PDFs in {data_directory} for questions labeled as 'QUESTION:'")
    
    create_database(database_name)
    find_questions_in_directory(data_directory, database_name)
    
    print("Questions stored in the database.")

if __name__ == "__main__":
    main()
