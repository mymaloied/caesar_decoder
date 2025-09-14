# Changelog

All notable changes to this project will be documented in this file.

## [improved] - 2025-09-14

### Added
- Support for uppercase letters preservation
- Proper handling of punctuation marks and special characters
- Non-alphabetic symbols now remain unchanged during decryption

### Fixed
- Fixed incorrect symbol display
- Fixed uppercase letters not being decrypted properly
- Removed duplicate code execution
- Improved character processing algorithm

### Changed
- Replaced loop-based shifting with modulo arithmetic for better performance
- Simplified character shifting algorithm using `(position - shift) % 26`

## [main] - 2025-09-13

### Added
- Initial release
- Basic Caesar cipher decryption
- Automatic shift detection using NLTK word database
- English word recognition and matching percentage calculation
