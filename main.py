Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from fastapi import FastAPI
... import uvicorn
... 
... app = FastAPI()
... 
... @app.get("/calculate-fit/{player_id}")
... def calculate_fit(player_id: int):
...     # Basit bir AI mantığı: Oyuncu verilerini al ve skor üret
...     # Gerçek projede burada daha önce yazdığımız Cosine Similarity çalışacak
...     base_stats = {"pace": 90, "passing": 85, "defending": 45} 
...     fit_score = (base_stats["pace"] * 0.4) + (base_stats["passing"] * 0.6)
...     
...     return {
...         "player_id": player_id,
...         "fit_score": int(fit_score),
...         "status": "Elite Talent" if fit_score > 85 else "Standard"
...     }
... 
... if __name__ == "__main__":
