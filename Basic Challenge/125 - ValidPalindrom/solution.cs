public class Solution {
    public bool IsPalindrome(string s) {
        s = ToAlphaOnly(s).ToLower();
        Console.WriteLine(s);
        return s.SequenceEqual(s.Reverse());
    }
    private string ToAlphaOnly(string input)
    {
        return new string(input.Where(c =>char.IsLetterOrDigit(c)).ToArray());
    }
}
