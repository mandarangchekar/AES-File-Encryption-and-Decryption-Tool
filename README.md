 
Intro to Cryptography 
User Manual 

Introduction
In an era where data security is paramount, the need for robust encryption tools has never been greater. With the increasing frequency of cyber threats and data breaches, protecting sensitive information has become a critical concern for individuals and organizations alike. The Advanced Encryption Standard (AES) has emerged as a leading encryption algorithm, widely recognized for its strength and efficiency in securing data. However, the technical complexity of implementing AES encryption has often been a barrier to its widespread adoption, particularly among users with limited technical expertise in cryptography.
This project, titled "Advanced Encryption Standard (AES) File Encryption and Decryption Tool," aims to address this gap by developing a user-friendly tool that simplifies the process of encrypting and decrypting files using AES. The primary objective is to make AES encryption more accessible and approachable for a broader audience, thereby enhancing the overall security of data management practices.
The project was undertaken as part of the coursework for CIS 628 Introduction to Cryptography at Syracuse University in the Fall of 2023. It represents a collaborative effort to integrate advanced cryptographic techniques with ease of use, ensuring that strong data protection is not just the domain of experts but is available to everyone.
In this report, we delve into the execution, significance, literature background, results, and challenges of the project. The report aims to provide a comprehensive overview of the project's development process, its contributions to the field of cryptography, and its potential impact on data security practices.
 
 

To run the Project follow the steps below!

Step 1 
Open the project folder in a code editor ( VS code, Sublime, Atom, etc)  Open terminal and navigate to the project directory. 
 
  
 
 
Before running the code, install the required package - Crypto Run the following command: pip install pycryptodome 
 
  
 
This command will install pycryptodome and its dependencies, allowing you to use the Crypto.Cipher, Crypto.U/l.Padding, and Crypto.Random modules in your Python code. 
 
Make a file in the same directory that you want to encrypt. The file can be of any type eg .txt, .csv, .png etc.  
 
  
 
Step 2: 
Run the python code file named “test.py”.  
Run the following command: 
python test.py 
 
  
 
 
Step 3: 
 
To encrypt a file type 1 and press Enter  
  
 
Enter the file you want to encrypt. The program can take any type of files as input. 
Please type the file name along with the extension (.txt, .csv, .png etc.) that you created in step 1.  Press Enter. 
 
  
 
 
 
This should create two files in the same directory namely:  
 
1)	Encrypted file: In this example encrypted_test.txt 
 
   
2)	Key: In this example test.txt.key 
 
  
 
 
Step 4: 
 
To decrypt a file type 2 and press Enter  
 
  
 
 
 
Enter the name of the encrypted file that was created in the directory in step3. In this example encrypted_test.txt 
Press Enter 
 
  
 
Enter the name of the fey file that was created in the directory in step 3. In this example test.text.key Press Enter 
 
   
This should create the decrypted file in the same directory: 
 
1) Decrypted file: In this example decrypted_test.txt 
 
Note: The decrypted file created using the encrypted file and the key should be the same as the original file you created in the step 1. 
Enter 3 to exit 
 
  
 
 
 
 
 
 
 
 
 

