import tkinter as tk
from tkinter import messagebox, ttk

# Data Functions 
def load_records(data):
    records = []
    try:
        with open(data, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",")]
                if len(parts) == 6:
                    student_code = parts[0]
                    name = parts[1]
                    course_marks = list(map(int, parts[2:5]))
                    exam_mark = int(parts[5])
                    total_mark = sum(course_marks) + exam_mark
                    records.append({
                        "student_code": student_code,
                        "name": name,
                        "course_marks": course_marks,
                        "exam_mark": exam_mark,
                        "total_mark": total_mark
                    })
    except FileNotFoundError:
        messagebox.showerror("Error", f"The file '{data}' was not found.")
    return records


def view_all(records, text_widget):
    text_widget.delete(1.0, tk.END) # Deletes anything in advance before adding anything.
    text_widget.insert(tk.END, f"=== ALL STUDENT RECORDS ===\n")
    text_widget.insert(tk.END, f"Total students: {len(records)}\n\n")
    for r in records:
        text_widget.insert(tk.END, f"Student Code: {r['student_code']}\n")
        text_widget.insert(tk.END, f"Name: {r['name']}\n")
        text_widget.insert(tk.END, f"Course Marks: {r['course_marks']}\n")
        text_widget.insert(tk.END, f"Exam Mark: {r['exam_mark']}\n")
        text_widget.insert(tk.END, f"Total Mark: {r['total_mark']}\n")
        text_widget.insert(tk.END, "-" * 40 + "\n")


def view_specific(records, student_var, text_widget):
    selection = student_var.get() #Acknowledges you clicked something from the dropdownlist.
    if not selection:
        messagebox.showwarning("Warning", "Please select a student.")
        return

    r = next((rec for rec in records if rec["name"] == selection), None) # finds soemthing that matches the data you selected from the dropdown.
    if r:
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, f"=== RECORD FOR {r['name']} ===\n")
        text_widget.insert(tk.END, f"Student Code: {r['student_code']}\n")
        text_widget.insert(tk.END, f"Course Marks: {r['course_marks']}\n")
        text_widget.insert(tk.END, f"Exam Mark: {r['exam_mark']}\n")
        text_widget.insert(tk.END, f"Total Mark: {r['total_mark']}\n")
    else:
        messagebox.showerror("Error", "Student not found.")


def highest_mark(records, text_widget):
    top_student = max(records, key=lambda r: r["total_mark"]) #max returns the largest value. lambda is an anonymous function, helping us to find the needed value and doesn't concern itself with a specific data, only that we need the maximum one.
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, f"=== STUDENT WITH HIGHEST MARK ===\n")
    text_widget.insert(tk.END, f"Name: {top_student['name']}\n")
    text_widget.insert(tk.END, f"Student Code: {top_student['student_code']}\n")
    text_widget.insert(tk.END, f"Course Marks: {top_student['course_marks']}\n")
    text_widget.insert(tk.END, f"Exam Mark: {top_student['exam_mark']}\n")
    text_widget.insert(tk.END, f"Total Mark: {top_student['total_mark']}\n")


def lowest_mark(records, text_widget):
    low_student = min(records, key=lambda r: r["total_mark"])
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, f"=== STUDENT WITH LOWEST MARK ===\n")
    text_widget.insert(tk.END, f"Name: {low_student['name']}\n")
    text_widget.insert(tk.END, f"Student Code: {low_student['student_code']}\n")
    text_widget.insert(tk.END, f"Course Marks: {low_student['course_marks']}\n")
    text_widget.insert(tk.END, f"Exam Mark: {low_student['exam_mark']}\n")
    text_widget.insert(tk.END, f"Total Mark: {low_student['total_mark']}\n")


# GUI 
def main():
    data = "records.txt"
    records = load_records(data)
    if not records:
        return

    root = tk.Tk()
    root.title("Student Manager")
    root.geometry('350x600')
    root.resizable(True, True)
    root.configure(bg="#020730")  # Dark blue background

    # Fonts and Style 
    font_label = ("Libre Baskerville", 14, "bold")
    font_button = ("Libre Baskerville", 12, "bold")
    font_text = ("Libre Baskerville", 12)

    style = ttk.Style()
    style.theme_use("clam")  # allows more control of colors
    style.configure("TButton", font=font_button, foreground="black", background="#7FA2C5")
    style.map("TButton", background=[('active', "#104E8B")])

    # Label for dropdown
    ttk.Label(root, text="Select Student:", font=font_label, background="#020730", foreground="white").pack(pady=5)

    # Dropdown for selecting individual students
    student_var = tk.StringVar()
    student_dropdown = ttk.Combobox(root, textvariable=student_var,
                                    values=[r["name"] for r in records],
                                    width=40, font=font_text)
    student_dropdown.pack(pady=5)

    # Buttons
    button_frame = tk.Frame(root, bg="#020730")
    button_frame.pack(pady=10)

    ttk.Button(button_frame, text="View All Records", command=lambda: view_all(records, text_box)).grid(row=0, column=0, padx=5)
    ttk.Button(button_frame, text="View Individual Record", command=lambda: view_specific(records, student_var, text_box)).grid(row=0, column=1, padx=5)
    ttk.Button(button_frame, text="Highest Mark", command=lambda: highest_mark(records, text_box)).grid(row=0, column=2, padx=5)
    ttk.Button(button_frame, text="Lowest Mark", command=lambda: lowest_mark(records, text_box)).grid(row=0, column=3, padx=5)
    ttk.Button(button_frame, text="Exit", command=root.destroy).grid(row=0, column=4, padx=5)

    # Text area for displaying results
    text_box = tk.Text(root, wrap="word", width=80, height=20, font=font_text, bg="#001533", fg="white")
    text_box.pack(padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
