class SingleVendorRouter:
    route_app_labels = {'accounts', 'blog', 'dashboard', 'store', 'order', 'vendor_store', 'notification', 'admin', 'contenttypes', 'sessions', 'auth', }

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'notification'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'notification'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or 
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'notification'
        return None
