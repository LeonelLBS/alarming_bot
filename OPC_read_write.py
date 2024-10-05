from opcua import Client, ua

def read_input_value(node_id):
    client_node = client.get_node(node_id)
    client_node_value = client_node.get_value()
    print('Value of : ' + str(client_node) + ' : ' + str(client_node_value))

def write_value_int(node_id, value):
    client_node = client.get_node(node_id)
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Int16))
    client_node.set_value(client_node_dv)
    print('Value of : ' + str(client_node) + ' : '+str(client_node_value))

def write_value_bool(node_id, value):
    client_node = client.get_node(node_id)
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Boolean))
    client_node.set_value(client_node_dv)
    print('Value of : ' + str(client_node) + ' : '+str(client_node_value))

if __name__ == '__main__':
    client = Client('opc.tcp://192.168.10.50:4840')
    try:
        client.connect()

        root = client.get_root_node()
        print('Object root is: ', root)

        #read_input_value('ns=4;i=5')
        write_value_bool('ns=4;i=5', True)
    finally:
        client.disconnect()