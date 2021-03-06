# canonical-ubuntu-18.04-lts-server-cis-baseline

InSpec profile to validate the secure configuration of Canonical Ubuntu 18.04 LTS Server against the [CIS'](https://www.cisecurity.org/cis-benchmarks/) - CIS Ubuntu Linux 18.04 LTS Benchmark v2.0.1.

## Getting Started

It is intended and recommended that InSpec and this profile overlay be run from a __"runner"__ host (such as a DevOps orchestration server, an administrative management system, or a developer's workstation/laptop) against the target remotely over __ssh__.

__For the best security of the runner, always install on the runner the _latest version_ of InSpec and supporting Ruby language components.__ 

Latest versions and installation options are available at the [InSpec](http://inspec.io/) site.

## Tailoring to Your Environment

The following inputs may be configured in an inputs ".yml" file for the profile to run correctly for your specific environment. More information about InSpec inputs can be found in the [InSpec Profile Documentation](https://www.inspec.io/docs/reference/profiles/).

```yaml
# Name of the OS/Platform
platform_name: ''

# Release number of the OS/Platform
platform_release: 18.04

# Support end date for OS/Platform security updates
supported_until: ''

# Audit log file path
log_file_path: ''

# Audit log file directory
log_file_dir: ''

# Organization Name
org_name: ''

# Banner message text for command line interface logins.
banner_message_text_cli: ''

# Banner message text for resource-limited command line interface logins.
banner_message_text_cli_limited: ''

# These shells do not allow a user to login
non_interactive_shells: []
```

# Running This Baseline Directly from Github

```
# How to run
inspec exec https://github.com/mitre/canonical-ubuntu-18.04-lts-server-cis-baseline/archive/master.tar.gz -t ssh://TARGET_USERNAME:TARGET_PASSWORD@TARGET_IP:TARGET_PORT --sudo --sudo-password=<SUDO_PASSWORD_IF_REQUIRED> --input-file=<path_to_your_inputs_file/name_of_your_inputs_file.yml> --reporter=cli json:<path_to_your_output_file/name_of_your_output_file.json>
```

### Different Run Options

  [Full exec options](https://docs.chef.io/inspec/cli/#options-3)

## Running This Baseline from a local Archive copy 

If your runner is not always expected to have direct access to GitHub, use the following steps to create an archive bundle of this baseline and all of its dependent tests:

(Git is required to clone the InSpec profile using the instructions below. Git can be downloaded from the [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) site.)

When the __"runner"__ host uses this profile baseline for the first time, follow these steps: 

```
mkdir profiles
cd profiles
git clone https://github.com/mitre/canonical-ubuntu-18.04-lts-server-cis-baseline
inspec archive canonical-ubuntu-18.04-lts-server-cis-baseline
inspec exec <name of generated archive> -t ssh://TARGET_USERNAME:TARGET_PASSWORD@TARGET_IP:TARGET_PORT --sudo --sudo-password=<SUDO_PASSWORD_IF_REQUIRED> --input-file=<path_to_your_inputs_file/name_of_your_inputs_file.yml> --reporter=cli json:<path_to_your_output_file/name_of_your_output_file.json>
```
For every successive run, follow these steps to always have the latest version of this baseline:

```
cd canonical-ubuntu-18.04-lts-server-cis-baseline
git pull
cd ..
inspec archive canonical-ubuntu-18.04-lts-server-cis-baseline --overwrite
inspec exec <name of generated archive> -t ssh://TARGET_USERNAME:TARGET_PASSWORD@TARGET_IP:TARGET_PORT --sudo --sudo-password=<SUDO_PASSWORD_IF_REQUIRED> --input-file=<path_to_your_inputs_file/name_of_your_inputs_file.yml> --reporter=cli json:<path_to_your_output_file/name_of_your_output_file.json>
```

## Viewing the JSON Results

The JSON results output file can be loaded into __[heimdall-lite](https://heimdall-lite.mitre.org/)__ for a user-interactive, graphical view of the InSpec results. 

The JSON InSpec results file may also be loaded into a __[full heimdall server](https://github.com/mitre/heimdall)__, allowing for additional functionality such as to store and compare multiple profile runs.

## Authors
* MITRE SAF Team

## Special Thanks
* Mohamed El-Sharkawi - [HackerShark](https://github.com/HackerShark)
* Shivani Karikar - [karikarshivani](https://github.com/karikarshivani)

## Contributing and Getting Help
To report a bug or feature request, please open an [issue](https://github.com/mitre/canonical-ubuntu-18.04-lts-server-cis-baseline/issues/new).

## Development, Testing and PRs

```
Describe our testing, and development process here
```
<https://kitchen.ci> has great documeation if you need a reference.
#### Our Pull Request Process
1. Fork the repo
2. Create a branch for your update
3. Update the control or controls
4. If needed, update the hardening content in the `spec` diretory
5. Lint your changes with `inspec check .` at the root of the profile
6. Run the Test Kitchen test suite to ensure your changes will pas CI
7. Submit a PR of your banch aginst the upstream master

#### Test Kitchen Steps

#### Create
This creates a base test target you can use for local testing
- Vanilla & Hardened
``` 
KITCHEN_LOCAL_YAML=kitchen.vagrant.yml CHEF_LICENSE=accept kitchen create vanilla-ubuntu-1804 

KITCHEN_LOCAL_YAML=kitchen.vagrant.yml CHEF_LICENSE=accept kitchen create hardened-ubuntu-1804
```

#### Converge
This runs the configuration managment content on the created host
- Vanilla & Hardened
```
KITCHEN_LOCAL_YAML=kitchen.vagrant.yml CHEF_LICENSE=accept kitchen create vanilla-ubuntu-1804

KITCHEN_LOCAL_YAML=kitchen.vagrant.yml CHEF_LICENSE=accept kitchen create hardened-ubuntu-1804
```

#### Verify
This runs the inspec validation profile aginst the host
- Vanilla & Hardened
```
KITCHEN_LOCAL_YAML=kitchen.vagrant.yml CHEF_LICENSE=accept kitchen verify vanilla-ubuntu-1804

KITCHEN_LOCAL_YAML=kitchen.vagrant.yml CHEF_LICENSE=accept kitchen verify hardened-ubuntu-1804
```

#### Destroy
This will clean up and destroy your testing host

- Vanilla & Hardened
```
KITCHEN_LOCAL_YAML=kitchen.vagrant.yml CHEF_LICENSE=accept kitchen verify vanilla-ubuntu-1804

KITCHEN_LOCAL_YAML=kitchen.vagrant.yml CHEF_LICENSE=accept kitchen verify hardened-ubuntu-1804
```

## Update to the repo and sub-modules

Update submodules
```
git submodule update --init --recursive
git submodule update --remote
```

## NOTICE

?? 2018-2020 The MITRE Corporation.

Approved for Public Release; Distribution Unlimited. Case Number 18-3678.

## NOTICE  

MITRE hereby grants express written permission to use, reproduce, distribute, modify, and otherwise leverage this software to the extent permitted by the licensed terms provided in the LICENSE.md file included with this project.

## NOTICE  

This software was produced for the U. S. Government under Contract Number HHSM-500-2012-00008I, and is subject to Federal Acquisition Regulation Clause 52.227-14, Rights in Data-General.  

No other use other than that granted to the U. S. Government, or to those acting on behalf of the U. S. Government under that Clause is authorized without the express written permission of The MITRE Corporation. 

For further information, please contact The MITRE Corporation, Contracts Management Office, 7515 Colshire Drive, McLean, VA  22102-7539, (703) 983-6000.

## NOTICE

CIS Benchmarks are published by the Center for Internet Security (CIS), see: https://www.cisecurity.org/.
