""" Example of usage:
python compile.py <program-to-compile>
"""
from nodes import AST
from parser_lexer import parser
import sys

if len(sys.argv) > 1:
    with open(sys.argv[1], "r") as f:
        data = f.read()
else:
    data = """
    int a, b, c;
    b=7;
    a=2;
   
   while (!(a==10)){
   write(a);

   if(b>=a){
   write(b>=a);
   } else{
   write(b>=a);
   }
   true xor false;
   a = a+ 1;
   }
    
    """
result = parser.parse(data)

print(result)

ast = AST(result)

ast.check_semantic_errors()

ast.create_llvm_output("output")
