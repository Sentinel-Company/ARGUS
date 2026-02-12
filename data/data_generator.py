import json

def filter_massive_data(input_file='data.json', output_file='data_optimized.json'):
    print("🧠 ARGUS Veri Filtreleme Başladı (Bu işlem biraz sürebilir)...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Her düğümün kaç bağlantısı olduğunu say
    link_counts = {}
    for link in data['links']:
        link_counts[link['source']] = link_counts.get(link['source'], 0) + 1
        link_counts[link['target']] = link_counts.get(link['target'], 0) + 1

    # 2. KRİTER: Sadece 2 veya daha fazla bağlantısı olanları tut 
    # (Tekil bağlantılar genelde gürültüdür)
    important_nodes = {node_id for node_id, count in link_counts.items() if count >= 2}
    
    # 3. Yeni düğüm ve bağlantı listesini oluştur
    new_nodes = [n for n in data['nodes'] if n['id'] in important_nodes]
    new_links = [l for l in data['links'] if l['source'] in important_nodes and l['target'] in important_nodes]

    # 4. Kaydet (Boşluksuz formatta)
    optimized_data = {"nodes": new_nodes, "links": new_links}
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(optimized_data, f, separators=(',', ':'))

    print(f"✅ FİLTRELEME TAMAMLANDI!")
    print(f"📊 Eski Düğüm: {len(data['nodes'])} -> Yeni Düğüm: {len(new_nodes)}")
    print(f"💾 Yeni dosya: {output_file} (Boyut ciddi oranda düştü)")

if __name__ == "__main__":
    filter_massive_data()