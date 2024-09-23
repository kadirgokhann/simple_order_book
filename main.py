def modify_order(order_book, order):
    """Modify an order's price or quantity in the order book."""
    # Example logic: Find the order in the heap, modify it, and re-heapify
    # For simplicity, you could reinsert the order after modification
    order_book.delete_order(order)  # Delete the old order
    order_book.add_order(order)  # Add the modified order

def delete_order_from_book(order_book, order):
    """Deletes an order from the order book."""
    # Mark an order as deleted, and re-heapify
    order_book.delete_order(order)

def process_message_with_timestamps(message):
    """Process a message with timestamps for latency tracking."""
    priority_timestamp = message['priority_timestamp']
    gateway_timestamp = message['gateway_in_timestamp']
    
    # Use these timestamps for latency analysis, ordering, or logging
    print(f"Message received with Priority Timestamp: {priority_timestamp}, Gateway-In Timestamp: {gateway_timestamp}")