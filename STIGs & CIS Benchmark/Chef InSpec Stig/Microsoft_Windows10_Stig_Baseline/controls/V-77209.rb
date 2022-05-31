# -*- encoding : utf-8 -*-

control 'V-77209' do
  title 'Exploit Protection mitigations in Windows 10 must be configured for FLTLDR.EXE.'
  desc  "Exploit protection in Windows 10 provides a means of enabling
        additional mitigations against potential threats at the system and application
        level. Without these additional application protections, Windows 10 may be
        subject to various exploits."
  impact 0.5
  tag severity: 'medium'
  tag gtitle: 'WN10-EP-000120'
  tag gid: 'V-77209'
  tag rid: 'SV-91905r3_rule'
  tag stig_id: 'WN10-EP-000120'
  tag fix_id: 'F-84341r4_fix'
  tag cci: ['CCI-000366']
  tag nist: ['CM-6 b', 'Rev_4']
  tag false_negatives: nil
  tag false_positives: nil
  tag documentable: false
  tag mitigations: nil
  tag severity_override_guidance: false
  tag potential_impacts: nil
  tag third_party_tools: nil
  tag mitigation_controls: nil
  tag responsibility: nil
  tag ia_controls: nil
  desc 'check', "This is NA prior to v1709 of Windows 10.

      This is applicable to unclassified systems, for other systems this is NA.

      Run \"Windows PowerShell\" with elevated privileges (run as administrator).

      Enter \"Get-ProcessMitigation -Name FLTLDR.EXE\".
      (Get-ProcessMitigation can be run without the -Name parameter to get a list of
      all application mitigations configured.)

      If the following mitigations do not have the listed status which is shown below, this is a finding:

      DEP:
      Override DEP: False

      ImageLoad:
      OverrideBlockRemoteImages: False

      Payload:
      OverrideExportAddressFilter: False
      OverrideExportAddressFilterPlus: False
      OverrideImportAddressFilter: False
      OverrideEnableRopStackPivot: False
      OverrideEnableRopCallerCheck: False
      OverrideEnableRopSimExec: False

      Child Process:
      OverrideChildProcess: False

      The PowerShell command produces a list of mitigations; only those with a 
      required status are listed here. If the PowerShell command does not
      produce results, ensure the letter case of the filename within the command
      syntax matches the letter case of the actual filename on the system."
  desc 'fix', "Ensure the following mitigations are configured as shown for FLTLDR.EXE:

      DEP:
      OverrideDEP: False

      ImageLoad:
      OverrideBlockRemoteImages: False

      Payload:
      OverrideExportAddressFilter: False
      OverrideExportAddressFilterPlus: False
      OverrideImportAddressFilter: False
      OverrideEnableRopStackPivot: False
      OverrideEnableRopCallerCheck: False
      OverrideEnableRopSimExec: False

      Child Process:
      OverrideChildProcess: False

      Application mitigations defined in the STIG are configured by a DoD EP XML file
      included with the Windows 10 STIG package in the \"Supporting Files\" folder.

      The XML file is applied with the group policy setting Computer Configuration >>
      Administrative Settings >> Windows Components >> Windows Defender Exploit Guard
      >> Exploit Protection >> \"Use a common set of exploit protection settings\"
      configured to \"Enabled\" with file name and location defined under
      \"Options:\".  It is recommended the file be in a read-only network location."

  if input('sensitive_system') == 'true' || nil
    impact 0.0
    describe 'This Control is Not Applicable to sensitive systems.' do
      skip 'This Control is Not Applicable to sensitive systems.'
    end
  elsif registry_key('HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion').ReleaseId < '1709'
    impact 0.0
    describe 'This STIG does not apply to Prior Versions before 1709.' do
      skip 'This STIG does not apply to Prior Versions before 1709.'
    end
  else
     dep = json( command: 'Get-ProcessMitigation -Name FLTLDR.EXE | Select DEP | ConvertTo-Json').params
       describe 'OverRide DEP is required to be false on FLTLDR' do
        subject { dep }
        its(['OverrideDEP']) { should eq 'false' }
       end
      imageload = json( command: 'Get-ProcessMitigation -Name FLTLDR.EXE | Select ImageLoad | ConvertTo-Json').params
       describe 'OverRide ImageLoad Block Remote Image Loads is required to be false on FLTLDR' do
        subject { imageload }
        its(['OverrideBlockRemoteImage']) { should eq 'false' }
       end
      payload = json( command: 'Get-ProcessMitigation -Name FLTLDR.EXE | Select Payload | ConvertTo-Json').params
       describe 'Override Payload ExportAddressFilter, Override Payload ExportAddressFilterPlus, Override ImportAddressFilter, Override EnableRopStackPivot, Override EnableRopCallerCheck, and Override EnableRopSimExec are required to be false on Adobe Reader' do
       subject { payload }
       its(['OverrideExportAddressFilter']) { should eq 'false' }
       its(['OverrideExportAddressFilterPlus']) { should eq 'false' }
       its(['OverrideImportAddressFilter']) { should eq 'false' }
       its(['OverrideEnableRopStackPivot']) { should eq 'false' }
       its(['OverrideEnableRopCallerCheck']) { should eq 'false' }
       its(['OverrideEnableRopSimExec']) { should eq 'false' }
       end
      child_process = json( command: 'Get-ProcessMitigation -Name FLTLDR.EXE | Select ChildProcess | ConvertTo-Json').params
       describe 'OverRide Child Process is required to be false on FLTLDR' do
        subject { child_process }
        its(['OverrideChildProcess']) { should eq 'false' }
       end
   end
end