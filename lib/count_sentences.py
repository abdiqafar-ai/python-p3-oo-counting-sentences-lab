#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = None  # Private attribute to store value
        self.value = value  # This will trigger the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            self._value = ""  # You can choose to assign an empty string or handle differently
        else:
            self._value = new_value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        # Define sentence-ending punctuation
        sentence_endings = {'.', '?', '!'}
        
        sentence_count = 0
        current_sentence = ""
        
        # Strip leading/trailing whitespaces
        text = self.value.strip()

        i = 0
        while i < len(text):
            char = text[i]
            current_sentence += char  # Add character to the current sentence
            
            # Check if the current character is a sentence-ending punctuation
            if char in sentence_endings:
                # After a sentence-ending punctuation, skip any following punctuation marks
                # Treat consecutive sentence-ending punctuation as a single sentence boundary
                while i + 1 < len(text) and text[i + 1] in sentence_endings:
                    i += 1
                
                # If we have a non-empty sentence, count it
                if current_sentence.strip():
                    sentence_count += 1
                current_sentence = ""  # Reset for the next sentence
                
            i += 1

        # Final check for any leftover content
        if current_sentence.strip():
            sentence_count += 1

        return sentence_count





