class Solution {
    public int characterReplacement(String s, int k) {

        int[] freq = new int[26];

        int left = 0;
        int maxFreq = 0;
        int maxLength = 0;

        for(int right = 0; right < s.length(); right++) {

            char ch = s.charAt(right);

            // Increase frequency
            freq[ch - 'A']++;

            // Track highest frequency character
            maxFreq = Math.max(maxFreq, freq[ch - 'A']);

            // Characters to replace
            int replacements = (right - left + 1) - maxFreq;

            // Shrink window if replacements exceed k
            while(replacements > k) {

                freq[s.charAt(left) - 'A']--;

                left++;

                replacements = (right - left + 1) - maxFreq;
            }

            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}