# UI.py
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import OCR
import Engine

class PuzzleSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧩 AI Puzzle Solver")
        self.root.geometry("700x750")
        self.root.configure(bg="#1e1e1e")  # dark background

        # State
        self.mode = None
        self.screenshot_path = None
        self.manual_array = None
        self.driver = None

        # ttk style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton",
                        font=("Segoe UI", 12, "bold"),
                        padding=10,
                        background="#0078D7",
                        foreground="white")
        style.map("TButton",
                  background=[("active", "#005a9e")])

        # Title
        title = tk.Label(root, text="AI Puzzle Solver",
                         font=("Segoe UI", 26, "bold"),
                         bg="#1e1e1e", fg="#ffffff")
        title.pack(pady=20)

        # Buttons frame
        btn_frame = tk.Frame(root, bg="#1e1e1e")
        btn_frame.pack(pady=10)

        self.live_btn = ttk.Button(btn_frame, text=" Live Puzzle", command=self.choose_live)
        self.live_btn.grid(row=0, column=0, padx=10, pady=5)

        self.screenshot_btn = ttk.Button(btn_frame, text="\ Screenshot", command=self.choose_screenshot)
        self.screenshot_btn.grid(row=0, column=1, padx=10, pady=5)

        self.manual_btn = ttk.Button(btn_frame, text="⌨️ Manual Input", command=self.choose_manual)
        self.manual_btn.grid(row=0, column=2, padx=10, pady=5)

        # Solve button
        self.solve_btn = ttk.Button(root, text=" Solve Puzzle", command=self.solve)
        self.solve_btn.pack(pady=15)

        # Status label
        self.status_label = tk.Label(root, text="Mode: None selected",
                                     font=("Segoe UI", 11, "italic"),
                                     bg="#1e1e1e", fg="#bbbbbb")
        self.status_label.pack(pady=5)

        # Results frame
        result_frame = tk.LabelFrame(root, text="Results",
                                     font=("Segoe UI", 12, "bold"),
                                     bg="#2d2d2d", fg="#ffffff",
                                     padx=10, pady=10)
        result_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.result_text = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD,
                                                     width=70, height=20,
                                                     font=("Consolas", 11),
                                                     bg="#1e1e1e", fg="#f0f0f0",
                                                     insertbackground="white",
                                                     relief="flat", borderwidth=0)
        self.result_text.pack(fill="both", expand=True)
        self.update_result_text("Welcome! Choose an input method, then press Solve.")

    # --- Input mode selection ---
    def choose_live(self):
        self.driver = OCR.open_puzzle()
        self.mode = "live"
        self.status_label.config(text="Mode: Live Puzzle")
        self.update_result_text("Live puzzle opened. Press Solve to read and solve.")

    def choose_screenshot(self):
        file_path = filedialog.askopenfilename(
            title="Select a Puzzle Screenshot",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if file_path:
            self.screenshot_path = file_path
            self.mode = "screenshot"
            self.status_label.config(text="Mode: Screenshot")
            self.update_result_text(f"Screenshot selected: {file_path}\nPress Solve to process.")

    def choose_manual(self):
        try:
            arr = OCR.extract_puzzle_from_input()
            self.manual_array = arr
            self.mode = "manual"
            self.status_label.config(text="Mode: Manual Input")
            self.update_result_text(f"Manual array entered:\n{arr}\nPress Solve to process.")
        except Exception as e:
            messagebox.showerror("Input Error", str(e))

    # --- Solve ---
    def solve(self):
        if not self.mode:
            messagebox.showwarning("No Input", "Please choose an input method first.")
            return
        try:
            if self.mode == "live":
                grid = OCR.extract_puzzle_from_site(self.driver)
            elif self.mode == "screenshot":
                grid = OCR.extract_puzzle_from_image(self.screenshot_path)
            elif self.mode == "manual":
                grid = self.manual_array
            else:
                grid = None

            if grid is None:
                self.update_result_text("Could not detect a valid grid.")
                return

            self.update_result_text(f"Detected Grid:\n{grid}\n\nSolving...")
            steps = Engine.solve_puzzle(grid)
            if steps:
                formatted = "\n".join([f"Step {i+1}: {s}" for i, s in enumerate(steps)])
                self.update_result_text(f" Solution in {len(steps)} moves:\n\n{formatted}")
            else:
                self.update_result_text(" No solution found (unsolvable state).")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.update_result_text(f"Error: {e}")

    # --- Helper ---
    def update_result_text(self, msg):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, msg)
        self.result_text.config(state=tk.DISABLED)
        self.root.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleSolverApp(root)
    root.mainloop()
