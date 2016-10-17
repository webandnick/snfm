from flask import Blueprint,make_response,jsonify,request


from flask.views import  MethodView

PostAppApi = Blueprint("postapi",__name__)
class PostApi(MethodView):

    #decorators = []
    def get(self,userid,*args,**kwargs):
        if userid is None:
            response = make_response()
            return response()
        else:
            response = make_response()
            return response()

    def post(self,*args,**kwargs):#try
        try:
            pass
        except:
            pass
        finally:
            response = make_response()
            return response()




    def update(self,*args,**kwargs):#try
        try:
            pass
        except:
            pass
        finally:
            response = make_response()
            return response()





    def delete(self,*args,**kwargs):
        try:
            pass#delete(token)
            #succesfully deleten
        except:
            pass#faile
        finally:
            response = make_response()
            return response()



def register_endpoint(view,endpoit,url,pk="user_id",pk_type="int"):
    viewfunc = view.as_view(endpoit)
    PostAppApi.add_url_rule("%s<%s:%s>" % (url,pk,pk_type), view_func=viewfunc, defaults={"userid": None}, methods=["GET"])
    PostAppApi.add_url_rule(url, view_func=viewfunc, methods=["POST","UPDATE","DELETE"])



register_endpoint(PostApi,"post","/post/")