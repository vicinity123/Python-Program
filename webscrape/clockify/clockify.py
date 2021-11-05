# Imports
from base_scrape import find_el, to_website, Keys
from time import sleep


# Steps for this sign_up function can be found in this markdown(.md) file = html_el.md
def sign_up(email, password):
    to_website("https://clockify.me")
    sleep(3)
    sign_btn = find_el("xpath", '//*[@id="hero"]/div[1]/a[1]/button')
    sign_btn.click()
    sleep(3)
    sign_email = find_el(
        "xpath",
        "/html/body/app-root/register-layout/div/div/div/div/div[2]/signup/div/form/div/div/div/div[2]/div[1]/input",
    )
    sign_password = find_el(
        "xpath",
        "/html/body/app-root/register-layout/div/div/div/div/div[2]/signup/div/form/div/div/div/div[2]/div[2]/input",
    )
    sign_submit = find_el(
        "xpath",
        "/html/body/app-root/register-layout/div/div/div/div/div[2]/signup/div/form/div/div/div/div[2]/div[4]/button",
    )
    sign_email.send_keys(email)
    sign_password.send_keys(password)
    sign_submit.click()


def log_in(email, password):
    to_website("https://clockify.me/login")
    sleep(3)
    log_email = find_el("xpath", '//*[@id="email"]')
    log_password = find_el("xpath", '//*[@id="password"]')
    log_submit = find_el(
        "xpath",
        "/html/body/app-root/register-layout/div/div/div/div/div[2]/login/div/form/div/div/div/div[2]/div[5]/button",
    )
    log_email.send_keys(email)
    log_password.send_keys(password)
    log_submit.click()


email_to_use = "randomemail@somedomain.com"
password_to_use = "SomeDomain@randomEmail13"
log_in(email_to_use, password_to_use)
