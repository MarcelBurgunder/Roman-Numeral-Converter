# Roman-Numeral-Converter

**Context**

Some jurisdictions use Roman numerals inconsistently. We need to convert the Roman
numeral so we can recognize “Article IV” and “Article 4” are referring to the same section for the
purpose of creating hyperlinks.

**Background**

Here are some Roman numerals:

- I -> 1
- V -> 5
- X -> 10
- L -> 50 
- C -> 100
- D -> 500
- M -> 1,000

**Examples**

- Input: "II" <br>
  Output: 2

- Input: "IV" <br>
  Output: 4

- Input: "VIII" <br>
  Output: 8

- Input: "LXXXIX" <br>
  Output: 89

- Input: "XCII" <br>
  Output: 92

**Important Assumptions and Technical Details**

- The script supports Roman Numeral characters up to, and including, *M* which represents 1,000. This means the largest number that can be converted is *MMMCMXCIX*, which translates to 3,999 in Arabic numerals. The script uses a dictionary to store the mapping of Roman characters to their Arabic number value. Note that:
  - For the purposes of this script we recreate two dictionaries everytime that the script is run. This is a minor performance hit, but is no problem given the scale of the task. If this were implemented on a larger scale, and would need to be reused across the board, it would make sense to store these dictionaries in a seperate file or in a database to then be loaded in.
  - We could combine both dictionaries into one and it would make no functional impact, but I chose to seperate them to make our code neater.
  - To expand this code solution to allow for the processing of Roman numerals larger than 3,999, we would require further discussion and clarification of assumptions and inputs, because as [this educational resource](https://byjus.com/maths/roman-numerals/) puts it, such values will include characters with bars over a letter, such as *V̅* representing 5,000. Such non-standard alphabetical characters may introduce new complexities due to an array of different conventions on how to represent these in text.
- This script accepts and requires a singular string input that represents a Roman numeral.
  - Additional inputs will be ignored, and providing no inputs will raise an error.
  - Any input that includes an invalid character, such as *A*, *G*, *Z*, *~*, *%*, will be evaluated as an invalid input and raise an error.
  - Input processing is case sensitive, meaning that a character such as *v* will not be recognised as *V*, and treated as an invalid character.
  - **Most Importantly:** Beyond these very simple validation checks we are assuming that the provided input is completely valid, thus inputting principally invalid (due to the ordering and/or frequency of valid characters) strings will result in no error and some nonsense incorrect Arabic equivalent. This includes invalid inputs such as *VIIIIIXI*, *XVX*, *MDD*, *IM*.  
- This script doesn't return anything, it only converts some inputted Roman numeral and print its Arabic equivalent.

**Testing**

- Make sure Python is installed (see https://www.python.org/downloads/).
- Download the file 'romanToArabic.py' and place it inside some working directory.
- In your terminal, run the Python script using the command 'python <path_to_file>\roman_to_arabic.py <roman>', whereby <path_to_file> represents the path file on your local machine, and <roman> represents some Roman numeral input. See the list of assumptions regarding the validation that will take place and which inputs we are assuming shall not.
