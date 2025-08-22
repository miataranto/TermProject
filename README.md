# TermProject
Interactive Python program demonstrating core programming concepts with a video walkthrough.
# BookBuddy

**BookBuddy** is a command-line Python application designed to help users organize and manage their personal book collection. Built with simplicity and functionality in mind, BookBuddy allows users to add new books, view their current reading list, and mark books as read — all from a clean, interactive menu interface. The project uses JSON for persistent data storage, ensuring that your book list is saved between sessions.

This project was developed by Mia Taranto in August 2025 as part of a personal enrichment and academic development initiative. It reflects a strong understanding of Python fundamentals, modular design, and user-centered programming.

---

## 🎯 Features

- **Add a Book**: Users can input a book’s title, author, and genre. Each new book is automatically marked as “Unread.”
- **View All Books**: Displays a numbered list of all books in the collection, including title, author, genre, and reading status.
- **Mark as Read**: Users can select a book by its number and update its status to “Read.”
- **Persistent Storage**: All book data is saved to a local `books.json` file, allowing users to resume their collection anytime.

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **JSON for data storage**
- **OS module for file existence checks**
- **VS Code for development**
- **GitHub for version control and project hosting**

No external libraries are required, making BookBuddy lightweight and easy to run on any system with Python installed.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/miataranto/BookBuddy.git
   cd BookBuddy
   
   
   BookBuddy is organized into modular components for clarity and maintainability:

TermProject.py: Main script containing the interactive menu and core logic for adding, viewing, and updating books.

books.json: Stores the book collection persistently between sessions using JSON format.

README.md: Project documentation including overview, features, setup instructions, and design rationale.

requirements.txt: (Optional) Included for completeness, though no external libraries are required.

This structure ensures that each file has a clear purpose and supports clean separation of concerns.

BookBuddy was built with simplicity and user experience in mind. Key design choices include:

JSON for Storage: Chosen for its readability and ease of use with Python’s built-in json module. It allows users to view and edit their book data manually if needed.

Command-Line Interface: Offers a lightweight, distraction-free way to interact with the program without requiring a GUI.

Modular Functions: Each feature (add, view, mark as read) is implemented as a separate function to promote reusability and clarity.

Error Handling: Basic checks are included to handle invalid inputs and ensure smooth user experience.

Scalability: While simple, the structure allows for future enhancements like search, sort, or genre filtering.

BookBuddy is a practical tool that reflects thoughtful design and a strong grasp of Python programming principles. It’s ready for presentation, peer review, and future iteration.

Developing BookBuddy reinforced key programming concepts such as file I/O, data structures, and user input validation. It also provided hands-on experience with GitHub workflows, documentation best practices, and project presentation. Through iterative testing and debugging, Mia refined her understanding of modular design and built a tool that is both functional and user-friendly.

This project also served as a foundation for learning version control with GitHub Desktop, writing professional docstrings, and preparing code for public sharing. The experience highlighted the importance of clear documentation, consistent formatting, and thoughtful user experience design.

Future Improvements:

Add a delete book feature

Implement search by author or genre

Refactor into an object-oriented design using classes

Build a GUI version using Tkinter or Flask

Export book list to CSV for external use