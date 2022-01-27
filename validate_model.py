

from transformers import AutoTokenizer,TFBertModel
from bert_model import prepare_model
tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')

new_model =  prepare_model()

texts = input(str('input the text'))
x_val = tokenizer(
    text=texts,
    add_special_tokens=True,
    max_length=15,
    truncation=True,
    padding='max_length', 
    return_tensors='tf',
    return_token_type_ids = False,
    return_attention_mask = True,
    verbose = True) 
prediction = new_model.predict({'input_ids':x_val['input_ids'],'attention_mask':x_val['attention_mask']})
print(prediction)