Repository contains code to config a 28M param GPT-2 model to train it on tinystories dataset like the TinyStories paper. In the paper, they used several variations of **GPT-2** and **GPT-Neo** model, but **GPT-2** was the spotlight version. They tried to show you can create a SLM (Small Language Model) upto which small size params until it makes sense and compete against LLMs. 

I am only providing the code to config a 28M model as transformers currently having a problem to install my favourite version `transformers==4.2.2` and new transformers requires accelerate if you're using pytorch and requires `partial state` I am not sure how you resolve the partial state error at least now. But, I wanted the method to config a 28M model asap! Which is why, I am only providing the config code. Will later update the repo to add training code. 

Upcoming updates:
* Providing training script
* ~~providing TinyStories dataset in `.txt` format~~

Dataset:
TinyStories dataset had two part ```1. GPT-3.5 Turbo generated dataset`` and ``2.GPT-4 generated dataset`` Including both will take a hue amount of space that's why, I am giving only **GPT-3.5 Turbo** dataset. [Google Drive Link](https://drive.google.com/drive/folders/12ZeAVOzuk3W_R0pBr-fXQkbTP_WRJUEx?usp=sharing)

**In the Google Drive link provided in the datasets section, you find both GPT-3.5 (Turbo) and GPT-4 datasets used by the paper's autors'**

Please, star the repository if you find it helpful and help others to find it. [Paper Link](https://arxiv.org/abs/2305.07759)
