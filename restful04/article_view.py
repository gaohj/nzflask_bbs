from flask import Blueprint
from flask_restful import Resource,Api,marshal_with,fields
from models import Article
bp = Blueprint('article',__name__,url_prefix='/article/')
api =Api(bp)

# class Article(object):
#     def __init__(self,title,content):
#         self.title = title
#         self.content = content
# article = Article(title='只要刷一辆法拉利主播带你去登记',content='只要礼物送的多，主播跟你去拍拖')
#
# class ArticleView(Resource):
#     resource_fields = {
#         'title':fields.String,
#         'content':fields.String,
#         'author':fields.String
#     }
#     @marshal_with(resource_fields)
#     def post(self):
#         return article


# api.add_resource(ArticleView,'/')
class ArticleView(Resource):
    resource_fields = {
        'wangbo_title':fields.String(attribute='title'),
        'content':fields.String,
        'author':fields.Nested({
            'username':fields.String,
            'email':fields.String,
        }), #如果这个下面是一个字典 那么可以使用fields.Nested
        'tags':fields.List(fields.Nested({
            'id':fields.Integer,
            'name':fields.String,
        })), #列表 用List
        'readcount':fields.Integer(default=100)
    }
    @marshal_with(resource_fields)
    def get(self,article_id):
        article = Article.query.get(article_id)
        print(article)
        return article
api.add_resource(ArticleView,'<int:article_id>/')