def valid_sentence(sentence):
    if isinstance(sentence, str):
        if sentence == "":
            raise Exception("Empty string given.")
        
        valid_punction = "?!."

        return sentence[0].isupper() and sentence[-1] in valid_punction
    else:
        raise Exception(f"valid_sentence expects str, given {type(sentence)}")