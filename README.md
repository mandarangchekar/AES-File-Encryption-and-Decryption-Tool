 
Intro to Cryptography 
User Manual 
 
 
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
 
  
 
 
 
 
 
 
 
 
 
![image](https://github.com/mandarangchekar/AES-File-Encryption-and-Decryption-Tool/assets/65801031/32fe1523-0a15-461a-bf12-c5b1dfed8412)
