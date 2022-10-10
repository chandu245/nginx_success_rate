# nginx_success_rate
This python script calculates the success rate of your nginx logs.

You can exclude common error codes in if condition to get accurate results, currently 304 and 200 are considered as success.

Make sure nginx access logs are in the default format, if any other format you may have to make changes to the regex.
