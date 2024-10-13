import string

def excel_column_to_index(column):
    """
    Convert an Excel-style column (e.g., G) to a 1-based index (G -> 7).
    """
    index = 0
    for i, char in enumerate(reversed(column.upper())):
        index += (ord(char) - 64) * (26 ** i)
    return index

def generate_index_formula(cell_reference, base_column="G"):
    """
    Convert a cell reference like 'Required Hours'!G7 to an INDEX formula.
    """
    # Extract the column and row from the cell reference
    column = ''.join([char for char in cell_reference if char.isalpha()])
    ref_row = ''.join([char for char in cell_reference if char.isdigit()])
    
    # Convert the base and current columns to indices
    base_index = excel_column_to_index(base_column)
    current_index = excel_column_to_index(column)
    
    # Calculate the offset for the INDEX formula (equivalent to Dashboard!AC50 - 6)
    offset = current_index - base_index + 6  # +6 to reverse the earlier subtraction
    
    # Return the generated INDEX formula
    return f"=INDEX('Required Hours'!{base_column}{ref_row}:BZ{ref_row}, 1, (Dashboard!AC50 - {6 - offset}))"

def convert_formula(formula):
    """
    Check if the formula is a simple reference or a sum of references,
    and convert accordingly.
    """
    if "+" in formula:
        # If it's a sum of multiple cell references
        parts = formula.split("+")
        converted_parts = [generate_index_formula(part.strip()) for part in parts]
        return " + ".join(converted_parts)
    else:
        # If it's a single cell reference
        return generate_index_formula(formula)

def process_formula_list(formula_list):
    """
    Iterate through a list of formulas and generate converted INDEX formulas.
    """
    for formula in formula_list:
        converted_formula = convert_formula(formula)
        print(f"Original: {formula} -> Converted: {converted_formula}")

# Example list of formulas to convert (includes both single references and summations)
formula_list = [
    "'Required Hours'!G7", "'Required Hours'!H7", "'Required Hours'!I7", 
    "'Required Hours'!J7", "'Required Hours'!K7", "'Required Hours'!L7",
    "'Required Hours'!G22+'Required Hours'!G36", "'Required Hours'!H22+'Required Hours'!H36",
    "'Required Hours'!I22+'Required Hours'!I36", "'Required Hours'!J22+'Required Hours'!J36",
    "'Required Hours'!K22+'Required Hours'!K36", "'Required Hours'!L22+'Required Hours'!L36",
    "'Required Hours'!G51+'Required Hours'!G65+'Required Hours'!G79", 
    "'Required Hours'!H51+'Required Hours'!H65+'Required Hours'!H79", 
    "'Required Hours'!I51+'Required Hours'!I65+'Required Hours'!I79", 
    "'Required Hours'!J51+'Required Hours'!J65+'Required Hours'!J79", 
    "'Required Hours'!K51+'Required Hours'!K65+'Required Hours'!K79", 
    "'Required Hours'!L51+'Required Hours'!L65+'Required Hours'!L79",
    "'Required Hours'!G94", "'Required Hours'!H94", "'Required Hours'!I94", 
    "'Required Hours'!J94", "'Required Hours'!K94", "'Required Hours'!L94"
]

# Process the list and print each result
process_formula_list(formula_list)


=INDEX('Required Hours'!G7:BB7, 1, (Dashboard!AC50 - 6))	=INDEX('Required Hours'!H7:BC7, 1, (Dashboard!AC50 - 6))	=INDEX('Required Hours'!I7:BD7, 1, (Dashboard!AC50 - 6))	=INDEX('Required Hours'!J7:BE7, 1, (Dashboard!AC50 - 6))	=INDEX('Required Hours'!K7:BF7, 1, (Dashboard!AC50 - 6))	=INDEX('Required Hours'!L7:BG7, 1, (Dashboard!AC50 - 6))




=INDEX('Required Hours'!G94:B49, 1, (Dashboard!AC50 - 6)) + =INDEX('Required Hours'!G94:BB94, 1, (Dashboard!AC50 - 6))

=INDEX('Required Hours'!G51:BB51, 1, (Dashboard!AC50 - 6)) + INDEX('Required Hours'!G65:BB65, 1, (Dashboard!AC50 - 6)) + INDEX('Required Hours'!G79:BB79, 1, (Dashboard!AC50 - 6))
='Required Hours'!G51+'Required Hours'!G65+'Required Hours'!G79


 

=INDEX('Required Hours'!G60:BB60, 1, (Dashboard!AC50 - 6)) + INDEX('Required Hours'!G74:BB74, 1, (Dashboard!AC50 - 6)) + INDEX('Required Hours'!G88:BB88, 1, (Dashboard!AC50 - 6))
=INDEX('Required Hours'!G61:BB61, 1, (Dashboard!AC50 - 6)) + INDEX('Required Hours'!G75:BB75, 1, (Dashboard!AC50 - 6)) + INDEX('Required Hours'!G89:BB89, 1, (Dashboard!AC50 - 6))
=INDEX('Required Hours'!G62:BB62, 1, (Dashboard!AC50 - 6)) + INDEX('Required Hours'!G76:BB76, 1, (Dashboard!AC50 - 6)) + INDEX('Required Hours'!G70:BB70, 1, (Dashboard!AC50 - 6))
=INDEX('Required Hours'!G63:BB63, 1, (Dashboard!AC50 - 6)) + INDEX('Required Hours'!G77:BB77, 1, (Dashboard!AC50 - 6)) + INDEX('Required Hours'!G71:BB71, 1, (Dashboard!AC50 - 6))