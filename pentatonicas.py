# --- Pentatônica maior --- #
maior = {
    'C': ['C', 'D', 'E', 'G', 'A'],
    'C#/Db': ['C#/Db', 'D#/Eb', 'F', 'G#/Ab', 'A#/Bb'],
    'D': ['D', 'E', 'F#/Gb', 'A', 'B'],
    'D#/Eb': ['D#/Eb', 'F', 'G', 'A#/Bb', 'C'],
    'E': ['E', 'F#/Gb', 'G#/Ab', 'B', 'C#/Db'],
    'F': ['F', 'G', 'A', 'C', 'D'],
    'F#/Gb': ['F#/Gb', 'G#/Ab', 'A#/Bb', 'C#/Db', 'D#/Eb'],
    'G': ['G', 'A', 'B', 'D', 'E'],
    'G#/Ab': ['G#/Ab', 'A#/Bb', 'C', 'D#/Eb', 'F'],
    'A': ['A', 'B', 'C#/Db', 'E', 'F#/Gb'],
    'A#/Bb': ['A#/Bb', 'C', 'D', 'F', 'G'],
    'B': ['B', 'C#/Db', 'D#/Eb', 'F#/Gb', 'G#/Ab']
}

# --- Pentatônica menor --- #
menor = {
    'C': ['C', 'D#/Eb', 'F', 'G', 'A#/Bb'],
    'C#/Db': ['C#/Db', 'E', 'F#/Gb', 'G#/Ab', 'B'],
    'D': ['D', 'F', 'G', 'A', 'C'],
    'D#/Eb': ['D#/Eb', 'F#/Gb', 'G#/Ab', 'A#/Bb', 'C#/Db'],
    'E': ['E', 'G', 'A', 'B', 'D'],
    'F': ['F', 'G#/Ab', 'A#/Bb', 'C', 'D#/Eb'],
    'F#/Gb': ['F#/Gb', 'A', 'B', 'C#/Db', 'E'],
    'G': ['G', 'A#/Bb', 'C', 'D', 'F'],
    'G#/Ab': ['G#/Ab', 'B', 'C#/Db', 'D#/Eb', 'F#/Gb'],
    'A': ['A', 'C', 'D', 'E', 'G'],
    'A#/Bb': ['A#/Bb', 'C#/Db', 'D#/Eb', 'F', 'G#/Ab'],
    'B': ['B', 'D', 'E', 'F#/Gb', 'A']
}

# --- Equivalência maior = menor --- #
equivalencia_maior_menor = {
    'C': 'A',
    'C#/Db': 'A#/Bb',
    'D': 'B',
    'D#/Eb': 'C',
    'E': 'C#/Db',
    'F': 'D',
    'F#/Gb': 'D#/Eb',
    'G': 'E',
    'G#/Ab': 'F',
    'A': 'F#/Gb',
    'A#/Bb': 'G',
    'B': 'G#/Ab'
}

# --- Equivalência menor = maior --- #
equivalencia_menor_maior = {
    'C': 'D#/Eb',
    'C#/Db': 'E',
    'D': 'F',
    'D#/Eb': 'F#/Gb',
    'E': 'G',
    'F': 'G#/Ab',
    'F#/Gb': 'A',
    'G': 'A#/Bb',
    'G#/Ab': 'B',
    'A': 'C',
    'A#/Bb': 'C#/Db',
    'B': 'D'
}
