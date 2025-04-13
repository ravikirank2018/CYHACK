import boto3

waf = boto3.client('wafv2')
sns = boto3.client('sns')

# ARN of the AWS WAF IP set
ip_set_arn = 'arn:aws:wafv2:REGION:ACCOUNT_ID:regional/ipset/IPSetName/IPSetId'

def lambda_handler(event, context):
    # Extract the IP address from the SNS notification
    ip_address = event['Records'][0]['Sns']['Message']
    
    # Get the current IP set
    response = waf.get_ip_set(Name='IPSetName', Scope='REGIONAL', Id='IPSetId')
    ip_addresses = response['IPSet']['Addresses']
    
    # Add the new IP address to the IP set
    ip_addresses.append(ip_address + '/32')
    
    # Update the IP set with the new IP address
    waf.update_ip_set(
        Name='IPSetName',
        Scope='REGIONAL',
        Id='IPSetId',
        Addresses=ip_addresses,
        LockToken=response['LockToken']
    )

    print(f"Added {ip_address} to AWS WAF IP set.")
