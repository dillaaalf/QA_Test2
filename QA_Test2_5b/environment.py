def before_all(context):
    context.browser = context.config.userdata.get("browser", "chrome")
