from huggingface_hub import snapshot_download
local_dir = '/data/irb/surgery/pro00114885/mistral-7b-instruct-v0.2'
snapshot_download(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    local_dir=local_dir
)
