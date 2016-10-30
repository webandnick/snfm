from flask import Blueprint,make_response,jsonify,request,g
from models import users
from flask_peewee.db import Database







from flask.views import  MethodView

UserAppApi = Blueprint("userapi",__name__)
class UserApi(MethodView):

    #decorators = []
    #get the inforamtion of this user /post
    def get(self,userid,*args,**kwargs):
        if userid is None:
            answer = users.User.select().tuples()
            response = make_response(jsonify(answer))
            return response()
        else:
            response = make_response(jsonify("bad"))
            return response()

    #create a new user
    def post(self,*args,**kwargs):#try
        try:

            users.User().save()


        except:
            print "error @ post"
        finally:
            response = make_response()
            return response()



    #update the informatuion of the user
    def update(self,*args,**kwargs):#try
        try:
            users.User().save()

        except:
            print "error @ post"
        finally:
            response = make_response()
            return response()




    #delete the user
    def delete(self,*args,**kwargs):
        try:
            users.User.delete()
        except:
            pass#faile
        finally:
            response = make_response()
            return response()



def register_endpoint(view,endpoit,url,pk="user_id",pk_type="int"):
    viewfunc = view.as_view(endpoit)
    UserAppApi.add_url_rule("%s<%s:%s>" % (url,pk,pk_type), view_func=viewfunc, defaults={"userid": None}, methods=["GET"])
    UserAppApi.add_url_rule(url, view_func=viewfunc, methods=["POST","UPDATE","DELETE"])



register_endpoint(UserApi,"user","/user/")