import numpy as np
import json
import sys


def print(*args, fun=False, positive_space='X', negative_space=' ', **kwargs):
    '''
    Fun-print version of printing
    '''
    printer = FunPrinter(fun, positive_space, negative_space)
    printer.print(*args, **kwargs)


class FunPrinter():
    def __init__(self, fun=False, positive_space='X', negative_space=' '):
        self.fun = fun
        with open('char_map.json', 'r') as fp:
            self.char_map_full = json.load(fp)
        self.char_map = self.char_map_full['char_map']
        self.positive_space = positive_space
        self.negative_space = negative_space
        
        background = [[self.negative_space for i in range(8)] for j in range(8)]
        foreground = [[self.positive_space for i in range(8)] for j in range(8)]

        self.background = np.array(background)
        self.foreground = np.array(foreground)
    

    def print(self, *args, **kwargs):
        '''
        The new-style print function from py3k.
        Taken from https://gist.github.com/dannguyen/b7d7ce593fe748157f34
        '''
        fp = kwargs.pop('file', sys.stdout)
        if fp is None:
            return
        def write(data):
            if not isinstance(data, str):
                data = str(data)
            ### New Code
            if self.fun:
                data = self.str_to_8x8(data)
            ### New Code
            fp.write(data)
        want_unicode = False
        sep = kwargs.pop('sep', None)
        if sep is not None:
            if isinstance(sep, str):
                want_unicode = True
            elif not isinstance(sep, str):
                raise TypeError('sep must be None or a string')
        end = kwargs.pop('end', None)
        if end is not None:
            if isinstance(end, str):
                want_unicode = True
            elif not isinstance(end, str):
                raise TypeError('end must be None or a string')
        if kwargs:
            raise TypeError('invalid keyword arguments to print()')
        if not want_unicode:
            for arg in args:
                if isinstance(arg, str):
                    want_unicode = True
                    break
        if want_unicode:
            newline = u'\n'
            space = u' '
        else:
            newline = '\n'
            space = ' '
        if sep is None:
            sep = space
        if end is None:
            end = newline
        for i, arg in enumerate(args):
            if i:
                write(sep)
            write(arg)
        write(end)

    
    def int_to_bin(self, int: int):
        '''
        Function to return 8-bit binary representation
        of and integer
        '''
        return bin(int)[2:].zfill(8)
    

    def char_to_matrix(self, char: str):
        '''
        Function that converts a single string character
        into an 8x8 matrix representation.
        '''
        # Get the integer representation
        representation = self.char_map[char]
        # Convert it to a 8 bit binary represtation
        expanded = [self.int_to_bin(i) for i in representation]
        # Convert binary to list: 010 -> [0,1,0]
        as_lists = [list(i) for i in expanded]
        # To array
        matrix = np.array(as_lists).astype(int)
        # Flip horizontally, because it's backwards
        matrix = matrix[:, ::-1]
        return matrix
    

    def matrix_to_output(self, matrix):
        '''
        Function that takes the 8x8 matrix representation
        and maps it to the respective positive and nagative
        space symbols.
        Then it concats the rows into singular strings.
        '''
        # Where matrix = 1 then foreground symbol, where 0
        # then background symbol
        matrix_out = np.where(matrix, self.foreground, self.background)
        arr_str_out = [''.join(i) for i in matrix_out]
        return arr_str_out
    

    def str_to_output(self, string):
        '''
        Function that takes each char in a string and
        maps it to the full 8x8 representation (with
        each matric row being a singular concatenated
        string). The function then joins the rows across
        the different characters so that the full row
        for the string is captured. Finally it joins the
        columns together with a \n so that the full
        string is represented as a nx8x8 string
        '''
        chars = [self.matrix_to_output(self.char_to_matrix(char)) for char in string]
        chars = np.array(chars)
        hrz_join = [''.join(chars[:,i]) for i in range(8)]
        vrt_join = '\n'.join(hrz_join)
        return vrt_join
    
    def handle_newline(self, string):
        '''
        We want to preserve newlines so that the print
        function actually works. So we split the string
        on all the newline characters, and then map
        each substring to the new view. Then join the
        substrings again using the newline, so that it's
        initial functionality is preserved.
        '''
        substrings = string.split('\n')
        outs = [
            self.str_to_output(substring) for substring in substrings
            if len(substring) > 0 # Ignores empty strings
        ]
        return '\n'.join(outs)

    def str_to_8x8(self, string):
        '''
        Function that calls the stuff to do the thing
        '''
        return self.handle_newline(string)