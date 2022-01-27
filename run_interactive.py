
import logging
import time
from typing import Optional, Union
import re
from scenario.plot import actor
from df_engine.core import Actor, Context
from annotators.main import annotate
from bert_model import prepare_model
import scenario.condition as cust_cnd
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

logger = logging.getLogger(__name__)



def turn_handler(
    in_request: str,
    ctx: Union[Context, str, dict],
    actor: Actor,
    true_out_response: Optional[str] = None,
):
   
    ctx = Context.cast(ctx)

    
    ctx.add_request(in_request)
    ctx = annotate(ctx)

    
    ctx = actor(ctx)
  
    out_response = ctx.last_response
    
    if true_out_response is not None and true_out_response != out_response:        
        raise Exception(f"{in_request} -> true_out_response != out_response: {true_out_response} != {out_response}")
    else:
        print(f"-> {out_response}")
    return out_response, ctx


def run_interactive_mode(actor):

    ctx = {}
    while True:
        in_request = input("type your answer: ")
        _, ctx = turn_handler(in_request, ctx, actor)

if __name__ == "__main__":
    ctx = {}
    print("Training model")
    cust_cnd.prepModel = prepare_model()
    print("Training model complited")
    clearConsole()
   
    logging.basicConfig(
        format="%(asctime)s-%(name)15s:%(lineno)3s:%(funcName)20s():%(levelname)s - %(message)s", level=logging.INFO
    )
    
    run_interactive_mode(actor)