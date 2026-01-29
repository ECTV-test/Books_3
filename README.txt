Book Reader Prototype (folder-based catalog)

STRUCTURE
- index.html
- books/
  - index.json               (catalog list)
  - <book-id>/
    - book.json              (full book)
    - cover.jpg              (cover image)
    - audio.mp3 (optional)   (if you add later)

HOW TO ADD A NEW BOOK
1) Copy any folder inside /books/ as a template.
2) Rename folder to your new id (e.g. my-book).
3) Edit /books/my-book/book.json (title, text, etc.)
4) Replace /books/my-book/cover.jpg
5) Add one item into /books/index.json with the same id.
   You can omit "cover" there: the app will auto-use books/<id>/cover.jpg

NOTE (GitHub Pages)
GitHub Pages can't list folders automatically, so index.json is required.
