def calculate_correction(white_pieces):
    correct_pieces = [1, 1, 2, 2, 2, 8]  
    corrections = [correct - found for correct, found in zip(correct_pieces, white_pieces)]
    return corrections

def main():
    white_pieces_found = list(map(int, input().split()))  
    corrections = calculate_correction(white_pieces_found)  

    for correction in corrections:
        print(correction)

if __name__ == "__main__":
    main()