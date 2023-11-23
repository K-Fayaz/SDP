import sys

# Retrieve the command line argument passed from Node.js
data_from_node = sys.argv[1] if len(sys.argv) > 1 else None

if data_from_node:
    print(f'Data received from Node.js: {data_from_node}')
else:
    print('No data received from Node.js')
