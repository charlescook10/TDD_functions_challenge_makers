import math
def estimate_reading_time(text):
    if isinstance(text, str):
        number_of_words = len(text.split())
        # 200 words can be read in 60 seconds
        # words per second = 200/60 = 1 word every 0.3 second

        return math.ceil(number_of_words*0.3)
    else:
        raise Exception(f"estimate_reading_time expects str, given {type(text)}")
    