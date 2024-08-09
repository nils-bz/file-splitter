Small sript capable of splitting each file within a directory into multiple files based on its contents. 

For each file within the given root directory, there will be one file created for each paragraph within the file. A paragraph in this context refers to a part of text without any blank line in between. The following example text would be split into 3 separate documents.
"""
This represents a test document.

Each paragraph in this document will become a separate file after applying the script onto this document.

The content of this line will be in the third document created.
This line will also be inside the third document.
"""

The script takes two arguments: "--root-dir", "--output-dir".
All files contained in the directory given via the "--root-dir" argument will be splitted according to the explanation above. Only files contained directly in this directory will be considered and any folder in the given root-directory will be ignored.
The directory given via "--output-dir" will hold all resulting files after applying the script. 
The output-directory must differ from the root-directory and the root-directory must exists, otherwise the script will exit without any effect.
