# TEXT-SUMMARIZATION-TOOL

*COMPANY* : CODETECH IT SOLUTIONS

*NAME* :  NAGISETTY HEMANTH SAI

*INTERN ID* : CT04DG2507

*DOMAIN* : AI(ARTIFICIAL INTELLIGENCE)

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH

# DESCRIPTION OF THE PROJECT

This project is all about building a simple and effective tool that can automatically summarize long pieces of text. It uses a powerful, pre-trained language model called `t5-small` from Hugging Face’s Transformers library. This model was originally created by Google as part of their T5 (Text-To-Text Transfer Transformer) framework, which treats every language task—like translation, summarization, or answering questions—as a text-in, text-out problem.

The idea is to help people quickly get the main points of a long article or paragraph without having to read through everything. This is especially useful for students, professionals, or anyone who regularly deals with large volumes of written content. Instead of spending several minutes or hours reading, you can get a compact summary in seconds.

The script itself is straightforward. It starts by importing the necessary tools: the tokenizer and model from the Transformers library, and PyTorch (through the `torch` library), which helps run the model. The tokenizer’s job is to convert the input text into a format the model can understand—basically numbers—and later convert the model’s output back into readable text.

There’s a single function called `summarize()` that handles the entire summarization process. First, it prepares the text by adding the prefix “summarize:” at the beginning. This lets the model know that the task is summarization. It also cleans up the text a bit by removing extra spaces and newlines.

Once the input is ready, it’s tokenized and passed into the model. The model then generates a shorter version of the input using a method called beam search, which helps it choose the best possible output. Parameters like maximum and minimum summary length, beam width, and a length penalty help control how the summary is generated—ensuring that it's concise, clear, and doesn’t miss important information.

After generating the summary, the script decodes the model’s output back into human-readable text and prints it alongside the original. So, when you run the script, you get to see both the full input paragraph and the summarized version for comparison.

The sample paragraph included in the script talks about artificial intelligence—what it is, how it’s categorized, and where it’s being used today. When the tool summarizes it, you get a clear, shortened version that still covers all the key ideas.

To use this tool, all you need is Python and a few libraries: `transformers` and `torch`. These can be installed with simple pip commands. The summarization runs entirely on your machine, and works well even without a high-end GPU, though it will run faster with one.

What makes this tool valuable is how little effort is needed to make it work. You don’t need to train any models, label data, or do complex programming. It’s ready to use out of the box. By combining clean code, pre-trained models, and user-friendly libraries, the tool demonstrates the real-world power of modern NLP with minimal setup—making it perfect for learning, experimenting, or even building into larger applications.

# OUTPUT

# Original Text
Artificial Intelligence is a branch of computer science that aims to create machines that can perform tasks that typically require human intelligence. These tasks include reasoning, learning, problem-solving, perception, and language understanding. AI is categorized into narrow AI, which is designed to perform a narrow task, and general AI, which performs any intellectual task a human can. AI techniques include machine learning, deep learning, and natural language processing. Over the years, AI has been integrated into various sectors such as healthcare, finance, automotive, and customer service. It helps improve productivity, reduce human error, and automate repetitive tasks. However, the ethical implications and potential job displacement caused by AI continue to be major concerns among policymakers and researchers.

# Summarized Text

Artificial Intelligence (AI) is a computer science field focused on creating machines that perform tasks requiring human intelligence. It includes narrow and general AI, with applications in healthcare, finance, and more. AI improves productivity and automation but raises ethical and employment concerns.


