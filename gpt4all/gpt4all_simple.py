from fal_serverless import isolated


# Run the model in an isolated environment
@isolated(
    "virtualenv",
    requirements=["git+https://github.com/nomic-ai/pygpt4all", "huggingface_hub"],
    machine_type="L",
    keep_alive=10,  # Keep alive for 10 seconds
)
def run_basic_gpt(prompt: str) -> str:
    import os

    # Use the data directory to cache the model
    os.environ["XDG_CACHE_HOME"] = "/data/.cache"

    from huggingface_hub import hf_hub_download
    from pygpt4all.models.gpt4all import GPT4All

    data_file = hf_hub_download(
        repo_id="LLukas22/gpt4all-lora-quantized-ggjt",
        filename="ggjt-model.bin",
    )

    model = GPT4All(data_file)
    return "".join(model.generate(prompt, n_predict=10))


print(run_basic_gpt("Explain how a compiler works in layman's terms."))
