import tkinter as tk
from tkinter import ttk, scrolledtext
import requests as req


# Mock API function to retrieve verses
def fetch_verses(keyword):
    """
    Function to fetch verses based on a keyword.
    This is a placeholder. Replace it with actual API logic.

    Args:
        keyword (str): The keyword to search for.

    Returns:
        list of dict: Each dictionary contains 'verse' (Arabic) and 'meaning' (English).
    """

    resp = req.get(f"https://api.quran.com/api/v4/search?q={keyword}&language=ur")
    if resp.status_code == 200:
        data = resp.json()
        data = data["search"]
        results = data["results"]
        verses = []  # List of dictionaries
        for result in results:
            verses.append(
                {"verse": result["text"], "meaning": result["translations"][0]["text"]}
            )
        return verses

    # Example response structure
    return [
        {"verse": "إِنَّ مَعَ الْعُسْرِ يُسْرًا", "meaning": "Indeed, with hardship comes ease."},
        {
            "verse": "وَإِذَا سَأَلَكَ عِبَادِي عَنِّي فَإِنِّي قَرِيبٌ",
            "meaning": "And when My servants ask you concerning Me, I am indeed near.",
        },
    ]


# Function to process user query
def ask_question():
    keyword = query_entry.get().strip()
    if keyword:
        # Fetch verses
        verses = fetch_verses(keyword)

        # Display results
        result_box.config(state="normal")
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, f"Keyword: {keyword}\n")
        result_box.insert(tk.END, "Results:\n\n")
        for i, verse in enumerate(verses, start=1):
            result_box.insert(tk.END, f"{i}. {verse['verse']} (Arabic)\n")
            result_box.insert(tk.END, f"   {verse['meaning']} (Urdu)\n\n")
        result_box.config(state="disabled")
    else:
        result_box.config(state="normal")
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Please enter a keyword.\n")
        result_box.config(state="disabled")


# Main Tkinter window
root = tk.Tk()
root.title("Quran Keyword Search")
root.geometry("800x600")
root.configure(bg="#f5f5dc")  # Beige background for Islamic aesthetics

# Header frame
header_frame = tk.Frame(root, bg="#004d00")  # Green banner
header_frame.pack(fill="x")
header_label = tk.Label(
    header_frame,
    text="Quran Keyword Search",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#004d00",
)
header_label.pack(pady=10)

# Query entry box
query_frame = tk.Frame(root, bg="#f5f5dc")
query_frame.pack(pady=20)
query_label = tk.Label(
    query_frame, text="Enter Keyword:", font=("Arial", 14), bg="#f5f5dc", fg="#004d00"
)
query_label.pack(side="left", padx=5)
query_entry = ttk.Entry(query_frame, width=50, font=("Arial", 12))
query_entry.pack(side="left", padx=5)
ask_button = ttk.Button(query_frame, text="Search", command=ask_question)
ask_button.pack(side="left", padx=5)

# Result display with scrolling
result_frame = tk.Frame(root, bg="#f5f5dc")
result_frame.pack(fill="both", expand=True, pady=10, padx=10)
result_box = scrolledtext.ScrolledText(
    result_frame, wrap=tk.WORD, font=("Arial", 12), height=15
)
result_box.pack(fill="both", expand=True)
result_box.config(state="disabled")  # Read-only until results are added

# Footer frame for aesthetics
footer_frame = tk.Frame(root, bg="#004d00")
footer_frame.pack(fill="x", side="bottom")
footer_label = tk.Label(
    footer_frame,
    text="Islamic-Themed Quran Keyword Search",
    font=("Arial", 10),
    fg="white",
    bg="#004d00",
)
footer_label.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()
