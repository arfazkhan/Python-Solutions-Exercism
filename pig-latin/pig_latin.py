def translate(text):
    def pig_latin(word):
        vowels = 'aeiou'
        if word[0] in vowels or word[:2] in ["yt", "xr"]:
            return word + 'ay'
        
        if word.startswith("qu"):
            return word[2:] + 'quay'
        
        if 'qu' in word:
            idx = word.index('qu') + 2
            return word[idx:] + word[:idx] + 'ay'
        
        for i in range(len(word)):
            if word[i] in vowels or (word[i] == 'y' and i != 0):
                return word[i:] + word[:i] + 'ay'
        
        return word + 'ay'
    
    return ' '.join(pig_latin(word) for word in text.split())
