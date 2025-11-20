
import math

nodes_order = [
    "MeskelSquare","Mexico","SarBet","Stadium","Kazanchis","Bole","BoleMedhanialem",
    "BoleBrass","Olympia","CMC","Gotera","AratKilo","Piassa","Churchill","Megenagna",
    "AutobusTera","Saris","Kaliti","Ayat","Torhailoch","OldAirport","Merkato"
]

coords = {
    "MeskelSquare": (9.010643934045525, 38.76112545288324),
    "Mexico": (9.010770133986124, 38.7443325798668),
    "SarBet": (8.99450953732196, 38.73830593436462),
    "Stadium": (9.01348309082329, 38.75644101398244),
    "Kazanchis": (9.016406086351257, 38.77607238690809),
    "Bole": (8.991132002070284, 38.794964763380015),
    "BoleMedhanialem": (8.99610032207546, 38.79013390076805),
    "BoleBrass": (8.990520073112398, 38.793559604663535),
    "Olympia": (9.005040980381432, 38.768950771320036),
    "CMC": (9.02120860318711, 38.85229120533341),
    "Gotera": (8.984559362261425, 38.75610642469874),
    "AratKilo": (9.032970353057891, 38.76370858912899),
    "Piassa": (9.032759615214328, 38.75404417986698),
    "Churchill": (9.026067910735058, 38.752025839391436),
    "Megenagna": (9.019833164210079, 38.80233123701409),
    "AutobusTera": (9.034173478584906, 38.73297934652353),
    "Saris": (8.955672965382771, 38.772070599525016),
    "Kaliti": (8.897006074957647, 38.77074725877929),
    "Ayat": (9.02165469413583, 38.871521156128225),
    "Torhailoch": (9.01131297134366, 38.7215334884652),
    "OldAirport": (8.986639750120112, 38.73107896480089),
    "Merkato": (9.035246322480004, 38.73290568699775),
}

def haversine_km(lat1, lon1, lat2, lon2):
    
    R = 6371.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2.0)**2 + math.cos(phi1)*math.cos(phi2)*(math.sin(dlambda/2.0)**2)
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return R * c


lines = []
for a in nodes_order:
    for b in nodes_order:
        (lat1, lon1) = coords[a]
        (lat2, lon2) = coords[b]
        d = haversine_km(lat1, lon1, lat2, lon2)
        
        d_rounded = round(d, 1)
        lines.append(f"{a} {b} {d_rounded:.1f}")


outname = "heuristic_generated_km_1dp.txt"
with open(outname, "w", encoding="utf-8") as f:
    for ln in lines:
        f.write(ln + "\n")

print(f"Wrote {len(lines)} lines to {outname}\n")


chunk_size = 44
num_chunks = (len(lines) + chunk_size - 1) // chunk_size
for i in range(num_chunks):
    start = i*chunk_size
    end = start + chunk_size
    print(f"--- CHUNK {i+1} (lines {start+1} to {min(end, len(lines))}) ---")
    for ln in lines[start:end]:
        print(ln)
    print()
