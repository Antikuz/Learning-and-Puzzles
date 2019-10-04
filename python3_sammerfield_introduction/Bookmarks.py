# -*- coding: utf8 -*-

import sqlite3
import Console
import os
import sys

WORDS = []


def main():
    menu_dict = dict(a=add, e=edit, l=list_bookmarks, r=remove, q=quit)
    menu = '(A)dd (E)dit (L)ist (R)emove (Q)uit [l]: '
    filename = "bookmarks.sdb"
    db = None
    try:
        db = connect(filename)
        while True:
            print("Bookmarks (" + filename + ")")
            list_bookmarks(db)
            print()
            action = input(menu)
            menu_dict[action](db)
    finally:
        if db is not None:
            db.close()


def connect(filename):
    create = not os.path.exists(filename)
    db = sqlite3.connect(filename)
    if create:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE bookmarks("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
                       "name TEXT UNIQUE NOT NULL, "
                       "site TEXT UNIQUE NOT NULL)")
        db.commit()
    return db


def add(db):
    name = Console.get_string("Name", "name")
    if not name:
        return
    site = Console.get_string("Site", "site")
    if not site:
        return
    if not site.startswith("http://") and not site.startswith("https://"):
        site = "http://" + site
    cursor = db.cursor()
    cursor.execute("INSERT INTO bookmarks (name, site) VALUES (?, ?)", (name, site))
    db.commit()
    print()


def edit(db):
    id = Console.get_integer("Number of bookmark to edit")
    if not id:
        return
    cursor = db.cursor()
    cursor.execute("SELECT name, site from bookmarks WHERE id=?", (id,))
    name, site = cursor.fetchone()
    name = Console.get_string("Name", "name", name)
    if not name:
        return
    site = Console.get_string("Site", "site", site)
    if not site:
        return
    if not site.startswith("http://") and not site.startswith("https://"):
        site = "http://" + site
    cursor.execute("UPDATE bookmarks SET name=:name, site=:site WHERE id=:id", dict(name=name, site=site, id=id))
    db.commit()
    print()

def remove(db):
    id = Console.get_integer("Number of bookmark to remove")
    if not id:
        return
    cursor = db.cursor()
    cursor.execute("SELECT name, site from bookmarks WHERE id=?", (id,))
    title = cursor.fetchone()[1]
    ans = Console.get_bool("Remove {0}?".format(title), "no")
    if ans:
        cursor.execute("DELETE FROM bookmarks WHERE id=?", (id,))
        db.commit()
    print()


def list_bookmarks(db):
    cursor = db.cursor()
    cursor.execute("SELECT id, name, site from bookmarks")
    for record in cursor:
        print("({0[0]}) {0[1]:.<31} {0[2]}".format(record))


def quit(db):
    if db is not None:
        db.commit()
        db.close()
    sys.exit()

main()

"""
Bookmarks (bookmarks.dbm)
(1) Programming in Python 3........ http://www.qtrac.eu/py3book.html
(2) PyQt........................... http://www.riverbankcomputing.com
(3) Python......................... http://www.python.org
(4) Qtrac Ltd...................... http://www.qtrac.eu
(5) Scientific Tools for Python.... http://www.scipy.org
(A)dd (E)dit (L)ist (R)emove (Q)uit [l]: e
Number of bookmark to edit: 2
URL [http://www.riverbankcomputing.com]:
Name [PyQt]: PyQt (Python bindings for GUI library)
"""