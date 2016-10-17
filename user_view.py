from flask import Blueprint,make_response,jsonify,request,g
import model



def get_db():
    return model.db.session
def destroy_db():
    model.db.session.remove()



from flask.views import  MethodView

UserAppApi = Blueprint("userapi",__name__)
class UserApi(MethodView):

    #decorators = []
    #get the inforamtion of this user /post
    def get(self,userid,*args,**kwargs):
        if userid is None:
            answer = model.User.query.all()
            response = make_response(jsonify(answer))
            return response()
        else:
            response = make_response(jsonify("bad"))
            return response()

    #create a new user
    def post(self,*args,**kwargs):#try
        try:
            user = model.User(name=request.form["name"],email=request.form["email"],password=request.form["password"])#make better
            get_db().add(user)
            get_db().commit()
            get_db().remove()

        except:
            print "error @ post"
        finally:
            response = make_response()
            return response()



    #update the informatuion of the user
    def update(self,*args,**kwargs):#try
        try:
            user = model.User(name=request.form["name"],email=request.form["email"],password=request.form["password"])#make better
            get_db().add(user)
            get_db().commit()
            get_db().remove()

        except:
            print "error @ post"
        finally:
            response = make_response()
            return response()




    #delete the user
    def delete(self,*args,**kwargs):
        try:
            model.User.query.all()
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