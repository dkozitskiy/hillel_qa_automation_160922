class Gender:
    def __init__(self, count, gender, name, probability):
        self.count = count
        self.gender = gender
        self.name = name
        self.probability = probability

    @classmethod
    def create_from_json(cls, **kwargs):
        return cls(kwargs['count'], kwargs['gender'], kwargs['name'], kwargs['probability'])

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
