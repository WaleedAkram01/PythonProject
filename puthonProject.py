import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Initialize SentenceTransformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
chunks = []  # To store text chunks
index = faiss.IndexFlatL2(384)  # Dimension of MiniLM embeddings

# Function to load and process PDF
def load_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        pdf_label.config(text=f"Loaded: {file_path}")
        pdf_object = PdfReader(file_path)
        text = ""
        for page in pdf_object.pages[:50]:  # Limit to first 50 pages
            text += page.extract_text()

        # Split the text into chunks
        chunk_size = 1000
        global chunks
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

        # Generate embeddings
        embeddings = model.encode(chunks)
        np_embeddings = np.array(embeddings).astype("float32")

        # Initialize FAISS index
        index.reset()  # Clear old embeddings
        index.add(np_embeddings)

        result_box.config(state="normal")
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "PDF Loaded and Indexed Successfully!\n")
        result_box.config(state="disabled")

# Function to process user query
def ask_question():
    query = query_entry.get()
    if query and chunks:
        # Generate query embedding
        query_embedding = model.encode([query]).astype("float32")

        # Search for the most similar chunks
        distances, indices = index.search(query_embedding, k=2)
        response = "\n\n".join([chunks[i] for i in indices[0]])

        # Display result
        result_box.config(state="normal")
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, f"Query: {query}\n")
        result_box.insert(tk.END, "Answer:\n")
        result_box.insert(tk.END, response)
        result_box.config(state="disabled")

# Main Tkinter window
root = tk.Tk()
root.title("Quran Chatbot")
root.geometry("800x600")
root.configure(bg="#f5f5dc")  # Beige background for Islamic aesthetics

# Header frame
header_frame = tk.Frame(root, bg="#004d00")  # Green banner
header_frame.pack(fill="x")
header_label = tk.Label(
    header_frame,
    text="Quran Chatbot",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#004d00"
)
header_label.pack(pady=10)

# Upload button and label
upload_frame = tk.Frame(root, bg="#f5f5dc")
upload_frame.pack(pady=20)
upload_button = ttk.Button(upload_frame, text="Upload PDF", command=load_pdf)
upload_button.pack(side="left", padx=10)
pdf_label = tk.Label(upload_frame, text="No PDF loaded", bg="#f5f5dc", fg="#555", font=("Arial", 12))
pdf_label.pack(side="left")

# Query entry box
query_frame = tk.Frame(root, bg="#f5f5dc")
query_frame.pack(pady=10)
query_label = tk.Label(query_frame, text="Ask a Question:", font=("Arial", 14), bg="#f5f5dc", fg="#004d00")
query_label.pack(side="left", padx=5)
query_entry = ttk.Entry(query_frame, width=50, font=("Arial", 12))
query_entry.pack(side="left", padx=5)
ask_button = ttk.Button(query_frame, text="Ask", command=ask_question)
ask_button.pack(side="left", padx=5)

# Result display with scrolling
result_frame = tk.Frame(root, bg="#f5f5dc")
result_frame.pack(fill="both", expand=True, pady=10, padx=10)
result_box = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD, font=("Arial", 12), height=15)
result_box.pack(fill="both", expand=True)
result_box.config(state="disabled")  # Read-only until results are added

# Footer frame for aesthetics
footer_frame = tk.Frame(root, bg="#004d00")
footer_frame.pack(fill="x", side="bottom")
footer_label = tk.Label(
    footer_frame,
    text="Islamic-Themed Quran Chatbot",
    font=("Arial", 10),
    fg="white",
    bg="#004d00"
)
footer_label.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()