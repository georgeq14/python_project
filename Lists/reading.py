"""
dna = ['AUG', 'AUC', 'UCG']

dna.append('UAA')     # ['AUG', 'AUC', 'UCG', 'UAA']
dna.insert(2, 'GAU')  # ['AUG', 'AUC', 'GAU', 'UCG', 'UAA']
dna.remove('AUC')     # ['AUG', 'GAU', 'UCG', 'UAA']
dna.pop(0)            # ['GAU', 'UCG', 'UAA']
"""

books = ["harry Potter", "1984", "The Fault in our stars", "The Mom Test", "Life in Code"]

books.append("Pachinko")
books.remove("The Fault in our stars")
books.pop(1)

print(books)