from opa_client.opa import OpaClient

# Initialize the OPA client
opa_client = OpaClient(host='localhost', port=8181)

# Create new policy from the rego file.
opa_client.update_policy_from_file("./policies.rego", endpoint="access_control")  # response is True

# check if the user has access according to the given policy and rule.
def check_access(data, policy_name, rule_name):
    return opa_client.check_permission(data, policy_name, rule_name)['result']

# add global data to opa.
def add_data(data, data_name):
    opa_client.update_or_create_data(data, endpoint=data_name)

