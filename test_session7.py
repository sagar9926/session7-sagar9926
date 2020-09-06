import pytest
import random
import string
import os
import inspect
import re
import math
import session7  
from session7 import fib_tester

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding = "utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding = "utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        print(space)
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_is_fibonacci():
    assert fib_tester(4181) == True , "The fibonacci tester is not functioning properly"
    assert fib_tester(2584) == True , "The fibonacci tester is not functioning properly"
    assert fib_tester(9999) == False , "The fibonacci tester is not functioning properly"
    assert fib_tester(6454) == False , "The fibonacci tester is not functioning properly"
    
def test_question_2_1():
    
    iter1 = [1,2,3,4,5,6]
    iter2 = [10,21,30,43,50,60]
    assert session7.question_2_1(iter1,iter2) == [23 , 47] , "The Question_2_1 function is not functioning properly"
    
def test_vowel_strip():
    input_string = 'sagartsaiepai'
    assert session7.vowel_strip(input_string) == 's g rts   p  ' , "The vowel strip function is not functioning properly"
    
def test_relu():
    Relu_input = [1,2,3,4,5,-8,-9,10,-100]
    assert session7.relu(Relu_input)  == [1,2,3,4,5,0,0,10,0] , "Relu is not functioning properly"
    
def test_sigmoid():
    Sigmoid_input = [1,2,3,4,5]
    assert session7.sigmoid(Sigmoid_input)  == [0.73, 0.88, 0.95, 0.98, 0.99] , "Sigmoid is not functioning properly"
    
def test_shift_alphabets():
    input_string = 'tsai'
    assert session7.shift_alphabets(input_string) == 'yxfn' , "Shift alphabets is not working properly"
    
def test_swear_detection():
    f = open("Paragraph.txt",'r',encoding = "utf-8")
    Paragraph = f.read()
    f.close()
    Paragraph = set(Paragraph.split())
    assert session7.swear_detection(Paragraph) == True , "Swear detection is not working properly"
    
def test_Add_only_even():
    list1 = [1,2,3,4,5,6]
    assert session7.add_only_even(list1) == 2+4+6 , "Add_only_even is not working properly"
    
def test_biggest_character():
    sample_string = 'STAHagar!~'
    assert session7.biggest_character(sample_string) == '~' , "biggest_character is not functioning properly"
    
def test_add_every_third():
    list1 = [10,20,30,40,50,60,70,80]
    assert session7.add_every_third(list1) == 30 + 60
    

    
    



    
