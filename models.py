from app import db
from sqlalchemy.dialects.postgresql import JSON
import uuid as pyuuid

# http://stackoverflow.com/a/12270917/130164
def uuid2slug(uuidstring):
    return pyuuid.UUID(uuidstring).bytes.encode('base64').rstrip('=\n').replace('/', '_')

def slug2uuid(slug):
    return str(pyuuid.UUID(bytes=(slug + '==').replace('_', '/').decode('base64')))

class Record(db.Model):
    __tablename__ = 'record'
    uuid = db.Column(db.String, primary_key=True)
    experiment_name = db.Column(db.String)
    user_id = db.Column(db.String)
    marked = db.Column(db.Boolean, default=False)

    def __init__(self, experiment, user, visited=False):
        self.uuid = str(pyuuid.uuid4())
        self.experiment_name = experiment
        self.user_id = user
        self.marked = visited

    def __repr__(self):
        return '<Experiment %s, User %s: %s>' % (self.experiment_name,
            self.user_id, 'MARKED' if self.marked else 'not marked')

    def csv(self):
        return '%s,%s,%s,%d' % (uuid2slug(self.uuid), self.experiment_name, self.user_id, 1 if self.marked else 0)
