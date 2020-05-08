# Description

Manage whitelists or blacklists of IPs

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Check If IP Is in List

This action is used to check if a given IP is included in any of the IPs or CIDR addresses managed by this plugin.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ip_address|string|None|True|IP Address to check|None|1.1.1.1|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|is_in_list|boolean|True|Is the IP in the list|

Example output:

```
```

#### Remove IP from List

This action is used to remove an IP or CIDR from the list managed by this plugin.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ip_address|string|None|True|IP or CIDR to store|None|1.1.1.1|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
```

#### Clear IP List

This action removes all IPs in the IP list managed by this plugin.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|success|

Example output:

```
```

#### Get IP List

This action gets the managed IP list from this plugin.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ip_list|[]string|True|List of IP and CIDR addresses stored in this plugin|

Example output:

```
```

#### Add IP to List

This action is used to add an IP or CIDR to a stored list of IP addresses.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ip_address|string|None|True|IP or CIDR to store|None|1.1.1.1|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ip_address|string|True|IP address that was stored|

Example output:

```
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._
## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [IP List Manager](LINK TO PRODUCT/VENDOR WEBSITE)
