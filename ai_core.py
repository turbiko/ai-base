class AICore:
    def __init__(self):
        self.model = None  # Тут буде завантаження моделі
        self.ready = False

    def load_model(self):
        # Логіка завантаження моделі
        self.model = "Loaded AI Model"
        self.ready = True
        return "AI Model Loaded"

    def predict(self, data):
        if not self.ready:
            return "Model not loaded"
        return f"Prediction for {data}: 42"  # Заглушка для передбачення

    def status(self):
        my_status = self.load_model(self) # try to load model
        print(f{my_status=})
        return "Ready" if self.ready else "Not Ready"
