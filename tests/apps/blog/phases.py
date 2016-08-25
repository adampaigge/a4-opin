from euth import phases

from . import apps, models, views


class BlogPhase(phases.PhaseContent):
    app = apps.BlogConfig.label
    phase = 'phase'
    view = views.PostDetail
    weight = 20

    features = {
        'comment': (models.Post, )
    }

phases.content.register(BlogPhase())
