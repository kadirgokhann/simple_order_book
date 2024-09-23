import struct
import socket

# Message Format Definition for Order Add (Template ID 13100)
# Example structure: Instrument ID (4 bytes), Side (1 byte), Price (8 bytes), Quantity (4 bytes)
# Priority Timestamp (8 bytes), Gateway-In Timestamp (8 bytes)
ORDER_ADD_FORMAT = "I B Q I Q Q"  # Struct format string for Order Add

def parse_order_add_message(binary_data):
    """Parse the Order Add message based on T7 EOBI specifications."""
    try:
        # Unpack the binary message based on the specified format
        unpacked_data = struct.unpack(ORDER_ADD_FORMAT, binary_data)

        # Assign variables to each part of the unpacked data
        instrument_id = unpacked_data[0]
        side = unpacked_data[1]  # 1 = Buy, 2 = Sell
        price = unpacked_data[2] / 100000000  # Adjust for scale
        quantity = unpacked_data[3]
        priority_timestamp = unpacked_data[4]
        gateway_in_timestamp = unpacked_data[5]

        # Print the extracted data for debugging purposes
        print(f"Order Add Message: Instrument ID: {instrument_id}, Side: {side}, Price: {price}, "
              f"Quantity: {quantity}, Priority Timestamp: {priority_timestamp}, Gateway-In Timestamp: {gateway_in_timestamp}")
    
        # Return the parsed data for further processing in the order book
        return {
            'instrument_id': instrument_id,
            'side': side,
            'price': price,
            'quantity': quantity,
            'priority_timestamp': priority_timestamp,
            'gateway_in_timestamp': gateway_in_timestamp
        }
    except struct.error as e:
        print(f"Error unpacking Order Add message: {e}")
        return None