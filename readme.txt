安装环境CentOS7
可以解压到任意目录，以下以/home目录为例
解压文件到/home目录
cd /home
tar xvf clangformat15.tar

拷贝clang-format文件到/usr/bin目录下
cp clang-format /usr/bin

查看clang-format版本
clang-format --version

将.clang-format文件拷贝到要格式化的文件目录或父级目录下
cp .clang-format /xxx/xxx/xxx

执行code-format.py格式化代码
1.格式化repos下的helloworld.cpp文件，使用.clang-format自定义格式
python code-format.py -path=/repos -file=helloworld.cpp -style=file -i
2.格式化repos下的所有文件，使用.clang-format自定义格式
python code-format.py -path=/repos -style=file -i


.clang-format配置参数说明：
https://www.cnblogs.com/PaulpauL/p/5929753.html
https://clang.llvm.org/docs/ClangFormatStyleOptions.html

clang-format supports two ways to provide custom style options: directly specify style configuration in the -style= command line option or use -style=file and put style configuration in the .clang-format or _clang-format file in the project directory.
.clang-format文件是自定义的格式化配置文件，当-style=file时表示使用自定义格式来格式化代码
When using -style=file, clang-format for each input file will try to find the .clang-format file located in the closest parent directory of the input file. 
使用-style=file时，对clang-format命令会优先查找位于输入文件最近的父目录中的. Clang-format文件

注意：
对于软连接文件，会破坏软连接，生产格式化后的新文件。当时用-path格式化所有路径下的文件时，需要注意这点。已经修复，自测通过。
