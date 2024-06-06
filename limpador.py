# Notas do modo Jônio em todos os 12 tons
modo = {
    'C': ['C', 'Eb', 'F', 'G', 'Bb'],
    'C#': ['C#', 'E', 'F#', 'G#', 'B'],
    'D': ['D', 'F', 'G', 'A', 'C'],
    'D#': ['D#', 'F#', 'G#', 'A#', 'C#'],
    'E': ['E', 'G', 'A', 'B', 'D'],
    'F': ['F', 'Ab', 'Bb', 'C', 'Eb'],
    'F#': ['F#', 'A', 'B', 'C#', 'E'],
    'G': ['G', 'Bb', 'C', 'D', 'F'],
    'G#': ['G#', 'B', 'C#', 'D#', 'F#'],
    'A': ['A', 'C', 'D', 'E', 'G'],
    'A#': ['A#', 'C#', 'D#', 'F', 'G#'],
    'B': ['B', 'D', 'E', 'F#', 'A']
}


# Simplificar notas com sustenidos ou bemóis duplos
for key in modo:
    modo[key] = [note.replace('E#', 'F').replace('B#', 'C').replace('C##', 'D').replace('F##', 'G').replace('A##', 'B').replace('G##', 'A').replace('D##', 'E').replace('Fb', 'E').replace('Cb', 'B') for note in modo[key]]

copia = modo.copy()

for chave in copia:
    copia[chave] = [nota.replace('C#', 'C#/Db').replace('D#', 'D#/Eb').replace('F#', 'F#/Gb').replace('G#', 'G#/Ab').replace('A#', 'A#/Bb') for nota in copia[chave]]

for chave, valor in copia.items():
    print(f"'{chave}': {valor},")
