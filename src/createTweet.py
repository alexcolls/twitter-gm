from time import sleep
from random import randint
from randoms import messages
import key
import openai
import prompts


def create_tweet(_prompts=prompts.prompts, _api_key=key.apik, _image=True, _print=True, _model='text-davinci-003', _max_letters=160, _sleep=3):
    try:
        openai.api_key = _api_key
        # get random propmt from _prompts[]
        i = randint(0, len(_prompts) - 1)
        prompt = _prompts[i]
        if (len(prompt) < _max_letters*0.1):
            j = randint(0, len(messages))
            return messages[j]
        # generate text from chatGPT
        if (_print):
            print('\n\nSTEP 1 - Get answer from:\n', prompt)
        completion = openai.Completion.create(
            engine=_model,
            prompt=prompt+'\n less than '+str(_max_letters)+' letters',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        chatGPTtxt = completion.choices[0].text
        sleep(_sleep)
        if (_print):
            print('\n\n', 'ChatGPT answer:\n', chatGPTtxt)
        # add emojis to answer
        if (_print):
            print('\n\nSTEP 2 - Add emojis to answer:')
        completion = openai.Completion.create(
            engine=_model,
            prompt=chatGPTtxt +
            '\n With the previous text, add emojis at the beggining of the main sentences giving spaces.',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        textEmojis = completion.choices[0].text
        sleep(_sleep)
        if (_print):
            print('\n', 'Answer with emojis: ', textEmojis)
        # generate topic from tweet
        if (_print):
            print('\n\nSTEP 3 - Get tweet topic:')
        topic_prompt = 'What is the topic of this text? \n' + chatGPTtxt
        completion = openai.Completion.create(
            engine=_model,
            prompt=topic_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        topic = completion.choices[0].text
        try:
            topic = topic.replace('The topic of this text is', ' ')
        except:
            pass
        sleep(_sleep)
        if (_print):
            print('\n', 'The topic is: ' + topic)
        # generate Dall-e prompt
        img_prompt = 'Describe a realistic image about ' + topic
        if (_print):
            print('\n\nSTEP 4 - Generative image prompt:\n', img_prompt)
        completion = openai.Completion.create(
            engine=_model,
            prompt=img_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        sleep(_sleep)
        if (_print):
            print('\n', 'Dall-E prompt: ', img_prompt)
        # generate img if _image=True <default>
        if (_image):
            if (_print):
                print('\n\nSTEP 5 - Generating image from Dall-E...')
            img = ''
            stableDif = openai.Image.create(
                prompt=img_prompt,
                n=1,
                size="246x250",
            )
            img = stableDif["data"][0]["url"]
        ret = {
            'text': textEmojis,
            'img': img,
        }
        sleep(_sleep)
        if (_print):
            print('\n', 'createTweet() return: ', ret)
        return ret
    except:
        print('\nERROR: openai api failed. \n1. Check  that apik in key.py is correct. \n2. Check also that prompt sent to chatGPT and/or Dall-E is correct.\n> Returning random message from randoms.py\n')
        j = randint(0, len(messages) - 1)
        return 'GM ' + messages[j]


if __name__ == '__main__':
    print(create_tweet())
