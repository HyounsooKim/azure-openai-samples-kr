def check_kernel():
    import json
    import ipykernel
    kernel_id = ipykernel.connect.get_connection_file()

    with open(kernel_id, 'r') as f:
        data = json.load(f)  

    if data["kernel_name"] == "":
        print("Select kernel first!")
    else:
        print(f"Kernel: {data['kernel_name']}")