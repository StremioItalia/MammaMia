import json
import requests

def get_domains():
    # Recupera il contenuto del Pastebin con i domini
    pastebin_url = 'https://pastebin.com/raw/KgQ4jTy6'
    response = requests.get(pastebin_url)
    
    # Estrai i domini dalla risposta e rimuovi eventuali caratteri di ritorno a capo
    domains = response.text.strip().split('\n')
    domains = [domain.strip().replace('\r', '') for domain in domains]  # Rimuove i caratteri \r
    return domains

def update_json_file():
    # Carica il file JSON che vuoi aggiornare
    with open('config.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Ottieni i domini
    domains = get_domains()

    # Mappatura dei siti da aggiornare
    site_mapping = {
        'StreamingCommunity': domains[0],       # Primo dominio
        'Filmpertutti': domains[3],             # Quarto dominio
        'Tantifilm': domains[10],               # Undicesimo dominio
        'CB01': domains[4],                    # Quinto dominio
        'AnimeWorld': domains[12],              # Tredicesimo dominio
    }

    # Aggiorna il file JSON per i siti specificati
    for site_key, domain_url in site_mapping.items():
        # Controlla che la chiave esista nel JSON (con la rimozione di spazi)
        if site_key in data['Siti']:
            domain_name = domain_url.split('.')[-1]  # Estrai solo la parte finale del dominio
            print(f"Aggiornato {site_key}: {domain_name}")  # Stampa per debug
            data['Siti'][site_key]['domain'] = domain_name

    # Scrivi il file JSON aggiornato
    with open('config.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print("File config.json aggiornato con successo!")

if __name__ == '__main__':
    update_json_file()
