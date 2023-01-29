# twitter-gm

A Twitter assistant bot, using Selenium (no Twitter api required), that allows you to manage your accounts with AI:

- Generative Pre-trained Transformer (GPT) to generate text from your insterests and your feed tweets to generate 'smart' answers.

- Stable Diffusiion from Dall-e engine to generate intentional images for your generative tweets and answers.

'twitter-gm' allows you to manage your twitter accounts automatically based on your interests. As it can use 'text-davinci-002' model from openai you can even configure a famous personality to publish tweets based on the trained data of your character, for example, Albert Enstein, the model will generate text on topics related to Albert.

To use this program you need to open an account in twitter.com and open.com and add your credentials to your key.py file, as explained below.

Just DM if you need help configuring it:
https://twitter.com/@fxmozart_sol

## Clone repo

```
git clone https://github.com/quantium-rock/twitter-gm
```

```
cd twitter-gm/
```

## Install dependencies install.txt

Make sure that you have installed python3 and pip3 and included in your OS PATH environment variables. You may need to use 'python3' and 'pip3' instead.

```
pip install -r install.txt
```

## Create key.py in the root folder with your twitter and opeanai credentials

```
touch key.py
```

In the key.py add your the following variables:

```
user = '@example' # your twitter username or email
pswd = 'your-password' # your twitter password
apik = 'your-openai-apikey' # your openai.com api key
```

## Run the app

```
python app.py
```

## Run the bot 24-7

```
python run.py
```

## Also you can try chatGPT and Dall-e outputs running:

```
python src/createTweet.py
```

You can modify prompts.py to get your desired responses.

.
.
.

# More updates coming soon...
