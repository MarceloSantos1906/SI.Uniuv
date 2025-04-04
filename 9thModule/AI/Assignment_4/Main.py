import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog, colorchooser
import cv2
import os
import csv
import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.cluster import KMeans


class RgbClusterApp():
    def __init__(self, root):
        self.root = root
        
        root.title("Cluster RGB Trainer")
        root.geometry("1400x700")

        self.canvas = tk.Canvas(root)
        self.canvas.pack(side="left", fill="both", expand=True)
        vbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        vbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=vbar.set)
        self.main_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")
        self.main_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
        self.open_rgb_cluster_window()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def open_rgb_cluster_window(self):
        self.color_row_tracker = {}
        self.rgb_entries_per_frame = {}
        self.params = {}
        self.id_entries_per_frame = {}

        firstFrame = tk.Frame(self.main_frame, highlightbackground='black', highlightcolor='red', borderwidth=10, highlightthickness=1)
        firstFrame.grid(row=0, column=0, padx=10, pady=10, sticky='N')

        secondFrame = tk.Frame(self.main_frame, highlightbackground='black', highlightcolor='red', borderwidth=10, highlightthickness=1)
        secondFrame.grid(row=0, column=1, padx=10, pady=10, sticky='N')

        thirdFrame = tk.Frame(self.main_frame, highlightbackground='black', highlightcolor='red', borderwidth=10, highlightthickness=1)
        thirdFrame.grid(row=0, column=2, padx=10, pady=10, sticky='N')

        forthFrame = tk.Frame(self.main_frame, highlightbackground='black', highlightcolor='red', borderwidth=10, highlightthickness=1)
        forthFrame.grid(row=0, column=3, padx=10, pady=10, sticky='N')

        self.add_character_input(firstFrame, "Personagem 1")
        self.add_character_input(secondFrame, "Personagem 2")
        self.add_training_parameters(thirdFrame)
        self.add_test_section(forthFrame)

    def add_character_input(self, frame, label):
        title = tk.Label(frame, text=label, font=("Arial", 14))
        title.grid(row=0, column=0, columnspan=3, pady=(10, 0))
        
        labelNameChar = tk.Label(frame, text="Nome do personagem:")
        labelNameChar.grid(row=1, column=0, sticky="w")
        tk.Entry(frame).grid(row=1, column=1)

        labelImages = tk.Label(frame, text="Imagens do personagem:")
        labelImages.grid(row=2, column=0, sticky="w")
        buttonSelectFolder = tk.Button(frame, text="Select folder", command=self.select_folder)
        buttonSelectFolder.grid(row=2, column=1)

        labelCores = tk.Label(frame, text="Cores Principais:", font=("Arial", 14))
        labelCores.grid(row=3, column=0, columnspan=3, pady=(10, 0))

        colorsFrame = tk.Frame(frame)
        colorsFrame.grid(row=5, column=0, columnspan=3)

        tk.Button(frame, text="Adicionar campo", command=lambda: self.addColorField(colorsFrame)).grid(row=4, column=2)

        tk.Label(colorsFrame, text="Area").grid(row=0, column=0)
        tk.Label(colorsFrame, text="RGB").grid(row=0, column=1)

    def add_training_parameters(self, frame):
        tk.Label(frame, text="Parametros", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

        params_list = ["Input Shape", "Units", "Layers", "Bias", "Epochs", "Batch Size"]
        for idx, param in enumerate(params_list):
            tk.Label(frame, text=f"{param}:").grid(row=idx+1, column=0, sticky="w")
            entry = tk.Entry(frame)
            entry.grid(row=idx+1, column=1)
            self.params[param] = entry

        tk.Button(frame, text="Treinar", width=20, command=lambda: self.generate_dataset).grid(row=8, column=0, columnspan=2, pady=5)
        tk.Button(frame, text="Carregar Modelo Existente", width=25).grid(row=9, column=0, columnspan=2, pady=5)
        tk.Button(frame, text="Salvar modelo", width=20, command=lambda: self.tset()).grid(row=10, column=0, columnspan=2, pady=5)

    def add_test_section(self, frame):
        tk.Label(frame, text="Teste", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=5)
        tk.Label(frame, text="Selecione uma imagem desconhecida\nde um dos personagens:", justify="center").grid(row=1, column=0, columnspan=2, pady=5)
        tk.Button(frame, text="Selecionar Arquivo", command=self.select_image).grid(row=2, column=0, columnspan=2, pady=5)

        tk.Label(frame, text="Resultado", font=("Arial", 12)).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Label(frame, text="%resultado%", font=("Arial", 12)).grid(row=4, column=0, columnspan=2, pady=5)

        tk.Label(frame, text="*Imagem Selecionada*", bd=1, relief="solid", width=30, height=10).grid(row=5, column=0, columnspan=2, pady=10)

    def select_folder(self):
        folder = filedialog.askdirectory()

    def select_image(self):
        file = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

    def pick_color(self, entry):
        color_code = colorchooser.askcolor(title="Escolha uma cor")
        if color_code:
            entry.delete(0, tk.END)
            entry.insert(0, str(color_code[0]))

    def addColorField(self, frame):
        if frame not in self.color_row_tracker:
            self.color_row_tracker[frame] = 1
        if frame not in self.id_entries_per_frame:
            self.id_entries_per_frame[frame] = []
        if frame not in self.rgb_entries_per_frame:
            self.rgb_entries_per_frame[frame] = []

        row = self.color_row_tracker[frame]

        entry_r = tk.Entry(frame, width=18)
        entry_r.grid(row=row, column=0, padx=10, pady=5)

        entry_g = tk.Entry(frame, width=18)
        entry_g.grid(row=row, column=1, padx=10, pady=5)

        btn_color = tk.Button(frame, text="🎨", command=lambda e=entry_g: self.pick_color(e))
        btn_color.grid(row=row, column=2)

        self.id_entries_per_frame[frame].append((entry_r))
        self.rgb_entries_per_frame[frame].append((entry_g))
        self.color_row_tracker[frame] += 1

    def modelTraining(self):
        dataset = pd.read_csv('personagens.csv')
        X = dataset.iloc[:, 0:6].values
        y = dataset.iloc[:, 6].values
        y = (y == 'Bart')

        X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size = 0.2)

        rede_neural = tf.keras.models.Sequential()
        rede_neural.add(tf.keras.layers.Dense(units=2, activation='relu', input_shape=(6,)))
        rede_neural.add(tf.keras.layers.Dense(units=2, activation='relu'))
        rede_neural.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

        rede_neural.compile(optimizer='Adam', loss='binary_crossentropy', metrics = ['accuracy'])

        rede_neural.fit(X_treinamento, y_treinamento, epochs=200, validation_split=0.1)

        previsoes = rede_neural.predict(X_teste)

        previsoes = (previsoes > 0.5)

        cm = confusion_matrix(y_teste, previsoes)

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
            distances = [self.color_distance(target_rgb, cluster_rgb) for cluster_rgb in cluster_centers]
            closest_rgb = cluster_centers[np.argmin(distances)]
            matches.append(tuple(closest_rgb))

        return matches

    def color_distance(self, c1, c2):
        return np.linalg.norm(np.array(c1) - np.array(c2))

    def generate_dataset_from_targets(self, base_dir, target_rgbs, output_csv='output.csv', n_clusters=5):
        with open(output_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['file', 'r', 'g', 'b', 'label'])

            for label in os.listdir(base_dir):
                folder = os.path.join(base_dir, label)
                if not os.path.isdir(folder):
                    continue

                for filename in os.listdir(folder):
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                        path = os.path.join(folder, filename)
                        try:
                            matched_rgbs = self.match_rgb_clusters_with_targets(path, target_rgbs, n_clusters)
                            for rgb in matched_rgbs:
                                writer.writerow([path, *rgb, label])
                        except Exception as e:
                            messagebox.showerror('Error', f"Error processing {path}\n {e}")

    def generate_dataset(self):
        target_rgbs = []
        for entry in self.rgb_entries:
            try:
                rgb = tuple(map(int, entry.get().strip('() ').split(',')))
                if len(rgb) == 3:
                    target_rgbs.append(rgb)
            except Exception as e:
                messagebox.showerror('Error', f"Invalid RGB: {entry.get()} - {e}")

        self.generate_dataset_from_targets(
            base_dir='path/to/your/training_folders',
            target_rgbs=target_rgbs,
            output_csv='generated_dataset.csv')

    def tset(self):
        print('ids:')
        for k in self.id_entries_per_frame.values():
            for i in k:
                print(i.get())
        print('rgbs:')
        for k in self.rgb_entries_per_frame.values():
            for i in k:
                print(i.get())

class App:
    def __init__(self, root):
        self.root = root
        root.title("AI Image Trainer")
        root.geometry("1200x600")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        self.add_main_interface()

    def add_main_interface(self):
        tk.Label(self.main_frame, text="Escolha o Método:", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.main_frame, text="Cluster RGB", width=30, height=2, command=self.start_rgb_cluster_mode).pack(pady=10)
        tk.Button(self.main_frame, text="Reconhecimento de Imagem", width=30, height=2, state='disabled').pack(pady=10)

    def start_rgb_cluster_mode(self):
        self.root.destroy()
        self.launch_rgb_cluster()

    def launch_rgb_cluster(self):
        new_root = tk.Tk()
        app = RgbClusterApp(new_root)
        new_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
