# PACInterview
Crawler of Microsoft Academic and Google Scholar implemented with python
###  1. Microsoft Academic Crawler
Use python to build a crawler for the following website
```
$ python3 MSSpider.py
```

### 2. Microsoft Academic API (POST way)
Pack Q1 function as an API(POST way) in flask framework
- Step 1. Run server
    ```
    $ python3 MSapi.py
    ```
 - Step 2. Send POST request in the folloing format
    > <p>Format: http://127.0.0.1:8000/msscholar/<query></p>
    > <p>Example : http://127.0.0.1:8000/msscholar/Fin10K</p>
### 3. Google Scholar Crawler
<p>Use python to build a crawler for the following website</p>

** (NOTE): This function cannot crawl target page because it will be detected as ROBOT.
It only implements a parser part. **

```
$ python3 GoogleScholarSpider.py GoogleSchlar_sample_file.html
```

### 4. free text mining.txt parser
Parse the paper titles form attachment file "free text mining.txt"
```
$ python3 free_text_parser.py [target_file]
```
Example Usage:
```
$ python3 free_text_parser.py free_text_mining.txt
```

### 5. Question
Show the answer in file "5_answer.txt"
# pythonCrawlers
