import json

# Bu veriyi senin CSV'lerinden veya manuel girişlerinden besleyebilirsin
# Şimdilik profesyonel bir örnek yapı kuralım:
data = {
    "nodes": [
        {"id": "Ahmet_Eren", "name": "System Architect", "group": 1, "size": 20},
        {"id": "Jeffrey_E", "name": "Target", "group": 2, "size": 15},
        {"id": "Senator_X", "name": "Politician", "group": 2, "size": 12},
        {"id": "Shadow_Bank", "name": "Offshore", "group": 3, "size": 10}
    ],
    "links": [
        {"source": "Jeffrey_E", "target": "Senator_X", "type": "MET_SECRETLY"},
        {"source": "Senator_X", "target": "Shadow_Bank", "type": "SENT_MONEY"},
        {"source": "Ahmet_Eren", "target": "Jeffrey_E", "type": "INVESTIGATING"}
    ]
}

with open('data.json', 'w') as f:
    json.dump(data, f)

print("✅ 'data.json' hazır. Şimdi görselleştirme katmanına geçiyoruz.")