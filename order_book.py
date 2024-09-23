import heapq

class OrderBook:
    def __init__(self):
        self.bids = []  # Max-heap for bids
        self.asks = []  # Min-heap for asks

    def add_order(self, order):
        """Adds an order to the order book."""
        if order['side'] == 1:  # Buy side (bids)
            heapq.heappush(self.bids, (-order['price'], order['priority_timestamp'], order))  # Negate price to simulate max-heap
        else:  # Sell side (asks)
            heapq.heappush(self.asks, (order['price'], order['priority_timestamp'], order))

    def modify_order(self, order):
        """Modify an existing order in the book."""
        # Modify logic, you would need to re-heapify after modification
        pass


    def delete_order(self, order):
        """Deletes an order from the book."""
        # Deleting an order could involve marking an order as deleted and re-heapifying
        pass

    def get_best_bid(self):
        """Returns the best bid price."""
        if self.bids:
            return -self.bids[0][0]  # Return negated price to get actual bid price
        return None

    def get_best_ask(self):
        """Returns the best ask price."""
        if self.asks:
            return self.asks[0][0]
        return None

    def print_order_book(self):
        """Print the top levels of the order book."""
        print("Bids:")
        for bid in self.bids[:5]:  # Print top 5 bids
            print(f"Price: {-bid[0]}, Quantity: {bid[2]['quantity']}")
        
        print("Asks:")
        for ask in self.asks[:5]:  # Print top 5 asks
            print(f"Price: {ask[0]}, Quantity: {ask[2]['quantity']}")