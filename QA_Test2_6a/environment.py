def before_all(context):
    context.config.setup_logging()
    context.server_url = "http://localhost:4723/wd/hub"
