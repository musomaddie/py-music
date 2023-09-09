# < measure
# number = "1"
# width = "234" >
# < print
# new - page = "yes" >
# < system - layout >
# < system - margins >
# < left - margin > 131 < / left - margin >
# < right - margin > 0 < / right - margin >
# < / system - margins >
# < top - system - distance > 218 < / top - system - distance >
# < / system - layout >
# < measure - layout >
# < measure - distance > 50 < / measure - distance >
# < / measure - layout >
# < / print >
# < attributes >
# < divisions > 256 < / divisions >
# < key
# color = "#000000" >
# < fifths > -2 < / fifths >
# < mode > major < / mode >
# < / key >
# < time
# color = "#000000" >
# < beats > 4 < / beats >
# < beat - type > 4 < / beat - type >
# < / time >
# < staves > 1 < / staves >
# < clef
# number = "1"
# color = "#000000" >
# < sign > G < / sign >
# < line > 2 < / line >
# < / clef >
# < staff - details
# number = "1"
# print - object = "yes" / >
# < / attributes >
# < harmony
# color = "#000000" >
# < root >
# < root - step > E < / root - step >
# < root - alter > -1 < / root - alter >
# < / root >
# < kind > major - ninth < / kind >
# < frame
# default - y = "25"
# valign = "bottom" >
# < frame - strings > 6 < / frame - strings >
# < frame - frets > 5 < / frame - frets >
# < frame - note >
# < string > 4 < / string >
# < fret > 1 < / fret >
# < / frame - note >
# < frame - note >
# < string > 3 < / string >
# < fret > 0 < / fret >
# < / frame - note >
# < frame - note >
# < string > 2 < / string >
# < fret > 3 < / fret >
# < / frame - note >
# < frame - note >
# < string > 1 < / string >
# < fret > 1 < / fret >
# < / frame - note >
# < / frame >
# < staff > 1 < / staff >
# < / harmony >
# < direction >
# < direction - type >
# < words
# relative - y = "25"
# justify = "left"
# valign = "middle"
# font - family = "Quicksand SemiBold"
# font - style = "normal"
# font - size = "12.5566"
# font - weight = "normal" > Moderately < / words >
# < / direction - type >
# < voice > 1 < / voice >
# < staff > 1 < / staff >
# < / direction >
# < direction
# directive = "yes" >
# < direction - type >
# < metronome
# color = "#000000"
# font - family = "Quicksand SemiBold"
# font - style = "normal"
# font - size = "12.5566"
# font - weight = "normal" >
# < beat - unit > quarter < / beat - unit >
# < per - minute > 100 < / per - minute >
# < / metronome >
# < / direction - type >
# < voice > 1 < / voice >
# < staff > 1 < / staff >
# < / direction >
# < note
# default - x = "110" >
# < rest / >
# < duration > 1024 < / duration >
# < instrument
# id = "P1-I1" / >
# < voice > 1 < / voice >
# < type > whole < / type >
# < staff > 1 < / staff >
# < / note >
# < / measure >

"""
Bar (children)
- attrib (in line)
    - number
    - width
- print info things
- attributes
    - divisions
    - key
        - fifths
        - mode
    - time
        -beats
        -beat type
    - staves
    - clef (number, color)
        - sign, line
    - staff details
- harmony (color)
    - root
        - step, alter
    - kind
    - frame
        - strings, frets, note, staff
- direction
    - type, (words)
    - voice, staff
- direction (directive)
- note


"""
pass
