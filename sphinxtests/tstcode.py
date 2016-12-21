# 12/21/2016
# MSSG


"""This class is a rather simplistic example, to just start learning the ropes of autodoc in sphinx."""

# Orig From: http://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html

class ClassNumUno(object):
    """This class docstring shows how to use sphinx and rst syntax

    The first line is generally a brief explanation, which can be added to later.
    
    The methods here are :func:`func1` and :func:`multfunc`. 

    - The doctest in the main method tests the docstring examples in the code vs. what they say they do, and will actually give output if run with a verbose flag as so:

          python tstcode.py -v

    - **parameters**, **types**, **return** and **return types**::

          :param arg1: any number (floats are specified by a decimal after)
          :param arg2: any number
          :param arg3: any number
          :return: (arg1 / arg2) + arg3 

    .. note::
        There are many other Info fields but they may be redundant:
            * param, parameter, arg, argument, key, keyword: Description of a
              parameter.
            * type: Type of a parameter.
            * raises, raise, except, exception: For when a specific
              exception is raised.
            * var, ivar, cvar: Description of a variable.
            * returns, return: Description of the return value.
            * rtype: Return type.

    Here below are the results of the :func:`func1` docstring.

    """

    def func1(self, arg1, arg2, arg3):
        """returns (arg1 / arg2) + arg3

        This is a longer explanation, which may include math with latex syntax
        :math:`\\alpha`, :math:`\\beta`  and such.


        :Example:

        >>> import tstcode
        >>> a = tstcode.ClassNumUno()
        >>> a.func1(1,1,1)
        2

        .. note:: can be useful to emphasize
            important features
        .. warning:: arg2 must be non-zero.
        .. todo:: check that arg2 is non zero.
        """
        return arg1/arg2 + arg3


    def multfunc(self, arg1, arg2):
        """returns (arg1 * arg2)

        :Example:

        >>> import tstcode
        >>> a = tstcode.ClassNumUno()
        >>> a.multfunc(4,5)
        20

        """
        return arg1*arg2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
