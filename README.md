# Repro

```
# get venv
python -m venv venv
source venv/bin/activate
# install deps
pip install -r requirements.txt
# run repro
python repro.py
# check highting in the doc out-pypdf.pdf out-pypdf2.pdf
```

Output
```
Traceback (most recent call last):
  File "repro.py", line 5, in <module>
    page.extract_text()
  File "/Users/sergei.vorobev/src/pypdf-text-parsing-repro/venv/lib/python3.7/site-packages/pypdf/_page.py", line 2266, in extract_text
    visitor_text,
  File "/Users/sergei.vorobev/src/pypdf-text-parsing-repro/venv/lib/python3.7/site-packages/pypdf/_page.py", line 1901, in _extract_text
    cmaps[f] = build_char_map(f, space_width, obj)
  File "/Users/sergei.vorobev/src/pypdf-text-parsing-repro/venv/lib/python3.7/site-packages/pypdf/_cmap.py", line 30, in build_char_map
    space_width, ft
  File "/Users/sergei.vorobev/src/pypdf-text-parsing-repro/venv/lib/python3.7/site-packages/pypdf/_cmap.py", line 54, in build_char_map_from_dict
    map_dict, space_code, int_entry = parse_to_unicode(ft, space_code)
  File "/Users/sergei.vorobev/src/pypdf-text-parsing-repro/venv/lib/python3.7/site-packages/pypdf/_cmap.py", line 240, in parse_to_unicode
    int_entry,
  File "/Users/sergei.vorobev/src/pypdf-text-parsing-repro/venv/lib/python3.7/site-packages/pypdf/_cmap.py", line 310, in process_cm_line
    multiline_rg = parse_bfrange(line, map_dict, int_entry, multiline_rg)
  File "/Users/sergei.vorobev/src/pypdf-text-parsing-repro/venv/lib/python3.7/site-packages/pypdf/_cmap.py", line 369, in parse_bfrange
    ] = unhexlify(fmt2 % c).decode("utf-16-be", "surrogatepass")
binascii.Error: Odd-length string
```
