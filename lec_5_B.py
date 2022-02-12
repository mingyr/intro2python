class B:
    def __init__(self):
        """Trival initialization of class B."""
        pass
    def bar(self):
        print(f"in namespace {__name__}")
        
        
if __name__ == "__main__":
    from lec_5_A import A
    A().foo()
    B().bar()    