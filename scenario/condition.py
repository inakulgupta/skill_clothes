from asyncio.windows_events import NULL
from df_engine.core import Context, Actor
import re
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')
prepModel=NULL

def buying_clothes(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    if prepModel:
        x_val = tokenizer(
            text=ctx.last_request,
            add_special_tokens=True,
            max_length=15,
            truncation=True,
            padding='max_length', 
            return_tensors='tf',
            return_token_type_ids = False,
            return_attention_mask = True,
            verbose = True) 
        validation = prepModel.predict({'input_ids':x_val['input_ids'],'attention_mask':x_val['attention_mask']})          
        return max(validation[0])>0.5 and validation[0][0]==max(validation[0])
    else:
        return False

def dry_cleaning(ctx: Context, actor: Actor, *args, **kwargs) -> bool:    
    if prepModel:
        x_val = tokenizer(
            text=ctx.last_request,
            add_special_tokens=True,
            max_length=15,
            truncation=True,
            padding='max_length', 
            return_tensors='tf',
            return_token_type_ids = False,
            return_attention_mask = True,
            verbose = True) 
        validation = prepModel.predict({'input_ids':x_val['input_ids'],'attention_mask':x_val['attention_mask']})   
        
        return max(validation[0])>0.5 and validation[0][1]==max(validation[0])
    else:
        return False

def custom_tailoring(ctx: Context, actor: Actor, *args, **kwargs) -> bool:    
    if prepModel:
        x_val = tokenizer(
            text=ctx.last_request,
            add_special_tokens=True,
            max_length=15,
            truncation=True,
            padding='max_length', 
            return_tensors='tf',
            return_token_type_ids = False,
            return_attention_mask = True,
            verbose = True) 
        validation = prepModel.predict({'input_ids':x_val['input_ids'],'attention_mask':x_val['attention_mask']})           
        return  max(validation[0])>0.5 and validation[0][2]==max(validation[0])
    else:
        return False    

def fallback(ctx: Context, actor: Actor, *args, **kwargs) -> bool:    
    if prepModel:
        x_val = tokenizer(
            text=ctx.last_request,
            add_special_tokens=True,
            max_length=15,
            truncation=True,
            padding='max_length', 
            return_tensors='tf',
            return_token_type_ids = False,
            return_attention_mask = True,
            verbose = True) 
        validation = prepModel.predict({'input_ids':x_val['input_ids'],'attention_mask':x_val['attention_mask']})    
           
        return  max(validation[0])<=0.5
    else:
        return False        