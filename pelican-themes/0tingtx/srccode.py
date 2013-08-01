#just use for have a look in dev theme, copy from pelican source 
class ArticlesGenerator(Generator):
    """Generate blog articles"""

    def __init__(self, *args, **kwargs):
        """initialize properties"""
        self.articles = []  # only articles in default language
        self.translations = []
        self.dates = {}
        self.tags = defaultdict(list)
        self.categories = defaultdict(list)
        self.related_posts = []
        self.authors = defaultdict(list)
        self.drafts = []
        super(ArticlesGenerator, self).__init__(*args, **kwargs)
        signals.article_generator_init.send(self)
        
        
        
        
        
class PagesGenerator(Generator):
    """Generate pages"""

    def __init__(self, *args, **kwargs):
        self.pages = []
        self.hidden_pages = []
        self.hidden_translations = []
        super(PagesGenerator, self).__init__(*args, **kwargs)
        signals.page_generator_init.send(self)
        
        
class Paginator(object):
    def __init__(self, object_list, per_page, orphans=0):
        self.object_list = object_list
        self.per_page = per_page
        self.orphans = orphans
        self._num_pages = self._count = None
        
class Page(object):
    def __init__(self, object_list, number, paginator):
        self.object_list = object_list
        self.number = number
        self.paginator = paginator
        
@functools.total_ordering
class URLWrapper(object):
    def __init__(self, name, settings):
        # next 2 lines are redundant with the setter of the name property
        # but are here for clarity
        self.settings = settings
        self._name = name
        self.slug = slugify(name, self.settings.get('SLUG_SUBSTITUTIONS', ()))
        self.name = name
