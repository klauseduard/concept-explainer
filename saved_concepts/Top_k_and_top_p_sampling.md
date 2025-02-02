### Explanation:

**Top-k Sampling:** In top-k sampling, you select the top k most likely tokens from a probability distribution and sample from only those k tokens. This helps in focusing on the most probable options and can improve the quality of generated text.

**Top-p Sampling:** In top-p sampling, also known as nucleus sampling, you select the smallest set of tokens whose cumulative probability exceeds a certain threshold p. Then, you sample from this reduced set of tokens. This method allows for dynamic selection of tokens based on their probabilities.

### Follow-up Questions:

1. **How do top-k and top-p sampling differ in practice?**
   - Top-k sampling selects a fixed number of tokens, while top-p sampling selects a dynamic set based on probability threshold.

2. **Can you provide an example of when to use each sampling method?**
   - For creative text generation, top-p sampling can introduce more diversity, while top-k sampling can ensure coherence in language generation tasks.

### Examples:

- **Top-k Sampling Example:**
  - Given a probability distribution over words, if we set k=5, we would sample from the top 5 most likely words.

- **Top-p Sampling Example:**
  - If we set p=0.9, we would select tokens until the cumulative probability exceeds 0.9 and then sample from this reduced set.

### Etymology and History:

The terms "top-k" and "top-p" sampling originated in the field of natural language processing and have gained popularity in the context of neural language models. They are commonly used in tasks like text generation and machine translation to improve the quality and diversity of generated text.

### Summary:

In summary, top-k sampling focuses on the most likely tokens, while top-p sampling dynamically selects tokens based on a probability threshold. Understanding these sampling methods can help improve the performance of language models in various text generation tasks.

### See also:

- [Beam Search](?concept=beam+search&specialist_role=language+model+researcher&target_audience=software+engineer)
- [Greedy Decoding](?concept=greedy+decoding&specialist_role=language+model+researcher&target_audience=software+engineer)