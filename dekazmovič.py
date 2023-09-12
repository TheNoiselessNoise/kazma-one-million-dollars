"""
    This is a template code for a cipher at https://www.miliondolaru.cz/
    I don't know if the cipher is done more by design than by calculation.
    Original made by: https://github.com/TheNoiselessNoise

    Every other hints and more (this is not an ad and it's not me) is at: https://www.youtube.com/@pajus4/streams
"""

def text2unicodehex(text):
    return "".join([hex(ord(c))[2:] for c in text])

class Base:
    def getCodeByChar(self, ch):
        if isinstance(self, Char) and ch == self.ch:
            return self.code
        elif isinstance(self, Similars):
            filtered = list(filter(lambda c: c.ch == ch, self.chars))
            if len(filtered) > 0:
                return filtered[0].code
        return None

class Char(Base):
    def __init__(self, name, ch, code):
        self.name = name
        self.ch = ch
        self.code = code

class Similars(Base):
    def __init__(self, name, *chars):
        self.name = name # NOTE: this is like an alias
        self.chars = chars

class Characters:
    def __init__(self, *chars):
        self.chars = chars

    def getCodeByChar(self, name):
        for char in self.chars:
            code = char.getCodeByChar(name)
            if code is not None:
                return code
        return None

characters = Characters(
    # NOTE: Characters and signs got from http://xahlee.info/comp/unicode_index.html
    # every Char.name can be searched on the site when "_" -> " "

    Char('A', 'A', 0x0041), Char('B', 'B', 0x0042), Char('C', 'C', 0x0043),
    Char('D', 'D', 0x0044), Char('E', 'E', 0x0045), Char('F', 'F', 0x0046),
    Char('G', 'G', 0x0047), Char('H', 'H', 0x0048), Char('I', 'I', 0x0049),
    Char('J', 'J', 0x004A), Char('K', 'K', 0x004B), Char('L', 'L', 0x004C),
    Char('M', 'M', 0x004D), Char('N', 'N', 0x004E), Char('O', 'O', 0x004F),
    Char('P', 'P', 0x0050), Char('Q', 'Q', 0x0051), Char('R', 'R', 0x0052),
    Char('S', 'S', 0x0053), Char('T', 'T', 0x0054), Char('U', 'U', 0x0055),
    Char('V', 'V', 0x0056), Char('W', 'W', 0x0057), Char('X', 'X', 0x0058),
    Char('Y', 'Y', 0x0059), Char('Z', 'Z', 0x005A),
    
    Char('pentagram', '⛤', 0x26E4),
    Char('dollar', '$', 0x0024), # NOTE: isn't double crossed

    # plus sign
    Similars('plus_signs',
        Char('plus', '+', 0x002B),
        Char('full_width_plus', '＋', 0xFF0B),
    ),

    # circled plus or crossed out o with two lines
    Similars('x_in_o',
        Char('circle_with_superimposed_x_2', '⦻', 0x29BB),

        # NOTE: not this, because the X is inside and not reaching behind the circle
        # Char('circle_with_superimposed_x', '⊗', 0x2297),

        # NOTE: these are plus signs with circles around them
        # Char('circled_plus', '⊕', 0x2295),
        # Char('nary_circled_plus', '⨁', 0x2A01),
    ),

    # down pointing filled triangles
    Similars('down_triangle',
        Char('black_down_pointing_triangle', '▼', 0x25BC),
        Char('black_down_pointing_small_triangle', '▾', 0x25BE),
    ),

    # left pointing not filled triangles
    Similars('left_triangle',
        Char('white_left_pointing_triangle', '◁', 0x25C1),
        Char('white_left_pointing_small_triangle', '◃', 0x25C3),
    ),

    # sigmas
    Similars('sum',
        Char('greek_capital_letter_sigma', 'Σ', 0x03A3),
        Char('math_sans_serif_capital_sigma', '𝝨', 0x1D7A8),
        Char('math_sans_serif_italic_capital_sigma', '𝞢', 0x1D7E2),
    ),

    # sun
    # NOTE: maybe the use for this sign in the cipher is to represent a dot (period) to end a sentence
    Char('black_sun_with_rays', '☀', 0x2600),

    # smaller circle inside a bigger circle
    Char('circled_ring_operator', '⊚', 0x229A),

    # small i letter with a dot
    Char('latin_small_letter_i', 'i', 0x0069),

    # circle with backslash
    Similars('circle_backslash',
        Char('apl_functional_symbol_circle_backslash', '⍉', 0x2340),

        # NOTE: not this, because the backslash is inside the circle and not reaching behind it
        # Char('combining_enclosing_circle_backslash', '⃠', 0x20E0),
    ),

    # circle with a slash -> phi
    Similars('phi',
        Char('latin_small_letter_phi', 'ɸ', 0x0278),
        Char('greek_capital_letter_phi', 'Φ', 0x03A6),
        Char('greek_phi_symbol', 'ϕ', 0x03D5)
    ),

    # conjunction
    Char('conjunction', '☌', 0x260C),
)

cipher = [
    'MK⍉LXP☀Σi',
    'TS⛤K◁iU$A',
    'M+▼$TɸM⦻L',
    'X◁☌OXΣ☌AU',
    'U⊚iΣP☀⊚iP',
    '⦻S+▼☌⛤S⛤L',
    '▼O⊚◁$☀▼A◁',
    'PLΣ+⦻☌AUO',
    '⊚⦻K⍉K☌XT⦻',
    'ST⍉$M⛤O+☀'
]

hint = "9X"

if __name__ == "__main__":
    pass