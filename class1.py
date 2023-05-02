class Hello:
    def __init__(self, str):
        self.str = str

        class Hi(Hello):

            def __str__(self):
                return f'Hello {self.str}'

