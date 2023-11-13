import os

label_path = r"C:\Users\Uib\yolov5\datasets\halimeda_xesc_y_git\labels\train"
classes = []
for filename in os.listdir(label_path):
        with open(f'{label_path}/{filename}', 'r') as file:
            labels = file.read().splitlines()

        with open(f"{label_path}/{filename}", 'w') as file:
            for label_idx, label_text in enumerate(labels):
                # Actualizar la etiqueta actual con el nuevo punto clave
                label_text = label_text.split()
                label_text[0] = '0'
                label_text = ' '.join(label_text)
                file.write(label_text + '\n')

