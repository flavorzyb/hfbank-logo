#!/bin/sh
/opt/scrapy/bin/coverage run /opt/scrapy/bin/pytest tests
/opt/scrapy/bin/coverage html
