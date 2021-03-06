from clear_my_record_backend.server import cmr, dbs
from clear_my_record_backend.server.models import User, Qualifying_Answer


@cmr.shell_context_processor
def make_shell_ctx():
    return {'dbs': dbs, 'User': User, 'Qualifying_Answer': Qualifying_Answer}
