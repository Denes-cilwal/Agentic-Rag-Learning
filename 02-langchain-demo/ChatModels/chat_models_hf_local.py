from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
# the basic diff between HuggingFaceEndpoint and HuggingFacePipeline is that
# HuggingFaceEndpoint interacts with the Hugging Face Inference API,
# while HuggingFacePipeline interacts with a local model via a pipeline object.

os.environ["HF_HOME"] = "/path/to/your/huggingface/cache"  # set your huggingface cache path if needed

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs= {"max_new_tokens": 128, "temperature": 0.2},
)

chat_model = ChatHuggingFace(llm=llm)
response = chat_model.invoke("What is the capital of France?")
print(response.content)

