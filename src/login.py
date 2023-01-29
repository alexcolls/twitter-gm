import key
from src.chromeDriver import driver, keys, by
from time import sleep


def log_in(user=key.user, pasw=key.pasw):
    driver.get('https://www.twitter.com/i/flow/login')
    sleep(2)
    user_in = driver.find_element(by=by.TAG_NAME, value='input')
    user_in.send_keys(user)
    user_in.send_keys(keys.ENTER)
    sleep(2)
    pasw_in = driver.find_element(by=by.NAME, value='password')
    pasw_in.send_keys(pasw)
    pasw_in.send_keys(keys.ENTER)
