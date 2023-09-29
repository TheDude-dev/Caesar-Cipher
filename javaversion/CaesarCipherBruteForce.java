package javaversion;

public class CaesarCipherBruteForce {
    private String ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public void crack(String cipherText) {
        for (int key = 0; key < ALPHABET.length(); ++key) {
            // reinitialize this to an empty string
            String plainText = "";

            // Make a caesar decrytpion
            for (int i = 0; i < cipherText.length(); i++) {
                char character = cipherText.charAt(i);
                int charIndex = ALPHABET.indexOf(character);
                int decryptedIndex = Math.floorMod((charIndex - key), ALPHABET.length());
                plainText += ALPHABET.charAt(decryptedIndex);
            }

            // print the actual decrypted string with the given key
            System.out.format("Cracking Caesar-cipher with %s key the result is: %s%n", key, plainText);

        }
    }
}
