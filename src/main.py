import customtkinter as ctk
from tkinter import filedialog

# Set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FileOrganizerGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart File Organizer")
        self.geometry("600x450")

        # Selected folder path
        self.folder_path = ctk.StringVar()

        # --- Folder Selection ---
        folder_frame = ctk.CTkFrame(self)
        folder_frame.pack(pady=20, padx=20, fill="x")

        ctk.CTkLabel(folder_frame, text="Select Folder to Organize").pack(anchor="w")

        path_entry = ctk.CTkEntry(folder_frame, textvariable=self.folder_path, width=400)
        path_entry.pack(side="left", padx=10)

        browse_btn = ctk.CTkButton(folder_frame, text="Browse", command=self.choose_folder)
        browse_btn.pack(side="left")

        # --- Options ---
        options_frame = ctk.CTkFrame(self)
        options_frame.pack(pady=10, padx=20, fill="x")

        self.sort_by_type = ctk.CTkSwitch(options_frame, text="Sort by File Type")
        self.sort_by_type.pack(anchor="w", pady=5)

        self.sort_by_date = ctk.CTkSwitch(options_frame, text="Sort by Date")
        self.sort_by_date.pack(anchor="w", pady=5)

        self.detect_duplicates = ctk.CTkSwitch(options_frame, text="Detect Duplicates")
        self.detect_duplicates.pack(anchor="w", pady=5)

        self.auto_rename = ctk.CTkSwitch(options_frame, text="Auto-Rename Files")
        self.auto_rename.pack(anchor="w", pady=5)

        self.organize_folders = ctk.CTkSwitch(options_frame, text="Organize Folders Alphabetically")
        self.organize_folders.pack(anchor="w", pady=5)

        self.preset_choice = ctk.CTkOptionMenu(
            options_frame,
            values=["GameDev", "GraphicDesign", "Documents"]
        )
        self.preset_choice.pack(anchor="w", pady=5)

        # --- Action Buttons ---
        action_frame = ctk.CTkFrame(self)
        action_frame.pack(pady=20)

        run_btn = ctk.CTkButton(action_frame, text="Run Organizer", command=self.run_organizer)
        run_btn.pack(side="left", padx=10)

        watch_btn = ctk.CTkButton(action_frame, text="Start Watching", command=self.start_watching)
        watch_btn.pack(side="left", padx=10)

        # --- Log Output ---
        self.log_box = ctk.CTkTextbox(self, height=120)
        self.log_box.pack(padx=20, pady=10, fill="both")

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)
            self.log(f"Selected folder: {folder}")

    def run_organizer(self):
        folder = self.folder_path.get()

        if not folder:
            self.log("Please select a folder first.")
            return

        from organizer import sort_by_type, sort_by_date, organize_folders_alphabetically, organize_by_preset


        self.log("Running organizer...")

        preset = self.preset_choice.get()
        organize_by_preset(folder, preset)
        self.log(f"Organized using preset: {preset}")

        if self.sort_by_type.get():
            sort_by_type(folder)
            self.log("Sorted by file type.")

        if self.sort_by_date.get():
            sort_by_date(folder)
            self.log("Sorted by date.")

        if self.organize_folders.get():
            organize_folders_alphabetically(folder)
            self.log("Organized folders alphabetically.")

        self.log("Done!")

    def start_watching(self):
        self.log("Starting folder watcher... (logic not connected yet)")

    def log(self, message):
        self.log_box.insert("end", message + "\n")
        self.log_box.see("end")


if __name__ == "__main__":
    app = FileOrganizerGUI()
    app.mainloop()