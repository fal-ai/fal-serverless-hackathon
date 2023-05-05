from fal_serverless import isolated, cached


# Run the model in an isolated environment
@isolated(
    "virtualenv",
    requirements=["git+https://github.com/nomic-ai/pygpt4all", "huggingface_hub"],
    machine_type="L",
    serve=True,
)
def run_basic_gpt(prompt: str) -> str:
    model = gpt()
    return "".join(
        model.generate(prompt, n_predict=10)
    )  # n_predict is the max of tokens to generate


# Cache the model in memory during keep alive to save time
@cached
def gpt():
    import os

    os.environ["XDG_CACHE_HOME"] = "/data/.cache"

    from huggingface_hub import hf_hub_download
    from pygpt4all.models.gpt4all import GPT4All

    data_file = hf_hub_download(
        repo_id="LLukas22/gpt4all-lora-quantized-ggjt",
        filename="ggjt-model.bin",
    )

    model = GPT4All(data_file)
    return model
