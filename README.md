### Pyupdate is an easy to use utility to update your Python installation quickly via bash/shell
#### NOTE: Pyupdate is only compatible with MacOS at the time of writing. I plan to give support to other operating systems soon.
#### Usage
```shell
$ pyupdate
```

#### How it works
```python
'File: .pyupdate.py'
```
- First, rather than scraping the Python Download's site from the installer, I created a custom server that scrapes it with BeatifulSoup4 and Python Requests, and gets the installer package for the current OS, which the program requests (This makes it over 25 times faster than simply scraping locally). \
(I did this rather than just getting the MacOS installer because of possible compatibility with other operating systems in the future)
- Next, using Python's built-in file I/O system, the script creates an empty file called `python.pkg`, and inserts the update's metadata into it using the file info from the previous step
- Thirdly, using Python's OS module, the script runs the following code:
```bash
$ sudo installer -pkg ' + pkg + ' -target /usr/local/bin/python3
```
(pkg is the downloaded package file)
- Finally, at the time of completion, Python is updated.
