# Counting words in a text using Python
![robot-reader](./Images/reader-robot.png)
## Introduction
I like to start my learning journey of new languages (like French, Spanish, English etc.) by reading before listening or speaking. I try to read the most I can: books, articles, news etc. By reading you become familiar with the structure of the language and also increase your vocabulary, making the next steps of listening and speaking much easier.

When reading a text, I try to identify the words that appear more frequently, because I know that are the words I have to memorize first. Before using computers to assist my learning process, I tried to manually count the occurrency of every word, taking notes directly in the text or in a separate notebook or piece of paper.

Now, with the advent of Python and other script languages, we can automate such tasks! This script is one example of how to do this automation. You can use it to count the occurrency of words in text of any Western languages, such as English, Spanish, French, Italian, etc. However, I haven't tried it in text written in Eastern languages, such as Chinese, Japanese, Arabic etc., but I'd love to receive any feedback of users that tried to use it that way.

## Script Usage

**Step 1:** To use this script, you must have the Python installed in your computer. If you don't have it, please download and install it. The download is available in the [Official Website](https://www.python.org/downloads/). Please be sure to check the option "Add Python.exe to PATH" in order to add the Python folder in the PATH Windows variable. This will make possible to execute Python commands from any place in the Windows command prompt in your computer.

**Step 2:** Create a text file (.txt) containing the text you want to count words from and save it to a local folder in your computer. If you prefer, you can try the script using the sample text (in English) I prepared for you, [Lisbon.txt](Lisbon.txt).

**Step 3:** From the Windows Command prompt, run the script, which has the following usage format:

``` python count_words.py <input_file> <output_file> ```

So, using my Lisbon.txt file and considering the output could be saved in a 'Lisbon-count.txt' file, the command would be:

``` python count_words.py Lisbon.txt Lisbon-count.txt ```

Let's see how the first 25 lines of the result looks like:

```
WORDS WITH 4 OR MORE CHARACTERS:

lisbon: 13
city: 11
name: 6
with: 5
area: 5
from: 5
portuguese: 4
capital: 4
after: 4
european: 4
other: 4
largest: 3
portugal: 3
being: 3
world: 3
modern: 3
later: 3
most: 3
since: 3
been: 3
centre: 3
global: 3
lisbons: 3
```
## Conclusion

That's it! I tried to comment the code in [count-words.py](count-words.py) the best as I could so that you can understand the full process.

Hope this script can be useful for you and that you enjoy this project!
