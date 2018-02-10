#!/usr/bin/env python3
# Copyright (c) 2008 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import sys
import xml.sax.saxutils


def main():
    option = process_option()
    if option[0] is None and option[1] is None:
        return
    maxwidth = option[0]
    format_num = option[1]
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"
            print_line(line, color, maxwidth,format_num)
            count += 1
        except EOFError:
            break
    print_end()


def print_start():
    print("<table border='1'>")


def print_line(line, color, maxwidth,format_num):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:{1}}</td>".format(round(x),format_num))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = xml.sax.saxutils.escape(field)
                else:
                    field = "{0} ...".format(
                            xml.sax.saxutils.escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c    # other quote inside quoted string
            continue
        if quote is None and c == ",": # end of a field
            fields.append(field)
            field = ""
        else:
            field += c        # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields


def print_end():
    print("</table>")

def process_option():
    option = [None, None]
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print ("{0:}".format("csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html"
                "\nmaxwidth – необязательное целое число. Если задано, определяет "
                "максимальное число символов для строковых полей. \nВ противном случае "
                "используется значение по умолчанию 100."
                "\nformat – формат вывода чисел. Если не задан, по умолчанию используется "
                'формат ".0f".'))
    else:
        option = [100,".0f"]
    if "maxwidth=" in sys.argv[1]:
        option[0] = int(sys.argv[1][sys.argv[1].rfind("=")+1:])
    if "format=" in sys.argv[2]:
        option[1] = sys.argv[2][sys.argv[2].rfind("0")+1:] 
    return option

    
main()
