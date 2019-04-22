# DesignByNumbers-alphabet

#### Studies and derivatives of Peter Cho's [Design By Numbers](https://dbn.media.mit.edu/whatisdbn.html) 26 letter alphabet

>***What is DBN?***
>
>*Design By Numbers [programming environment] was created for visual designers and artists as an introduction to computational design. It is the result of a continuing endeavor by Professor John Maeda to teach the “idea” of computation to designers and artists. It is his belief that the quality of media art and design can only improve through establishing educational infrastructure in arts and technology schools that create strong, cross-disciplinary individuals.*

As I was reading Maeda's Design By Numbers book for my master's degree about a year ago I was amazed by a set of DBN letter "commands" [written by Peter Cho](https://twitter.com/johnmaeda/status/1120021496733347840), available as a `.dbn` code file as well, so I didn't have to type them out, so I  wrote a sketch that would translate them into Processing equivalents (sort of).

Lately I  also [tried my hand with fontstruct](https://fontstruct.com/fontstructors/159258/villares) and made some derivative fonts. 


### Processing Python Mode

![sample_parse](https://raw.githubusercontent.com/villares/DesignByNumbers-alphabet/master/parse_dbn_letters/sample_parse.png)

- Code to parse the `dbnletters.dbn` file defining letter drawing functions in Processing Python Mode at execution time: [parse_dbn_letters](https://github.com/villares/DesignByNumbers-alphabet/tree/master/parse_dbn_letters)

- Code that generates, also from the `dbnletters.dbn` data, a static module [dbn_letters.py](https://github.com/villares/DesignByNumbers-alphabet/tree/master/dbn_letters_example/dbn_letters.py) for use with Processing Python Mode: [generate_dbn_letters_py](https://github.com/villares/DesignByNumbers-alphabet/tree/master/generate_dbn_letters_py) 

- An example sketch using the generated code: [dbn_letters_example](https://github.com/villares/DesignByNumbers-alphabet/tree/master/dbn_letters_example)

- Some other experiments, color strokes and a poly-shape trial: [dbn_color_and_polys](https://github.com/villares/DesignByNumbers-alphabet/tree/master/dbn_color_and_polys)

![color_and_polys_sample](https://raw.githubusercontent.com/villares/DesignByNumbers-alphabet/master/dbn_color_and_polys/color_and_polys_sample.png)

### Font derivations

![image](fontstruct.png)

- A pixel font with the same pixels: [pixels-from-DBN](https://fontstruct.com/fontstructions/show/1628742/pixels-from-dbn)

- A derivative scaleable font: [lines-from-DBN](https://fontstruct.com/fontstructions/show/1628754/)
