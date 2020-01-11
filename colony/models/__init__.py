from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from .company import Company
from .fruit import Fruit
from .vegetable import Vegetable
from .tag import Tag
from .people import People, Friend

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
