# -*- coding:utf-8 -*-

from flask import Flask

from conf import server
from gs.common import cjinjafilters

app = Flask(__name__)
app.config['SECRET_KEY'] = 'J0T01M/2yX P~XHY111111]PPO/,?IT3'
# 调试模式
if not server.ONLINE:
    app.config['DEBUG'] = True

# 初始化工作
# log
from gs.common import clogger
from gs.conf import logger as loggerconf

clogger.init(loggerconf.LOGNAME_BLOG)

# db
from common import cdb

cdb.init_flaskdb(app)
from views import bp_blog

app.register_blueprint(bp_blog)

cjinjafilters.init(app)
