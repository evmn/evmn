# Crop pdf files

If you wish to crop a pdf with left, top, right and bottom margins of 25, 21, 25, and 19 pt (points), then run

```sh
pdfcrop --margins '-25 -21 -25 -19' Game\ Engine\ Architecture.pdf output.pdf
```

# Convert pdf page to jpg


```sh
convert -density 300 input.pdf[66] -quality 100 output.png
```

 - PNG, JPG or (virtually) any other image format can be chosen.

 - -density xxx will set the DPI to xxx (common are 150 and 300).

 - -quality xxx will set the compression to xxx for PNG, JPG and MIFF file formates (100 means no compression).
 - [666] will convert only the 667th page to PNG (zero-based numbering so [0] is the 1st page).

