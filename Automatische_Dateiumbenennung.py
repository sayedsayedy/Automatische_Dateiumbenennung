import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk  # Pillow-Bibliothek erforderlich
from datetime import datetime

# Globale Variable für die DataFrame-Daten
df = None

def load_csv():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        return df
    return None

def select_folder():
    folder_path = filedialog.askdirectory()
    return folder_path

def last_day_of_month(month, year):
    """Berechnet den letzten Tag des Monats."""
    next_month = month % 12 + 1
    next_month_year = year if month < 12 else year + 1
    first_day_next_month = datetime(next_month_year, next_month, 1)
    last_day = first_day_next_month - pd.DateOffset(days=1)
    return last_day.strftime("%d%m%Y")

def rename_files(df, folder_path):
    try:
        for _, row in df.iterrows():
            personalnummer = row['Personalnummer']
            vorname = row['Vorname']
            nachname = row['Nachname']

            for file_name in os.listdir(folder_path):
                # Debugging: Überprüfe, ob die Datei gefunden wird
                print(f"Überprüfe Datei: {file_name}")

                if f"PersonalNr={personalnummer}" in file_name:
                    parts = file_name.split()

                    # Unterschiedliche Dateitypen behandeln: Verdienstabrechnung oder Meldebescheinigung
                    if "Verdienstabrechnung" in file_name:
                        date_part = parts[1]   # Format: mm.yyyy
                    elif "Meldebescheinigung" in file_name:
                        # Meldebescheinigung enthält das Wort "Sozialvers", daher ist der Datumsindex anders
                        date_part = parts[2]   # Format: mm.yyyy
                    else:
                        continue

                    # Monat und Jahr aus dem Dateinamen extrahieren
                    month = int(date_part.split(".")[0])
                    year = int(date_part.split(".")[1])
                    last_day = last_day_of_month(month, year)

                    # Erstelle den neuen Dateinamen basierend auf dem Typ der Datei
                    if "Verdienstabrechnung" in file_name:
                        new_name = f"{personalnummer}_{vorname}_{nachname}_Gehaltsabrechnung_{last_day}.pdf"
                    elif "Meldebescheinigung" in file_name:
                        new_name = f"{personalnummer}_{vorname}_{nachname}_Meldebescheinigung Sozialversicherung_{last_day}.pdf"

                    old_path = os.path.join(folder_path, file_name)
                    new_path = os.path.join(folder_path, new_name)

                    # Debugging: Zeige die alten und neuen Dateipfade an
                    print(f"Alter Pfad: {old_path}")
                    print(f"Neuer Pfad: {new_path}")

                    os.rename(old_path, new_path)

        messagebox.showinfo("Erfolg", "Dateien wurden erfolgreich umbenannt.")
    except Exception as e:
        # Debugging: Zeige den Fehler an
        print(f"Fehler: {e}")
        messagebox.showerror("Fehler", f"Es ist ein Fehler aufgetreten: {e}")

def main():
    global df

    root = tk.Tk()
    root.title("HR Automatische Dateiumbenennung")

    # Hauptfenster für Flexibilität konfigurieren
    root.geometry("600x600")
    root.configure(bg="#f0f0f0")
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)

    # Laden und Anzeigen des Logos
    logo_path = r"C:\Users\Admin\sayed.sayedy\AdW-Tool\logo.png"  # Pfad zum Logo
    img = Image.open(logo_path)
    img = img.resize((180, 180), Image.LANCZOS)  # Größe anpassen
    logo = ImageTk.PhotoImage(img)

    logo_label = tk.Label(root, image=logo, bg="#f0f0f0")
    logo_label.grid(row=0, column=0, pady=20, sticky="n")

    # Anleitung für den Benutzer in Du-Form
    instruction_label = tk.Label(root, text=(
        "Anleitung:\n"
        "1. Klicke auf 'CSV-Datei laden', um die CSV-Datei mit den Mitarbeiterdaten auszuwählen.\n"
        "2. Wähle danach den Ordner aus, wo Du die neu umbenannten Dateien speichern möchtest.\n"
        "3. Klicke auf 'Dateien umbenennen', um die Dateien umzubenennen."
    ), justify="left", wraplength=550, font=("Arial", 14), bg="#f0f0f0")
    instruction_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

    # Buttons untereinander anordnen
    load_button = tk.Button(root, text="CSV-Datei laden", font=("Arial", 14), bg="#007BFF", fg="white", padx=10, pady=5, command=load_csv)
    load_button.grid(row=2, column=0, pady=15)

    rename_button = tk.Button(root, text="Dateien umbenennen", font=("Arial", 14), bg="#28a745", fg="white", padx=10, pady=5, command=lambda: rename_files(df, select_folder()) if df is not None else messagebox.showerror("Fehler", "CSV-Datei wurde nicht geladen."))
    rename_button.grid(row=3, column=0, pady=15)

    # Flexibler Text am unteren Rand des Fensters mit grünem Herz
    footer_frame = tk.Frame(root, bg="#f0f0f0")
    footer_frame.grid(row=4, column=0, pady=20, sticky="s")

    footer_label1 = tk.Label(footer_frame, text="Ärzte der Welt e.V.", font=("Arial", 12), bg="#f0f0f0")
    footer_label1.pack()

    footer_label2 = tk.Frame(footer_frame, bg="#f0f0f0")
    footer_label2.pack()

    footer_text = tk.Label(footer_label2, text="HR Automatische Dateiumbenennung - Made with", font=("Arial", 12), bg="#f0f0f0")
    footer_text.pack(side="left")

    heart_label = tk.Label(footer_label2, text="💚", font=("Arial", 14), fg="green", bg="#f0f0f0")  # Größeres und grünes Herz
    heart_label.pack(side="left")

    by_sayed_label = tk.Label(footer_label2, text="by Sayed", font=("Arial", 12), bg="#f0f0f0")
    by_sayed_label.pack(side="left")

    root.mainloop()

if __name__ == "__main__":
    main()
