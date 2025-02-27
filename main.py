import openai
from dotenv import load_dotenv
import time
import logging
from datetime import datetime

load_dotenv()

client = openai.OpenAI()
model = "gpt-3.5-turbo-16k"

#--- Create our Assistant ---
# personal_trainer_assis = client.beta.assistants.create(
#     name="Pesonal Trainer",
#     instructions="""You are the best personal trainer and nutritionist 
#     who knows everything about food and build muscles. 
#     You've trained high-caliber athletes and movie stars""",
#     model=model
# )

# assistant_id = personal_trainer_assis.id
# print(assistant_id)



#--- Thread ---
# thread = client.beta.threads.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "How do I get started working out to lose fat and build muscles?"
#         }
#     ]
# )

# thread_id = thread.id
# print(thread_id)

#--- Hard Code our Id ---

assistant_id = "asst_jJSNGW6IGtPqACIrlkAauTQR"
thread_id = "thread_5ZizQuzcuZhYagaUKGYhViHQ"

#--- Create a Message---
message = "How many reps do I need to do to build lean muscles?"
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content=message
)

#--- Run our Assistant ---
run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    instructions="Please address the user as James Bond"
)

def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
    
    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            if run.completed_at:
                elapsed_time = run.completed_at - run.created_at
                formatted_elapsed_time = time.strftime(
                    "%H:%M:%S", time.gmtime(elapsed_time)
                )
                print(f"Run completed in {formatted_elapsed_time}")
                logging.info(f"Run completed in {formatted_elapsed_time}")
                # Get messages here once Run is completed
                messages = client.beta.threads.messages.list(thread_id=thread_id)
                last_message = messages.data[0]
                response = last_message.content[0].text.value
                print(f"Assistant Response: {response}")
                break
        except Exception as e:
            logging.error(f"An error occured while retrieving the run: {e}")
            break
        logging.info("Waiting for run to complete...")
        time.sleep(sleep_interval)

#--- Run ---
wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)

#--- Steps --- Logs
run_steps = client.beta.threads.runs.steps.list(
    thread_id=thread_id,
    run_id=run.id
)

#print(f"Stemps---> {run_steps.data[0]}")