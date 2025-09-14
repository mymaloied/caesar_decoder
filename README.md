# 🔐 Caesar Cipher Decoder

A Python tool that automatically decrypts Caesar cipher messages using dictionary-based word recognition.

## ✨ Features

- **Automatic decryption**: Tries all possible shifts and finds the most likely solution
- **Dictionary validation**: Uses NLTK's English word corpus to identify meaningful text  
- **Manual mode**: View all decryption variants if automatic detection fails
- **User-friendly interface**: Clear prompts and error handling

## 🚀 Quick Start

### Prerequisites

```bash
pip install nltk
```

### Usage

1. Run the program:
```bash
python main.py
```

2. Enter your encrypted message:
```
Enter your cipher: WKLV LV D WHVW PHVVDJH
```

3. Choose automatic or manual decryption:
```
Do you want to automatically find the most likely decryption?(Y/N) Y
```

4. Get your result:
```
this is a test message
```

## 📋 Example

**Input:** `WKLV LV D WHVW PHVVDJH`  
**Output:** `this is a test message`

**Input:** `KHOOR ZRUOG`  
**Output:** `hello world`

## ⚙️ How It Works

1. **Generate all variants**: Creates 26 possible decryptions (one for each shift)
2. **Word matching**: Compares each variant against English dictionary
3. **Score calculation**: Counts valid English words in each variant
4. **Best match selection**: Returns the variant with highest word recognition rate

## 🛠️ Technical Details

- **Algorithm**: Caesar cipher with all possible shifts (0-25)
- **Dictionary**: NLTK English words corpus (~236,000 words)
- **Threshold**: Requires >50% word recognition for automatic selection
- **Fallback**: Shows all variants if automatic detection fails

## 📝 Requirements

- Python 3.x
- NLTK library
- Internet connection (for first-time NLTK data download)

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## ⬆️ Changes

See the CHANGELOG.md file
 
## 📄 License

This project is open source and available under the MIT License.