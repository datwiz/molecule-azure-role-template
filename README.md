# Molecule + Azure Role Template
A cookiecutter template for ansible role development using molecule on azure.

## Assumptions
* Using an existing Azure resource group.  (env var ${ASURE_RESOURCE_GROUP})
* The existing resource group contains a single vnet and subnet

## Configuration
Out-of-the-box configuration:
* an Ubunutu 18.04 Canonical instance
* instance uses managed disks with Standard tier storage
* instance size is a Standard_B1s burstable
The initial molecule configuration can be customised in the `molecule.yml` file.

## References
* This template was created by customsing the default molecule template using the azure driver.
```
molecule init --role-name default --driver azure
```
* cookiecutter-molecule reference example: [retr0h/cookiecutter-molecule](https://github.com/retr0h/cookiecutter-molecule)
