class StockSellTime:
    def __init__(self, prices):
        self.prices = prices

    def build_min_max_values(self):
        prices = self.prices

        if prices:
            current_min = prices[0]
            current_max_profit = 0
            best_min = current_min
            best_max = current_min

        else:
            # Return a dictionary so the next function doesn't crash
            return {"min": 0, "max": 0}

        for price in prices[1:]:
            if price < current_min:
                current_min = price
            else:
                profit = price - current_min
                if profit > current_max_profit:
                    current_max_profit = profit
                    best_min = current_min
                    best_max = price

        return {"min": best_min, "max": best_max}

    def determine_sell_time(self):
        values = self.build_min_max_values()
        maximum_profit = values["max"] - values["min"]

        if maximum_profit <= 0:
            print("No profit can be made")
            return 0
        else:
            print(f"Maximum profit that can be made is: {maximum_profit}.")
            return maximum_profit


def main():
    prices = []
    test_object = StockSellTime(prices)
    test_object.determine_sell_time()


if __name__ == "__main__":
    main()
