from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping
from tkinter import filedialog, colorchooser
from tensorflow.keras import regularizers
from sklearn.cluster import KMeans
from tkinter import messagebox
from PIL import Image, ImageTk
from ttkthemes import ThemedTk
import tensorflow as tf
from tkinter import ttk
import tkinter as tk
import pandas as pd
import numpy as np
import threading
import platform
import json
import sys
import cv2
import csv
import os
import re


class ConsoleText:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.original_stdout = sys.__stdout__
        self.original_stderr = sys.__stderr__

        self.ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    def write(self, message):
        clean_message = self.ansi_escape.sub("", message)

        self.text_widget.configure(state="normal")
        self.text_widget.insert("end", clean_message)
        self.text_widget.see("end")
        self.text_widget.configure(state="disabled")

        self.original_stdout.write(message)
        self.original_stdout.flush()

    def flush(self):
        pass


class App:
    def __init__(self, root):
        self.root = root
        root.title("AI Image Trainer")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.configure(width=screen_width, height=screen_height)

        if platform.system() == "Windows":
            root.state("zoomed")
        elif platform.system() == "Linux":
            root.attributes("-zoomed", True)

        root.configure(bg="#2e2e2e")
        style = ttk.Style(root)
        style.theme_use("equilux")
        style.configure(
            ".", background="#2e2e2e", foreground="white", fieldbackground="#3c3f41"
        )
        style.configure("TButton", background="#3c3f41", foreground="white")
        style.configure("TEntry", fieldbackground="#3c3f41", foreground="white")
        style.configure("TLabel", background="#2e2e2e", foreground="white")
        style.configure("TNotebook", background="#2e2e2e")
        style.configure("TNotebook.Tab", background="#3c3f41", foreground="white")
        self.main_frame = ttk.Frame(root, style="TFrame")
        self.main_frame.pack(fill="both", expand=True)

        self.add_main_interface()

    def add_main_interface(self):
        ttk.Label(self.main_frame, text="Escolha o Método:", font=("Arial", 16)).pack(
            pady=10
        )

        ttk.Button(
            self.main_frame, text="Cluster RGB", width=30, command=self.rgb_cluster
        ).pack(pady=10)
        ttk.Button(
            self.main_frame,
            text="Convolutional Neural Network",
            width=30,
            command=self.convolutional_neural_network,
        ).pack(pady=10)
        ttk.Button(
            self.main_frame,
            text="CNN multiple characters",
            width=30,
            command=self.convolutional_neural_network_multiple,
        ).pack(pady=10)
        ttk.Button(
            self.main_frame, text="Reconhecimento de Imagem", width=30, state="disabled"
        ).pack(pady=10)

    def on_close_second_window(self, window):
        window.destroy()
        self.root.deiconify()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.configure(width=screen_width, height=screen_height)

        if platform.system() == "Windows":
            root.state("zoomed")
        elif platform.system() == "Linux":
            root.attributes("-zoomed", True)


    def rgb_cluster(self):
        self.root.withdraw()
        new_window = tk.Toplevel(self.root)
        new_window.title("Cluster RGB Trainer")

        app = RgbClusterApp(new_window)

        new_window.protocol(
            "WM_DELETE_WINDOW", lambda: self.on_close_second_window(new_window)
        )

    def convolutional_neural_network(self):
        self.root.withdraw()
        new_window = tk.Toplevel(self.root)
        new_window.title("Convolutional Neural Network Trainer")

        app = ConvolutionalNeuralNetworkApp(new_window)

        new_window.protocol(
            "WM_DELETE_WINDOW", lambda: self.on_close_second_window(new_window)
        )

    def convolutional_neural_network_multiple(self):
        self.root.withdraw()
        new_window = tk.Toplevel(self.root)

        app = ConvolutionalNeuralNetworkMultipleCharApp(new_window)

        new_window.protocol(
            "WM_DELETE_WINDOW", lambda: self.on_close_second_window(new_window)
        )


class RgbClusterApp:
    def __init__(self, root):
        self.root = root

        root.configure(bg="#3c3f41")
        style = ttk.Style(self.root)
        style.theme_use("equilux")
        style.configure(
            ".", background="#3c3f41", foreground="white", fieldbackground="#3c3f41"
        )
        style.configure("TButton", background="#3c3f41", foreground="white")
        style.configure("TEntry", fieldbackground="#3c3f41", foreground="white")
        style.configure("TLabel", background="#3c3f41", foreground="white")
        style.configure("TNotebook", background="#3c3f41")
        style.configure("TNotebook.Tab", background="#3c3f41", foreground="white")
        style.configure(
            "Custom.TFrame", background="#3c3f41", borderwidth=2, relief="solid"
        )

        self.icon_delete = Image.open("./Icons/bin.png")
        self.icon_delete = self.icon_delete.resize((20, 20))
        self.icon_delete = ImageTk.PhotoImage(self.icon_delete)

        self.icon_color = Image.open("./Icons/palette.png")
        self.icon_color = self.icon_color.resize((20, 20))
        self.icon_color = ImageTk.PhotoImage(self.icon_color)

        root.title("Cluster RGB Trainer")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.configure(width=screen_width, height=screen_height)
        if platform.system() == "Windows":
            root.state("zoomed")
        elif platform.system() == "Linux":
            root.attributes("-zoomed", True)

        self.canvas = tk.Canvas(root, background="#3c3f41")
        self.canvas.pack(side="top", fill="both", expand=True)

        vbar = ttk.Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
        vbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=vbar.set)

        self.main_frame = ttk.Frame(self.canvas, style="Custom.TFrame")
        self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")

        self.main_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel_windows)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel_linux)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel_linux)

        self.canvas2 = tk.Canvas(root, height=0)
        self.canvas2.pack(fill="x", expand=False)
        self.console_frame = ttk.Frame(self.canvas2, style="Custom.TFrame")
        self.console_frame.pack(fill="x")

        self.canvas1 = tk.Canvas(root, height=0)
        self.canvas1.pack(side="bottom", fill="x", expand=False)
        self.status_frame = ttk.Frame(self.canvas1, style="Custom.TFrame")
        self.status_frame.pack(fill="x")

        self.open_rgb_cluster_window()

    def _on_mousewheel_windows(self, event):
        content_height = self.canvas.bbox("all")[3]
        visible_height = self.canvas.winfo_height()

        if content_height > visible_height:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _on_mousewheel_linux(self, event):
        content_height = self.canvas.bbox("all")[3]
        visible_height = self.canvas.winfo_height()

        if content_height > visible_height:
            if event.num == 4:
                self.canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.canvas.yview_scroll(1, "units")

    def open_rgb_cluster_window(self):
        self.color_row_tracker = {}
        self.rgb_entries_per_frame = {}
        self.params = {}
        self.id_entries_per_frame = {}
        self.char1_pictures_path = ""
        self.char2_pictures_path = ""
        self.char1_name = ""
        self.char2_name = ""

        char1_frame = ttk.Frame(self.main_frame, style="Custom.TFrame", padding=10)
        char1_frame.pack(padx=10, pady=10, side="left", expand=True, fill="both")

        char2_frame = ttk.Frame(self.main_frame, style="Custom.TFrame", padding=10)
        char2_frame.pack(padx=10, pady=10, side="left", expand=True, fill="both")

        training_frame = ttk.Frame(self.main_frame, style="Custom.TFrame", padding=10)
        training_frame.pack(padx=10, pady=10, side="left", expand=True, fill="both")

        testing_frame = ttk.Frame(self.main_frame, style="Custom.TFrame", padding=10)
        testing_frame.pack(padx=10, pady=10, side="left", expand=True, fill="both")

        self.add_character_input(char1_frame, "Personagem 1", "char1")
        self.add_character_input(char2_frame, "Personagem 2", "char2")
        self.add_training_parameters(training_frame)
        self.add_test_section(testing_frame)
        self.add_status_section(self.status_frame)
        self.add_console_section(self.console_frame)

    def add_character_input(self, frame, label, char):
        title = ttk.Label(frame, text=label, font=("Arial", 14))
        title.grid(row=0, column=0, columnspan=3, pady=(10, 0))

        labelNameChar = ttk.Label(frame, text="Nome do personagem:")
        labelNameChar.grid(row=1, column=0, sticky="w")
        if char == "char1":
            self.char1_name = ttk.Entry(frame)
            self.char1_name.grid(row=1, column=1)
        elif char == "char2":
            self.char2_name = ttk.Entry(frame)
            self.char2_name.grid(row=1, column=1)

        labelImages = ttk.Label(frame, text="Imagens do personagem:")
        labelImages.grid(row=2, column=0, sticky="w")
        entry_path = ttk.Entry(frame)
        entry_path.grid(row=2, column=1)
        ttk.Button(
            frame,
            text="Select folder",
            command=lambda: self.select_picture_folder(char, entry_path),
        ).grid(row=2, column=2)

        labelCores = ttk.Label(frame, text="Cores Principais:", font=("Arial", 14))
        labelCores.grid(row=3, column=0, columnspan=3, pady=(10, 0))

        colorsFrame = ttk.Frame(frame)
        colorsFrame.grid(row=5, column=0, columnspan=3)

        ttk.Button(
            frame,
            text="Adicionar campo",
            command=lambda: self.addColorField(colorsFrame),
        ).grid(row=4, column=0, columnspan=3, sticky="nsew")

        ttk.Label(colorsFrame, text="Area").grid(row=0, column=0)
        ttk.Label(colorsFrame, text="RGB").grid(row=0, column=1)

    def add_training_parameters(self, frame):
        vcmd = frame.register(self.check_num)
        ttk.Label(frame, text="Parametros", font=("Arial", 14)).grid(
            row=0, column=0, columnspan=2, pady=10
        )

        params_list = [
            "Input Shape",
            "Units",
            "Layers",
            "Bias",
            "Epochs",
            "Batch Size",
            "Test Size",
        ]
        for i in range(len(params_list)):
            ttk.Label(frame, text=f"{params_list[i]}:").grid(
                row=i + 1, column=0, sticky="w"
            )

        self.input_shape = tk.IntVar()
        self.input_shape_label = tk.StringVar(value="0.00")
        ttk.Scale(
            frame, from_=0, to=100, orient="horizontal", variable=self.input_shape
        ).grid(row=1, column=1)
        ttk.Label(frame, textvariable=self.input_shape_label, width=5).grid(
            row=1, column=2
        )

        self.units = tk.IntVar()
        self.units_label = tk.StringVar(value="0.00")
        ttk.Scale(
            frame, from_=0, to=100, orient="horizontal", variable=self.units
        ).grid(row=2, column=1)
        ttk.Label(frame, textvariable=self.units_label, width=5).grid(row=2, column=2)

        self.layers = tk.IntVar()
        self.layers_label = tk.StringVar(value="0.00")
        ttk.Scale(
            frame, from_=0, to=100, orient="horizontal", variable=self.layers
        ).grid(row=3, column=1)
        ttk.Label(frame, textvariable=self.layers_label, width=5).grid(row=3, column=2)

        self.bias = tk.IntVar()
        self.bias_label = tk.StringVar(value="0.00")
        ttk.Scale(frame, from_=0, to=1, orient="horizontal", variable=self.bias).grid(
            row=4, column=1
        )
        ttk.Label(frame, textvariable=self.bias_label, width=5).grid(row=4, column=2)

        self.epochs = ttk.Entry(frame, validate="key", validatecommand=(vcmd, "%P"))
        self.epochs.grid(row=5, column=1)

        self.batch_size = ttk.Entry(frame, validate="key", validatecommand=(vcmd, "%P"))
        self.batch_size.grid(row=6, column=1)

        self.test_size = tk.DoubleVar()
        self.test_size_label = tk.StringVar(value="0.00")
        ttk.Scale(
            frame, from_=0, to=1, orient="horizontal", variable=self.test_size
        ).grid(row=7, column=1)
        ttk.Label(frame, textvariable=self.test_size_label, width=5).grid(
            row=7, column=2
        )

        self.input_shape.trace_add("write", self.update_input_shape)
        self.units.trace_add("write", self.update_units_label)
        self.layers.trace_add("write", self.update_layers_label)
        self.bias.trace_add("write", self.update_bias_label)
        self.test_size.trace_add("write", self.update_test_size_label)

        ttk.Button(
            frame,
            text="Treinar",
            width=20,
            command=lambda: self.start_task(self.generate_dataset),
        ).grid(row=8, column=0, columnspan=3, pady=5, sticky="nsew")
        ttk.Button(
            frame,
            text="Carregar Modelo Existente",
            width=25,
            command=lambda: self.load_model(),
        ).grid(row=9, column=0, columnspan=3, pady=5, sticky="nsew")
        ttk.Button(
            frame, text="Salvar modelo", width=20, command=lambda: self.save_model()
        ).grid(row=10, column=0, columnspan=3, pady=5, sticky="nsew")

    def update_input_shape(self, *args):
        value = self.input_shape.get()
        self.input_shape_label.set(f"{value:.2f}")

    def update_units_label(self, *args):
        value = self.units.get()
        self.units_label.set(f"{value:.2f}")

    def update_layers_label(self, *args):
        value = self.layers.get()
        self.layers_label.set(f"{value:.2f}")

    def update_bias_label(self, *args):
        value = self.bias.get()
        self.bias_label.set(f"{value:.2f}")

    def update_test_size_label(self, *args):
        value = self.test_size.get()
        self.test_size_label.set(f"{value:.2f}")

    def add_test_section(self, frame):
        ttk.Label(frame, text="Teste", font=("Arial", 14)).grid(
            row=0, column=0, columnspan=2, pady=5
        )
        ttk.Label(
            frame,
            text="Selecione uma imagem desconhecida\nde um dos personagens:",
            justify="center",
        ).grid(row=1, column=0, columnspan=2, pady=5)

        ttk.Button(frame, text="Selecionar Arquivo", command=self.select_image).grid(
            row=2, column=0, columnspan=2, pady=5, sticky="nsew"
        )
        ttk.Button(frame, text="Iniciar teste", command=self.test_model).grid(
            row=3, column=0, columnspan=2, pady=5, sticky="nsew"
        )

        ttk.Label(frame, text="Resultado", font=("Arial", 12)).grid(
            row=4, column=0, columnspan=2, pady=5
        )
        self.result = ttk.Label(frame, text="", font=("Arial", 12))
        self.result.grid(row=5, column=0, columnspan=2)

        self.image_box = ttk.Label(frame, relief="solid")
        self.image_box.grid(row=6, column=0, columnspan=2)

        self.tset_image = None
        self.test_image_tk = None

    def add_status_section(self, frame):
        self.status = ttk.Label(frame, text="", justify="center")
        self.status.grid(row=0, column=0, columnspan=3)

    def add_console_section(self, frame):
        self.console_text = tk.Text(frame, height=10, bg="black", fg="white")
        self.console_text.bind("<KeyPress>", lambda e: "break")
        self.console_text.pack(fill="both", expand=True)

        sys.stdout = ConsoleText(self.console_text)
        sys.stderr = ConsoleText(self.console_text)

    def check_num(self, newval):
        return newval.isdigit() or newval == ""

    def select_folder(self):
        folder = filedialog.askdirectory(initialdir=os.path.expanduser("~/Downloads"))
        self.status.configure(text=f"Selected: {folder}")
        return folder

    def select_picture_folder(self, char, entry_path):
        folder = filedialog.askdirectory(initialdir=os.path.expanduser("~/Downloads"))
        entry_path.delete(0, tk.END)
        entry_path.insert(0, folder)
        try:
            if char == "char1":
                self.char1_pictures_path = folder
                self.status.configure(text=f"Selected: {folder}")
                return folder
            elif char == "char2":
                self.char2_pictures_path = folder
                self.status.configure(text=f"Selected: {folder}")
                return folder
        except Exception as e:
            messagebox.showerror("Error", e)

    def select_image(self):
        file = filedialog.askopenfilename(initialdir=os.path.expanduser("~/Downloads"))
        if file:
            self.tset_image = file
            self.status.configure(text=f"Selected: {file}")

            img = Image.open(file)
            img = img.resize((200, 200))

            self.test_image_tk = ImageTk.PhotoImage(img)
            self.image_box.configure(image=self.test_image_tk)

    def pick_color(self, entry):
        color_code = colorchooser.askcolor(title="Escolha uma cor")
        if color_code:
            entry.delete(0, tk.END)
            entry.insert(0, str(color_code[0]))

    def delete_widget(self, frame, entry_r, entry_g, widgets=[]):
        self.id_entries_per_frame[frame].remove(entry_r)
        self.rgb_entries_per_frame[frame].remove(entry_g)
        for widget in widgets:
            widget.destroy()

    def addColorField(self, frame):
        if frame not in self.color_row_tracker:
            self.color_row_tracker[frame] = 1
        if frame not in self.id_entries_per_frame:
            self.id_entries_per_frame[frame] = []
        if frame not in self.rgb_entries_per_frame:
            self.rgb_entries_per_frame[frame] = []

        row = self.color_row_tracker[frame]

        entry_r = ttk.Entry(frame, width=18)
        entry_r.grid(row=row, column=0, padx=10, pady=5)

        entry_g = ttk.Entry(frame, width=18)
        entry_g.grid(row=row, column=1, padx=10, pady=5)

        btn_color = ttk.Button(
            frame, image=self.icon_color, command=lambda e=entry_g: self.pick_color(e)
        )
        btn_color.grid(row=row, column=2)

        btn_delete = ttk.Button(
            frame,
            image=self.icon_delete,
            command=lambda: self.delete_widget(
                frame,
                entry_r,
                entry_g,
                widgets=[entry_r, entry_g, btn_color, btn_delete],
            ),
        )
        btn_delete.grid(row=row, column=3)

        self.id_entries_per_frame[frame].append(entry_r)
        self.rgb_entries_per_frame[frame].append(entry_g)
        self.color_row_tracker[frame] += 1

    def modelTraining(self):
        dataset = pd.read_csv("generated_dataset.csv")
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, -1].values
        y = y == self.char1_name.get()

        X = X / 255.0

        print(f"Classes in y: {np.unique(y, return_counts=True)}")

        X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(
            X, y, test_size=self.test_size.get(), stratify=y
        )

        input_shape = X.shape[1]

        self.rede_neural = tf.keras.models.Sequential()
        self.rede_neural.add(tf.keras.Input(shape=(input_shape,)))
        self.rede_neural.add(
            tf.keras.layers.Dense(
                units=self.units.get(),
                activation="relu",
                use_bias=self.bias.get(),
                kernel_initializer="he_normal",
            )
        )
        self.rede_neural.add(tf.keras.layers.Dropout(0.3))

        for _ in range(self.layers.get()):
            self.rede_neural.add(
                tf.keras.layers.Dense(
                    units=self.units.get(),
                    activation="relu",
                    kernel_initializer="he_normal",
                )
            )
            self.rede_neural.add(tf.keras.layers.Dropout(0.3))

        self.rede_neural.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))
        optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001)
        self.rede_neural.compile(
            optimizer="Adam", loss="binary_crossentropy", metrics=["accuracy"]
        )

        self.status.configure(text="Starting training")

        history = self.rede_neural.fit(
            X_treinamento,
            y_treinamento,
            epochs=int(self.epochs.get()),
            validation_data=(X_teste, y_teste),
            batch_size=int(self.batch_size.get()),
        )

        self.status.configure(text="Training complete")

    def preprocess_image(self, image_paths):
        print(image_paths)
        for folder_path in image_paths:
            self.status.configure(text=f"Processing images from {folder_path}")
            for filename in os.listdir(folder_path):
                print(filename)
                full_path = os.path.join(folder_path, filename)
                if os.path.isdir(full_path):
                    continue
                if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                    self.status.configure(text=f"Processing {full_path}")
                    img = cv2.imread(full_path)
                    if img is None:
                        print(f"Failed to load {full_path}")
                        continue
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    img = cv2.resize(img, (100, 100))
                    img = img.astype("float32") / 255.0
                    img = img.flatten()
                    img = np.expand_dims(img, axis=0)
                    og_img = cv2.imread(full_path)
                    og_img = cv2.resize(og_img, (400, 400))
                    new_img = img.reshape(100, 100)
                    new_img = cv2.resize(new_img, (400, 400))
                    
        return img

    def test_model(self):
        if not self.tset_image:
            messagebox.showwarning("Warning", "No test image selected!")
            return

        matched_rgbs = self.match_rgb_clusters_with_targets(
            self.tset_image, self.target_rgbs, n_clusters=5
        )

        feature_vector = []
        for rgb in matched_rgbs:
            avg_rgb = sum(rgb) / 3.0
            feature_vector.append(avg_rgb)

        # feature_vector = np.array(feature_vector).reshape(1, -1)

        feature_vector = np.array(feature_vector) / 255.0
        feature_vector = feature_vector.reshape(1, -1)

        expected_features = self.rede_neural.input_shape[1]
        feature_vector = feature_vector[:, :expected_features]

        prediction = self.rede_neural.predict(feature_vector)
        print("Raw prediction:", prediction)
        prediction = prediction > 0.5

        if prediction:
            prediction = self.char1_name.get()
        else:
            prediction = self.char2_name.get()

        self.result.configure(text=prediction)

    def save_model(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".keras",
            initialdir="./Models",
            title="Save As",
            filetypes=[["", "*.keras"]],
        )
        if path:
            try:
                tf.keras.models.save_model(self.rede_neural, path)
                path = os.path.dirname(path)
                path_json = f"{path}/metadata.json"
                metadata = {
                    "target_rgbs": self.target_rgbs,
                    "char1_name": self.char1_name.get(),
                    "char2_name": self.char2_name.get(),
                    "input_shape": self.input_shape.get(),
                    "units": self.units.get(),
                    "layers": self.layers.get(),
                    "bias": self.bias.get(),
                    "epochs": self.epochs.get(),
                    "batch_size": self.batch_size.get(),
                    "test_size": self.test_size.get(),
                }
                metadata_path = os.path.join(path_json)
                with open(metadata_path, "w") as f:
                    json.dump(metadata, f)
                self.status.configure(text=f"Model and metadata saved to: {path}")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving file: {e}")

        else:
            self.status.configure(text="Save cancelled")

    def load_model(self):
        path = filedialog.askopenfilename(
            initialdir="./Models", filetypes=[["", "*.keras"]]
        )
        json_path = f"{os.path.dirname(path)}/metadata.json"
        if path and json_path:
            self.rede_neural = tf.keras.models.load_model(path)

            if os.path.exists(json_path):
                with open(json_path, "r") as f:
                    metadata = json.load(f)
                self.target_rgbs = metadata.get("target_rgbs", [])
                char1_name = metadata.get("char1_name", "")
                char2_name = metadata.get("char2_name", "")
                input_shape = metadata.get("input_shape", "")
                units = metadata.get("units", "")
                layers = metadata.get("layers", "")
                bias = metadata.get("bias", "")
                epochs = metadata.get("epochs", "")
                batch_size = metadata.get("batch_size", "")
                test_size = metadata.get("test_size", "")

                self.char1_name.delete(0, tk.END)
                self.char1_name.insert(0, char1_name)

                self.char2_name.delete(0, tk.END)
                self.char2_name.insert(0, char2_name)

                self.epochs.delete(0, tk.END)
                self.epochs.insert(0, epochs)

                self.batch_size.delete(0, tk.END)
                self.batch_size.insert(0, batch_size)

                self.input_shape.set(input_shape)
                self.units.set(units)
                self.layers.set(layers)
                self.bias.set(bias)
                self.test_size.set(test_size)

                self.status.configure(text="Model and metadata loaded")
        elif path == True and json_path == False:
            messagebox.showerror("Error", f"Metadata não encontrado")
        elif path == False and json_path == True:
            messagebox.showerror("Error", f"Modelo não encontrado")
        else:
            messagebox.showerror("Error", f"Modelo e metadata não encontrados")

    def match_rgb_clusters_with_targets(self, image_path, target_rgbs, n_clusters=5):
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (100, 100))

        pixels = img.reshape(-1, 3)
        kmeans = KMeans(n_clusters=n_clusters)
        kmeans.fit(pixels)

        cluster_centers = kmeans.cluster_centers_.astype(int)

        matches = []
        for target_rgb in target_rgbs:
            distances = [
                self.color_distance(target_rgb, cluster_rgb)
                for cluster_rgb in cluster_centers
            ]
            closest_rgb = cluster_centers[np.argmin(distances)]
            matches.append(tuple(closest_rgb))

        return matches

    def color_distance(self, c1, c2):
        return np.linalg.norm(np.array(c1) - np.array(c2))

    def generate_dataset_from_targets(
        self, base_dir, headers, target_rgbs, output_csv, character_names, n_clusters=5
    ):
        with open(output_csv, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)

            for images_path in base_dir:
                self.status.configure(text=f"Processing images from {images_path}")
                for filename in os.listdir(images_path):
                    path = os.path.join(images_path, filename)
                    if os.path.isdir(path):
                        continue
                    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                        self.status.configure(text=f"Processing {path}")
                        try:
                            matched_rgbs = self.match_rgb_clusters_with_targets(
                                path, target_rgbs, n_clusters
                            )
                            row_features = []

                            for target_rgb in target_rgbs:
                                distances = [
                                    np.linalg.norm(
                                        np.array(cluster_rgb) - np.array(target_rgb)
                                    )
                                    for cluster_rgb in matched_rgbs
                                ]
                                min_distance = min(distances)
                                row_features.append(min_distance)

                            index = base_dir.index(images_path)
                            label = character_names[index]

                            row_features.append(label)
                            writer.writerow(row_features)

                        except Exception as e:
                            messagebox.showerror(
                                "Error", f"Error processing {path}\n {e}"
                            )

        self.status.configure(text=f"Process complete")

    def generate_dataset(self):
        target_rgbs = []
        headers = []
        paths = [self.char1_pictures_path, self.char2_pictures_path]
        self.preprocess_image(image_paths=paths)
        exit(0)
        for frame in self.rgb_entries_per_frame.values():
            for entry in frame:
                try:
                    rgb = tuple(map(int, entry.get().strip("() ").split(",")))
                    if len(rgb) == 3:
                        target_rgbs.append(rgb)
                except Exception as e:
                    messagebox.showerror("Error", f"Invalid RGB: {entry.get()} - {e}")

        for entries in self.id_entries_per_frame.values():
            for id in entries:
                headers.append(id.get())

        names = [self.char1_name.get(), self.char2_name.get()]
        headers.append("class")

        self.generate_dataset_from_targets(
            base_dir=paths,
            headers=headers,
            target_rgbs=target_rgbs,
            output_csv="generated_dataset.csv",
            character_names=names,
        )
        self.target_rgbs = target_rgbs
        self.modelTraining()

    def start_task(self, task):
        threading.Thread(target=task).start()

    def tset(self):
        pass


if __name__ == "__main__":
    os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
    root = ThemedTk(theme="equilux")
    app = App(root)
    root.mainloop()
