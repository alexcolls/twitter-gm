# twitter-gm

A Twitter assistant bot, using Selenium (no Twitter api required), that allows you to manage your accounts with AI:

- Generative Pre-trained Transformer (GPT) to generate text from your insterests and your feed tweets to generate 'smart' answers.

- Stable Diffusiion from Dall-e engine to generate intentional images for your generative tweets and answers.

'twitter-gm' allows you to manage your twitter accounts automatically based on your interests. As it can use 'text-davinci-002' model from openai you can even configure a famous personality to publish tweets based on the trained data of your character, for example, Albert Enstein, the model will generate text on topics related to Albert.

To use this program you need to open an account in twitter.com and open.com and add your credentials to your key.py file, as explained below.

Just DM if you need help configuring it.
@fxmozart_sol
twitter.com/fxmozart_sol

## Clone repo

```
git clone https://github.com/quantium-rock/twitter-gm
```

```
cd twitter-gm/
```

## Install dependencies install.txt

```
pip install -r install.txt
```

## Create key.py in the root folder with your twitter and opeanai credentials

```
touch key.py
```

In the key.py add your the following variables:

```
user = '@example'
pswd = 'your-password'
apik = 'your-openai-apikey'
```

## Run the app

```
python app.py
```

## Run the bot 25-7

```
python run.py
```

## Also you can try chatGPT and Dall-e outputs running:

```
python src/createTweet.py
```

You can modify prompts.py to get your desired responses.

# More updates comming soon...
