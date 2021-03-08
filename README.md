# Linkedin Jobs Scrapy
 Scrapy jobs requirements on linkedin with Selenium and Python.

To execute it is necessary to install the selenium library:
```
$ pip install selenium
```
After cloning or downloading the script, execute it by passing the job you want to search and the location as a parameter.

```
$ python scrapy-linkedin.py "Jobs search" "Location"
```
After execution, the `jobs_info_linkedin.csv` file will be generated with the following information:

Company | Location | Post | Description | Url
--- | --- | --- | --- | --- | 
