import tkinter as tk
from tkinter import filedialog, colorchooser
import os
import time
import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

class ClusterNeuralNetwork():
    def __init__(self, epochs, validation_split, batchSize, inputShape, units, layers):
        self.epochs = epochs
        self.validation_split = validation_split
        self.test_size = batchSize
        self.inputShape = inputShape
        self.units = units
        self.layers = layers

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
        self.rgb_entries_char1 = []
        self.rgb_entries_char2 = []
        
        firstFrame = tk.Frame(self.main_frame, highlightbackground='black', highlightcolor='red', borderwidth=10, highlightthickness=1)
        firstFrame.grid(row=0, column=0, padx=10, pady=10, sticky='N')

        secondFrame = tk.Frame(self.main_frame, highlightbackground='black', highlightcolor='red', borderwidth=10, highlightthickness=1)
        secondFrame.grid(row=0, column=1, padx=10, pady=10, sticky='N')

        thirdFrame = tk.Frame(self.main_frame, highlightbackground='black', highlightcolor='red', borderwidth=10, highlightthickness=1)
        thirdFrame.grid(row=0, column=2, padx=10, pady=10, sticky='N')

        forthFrame = tk.Frame(self.main_frame, highlightbackground='black', highlightcolor='red', borderwidth=10, highlightthickness=1)
        forthFrame.grid(row=0, column=3, padx=10, pady=10, sticky='N')

        consoleFrame = tk.Frame(self.main_frame, highlightbackground='black', highlightcolor='red', borderwidth=10, highlightthickness=1)
        consoleFrame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='N')

        self.add_character_input(firstFrame, "Personagem 1", self.rgb_entries_char1)
        self.add_character_input(secondFrame, "Personagem 2", self.rgb_entries_char2)
        self.add_training_parameters(thirdFrame)
        self.add_test_section(forthFrame)

    def add_character_input(self, frame, label, rgb_entries):
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

        self.params = {}
        params_list = ["Input Shape", "Units", "Layers", "Bias", "Epochs", "Batch Size"]
        for idx, param in enumerate(params_list):
            tk.Label(frame, text=f"{param}:").grid(row=idx+1, column=0, sticky="w")
            entry = tk.Entry(frame)
            entry.grid(row=idx+1, column=1)
            self.params[param] = entry

        tk.Button(frame, text="Treinar", width=20).grid(row=8, column=0, columnspan=2, pady=5)
        tk.Button(frame, text="Carregar Modelo Existente", width=25).grid(row=9, column=0, columnspan=2, pady=5)
        tk.Button(frame, text="Salvar modelo", width=20).grid(row=10, column=0, columnspan=2, pady=5)

    def add_test_section(self, frame):
        tk.Label(frame, text="Teste", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=5)
        tk.Label(frame, text="Selecione uma imagem desconhecida\nde um dos personagens:", justify="center").grid(row=1, column=0, columnspan=2, pady=5)
        tk.Button(frame, text="Selecionar Arquivo", command=self.select_image).grid(row=2, column=0, columnspan=2, pady=5)

        tk.Label(frame, text="Resultado", font=("Arial", 12)).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Label(frame, text="%resultado%", font=("Arial", 12)).grid(row=4, column=0, columnspan=2, pady=5)

        tk.Label(frame, text="*Imagem Selecionada*", bd=1, relief="solid", width=30, height=10).grid(row=5, column=0, columnspan=2, pady=10)

    def select_folder(self):
        folder = filedialog.askdirectory()
        print(f"Selected folder: {folder}")

    def select_image(self):
        file = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        print(f"Selected image for testing: {file}")

    def pick_color(self, entry):
        color_code = colorchooser.askcolor(title="Escolha uma cor")
        if color_code:
            entry.delete(0, tk.END)
            entry.insert(0, str(color_code[0]))

    def addColorField(self, frame):
        if frame not in self.color_row_tracker:
            self.color_row_tracker[frame] = 1
        if frame not in self.rgb_entries_per_frame:
            self.rgb_entries_per_frame[frame] = []

        row = self.color_row_tracker[frame]

        entry_r = tk.Entry(frame, width=18)
        entry_r.grid(row=row, column=0, padx=10, pady=5)

        entry_g = tk.Entry(frame, width=18)
        entry_g.grid(row=row, column=1, padx=10, pady=5)

        btn_color = tk.Button(frame, text="🎨", command=lambda e=entry_g: self.pick_color(e))
        btn_color.grid(row=row, column=2)

        self.rgb_entries_per_frame[frame].append((entry_r, entry_g))
        print(self.rgb_entries_per_frame)
        self.color_row_tracker[frame] += 1

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
