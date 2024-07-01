# Coreutils-Python-Mohamed-Riyad
To run each command, you can use `go run` followed by the Go file name and any arguments required by the command. Here’s how you can run each one:

 1. head :
    Print the first 10 lines of input by default. Use the `-n` flag to specify a different number of lines to print.
    ```sh
    python ./head.py  -n [number] [filename]
    ```
 2. tail :
    Print the last 10 lines of input by default. Use the `-n` flag to specify a different number of lines to print.
    ```sh
    python ./tail.py -n [number] [filename]
    ```
 3. echo :
    Print arguments to standard output. use -n to omit the trailing newline.
    ```sh
    python ./echo.py -n [text]
    ```
 4. cat :
    print files. Use -n to output lines numbers.
    ```sh
    python ./cat.py -n [filename]
    ```
 5. wc : 
    Count lines, words, and characters in the input.
    Add -l, -w, and -c flags to display only lines, words, or characters respectively.
    ```sh
    python ./wc.py -w -l [filename]
    ```
 6. true :
    A command that does nothing successfully.
    ```sh
    python ./true.py
    ```
 7. false :
    A command that does nothing unsuccessfully.
    ```sh
    python ./false.py
    ```

 8. tree :
    Print all files and folders inside a directory recursively. Use the `-l` flag to specify the maximum depth of printing files.
    ```sh
    python ./tree.py -l [number]
    ```
    
 9. env :
  Print all environment variables.
    ```sh
    python ./env.py
    ```
