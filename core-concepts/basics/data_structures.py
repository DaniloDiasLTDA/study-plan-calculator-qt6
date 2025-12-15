#likedin learn

def run_basics():
    start1 = 'Sol'
    start2 = 'Alpha Centauri'
    start3 = 'Barnard'
    start4 = 'Wolf 359'

    stars = [
        start1,
        start2,
        start3,
        start4
    ]
    print(f"Estrela na posição 3: {stars[3]}")

    peaks = {
        'african': 'Kilinmanjaro',
        'antarctic': 'Vinson',
        'australian':  'Puncak Jaya',
        'eurasian': 'Everest'
    }
    print(f"Pico Africano: {peaks['african']}")

if __name__ == "__main__":
    run_basics()