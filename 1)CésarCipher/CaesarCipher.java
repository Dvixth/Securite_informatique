import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class CaesarCipher {

    // Fonction de chiffrement de César
    public static String encrypt(String text, int s) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < text.length(); i++) {
            // Vérifier si le caractère est une lettre majuscule
            if (Character.isUpperCase(text.charAt(i))) {
                // Appliquer le décalage à la lettre majuscule
                char ch = (char)(((int)text.charAt(i) + s - 65) % 26 + 65); 
                result.append(ch);
            } else {
                // Appliquer le décalage à la lettre minuscule
                char ch = (char)(((int)text.charAt(i) + s - 97) % 26 + 97);
                result.append(ch);
            }
        }
        return result.toString();
    }

    // Fonction de déchiffrement de César
    public static String decrypt(String text, int s) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < text.length(); i++) {
            // Vérifier si le caractère est une lettre majuscule
            if (Character.isUpperCase(text.charAt(i))) {
                // Appliquer le décalage inverse à la lettre majuscule
                char ch = (char)(((int)text.charAt(i) - s - 65 + 26) % 26 + 65);
                result.append(ch);//ajoute du résultat au StringBuilder result 
            } else {
                // Appliquer le décalage inverse à la lettre minuscule
                char ch = (char)(((int)text.charAt(i) - s - 97 + 26) % 26 + 97);
                result.append(ch);
            }
        }
        return result.toString();
    }

    // Fonction de brute force pour déchiffrer le message avec toutes les clés possibles
    public static void bruteForceCesar(String messageChiffre) {
        System.out.println("Tentative de brut force du chiffrement");
        for (int decalage = 0; decalage < 26; decalage++) {
            String messageDechiffre = decrypt(messageChiffre, decalage);
            System.out.println("Clé " + decalage + ": " + messageDechiffre);
        }
    }

    // Fonction d'analyse des fréquences pour le texte donné
    public static double lettrefrequence(String text) {
        // Définir les fréquences attendues pour chaque lettre de l'alphabet
        Map<Character, Double> expectedFrequency = new HashMap<>();
        expectedFrequency.put('a', 8.41);
        expectedFrequency.put('b', 1.06);
        expectedFrequency.put('c', 3.03);
        expectedFrequency.put('d', 4.18);
        expectedFrequency.put('e', 17.26);
        expectedFrequency.put('f', 1.12);
        expectedFrequency.put('g', 1.27);
        expectedFrequency.put('h', 0.92);
        expectedFrequency.put('i', 7.34);
        expectedFrequency.put('j', 0.31);
        expectedFrequency.put('k', 0.05);
        expectedFrequency.put('l', 6.01);
        expectedFrequency.put('m', 2.96);
        expectedFrequency.put('n', 7.13);
        expectedFrequency.put('o', 5.26);
        expectedFrequency.put('p', 3.01);
        expectedFrequency.put('q', 0.99);
        expectedFrequency.put('r', 6.55);
        expectedFrequency.put('s', 8.08);
        expectedFrequency.put('t', 7.07);
        expectedFrequency.put('u', 6.36);
        expectedFrequency.put('v', 1.91);
        expectedFrequency.put('w', 0.01);
        expectedFrequency.put('x', 0.42);
        expectedFrequency.put('y', 0.88);
        expectedFrequency.put('z', 0.09);
        // ... (les autres fréquences)

        // Convertir le texte en minuscules pour normaliser
        text = text.toLowerCase();

        // Compter les occurrences de chaque lettre dans le texte
        Map<Character, Integer> letterCounts = new HashMap<>();
        for (char c : text.toCharArray()) {
            if (Character.isLetter(c)) {
                letterCounts.put(c, letterCounts.getOrDefault(c, 0) + 1);
            }
        }

        // Calculer le test du chi carré pour l'analyse des fréquences
        double chiSquare = 0.0;
        for (char letter : letterCounts.keySet()) {
            int observedCount = letterCounts.get(letter);
            double expectedCount = (text.length() * expectedFrequency.getOrDefault(letter, 0.0) / 100.0);
            double difference = observedCount - expectedCount;
            chiSquare += (difference * difference) / expectedCount;
        }

        return chiSquare;
    }

    // Fonction de cryptanalyse pour trouver le message chiffré en utilisant l'analyse de fréquence
    public static String cryptanalysforce(String text) {
        String bestGuess = null;
        double bestScore = Double.MAX_VALUE;

        for (int s = 1; s <= 25; s++) {
            // Déchiffrer le texte avec le décalage actuel
            String decryptedText = decrypt(text, s);

            // Calculer le score en utilisant l'analyse des fréquences
            double score = lettrefrequence(decryptedText);

            // Mettre à jour la meilleure supposition avec le score le plus bas
            if (score < bestScore) {
                bestScore = score;
                bestGuess = decryptedText;
            }
        }
        return bestGuess;
    }

    // Fonction principale
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Demander à l'utilisateur de saisir le texte et la clé
        System.out.print("Entrez le texte à chiffrer : ");
        String text = sc.nextLine();
        System.out.print("Entrez la clé : ");
        int s = sc.nextInt();

        // Chiffrer le texte
        String encryptedText = encrypt(text, s);
        System.out.println("Cipher : " + encryptedText);

        // Déchiffrer le texte
        String decryptedText = decrypt(encryptedText, s);
        System.out.println("DeCipher : " + decryptedText);

        bruteForceCesar(encryptedText); //brut force de message avec la méthode de chiffrement 

        // Effectuer la cryptanalyse en utilisant l'analyse de fréquence
        String cryptanalyse = cryptanalysforce(encryptedText);
        System.out.println("Best Guess : " + cryptanalyse);

        // Utiliser la brute force pour déchiffrer le texte
        
    }
}
