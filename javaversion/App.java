package javaversion;

public class App {
    public static void main(String[] agrs) {
        String text = "If he had anything confidential to say he wrote it in cipher that is by so changing the order of the letters of the alphabet that not a word could be made out ";

        CaesarCipher cipher = new CaesarCipher();

        String cipherText = cipher.encrypt(text, 3);
        System.out.println(cipherText);
        String plainText = cipher.decrypt(cipherText, 3);
        System.out.println(plainText);

    }
}
