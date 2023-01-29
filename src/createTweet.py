from random import randint
from randoms import messages
import key
import openai
import prompts


def create_tweet(_prompts=prompts.prompts, _api_key=key.apik, _image=True, _print=True, _model='text-davinci-003', _max_letters=160):
    try:
        openai.api_key = _api_key
        i = randint(0, len(_prompts) - 1)
        prompt = _prompts[i]
        if (len(prompt) < _max_letters*0.1):
            j = randint(0, len(messages))
            return messages[j]
        # generate text from chatGPT
        completion = openai.Completion.create(
            engine=_model,
            prompt=prompt+' less than '+str(_max_letters)+' letters',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        chatGPTtxt = completion.choices[0].text
        if (_print):
            print(chatGPTtxt)
        # add emojis to answer
        completion = openai.Completion.create(
            engine=_model,
            prompt=chatGPTtxt +
            '\n With the previous text, add emojis at the beggining of the main 3 sentences giving two spaces',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        textEmojis = completion.choices[0].text
        if (_print):
            print(textEmojis)
        # generate Dall-e prompt
        img_prompt = 'Describe the following text as an image ' + chatGPTtxt
        completion = openai.Completion.create(
            engine=_model,
            prompt=img_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        # generate img if _image=True <default>
        img = ''
        if (_image):
            stableDif = openai.Image.create(
                prompt=img_prompt,
                n=1,
                size="256x256",
            )
            img = stableDif["data"][0]["url"]
        ret = {
            'text': textEmojis,
            'img': img,
        }
        if (_print):
            print('\n', ret)
        return ret
    except:
        j = randint(0, len(messages) - 1)
        return 'GM ' + messages[j]
