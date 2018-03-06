# Dr. Varshney Website
* Written in Python + Markdown + HTML
* Deployed site is located at http://www.cs.umd.edu/~varshney

## Short Edit
* Just clone the repo, make tiny edits, and run:
```bash
python build.py
```
to rebuild all html files
* Commit and push
```bash
git add -A
git commit -m "documentation of your modification"
git push
```
* DONE!

## Long Edit
* First, clone this repo, and create your own branch of this:
```bash
git clone git@github.com:AugmentariumLab/VarshneyWebsite.git
git branch feature-your-branch-name
```
* Then edit data/students.json and data/papers.json
* You may want to put new teaser images and paper preprints under teaser/ and papers/
* (optional) Run:
```bash
python build.py
```
* Commit and push
```bash
git add -A
git commit -m "documentation of your modification"
git push
```
* Send a pull request to the main branch
* DONE!

## Students
* All students are structured as JSON objects now so it's easier to add new people or hide people
* For example:
```json
{
    "url": "http://www.duruofei.com",
    "photo": "RuofeiDu.jpg",
    "name": "Ruofei Du",
    "title": "Ph.D. Student",
    "category": "Graduate Students",
    "time": "",
    "visible": true,
    "tags": "GVIL,Augmentarium",
    "department": "Computer Science",
    "current": "University of Maryland",
    "year": 2013
}
```

## Publications
* Every paper is structured as JSON objects now, so it's easier to generate BibTeX, change visualization, and add filters in the future:
```json
{
    "bibname": "HsuehChien2018Winnow",
    "url": "https://dl.acm.org/citation.cfm?id=3107449",
    "title": "Winnow: Interactive Visualization of Temporal Changes in Multidimensional Clinical Data",
    "bib": "",
    "author": "Hsueh-Chien Cheng, Antonio Cardone, and Amitabh Varshney",
    "type": "article",
    "booktitle": "Proceedings of IEEE International Conference on Image Processing, 2017",
    "attr": "",
    "pages": "",
    "year": "2018",
    "month": "",
    "day": "",
    "series": "",
    "book_title_short": "",
    "editor": "",
    "isbn": "",
    "numpages": 1,
    "doi": "",
    "publisher": "",
    "address": "",
    "location": "",
    "volume": 1,
    "number": 1,
    "keywords": "",
    "note": "",
    "citations": "",
    "published": true,
    "visible": true,
    "poseter": "",
    "video": "",
    "youtube": "",
    "vimeo": "",
    "code": "",
    "slides": "",
    "talk": "",
    "award": "",
    "abstract": "",
    "image": "HsuehChien2018Winnow.png",
    "supple": "",
    "categories": ""
}
```
