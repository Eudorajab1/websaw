import os
from websaw import DefaultApp, DefaultContext, Reloader
from websaw.templates import UTemplate
from . import utemplates as ut

class Context(DefaultContext):
    env = {
        'template_context' : dict(user = 'John Andrew'),
    }
    
    # To make template replaceable/referenceable we should assign a fixture key (e.g. welcome_template)
    # To do that use the following syntax for template:
    # <fixture_key>:UTemplate(<template>)

    welcome_template = UTemplate(ut.welcome)
    index_template = UTemplate(ut.welcome)

ctxd = Context()
app = DefaultApp(ctxd, name=__package__)


@app.route('welcome')
@app.use(ctxd.welcome_template)
def welcome(ctx):
    msg = (
        'Hey! this is a message from the info-mixin controller'
        'It uses teh mixin welcome template'
    )
    return dict(msg=msg)

@app.route('mixin_template_overwritten')
@app.use(ctxd.welcome_template)
def welcome(ctx):
    msg = dict(mixin_message = 'Hey! this is a message from the info-mixin controller'
                                'It uses teh mixin welcome template'
    )    
    return dict(msg=msg)


@app.route('info/app')
@app.use(ctxd.index_template)
def info_app(ctx: Context):

    def rep(v):
        if isinstance(v, list):
            return [rep(_) for _ in v]
        if isinstance(v, str):
            return v
        return repr(v)

    ret = {
        k: rep(v) for k, v in ctx.app_data.__dict__.items()
    }
    ret['env'] = ctx.env
    ret['ctx_fixtures'] = {k: repr(f) for k, f in ctx._fixt.items()}
    
    return dict (msg = ret)
