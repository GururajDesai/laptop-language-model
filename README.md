## Local Language Model

Run llm model locally and interact with it like we do with ChatGPT/Bard/Bing/etc

### Main Features:

1. If you're interested in exploring or building ChatGPT-like applications, this repository is a valuable resource.

2. It's particularly well-suited for those with limited resources, such as laptops with 4GB of RAM or no dedicated graphics card (GPU).

### Simple steps to run a language model locally:

1. Clone this repository to your local machine.
2. Create virtual environment -> download virtualenv package

```py
    python3 -m venv venv_laptop_language_model
```

3. Activate the virtual environment

```py
    source venv_laptop_language_model/bin/activate
```

4. Install dependencies

```py
    pip3 install -r requirements.txt
```

5. Download the folder "LaMini-Flan-T5-248M" and model "pytorch_model.bin" from the Hugging Face Model Hub: https://huggingface.co/MBZUAI/LaMini-Flan-T5-248M. Because cloning from huggingface will not download the model only downloads the pointer to the file.

6. Execute the run.py script to start the language model -> Only runs using transformers package
   ```py
       python3 run.py
   ```
7. Execute the run_langchain_from_local.py -> if you want to use langchain
   ```py
       python3 run_langchain_from_local_model.py
   ```
8. Execute the run_langchain_from_remote.py -> if you do not want to download the model file prior to running this.

   ```py
   python3 run_langchain_from_remote_model.py
   ```

   ```

   ```

### More resources ? Want to try bigger models ?

You can have look for models of the same variant here: https://huggingface.co/MBZUAI/LaMini-Flan-T5-248M
