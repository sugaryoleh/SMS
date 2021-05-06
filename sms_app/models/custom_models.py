class CustomModel():

    def dict(self):
        return dict(zip(self.retrieve_field_names(), self.retrieve_field_values()))

    def customer_dict(self):
        return dict(zip(self.retrieve_customer_field_names(), self.retrieve_customer_field_values()))

    @staticmethod
    def retrieve_field_names():
        return ()

    def retrieve_field_values(self):
        return ()

    @staticmethod
    def retrieve_customer_field_names():
        return ()

    def retrieve_customer_field_values(self):
        return ()

