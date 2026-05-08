class Failure:
    def apply(self, state, tick):
        """
        Mutate system state over time.
        """
        raise NotImplementedError