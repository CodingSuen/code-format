import argparse
import re
import subprocess
import sys
import os 
from os import path 

regex_file = re.compile('.*\.(cpp|cc|c\+\+|cxx|c|cl|h|hh|hpp|m|mm|inc|js|ts|proto|protodevel|java|cs|'
    'CPP|CC|C\+\+|CXX|C|CL|H|HH|HPP|M|MM|INC|JS|TS|PROTO|PROTODEVEL|JAVA|CS)$')
regex_path = re.compile('(^//.|^/|^[a-zA-Z])?:?/.+(/$)?')

parser = argparse.ArgumentParser(description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-i', 
    action='store_true',
    default=False,
    help='apply edits to files instead of displaying a diff')
parser.add_argument('-style',
    help='formatting style to apply (LLVM, Google, Chromium, Mozilla, WebKit)')
parser.add_argument('-path',
    help='specify the path of the files to be formatted')
parser.add_argument('-file',
    default=False,
    help='specify the file to be formatted')
args = parser.parse_args()

def scaner_files(file_path, file_list):
    if args.file:
        if regex_file.match(args.file):
            if file_path[-1] == '/':
                real_filepath = file_path + args.file
            else:
                real_filepath = file_path + '/' + args.file
            file_list.append(real_filepath)
        else:
            sys.exit('file is not correct!')
    else:
        file = os.listdir(file_path)
        for f in file:
            real_filepath = path.join(file_path, f)
            if path.isfile(real_filepath):
                if regex_file.match(f):
                    file_list.append(real_filepath)
            elif path.isdir(real_filepath):
                scaner_files(real_filepath, file_list)
            else:
                sys.exit('other situation')

def clang_format(file_list, format_command):
    for file in file_list:
        command = []
        command.append('clang-format')
        command.append(file)
        command.extend(format_command)
        p = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=None,
                            stdin=subprocess.PIPE,
                            universal_newlines=True)
        stdout, stderr = p.communicate()
        if p.returncode != 0:
            sys.exit(p.returncode)
        elif p.returncode == 0:
            pass

def main():
    file_path = args.path
    file_list = []
    format_command = []
    if regex_path.match(str(file_path)):
        scaner_files(file_path, file_list)
        if args.style:
            if args.style == 'LLVM' or args.style == 'Google' or args.style == 'Chromium' or args.style == 'Mozilla' or args.style == 'WebKit':
                format_command.extend(['-style', args.style])
            else:
                sys.exit("-systel shuould be LLVM, Google, Chromium, Mozilla or WebKit")
                exit()
        if args.i:
            format_command.append('-i')
        clang_format(file_list, format_command)
    else:
        sys.exit('path is not correct!')

if __name__ == '__main__':
  main()
