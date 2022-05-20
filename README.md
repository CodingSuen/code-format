code_format.py is modified based on clang-format-diff.py.
It is used to generate the command of clang-format and execute it.

To use code_format.py to format the code, you need to install clang first. 
Please refer to https://clang.llvm.org/get_started.html, and building clang.

There are some examples for how to use this script:
format the file xxx under the path /home
python format.py -path=/home -file=xxx -i -style=Google
format all the files unde the path /home
python format.py -path=/home -file=xxx -i -style=Google

Also you can use custom style, put style configuration in the .clang-format file in the path where you execute command.
