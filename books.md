# Books for Programmer

---

## Programming Language

### Lisp

|Name|Author|Release Date|
|:-|:-|:-|
|[How to Design Programs](https://htdp.org/)||2018|
|Structure and Interpretation of Computer Programs|||
|Land of Lisp||2010|
|Realm of Racket|||
|ANSI Common Lisp|||
|The Scheme Programming Language|||

## Games

me|Author|Release Date|
|:-|:-|:-|
|Game Engine Architecture|||

## Windows Systems

### C#

|Name|Author|Release Date|
|:-|:-|:-|
|Microsoft Visual C# Step by Step|||


## Skills

|Name|Author|Release Date|
|:-|:-|:-|
|More Joel on Software|Joel Spolsky|2008|



## Android Development & Reverse Engineering

|Name|Author|Release Date|
|:-|:-|:-|
|Embedded Android|Karim Yaghmour|2013|
|The Java Native Interface Programmer's Guide and Specification||2002|


## Computer Science

|Name|Author|Release Date|
|:-|:-|:-|
|Computer Systems: A Programmer's Perspective|Randal Bryant|2010|


## Convert books from PDF/txt to epub/azw3

We need the following tools:

 - ABBYY FineReader(ocr)
 - Calibre(convert, edit books)
 - E-Book Viewer

First, use 'FineReader' convert PDF to html.

Then copy html to text editor, edit to markdown format, you can add pictures.

Open Markdown file with `E-Book Viewer`, then you will have a better html file.

Open Calibre, add html file and convert it to epub book, edit metainfo, add cover, generate table of content, then convert to azw3 format, send it to kindle.


## Remove Text Watermark from PDF Files


Watermark is in the format `(Watermark Text) Tj`, the line start with "(" and end with "Tj". First open PDF file with vim, then can delete watermark in a PDF file with `:g/^(.*Tj$/d`.

If we have a lot pdf file, we can remove text watermark with the script below:


```sh
#/bin/bash


for fullName in *.pdf;do
    sed -i '/^(.*Tj$/d' "$fullName"
done
```

## Crop pdf files

If you wish to crop a pdf with left, top, right and bottom margins of 25, 21, 25, and 19 pt (points), then run

```sh
pdfcrop --margins '-25 -21 -25 -19' Game\ Engine\ Architecture.pdf output.pdf
```

## Convert pdf page to jpg



```sh
convert -density 300 input.pdf[66] -quality 100 output.png
```

 - PNG, JPG or (virtually) any other image format can be chosen.

 - -density xxx will set the DPI to xxx (common are 150 and 300).

 - -quality xxx will set the compression to xxx for PNG, JPG and MIFF file formates (100 means no compression).
 - [666] will convert only the 667th page to PNG (zero-based numbering so [0] is the 1st page).
