from selenium.webdriver import Firefox
from notebook.notebookapp import list_running_servers


def quick_driver():
    """Quickly create a selenium driver pointing at an active noteboook server.

    Usage example
    
    from inside the selenium test directory:
    
        import quick_selenium, test_markdown, utils
        nb = utils.Notebook(test_markdown.notebook(quick_selenium.quick_driver()))
    """
    try:
        server = list(list_running_servers())[0]
    except IndexError as e:
        e.message = 'You need a server running before you can run this command'
    driver = Firefox()
    auth_url = '{url}?token={token}'.format(**server)
    driver.get(auth_url)
    return driver