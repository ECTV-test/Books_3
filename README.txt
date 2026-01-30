Book Reader Prototype (folder-based catalog + plain text books)

STRUCTURE
- index.html
- books/
  - index.json                 (catalog list, can be auto-generated)
  - <book-id>/
    - book.json                (metadata)
    - book.txt                 (plain text; paste your book as-is)
    - cover.jpg                (cover image)
    - audio.mp3 (optional)

ADD A NEW BOOK (recommended)
1) Copy any folder inside /books/ as a template.
2) Rename folder to your new id (e.g. my-book).
3) Edit /books/my-book/book.json (title, level, description, etc.)
4) Paste the full book into /books/my-book/book.txt (no JSON quoting needed).
5) Replace /books/my-book/cover.jpg
6) Run:  python3 tools/generate_index.py
   This regenerates /books/index.json automatically.

MODES
- "Слухати" -> original reader mode (word-level highlight + tap-to-translate)
- "Читати"  -> line-by-line mode (original line + translated line under it)
  Settings: you can hide/show translated line. Tap-to-translate is disabled.

DEFAULTS
- Speed default is 0.70×
