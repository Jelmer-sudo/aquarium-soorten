"""Schrijft README.md van de repo aquarium-soorten met de bronvermelding per foto.

Gebruik: maak_readme_soortenrepo.py <map van aquarium-soorten>
"""
import json, sys
from pathlib import Path
repo = Path(sys.argv[1])
d = json.loads((repo / "species.json").read_text(encoding="utf-8"))
rijen = []
for s in d["soorten"]:
    f = s.get("foto")
    if f:
        rijen.append(f"| {s['naam']} (*{s['latijn']}*) | {f['maker']} | {f['licentie']} | [Commons]({f['bron']}) |")
    else:
        rijen.append(f"| {s['naam']} (*{s['latijn']}*) | AI-beeld, zelf gemaakt met ComfyUI | — | — |")
tekst = f"""# aquarium-soorten

Soortenlijst en afbeeldingen voor een persoonlijke Android-app om aquaria bij te houden. De app haalt `species.json` en de afbeeldingen hier op; zonder internet gebruikt ze de kopie die in de app zit.

## Wat erin staat

- `species.json`: {len(d['soorten'])} zoetwatersoorten (dieren en planten) met temperatuur, pH, grootte, minimale bakgrootte, groepsgrootte, karakter en verzorging. De waarden komen uit algemeen bekende aquariumkennis, gecontroleerd met openbare bronnen, en zijn in eigen woorden opgeschreven.
- `afbeeldingen/<id>.webp`: één afbeelding per soort, 512 × 512 pixels.

## Afbeeldingen en licenties

De meeste afbeeldingen zijn foto's van [Wikimedia Commons](https://commons.wikimedia.org/). Ze zijn vierkant bijgesneden en verkleind, en vallen onder hun eigen licentie (CC0, publiek domein, CC BY of CC BY-SA). Een bijgesneden CC BY-SA-foto valt onder dezelfde CC BY-SA-licentie. Maker, licentie en bron staan ook per soort in het veld `foto` van `species.json`.

Twee afbeeldingen zijn met AI gemaakt (lokale ComfyUI), omdat er geen bruikbare vrije foto van te vinden was.

| Soort | Maker | Licentie | Bron |
|---|---|---|---|
""" + "\n".join(rijen) + "\n"
(repo / "README.md").write_text(tekst, encoding="utf-8")
print(len(rijen))
