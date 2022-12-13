from Stock import Stock

class TestStock:
    def __init__(self):
        stock = Stock("INTC", "Intel Corporation", 20.5, 20.35)
        stock.display()

if __name__ == "__main__":
    TestStock()