import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os


class ASCIIConverter:
    # Different ASCII character sets - longer sets = better detail
    ASCII_SETS = {
        "Standard": "@%#*+=-:. ",
        "Detailed": "@%#*+=-:. ",
        "Enhanced": "@@@##%%***++++====----::::....    ",
        "Best": "@@@##%%***++++====----::::......        ",
        "Extreme": "@WWMMBBAA88&&%%%???***+++===---...'''\"\"\" ",
    }

    def __init__(self, root):
        self.root = root
        self.root.title("ASCII Art Converter")
        self.root.geometry("500x350")

        # Title label
        title = tk.Label(root, text="ASCII Art Converter", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Width input
        width_frame = tk.Frame(root)
        width_frame.pack(pady=5)
        tk.Label(width_frame, text="Width (chars):").pack(side=tk.LEFT, padx=5)
        self.width_var = tk.StringVar(value="120")
        tk.Entry(width_frame, textvariable=self.width_var, width=10).pack(side=tk.LEFT)

        # Contrast input
        contrast_frame = tk.Frame(root)
        contrast_frame.pack(pady=5)
        tk.Label(contrast_frame, text="Contrast (1-3):").pack(side=tk.LEFT, padx=5)
        self.contrast_var = tk.StringVar(value="1.5")
        tk.Entry(contrast_frame, textvariable=self.contrast_var, width=10).pack(side=tk.LEFT)

        # Character set selection
        charset_frame = tk.Frame(root)
        charset_frame.pack(pady=5)
        tk.Label(charset_frame, text="Detail Level:").pack(side=tk.LEFT, padx=5)
        self.charset_var = tk.StringVar(value="Best")
        charset_menu = tk.OptionMenu(charset_frame, self.charset_var, "Standard", "Enhanced", "Best", "Extreme")
        charset_menu.pack(side=tk.LEFT)

        # Upload button
        upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image,
                               bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), padx=20, pady=12)
        upload_btn.pack(pady=20)

        # Status label
        self.status_label = tk.Label(root, text="", fg="gray")
        self.status_label.pack(pady=10)

    def resize_image(self, image, new_width=120):
        width, height = image.size
        aspect_ratio = height / width
        new_height = int(new_width * aspect_ratio * 0.55)  # 0.55 accounts for character height
        return image.resize((new_width, new_height))

    def adjust_contrast(self, image, factor=1.5):
        from PIL import ImageEnhance
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(factor)

    def grayscale(self, image):
        return image.convert("L")

    def pixels_to_ascii(self, image, charset):
        pixels = image.getdata()
        ascii_str = ""
        charset_len = len(charset)
        for pixel in pixels:
            ascii_str += charset[min(pixel * charset_len // 256, charset_len - 1)]
        return ascii_str

    def main(self, image_path, new_width=120, contrast=1.5, charset="Best"):
        try:
            image = Image.open(image_path)
            image = self.resize_image(image, new_width)
            image = self.adjust_contrast(image, contrast)
            image = self.grayscale(image)

            # Get the character set
            chars = self.ASCII_SETS.get(charset, self.ASCII_SETS["Best"])
            ascii_str = self.pixels_to_ascii(image, chars)

            img_width = image.width
            ascii_str_len = len(ascii_str)
            ascii_img = ""

            for i in range(0, ascii_str_len, img_width):
                ascii_img += ascii_str[i:i + img_width] + "\n"

            return ascii_img
        except Exception as e:
            messagebox.showerror("Error", f"Error processing image: {str(e)}")
            return None

    def upload_image(self):
        file_path = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"), ("All files", "*.*")]
        )

        if file_path:
            try:
                width = int(self.width_var.get())
                contrast = float(self.contrast_var.get())
                charset = self.charset_var.get()

                if width <= 0:
                    messagebox.showerror("Error", "Width must be positive")
                    return
                if contrast <= 0:
                    messagebox.showerror("Error", "Contrast must be positive")
                    return

                self.status_label.config(text="Converting...", fg="blue")
                self.root.update()

                ascii_art = self.main(file_path, width, contrast, charset)

                if ascii_art:
                    self.display_ascii_art(ascii_art, file_path)
                    self.status_label.config(text="Conversion complete!", fg="green")
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers for width and contrast")

    def display_ascii_art(self, ascii_art, original_path):
        # Create a new window to display the ASCII art
        art_window = tk.Toplevel(self.root)
        art_window.title("ASCII Art Output")
        art_window.geometry("1000x700")

        # Create a frame with scrollbar
        frame = tk.Frame(art_window)
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_widget = tk.Text(frame, font=("Courier New", 7), wrap=tk.NONE,
                              yscrollcommand=scrollbar.set, bg="black", fg="lime",
                              highlightthickness=0)
        text_widget.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)

        # Insert ASCII art
        text_widget.insert(1.0, ascii_art)
        text_widget.config(state=tk.DISABLED)

        # Save button
        save_btn = tk.Button(art_window, text="Save as .txt",
                             command=lambda: self.save_ascii_art(ascii_art),
                             bg="#2196F3", fg="white", padx=10, pady=5)
        save_btn.pack(pady=5)

    def save_ascii_art(self, ascii_art):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )

        if file_path:
            try:
                with open(file_path, 'w') as f:
                    f.write(ascii_art)
                messagebox.showinfo("Success", "ASCII art saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving file: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ASCIIConverter(root)
    root.mainloop()