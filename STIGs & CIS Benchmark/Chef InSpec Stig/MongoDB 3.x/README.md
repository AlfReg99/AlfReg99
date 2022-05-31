## MongoDB STIG Automated Compliance Validation Profile
<b>MongoDB 3.X</b>

<b>MongoDB 3.X</b> STIG Automated Compliance Validation Profile works with Chef InSpec to perform automated compliance checks of <b>MongoDB</b>.

This automated Security Technical Implementation Guide (STIG) validator was developed to reduce the time it takes to perform a security check based upon STIG Guidance from DISA. These check results should provide information needed to receive a secure authority to operate (ATO) certification for the applicable technology.
<b>MongoDB</b> uses [Chef InSpec](https://github.com/chef/inspec), which provides an open source compliance, security and policy testing framework that dynamically extracts system configuration information.

## MongoDB STIG Overview

The <b>MongoDB</b> STIG (https://public.cyber.mil/stigs/) by the United States Defense Information Systems Agency (DISA) offers a comprehensive compliance guide for the configuration and operation of various technologies.
DISA has created and maintains a set of security guidelines for applications, computer systems or networks connected to the DoD. These guidelines are the primary security standards used by many DoD agencies. In addition to defining security guidelines, the STIG also stipulates how security training should proceed and when security checks should occur. Organizations must stay compliant with these guidelines or they risk having their access to the DoD terminated.

[STIG](https://en.wikipedia.org/wiki/Security_Technical_Implementation_Guide)s are the configuration standards for United States Department of Defense (DoD) Information Assurance (IA) and IA-enabled devices/systems published by the United States Defense Information Systems Agency (DISA). Since 1998, DISA has played a critical role enhancing the security posture of DoD's security systems by providing the STIGs. The STIGs contain technical guidance to "lock down" information systems/software that might otherwise be vulnerable to a malicious computer attack.

The requirements associated with the <b>MongoDB</b> STIG are derived from the [National Institute of Standards and Technology](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology) (NIST) [Special Publication (SP) 800-53, Revision 4](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53) and related documents.

While the MongoDB STIG automation profile check was developed to provide technical guidance to validate information with security systems such as applications, the guidance applies to all organizations that need to meet internal security as well as compliance standards.

### This STIG Automated Compliance Validation Profile was developed based upon:
- MongoDB Security Technical Implementation Guide
### Update History 
| Guidance Name  | Guidance Version | Guidance Location                            | Profile Version | Profile Release Date | STIG EOL    | Profile EOL |
|---------------------------------------|------------------|--------------------------------------------|-----------------|----------------------|-------------|-------------|
| MongoDB Enterprise 3.x STIG  | Ver 1, Rel 2    | https://public.cyber.mil/stigs/downloads/  |  |      | NA | NA |
| CIS Benchmark for MongoDB Enterprise 3.x |   | https://www.cisecurity.org/cis-benchmarks/ |    |    | NA | NA |


## Getting Started

### Requirements

#### MongoDB  
- MongoDB
- Access to the database
- Account providing appropriate permissions to perform audit scan


#### Required software on MongoDB cluster
- git
- [InSpec](https://www.chef.io/products/chef-inspec/)

### Setup Environment on MongoDB cluster 
#### Install InSpec
Goto https://www.inspec.io/downloads/ and consult the documentation for your Operating System to download and install InSpec.

#### Ensure InSpec version is at least 4.23.10 
```sh
inspec --version
```

### How to execute this instance  
(See: https://www.inspec.io/docs/reference/cli/)

#### Execute a single Control in the Profile 
**Note**: Replace the profile's directory name - e.g. - `<Profile>` with `.` if currently in the profile's root directory.
```sh
inspec exec <Profile>/controls/V-81843.rb --show-progress
```
or use the --controls flag to execute checking with a subset of controls
```sh
inspec exec <Profile> --controls=V-81841.rb V-81843.rb --show-progress
```

#### Execute a Single Control and save results as JSON 
```sh
inspec exec <Profile> --controls=V-81843.rb --show-progress --reporter json:results.json
```

#### Execute All Controls in the Profile 
```sh
inspec exec <Profile> --show-progress
```

#### Execute all the Controls in the Profile and save results as JSON 
```sh
inspec exec <Profile> --show-progress  --reporter json:results.json
```

## Check Overview:

**Manual Checks**

These checks are not included in the automation process.

| Check Number | Description |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| V-81845      | MongoDB must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies. |
| V-81853      | MongoDB software installation account must be restricted to authorized users. |
| V-81855      | Database software, including DBMS configuration files, must be stored in dedicated directories, or DASD pools, separate from the host OS and other applications. |
| V-81857      | The role(s)/group(s) used to modify database structure (including but not necessarily limited to tables, indexes, storage, etc.) and logic modules (stored procedures, functions, triggers, links to software external to MongoDB, etc.) must be restricted to authorized users. |
| V-81859      | Unused database components, DBMS software, and database objects must be removed. |
| V-81865      | If DBMS authentication, using passwords, is employed, MongoDB must enforce the DoD standards for password complexity and lifetime. |
| V-81867      | If passwords are used for authentication, MongoDB must store only hashed, salted representations of passwords. |
| V-81873      | MongoDB must map the PKI-authenticated identity to an associated user account. |
| V-81877      | MongoDB must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).|
|V-81885 |Database contents must be protected from unauthorized and unintended information transfer by enforcement of a data-transfer policy.|
| V-81893      | MongoDB must check the validity of all data inputs except those specifically identified by the organization. |
| V-81897      | MongoDB must associate organization-defined types of security labels having organization-defined security label values with information in storage. |
| V-81899      | MongoDB must enforce discretionary access control policies, as defined by the data owner, over defined subjects and objects. |
| V-81901      | MongoDB must provide the means for individuals in authorized roles to change the auditing to be performed on all application components, based on all selectable event criteria within organization-defined time thresholds. |
| V-81903      | MongoDB must utilize centralized management of the content captured in audit records generated by all components of MongoDB. |
| V-81909      | MongoDB must prohibit user installation of logic modules (stored procedures, functions, triggers, views, etc.) without explicit privileged status. |
| V-81911      | MongoDB must enforce access restrictions associated with changes to the configuration of MongoDB or database(s). |
| V-81913      | MongoDB must require users to reauthenticate when organization-defined circumstances or situations require reauthentication. |
| V-81915      | MongoDB must prohibit the use of cached authenticators after an organization-defined time period. |
| V-81917      | MongoDB must only accept end entity certificates issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs) for the establishment of all encrypted sessions. |
| V-81919      | MongoDB must implement cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest (to include, at a minimum, PII and classified information) on organization-defined information system components. |
| V-81921      | MMongoDB must maintain the confidentiality and integrity of information during preparation for transmission. |
| V-81923      | MongoDB must maintain the confidentiality and integrity of information during reception. |
| V-81925      | When invalid inputs are received, MongoDB must behave in a predictable and documented manner that reflects organizational and system objectives. |
| V-81927      | MongoDB must obscure feedback of authentication information during the authentication process to protect the information from possible exploitation/use by unauthorized individuals. |
| V-81929      | MongoDB must be configured in accordance with the security configuration settings based on DoD security configuration and implementation guidance, including STIGs, NSA configuration guides, CTOs, DTMs, and IAVMs. |

**Normal Checks**

These checks will follow the normal automation process and will report accurate STIG compliance PASS/FAIL.


| Check Number | Description|
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| V-81843      | MongoDB must integrate with an organization-level authentication/access mechanism.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| V-81847      | MongoDB must provide audit record generation capability for DoD-defined auditable events.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| V-81849      | Verify User ownership, Group ownership, and permissions on the MongoDB audit log directory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| V-81851      | Verify User ownership, Group ownership, and permissions on the MongoDB configuration file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| V-81861      | MongoDB unused database components must be disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| V-81863      | MongoDB must uniquely identify and authenticate organizational users.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| V-81869      | MongoDB DoD standard for authentication is DoD-approved PKI certificates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| V-81871      | MongoDB must enforce authorized access to all PKI private keys stored/utilized by MongoDB.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| V-81875      | MongoDB must use NIST FIPS 140-2-validated cryptographic modules for cryptographic operations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| V-81879      | MongoDB must maintain the authenticity of communications sessions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| V-81881      | MongoDB must fail to a secure state if system initialization fails, shutdown fails, or aborts fail.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| V-81883      | MongoDB must protect the confidentiality and integrity of all information at rest.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |V-81887|MongoDB must prevent unauthorized and unintended information transfer.  |                         
|V-81889|MongoDB must check the validity of all data inputs.|
|V-81891|MongoDB operations permit arbitrary JavaScript expressions to be run directly on the server|
|V-81895|A MongoDB or Mongos running with \"security.redactClientLogData\".|
| V-81905      | MongoDB must allocate audit record storage capacity.|
| V-81907      | MongoDB must provide a warning to appropriate support staff when allocated audit.|                                                                                                                                                                                                                                                                                                                                                                                                                                |


## Authors

Defense Information Systems Agency (DISA) https://www.disa.mil/

STIG support by DISA Risk Management Team and Cyber Exchange https://public.cyber.mil/

## Legal Notices

Copyright © 2020 Defense Information Systems Agency (DISA)