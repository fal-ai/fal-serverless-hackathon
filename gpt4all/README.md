# fal-serverless Example with GPT4All

In here, you will find 3 examples of how to deploy GPT4All on fal-serverless

To get started:

```bash
$ pip install fal-serverless # Installs fal-serverless
$ fal-serverless auth login # Creates an account and logs in to fal-serverless

$ git clone git@github.com:fal-ai/fal-serverless-hackathon.git

$ cd fal-serverless-hackathon/gpt4all

$ python gpt4all_simple.py
```

The `gpt4all_simple.py` example is the most basic way of running gpt4all on fal-serverless. It takes in a prompt and returns a completion.
You can call this function as if it's a local function.

`gpt4all_cached.py` introduces the `cached` decorator that allows you to cache the results of a function. This is useful if you want to cache the results of a function that takes a long time to run. In this case, the model instance can be cached.

`gpt4all_served.py` introduces the `serve` attribute that turns an isolated function into a web endpoint. With this, you can call a function as a RESTful endpoint. This endpoint will autoscale.
