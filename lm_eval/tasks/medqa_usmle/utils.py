import datasets

def doc_to_text(doc):
    choices = "\n".join([f'- "({k}) {v}"' for i, (k, v) in enumerate(doc["options"].items())])
    return f'''### System:
Choose the answer that best answers the question. Explain your reasoning.

### Instruction:
{doc['question']}

### Input:
{choices}

### Response:

Answer: ('''

def doc_to_target(doc):
    return "{}".format(doc["answer_idx"])

def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    #dataset = dataset.select(range(1))
    return dataset

def gold_alias(doc):
    return ord(doc["final_decision"]) - ord("A")
