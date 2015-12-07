import keyring
import emoji 
from time import sleep
import webbrowser
import github
import subprocess

GITHUB_NEW_TOKEN_URI = 'https://github.com/settings/tokens/new'

def setup_github_credentials(log):
    token = keyring.get_password('session','github_token')

    if token is None:
        GITHUB_NEW_TOKEN_URI = 'https://github.com/settings/tokens/new'
        log.info(emoji.emojize(":heart_with_arrow: == LOVE == :heart_with_arrow:"))
        log.info("I will need a new token to access your GitHub account, please give me a token that have `write:repo_hook` enable.")
        log.info("I'll try to open github for you at the right page, otherwise please visit %s", GITHUB_NEW_TOKEN_URI)
        sleep(5)
        webbrowser.open_new_tab(GITHUB_NEW_TOKEN_URI)
        token = input('github token:')
        keyring.set_password('session','github_token', token)
        log.info('token stored in your keyring as session:github_token')
    gh = github.Github(token)
    user = gh.get_user()
    log.info('Logged in on GitHub as %s ', user.name)
    return token, user



def setup_github_repository(user, proposal, log):
    from github import UnknownObjectException 
    try:
        repo = user.get_repo(proposal)
        log.info('It appears like %s repository already exists, using it as remote', repr(proposal))
    except UnknownObjectException:
        repo = user.create_repo(proposal)

    ssh_url = repo.ssh_url
    slug = repo.full_name
    log.info('Working with repository %s', slug)


    # Clone github repo locally, over SSH an chdir into it

    log.info("Cloning github repository locally")
    log.info("Calling subprocess : %s", ' '.join(['git', 'clone' , ssh_url]))
    subprocess.call(['git', 'clone' , ssh_url])
    return slug
