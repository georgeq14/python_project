dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

#variables
item_to_find = "TAT"
item_found = False

for item in dna_sequence:
    if item == item_to_find:
        item_found = True
        
if item_found == True:
    print("Item Found")
else:
    print("Item Not Found")