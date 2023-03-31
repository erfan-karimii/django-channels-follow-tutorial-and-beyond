
class OtherRouter:
    """
    A router to control all database operations on models other applications.
    """
    route_app_labels = {'auth','contenttypes','admin','sessions'}
    def db_for_read(self, model, **hints):
        """
        Attempts to read other models go to default_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'default_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write other models go to default_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'default_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the other apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the other app only appear in the
        'default_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'default_db'
        return None

class ChatRouter:
    """
    A router to control all database operations on models chat applications.
    """
    route_app_labels = {'chat'}
    def db_for_read(self, model, **hints):
        """
        Attempts to read chat models go to chat_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'chat_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write chat models go to chat_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'chat_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the chat apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the chat app only appear in the
        'chat_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'chat_db'
        return None