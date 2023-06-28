[Doc Reference Link](https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/)

[Python `argparse` Doc Link](https://docs.python.org/3/library/argparse.html)

### poll custom commands

1. close a poll
```bash
python manage.py closepoll 1
```


2. delete a poll

```bash
python manage.py deletepoll --delete 1
```


#### Note -

[Management Commands Testing Doc](https://docs.djangoproject.com/en/4.1/topics/testing/tools/#topics-testing-management-commands/)

[Demo Test Example](https://github.com/satyam-seth-learnings/django_learning/blob/37f472a4752d28279eda38163cfa19d7dd19dd3b/Official%20Docs/howto/How%20to%20create%20custom%20django-admin%20commands/mysite/polls/tests.py#L135C4-L135C4)
