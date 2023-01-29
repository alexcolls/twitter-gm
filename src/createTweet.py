from key import key
from random import randint
import openai
import prompts


def create_tweet(_prompts=prompts, _api_key=key.apik):
    openai.api_key = _api_key
    # select model
    model_engine = "text-davinci-003"
    i = randint(0, len(_prompts.prompts)-1)
    prompt = _prompts.prompts[i]
    print(prompt)
    # generate text
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt + ' less than 120 letters',
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    chatGPTtxt = completion.choices[0].text
    print(chatGPTtxt)
    # add emojis
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=chatGPTtxt +
        '\n With the previous text, add emojis at the beggining of the main 3 sentences giving two spaces',
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    textEmojis = completion.choices[0].text
    print(textEmojis)
    # generate img
    # j = randint(0, len(_prompts.images)-1)
    stableDif = openai.Image.create(
        prompt=_prompts[i],
        n=1,
        size="256x256",
    )
    img = stableDif["data"][0]["url"]
    ret = {
        'text': textEmojis,
        'img': img,
    }
    return ret


print('\n\n', createTweet())
