from exercise1 import ShiftCipher

def main():
    ciphertext = "GurPnrfnepvcurevfernyylrnflgboernx"
    results = []

    for shift in range(26):
        shift_cipher = ShiftCipher(shift=shift)
        decrypted_text = shift_cipher.decrypt(ciphertext=ciphertext)
        results.append(decrypted_text)

    print(results)
    return results

if __name__ == "__main__":
    main()
