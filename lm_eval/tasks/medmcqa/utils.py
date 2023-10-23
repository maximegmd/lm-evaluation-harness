def doc_to_text(doc):
    choices = "\n".join([f'- "({k}) {v}"' for i, (k, v) in enumerate(doc["options"].items())])
    return f'''### System:
Choose the answer that best answers the question. Explain your reasoning.

### Instruction:
{doc['question']}

### Input:
- "(A) {doc['opa']}"
- "(B) {doc['opb']}"
- "(C) {doc['opc']}"
- "(D) {doc['opd']}"

### Response:

Answer: ('''

def doc_to_target(doc):
    return '' + chr(ord('A') + int(doc["cop"]))
