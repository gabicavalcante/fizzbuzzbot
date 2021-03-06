from flask_admin import Admin, expose
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_simplelogin import login_required
from flask_admin.model import typefmt
from datetime import datetime

from fizzbuzz.ext.database import db
from fizzbuzz.models import Chat, User

AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)


class AdminView(sqla.ModelView):
    def __init__(self, *args, **kwargs):
        super(AdminView, self).__init__(*args, **kwargs)

        self.column_formatters = dict(typefmt.BASE_FORMATTERS)
        self.column_formatters.update(
            {type(None): typefmt.null_formatter, datetime: self.date_format}
        )

        self.column_type_formatters = self.column_formatters

    def date_format(self, view, value):
        return value.strftime("%d %b %Y - %I:%M:%p")


class HomeView(AdminIndexView):
    @expose("/")
    def index(self):
        users_count = User.query.count()
        chats_count = Chat.query.count()
        return self.render(
            "admin/home.html", users_count=users_count, chats_count=chats_count
        )


class UserAdmin(AdminView):
    column_list = ["username"]
    can_edit = False


class ChatView(AdminView):
    page_size = 50
    can_edit = False
    can_create = False


def init_app(app):
    admin = Admin(index_view=HomeView())
    admin.name = app.config.TITLE
    admin.template_mode = "bootstrap3"
    admin.base_template = "layout.html"
    admin.init_app(app)
    admin.add_view(ChatView(Chat, db.session))
    admin.add_view(UserAdmin(User, db.session))
