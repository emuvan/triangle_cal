class triangle:
    
    
    
    # creating an new instance of the triangle class and the self within the parameter represent the instance itself and it is a constructor as well.
    def __init__(self, product, origin_year, development_year, incremental_value):
        self.product = product
        self.origin_year = origin_year
        self.development_year = development_year
        self.incremental_value = incremental_value
    
    """    
    Formatted string literals which let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.
     it is returning all the self.product, self.origin_year, self.development_year, and self.incremental_value
    
     """
    def __repr__(self):
        return f"{self.product} |{self.origin_year} |{self.development_year} |{self.incremental_value}"

    """
    giving out the result the total value from the self.incremental_value + other.__incremental_value by the addition operator
    """

    def __add__(self, other):
        return self.incremental_value + other.__incremental_value
