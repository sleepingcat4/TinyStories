from transformers import GPT2Model, GPT2Config

# Configuring the model for 28M param
# my code implements a 29M but still very close and you can twinker with the hidden layers to get a perfect 28M
# this code provides the method to config a model for 28M 

config = GPT2Config(
    vocab_size=50257,  # Vocabulary size of the GPT-2 model
    n_embd=240,  # Hidden size of the transformer embeddings
    n_layer=10,  # Number of transformer layers
    n_head=10,  # Number of attention heads
    n_positions=1024,  # Maximum sequence length
)

# creating the model
model = GPT2Model(config)

params = model.state_dict()

# calc the total param
total_params = sum(p.numel() for p in params.values())

# printing the number of params
print("Total Parameters:", total_params)
