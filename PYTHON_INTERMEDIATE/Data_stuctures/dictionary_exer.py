artifact = {
    
    "artist": "Buddha Maitreya",
    "period": "Northern Wei Dynasty",
    "date": 486
    
}

print(artifact)
print(artifact["artist"])
print(artifact["period"])
print(artifact["date"])


# Dictionary representing a Pyxis (with some extra info)
pyxis = {
  'artist': 'Penthesilea painter',
  'period': 'classical',
  'date': '465-460 BCE',
  'culture': ['Greek', 'Attic'],
  'medium': ['terracotta', 'white-ground'],
  'dimensions': {'height': '4.75in', 'height w/cover': '6.75in'}
}

print('Printing the dictionary: ', pyxis)
print('\nPrinting the keys: ', pyxis.keys())
print('\nPrinting the values: ', pyxis.values())