from flask_restful import Resource, reqparse, marshal, fields, abort
from flask_security import auth_token_required, roles_required, login_user
from .models import User, Ticket
from Ticket_App import app, db
from flask_restful import Api

ticket_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'assigned_to': fields.String
}

class TicketsAPI(Resource):
    @auth_token_required
    @roles_required('Admin')
    def post(self):
        # args = self.reqparse.parse_args()
        args = reqparse.RequestParser() \
            .add_argument('title', type=str, location='json', required=True, help="Please enter username") \
            .add_argument("description", type=str, location='json') \
            .add_argument("done", type=bool, location='json') \
            .add_argument("assigned_to", type=str, location='json') \
            .parse_args()
        tk = Ticket(title=args['title'], description=args['description'],
                    done=args['done'], assigned_to=args['assigned_to'])
        try:
            db.session.add(tk)
            db.session.commit()
            return {'ticket': 'ticket created.'}, 201
        except:
            return {'error': "Internal Server Error"}, 500

    def get(self):
        tickets = Ticket.query.all()
        return {'results': [marshal(ticket, ticket_fields) for ticket in tickets], 'count': len(tickets)}


class TicketAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('description', type=str, default="",
                                   location='json')
        self.reqparse.add_argument('done', type=bool, default=False,
                                   location='json')
        self.reqparse.add_argument('assigned_to', type=str, default="",
                                   location='json')
        super(TicketAPI, self).__init__()

    def get(self, tk_id):
        tickets = Ticket.query.filter(Ticket.id == tk_id).all()
        return {'results': [marshal(ticket, ticket_fields) for ticket in tickets], 'count': len(tickets)}

    @auth_token_required
    @roles_required('Admin')
    def put(self, tk_id):
        results = []
        tickets = Ticket.query.filter(Ticket.id == tk_id).all()
        if len(tickets) == 0:
            abort(404)
        args = self.reqparse.parse_args()
        try:
            for tk in tickets:
                # temp_tk = Ticket(tk.title)
                for k, v in args.items():
                    if v is not None:
                        setattr(tk, k, v)
                db.session.commit()
                results.append("Updated Ticket ID: %s" % tk.id)
            return {"results": results}, 201
        except:
            return {'error': "Internal Server Error"}, 500

    @auth_token_required
    @roles_required('Admin')
    def delete(self, tk_id):
        try:
            Ticket.query.filter(Ticket.id == tk_id).delete()
            db.session.commit()
            result = "Successfully deleted ticket ID: %s" % tk_id
            return {'results': result}, 201
        except:
            return {'error': "Internal Server Error"}, 500


class Login(Resource):
    def post(self):
        args = reqparse.RequestParser() \
            .add_argument('username', type=str, location='json', required=True, help="Please enter username") \
            .add_argument("password", type=str, location='json', required=True, help="Please enter password") \
            .parse_args()
        user = User.authenticate(args['username'], args['password'])
        if user:
            login_user(user=user)
            return {"message": "Hii!", "token": user.get_auth_token()}, 200
        else:
            return {"message": "UNAUTHORIZED REQUEST"}, 401


api = Api(app, default_mediatype="application/json")
api.add_resource(Login, '/api/login')
api.add_resource(TicketsAPI, '/api/tickets')
api.add_resource(TicketAPI, '/api/ticket/<int:tk_id>')
