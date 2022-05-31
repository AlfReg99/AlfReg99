
def getGroupNameFromGroupId(groupId):
    return groups[groupId]

def getFamilyNameFromFamilyId(familyId):
    return families[familyId]


families={
    "1" : "Account Policies",
    "2" : "Local Policies",
    "3" : "Event Log",
    "4" : "Restricted Groups",
    "5" : "System Services",
    "6" : "Registry",
    "7" : "File System",
    "8" : "Wired Network (IEEE 802.3) Policies",
    "9" : "Windows Defender Firewall with Advanced Security (formerly Windows Firewall with Advanced Security)",
    "10" : "Network List Manager Policies",
    "11" : "Wireless Network (IEEE 802.11) Policies",
    "12" : "Public Key Policies",
    "13" : "Software Restriction Policies",
    "14" : "Network Access Protection NAP Client Configuration",
    "15" : "Application Control Policies",
    "16" : "IP Security Policies",
    "17" : "Advanced Audit Policy Configuration",
    "18" : "Administrative Templates (Computer)",
    "19" : "Administrative Templates (User)"
}

groups={
    "1.1" : "Password Policy",
    "1.2" : "Account Lockout Policy",
    "2.1" : "Audit Policy",
    "2.2" : "User Rights Assignment",
    "2.3" : "Security Options",
    "2.3.1" : "Accounts",
    "2.3.2" : "Audit",
    "2.3.3" : "DCOM",
    "2.3.4" : "Devices",
    "2.3.5" : "Domain controller",
    "2.3.6" : "Domain member",
    "2.3.7" : "Interactive logon",
    "2.3.8" : "Microsoft network client",
    "2.3.9" : "Microsoft network server",
    "2.3.10" : "Network access",
    "2.3.11" : "Network security",
    "2.3.12" : "Recovery console",
    "2.3.13" : "Shutdown",
    "2.3.14" : "System cryptography",
    "2.3.15" : "System objects",
    "2.3.16" : "System settings",
    "2.3.17" : "User Account Control",
    "9.1" : "Domain Profile",
    "9.2" : "Private Profile",
    "9.3" : "Public Profile",
    "17.1" : "Account Logon",
    "17.2" : "Account Management",
    "17.3" : "Detailed Tracking",
    "17.4" : "DS Access",
    "17.5" : "Logon/Logoff",
    "17.6" : "Object Access",
    "17.7" : "Policy Change",
    "17.8" : "Privilege Use",
    "17.9" : "System",
    "18.1" : "Control Panel",
    "18.1.1" : "Personalization",
    "18.1.2" : "Regional and Language Options",
    "18.1.2.1" : "Handwriting personalization",
    "18.2" : "LAPS",
    "18.3" : "MS Security Guide",
    "18.4" : "MSS (Legacy)",
    "18.5" : "Network",
    "18.5.1" : "Background Intelligent Transfer Service (BITS)",
    "18.5.2" : "BranchCache",
    "18.5.3" : "DirectAccess Client Experience Settings",
    "18.5.4" : "DNS Client",
    "18.5.5" : "Fonts",
    "18.5.6" : "Hotspot Authentication",
    "18.5.7" : "Lanman Server",
    "18.5.8" : "Lanman Workstation",
    "18.5.9" : "Link-Layer Topology Discovery",
    "18.5.10" : "Microsoft Peer-to-Peer Networking Services",
    "18.5.10.1" : "Peer Name Resolution Protocol",
    "18.5.11" : "Network Connections",
    "18.5.11.1" : "Windows Defender Firewall (formerly Windows Firewall)",
    "18.5.12" : "Network Connectivity Status Indicator",
    "18.5.13" : "Network Isolation",
    "18.5.14" : "Network Provider",
    "18.5.15" : "Offline Files",
    "18.5.16" : "QoS Packet Scheduler",
    "18.5.17" : "SNMP",
    "18.5.18" : "SSL Configuration Settings",
    "18.5.19" : "TCPIP Settings",
    "18.5.19.1" : "IPv6 Transition Technologies",
    "18.5.19.2" : "Parameters",
    "18.5.20" : "Windows Connect Now",
    "18.5.21": "Windows Connection Manager",
    "18.5.22" : "Wireless Display",
    "18.5.23" : "WLAN Service",
    "18.5.23.1" : "WLAN Media Cost",
    "18.5.23.2" : "WLAN Settings",
    "18.6" : "Printers",
    "18.7" : "Start Menu and Taskbar",
    "18.7.1" : "Notifications",
    "18.8" : "System",
    "18.8.1" : "Access-Denied Assistance",
    "18.8.2" : "App-V",
    "18.8.3" : "Audit Process Creation",
    "18.8.4" : "Credentials Delegation",
    "18.8.5" : "Device Guard",
    "18.8.6" : "Device Health Attestation Service",
    "18.8.7" : "Device Installation",
    "18.8.7.1" : "Device Installation Restrictions",
    "18.8.8" : "Device Redirection",
    "18.8.9" : "Disk NV Cache",
    "18.8.10" : "Disk Quotas",
    "18.8.11" : "Display",
    "18.8.12" : "Distributed COM",
    "18.8.13" : "Driver Installation",
    "18.8.14" : "Early Launch Antimalware",
    "18.8.15" : "Enhanced Storage Access",
    "18.8.16" : "File Classification Infrastructure",
    "18.8.17" : "File Share Shadow Copy Agent",
    "18.8.18" : "File Share Shadow Copy Provider",
    "18.8.19" : "Filesystem (formerly NTFS Filesystem)",
    "18.8.20" : "Folder Redirection",
    "18.8.21" : "Group Policy",
    "18.8.21.1" : "Logging and tracing",
    "18.8.22" : "Internet Communication Management",
    "18.8.22.1" : "Internet Communication settings",
    "18.8.23" : "iSCSI",
    "18.8.24" : "KDC",
    "18.8.25" : "Kerberos",
    "18.8.26" : "Kernel DMA Protection",
    "18.8.27" : "Locale Services",
    "18.8.28" : "Logon",
    "18.8.29" : "Mitigation Options",
    "18.8.30" : "Net Logon",
    "18.8.31" : "OS Policies",
    "18.8.32" : "Performance Control Panel",
    "18.8.33" : "PIN Complexity",
    "18.8.34" : "Power Management",
    "18.8.34.1" : "Button Settings",
    "18.8.34.2" : "Energy Saver Settings",
    "18.8.34.3" : "Hard Disk Settings",
    "18.8.34.4" : "Notification Settings",
    "18.8.34.5" : "Power Throttling Settings",
    "18.8.34.6" : "Sleep Settings",
    "18.8.35" : "Recovery",
    "18.8.36" : "Remote Assistance",
    "18.8.37" : "Remote Procedure Call",
    "18.8.38" : "Removable Storage Access",
    "18.8.39" : "Scripts",
    "18.8.40" : "Security Account Manager",
    "18.8.41" : "Server Manager",
    "18.8.42" : "Service Control Manager Settings",
    "18.8.43" : "Shutdown",
    "18.8.44" : "Shutdown Options",
    "18.8.45" : "Storage Health",
    "18.8.46" : "Storage Sense",
    "18.8.47" : "System Restore",
    "18.8.48" : "Troubleshooting and Diagnostics",
    "18.8.48.1" : "Application Compatibility Diagnostics",
    "18.8.48.2" : "Corrupted File Recovery",
    "18.8.48.3" : "Disk Diagnostic",
    "18.8.48.4" : "Fault Tolerant Heap",
    "18.8.48.5" : "Microsoft Support Diagnostic Tool",
    "18.8.48.6" : "MSI Corrupted File Recovery",
    "18.8.48.7" : "Scheduled Maintenance",
    "18.8.48.8" : "Scripted Diagnostics",
    "18.8.48.9" : "Windows Boot Performance Diagnostics",
    "18.8.48.10" : "Windows Memory Leak Diagnosis",
    "18.8.48.11" : "Windows Performance PerfTrack",
    "18.8.49" : "Trusted Platform Module Services",
    "18.8.50" : "User Profiles",
    "18.8.51" : "Windows File Protection",
    "18.8.52" : "Windows HotStart",
    "18.8.53" : "Windows Time Service",
    "18.5.53.1" : "Time Providers",
    "18.9" : "Windows Components",
    "18.9.1" : "Active Directory Federation Services",
    "18.9.2" : "ActiveX Installer Service",
    "18.9.3" : "Add features to Windows 8 / 8.1 / 10 (formerly Windows Anytime Upgrade)",
    "18.9.4" : "App Package Deployment",
    "18.9.5" : "App Privacy",
    "18.9.6" : "App runtime",
    "18.9.7" : "Application Compatibility",
    "18.9.8" : "AutoPlay Policies",
    "18.9.9" : "Backup",
    "18.9.10" : "Biometrics",
    "18.9.10.1" : "Facial Features",
    "18.9.11" : "BitLocker Drive Encryption",
    "18.9.11.1" : "Fixed Data Drives",
    "18.9.11.2" : "Operating System Drives",
    "18.9.11.3" : "Removable Data Drives",
    "18.9.12" : "Camera",
    "18.9.13" : "Chat",
    "18.9.14" : "Cloud Content",
    "18.9.15" : "Connect",
    "18.9.16" : "Credential User Interface",
    "18.9.17" : "Data Collection and Preview Builds",
    "18.9.18" : "Delivery Optimization",
    "18.9.19" : "Desktop Gadgets",
    "18.9.20" : "Desktop Window Manager",
    "18.9.21" : "Device and Driver Compatibility",
    "18.9.22" : "Device Registration (formerly Workplace Join)",
    "18.9.23" : "Digital Locker",
    "18.9.24" : "Edge UI",
    "18.9.25" : "EMET",
    "18.9.26" : "Event Forwarding",
    "18.9.27" : "Event Log Service",
    "18.9.27.1" : "Application",
    "18.9.27.2" : "Security",
    "18.9.27.3" : "Setup",
    "18.9.27.4" : "System",
    "18.9.28" : "Event Logging",
    "18.9.29" : "Event Viewer",
    "18.9.30" : "Family Safety (formerly Parental Controls)",
    "18.9.31" : "File Explorer (formerly Windows Explorer)",
    "18.9.31.1" : "Previous Versions",
    "18.9.32" : "File History",
    "18.9.33" : "Find My Device",
    "18.9.34" : "Game Explorer",
    "18.9.35" : "Handwriting",
    "18.9.36" : "HomeGroup",
    "18.9.37" : "Human Presence",
    "18.9.38" : "Import Video",
    "18.9.39" : "Internet Explorer",
    "18.9.40" : "Internet Information Services",
    "18.9.41" : "Location and Sensors",
    "18.9.42" : "Maintenance Scheduler",
    "18.9.43" : "Maps",
    "18.9.44" : "MDM",
    "18.9.45" : "Messaging",
    "18.9.46" : "Microsoft account",
    "18.9.47" : "Microsoft Defender Antivirus (formerly Windows Defender and Windows Defender Antivirus)",
    "18.9.47.1" : "Client Interface",
    "18.9.47.2" : "Device Control",
    "18.9.47.3" : "Exclusions",
    "18.9.47.4" : "MAPS",
    "18.9.47.5" : "Microsoft Defender Exploit Guard (formerly Windows Defender Exploit Guard)",
    "18.9.47.5.1" : "Attack Surface Reduction",
    "18.9.47.5.2" : "Controlled Folder Access",
    "18.9.47.5.3" : "Network Protection",
    "18.9.47.6" : "MpEngine",
    "18.9.47.7" : "Network Inspection System",
    "18.9.47.8" : "Quarantine",
    "18.9.47.9" : "Real-time Protection",
    "18.9.47.10" : "Remediation",
    "18.9.47.11" : "Reporting",
    "18.9.47.12" : "Scan",
    "18.9.47.13" : "Security Intelligence Updates (formerly Signature Updates)",
    "18.9.47.14" : "Threats",
    "18.9.48" : "Microsoft Defender Application Guard (formerly Windows Defender Application Guard)",
    "18.9.49" : "Microsoft Defender Exploit Guard (formerly Windows Defender Exploit Guard)",
    "18.9.50" : "Microsoft Edge",
    "18.9.51" : "Microsoft FIDO Authentication",
    "18.9.52" : "Microsoft Secondary Authentication Factor",
    "18.9.53" : "Microsoft User Experience Virtualization",
    "18.9.54" : "NetMeeting",
    "18.9.55" : "Network Access Protection",
    "18.9.56" : "Network Projector",
    "18.9.57" : "News and interests",
    "18.9.58" : "OneDrive (formerly SkyDrive)",
    "18.9.59" : "Online Assistance",
    "18.9.60" : "OOBE",
    "18.9.61" : "Password Synchronization",
    "18.9.62" : "Portable Operating System",
    "18.9.63" : "Presentation Settings",
    "18.9.64" : "Push To Install",
    "18.9.65" : "Remote Desktop Services (formerly Terminal Services)",
    "18.9.65.1" : "RD Licensing (formerly TS Licensing)",
    "18.9.65.2" : "Remote Desktop Connection Client",
    "18.9.65.2.1" : "RemoteFX USB Device Redirection",
    "18.9.65.3" : "Remote Desktop Session Host (formerly Terminal Server)",
    "18.9.65.3.1" : "Application Compatibility",
    "18.9.65.3.2" : "Connections",
    "18.9.65.3.3" : "Device and Resource Redirection",
    "18.9.65.3.4" : "Licensing",
    "18.9.65.3.5" : "Printer Redirection",
    "18.9.65.3.6" : "Profiles",
    "18.9.65.3.7" : "RD Connection Broker (formerly TS Connection Broker)",
    "18.9.65.3.8" : "Remote Session Environment",
    "18.9.65.3.9" : "Security",
    "18.9.65.3.10" : "Session Time Limits",
    "18.9.65.3.11" : "Temporary folders",
    "18.9.66" : "RSS Feeds",
    "18.9.67" : "Search",
    "18.9.67.1" : "OCR",
    "18.9.68" : "Security Center",
    "18.9.69" : "Server for NIS",
    "18.9.70" : "Shutdown Options",
    "18.9.71" : "Smart Card",
    "18.9.72" : "Software Protection Platform",
    "18.9.73" : "Sound Recorder",
    "18.9.74" : "Speech",
    "18.9.75" : "Store",
    "18.9.76" : "Sync your settings",
    "18.9.77" : "Tablet PC",
    "18.9.78" : "Task Scheduler",
    "18.9.79" : "Tenant Restrictions",
    "18.9.80" : "Text Input",
    "18.9.81" : "Widgets",
    "18.9.82" : "Windows Calendar",
    "18.9.83" : "Windows Color System",
    "18.9.84" : "Windows Customer Experience Improvement Program",
    "18.9.85" : "Windows Defender SmartScreen",
    "18.9.85.1" : "Explorer",
    "18.9.85.2" : "Microsoft Edge",
    "18.9.86" : "Windows Error Reporting",
    "18.9.87" : "Windows Game Recording and Broadcasting",
    "18.9.88" : "Windows Hello for Business (formerly Microsoft Passport for Work)",
    "18.9.89" : "Windows Ink Workspace",
    "18.9.90" : "Windows Installer",
    "18.9.91" : "Windows Logon Options",
    "18.9.92" : "Windows Mail",
    "18.9.93" : "Windows Media Center",
    "18.9.94" : "Windows Media Digital Rights Management",
    "18.9.95" : "Windows Media Player",
    "18.9.96" : "Windows Meeting Space",
    "18.9.97" : "Windows Messenger",
    "18.9.98" : "Windows Mobility Center",
    "18.9.99" : "Windows Movie Maker",
    "18.9.100" : "Windows PowerShell",
    "18.9.101" : "Windows Reliability Analysis",
    "18.9.102" : "Windows Remote Management (WinRM)",
    "18.9.102.1" : "WinRM Client",
    "18.9.102.2" : "WinRM Service",
    "18.9.103" : "Windows Remote Shell",
    "18.9.104" : "Windows Sandbox",
    "18.9.105" : "Windows Security (formerly Windows Defender Security Center)",
    "18.9.105.1" : "Account protection",
    "18.9.105.2" : "App and browser protection",
    "18.9.106" : "Windows SideShow",
    "18.9.107" : "Windows System Resource Manager",
    "18.9.108" : "Windows Update",
    "18.9.108.1" : "Legacy Policies",
    "18.9.108.2" : "Manage end user experience",
    "18.9.108.3" : "Manage updates offered from Windows Server Update Service",
    "18.9.108.4" : "Manage updates offered from Windows Update (formerly Defer Windows Updates and Windows Update for Business)",
    "19.1" : "Control Panel",
    "19.1.1" : "Add or Remove Programs",
    "19.1.2" : "Display",
    "19.1.3" : "Personalization (formerly Desktop Themes)",
    "19.2" : "Desktop",
    "19.3" : "Network",
    "19.4" : "Shared Folders",
    "19.5" : "Start Menu and Taskbar",
    "19.5.1" : "Notifications",
    "19.6" : "System",
    "19.6.1" : "Ctrl+Alt+Del Options",
    "19.6.2" : "Display",
    "19.6.3" : "Driver Installation",
    "19.6.4" : "Folder Redirection",
    "19.6.5" : "Group Policy",
    "19.6.6" : "Internet Communication Management",
    "19.6.6.1" : "Internet Communication settings",
    "19.7" : "Windows Components",
    "19.7.1" : "Add features to Windows 8 / 8.1 / 10 (formerly Windows Anytime Upgrade)",
    "19.7.2" : "App runtime",
    "19.7.3" : "Application Compatibility",
    "19.7.4" : "Attachment Manager",
    "19.7.5" : "AutoPlay Policies",
    "19.7.6" : "Backup",
    "19.7.7" : "Calculator",
    "19.7.8" : "Cloud Content",
    "19.7.9" : "Credential User Interface",
    "19.7.10" : "Data Collection and Preview Builds",
    "19.7.11" : "Desktop Gadgets",
    "19.7.12" : "Desktop Window Manager",
    "19.7.13" : "Digital Locker",
    "19.7.14" : "Edge UI",
    "19.7.15" : "File Explorer (formerly Windows Explorer)",
    "19.7.16" : "File Revocation",
    "19.7.17" : "IME",
    "19.7.18" : "Import Video",
    "19.7.19" : "Instant Search",
    "19.7.20" : "Internet Explorer",
    "19.7.21" : "Location and Sensors",
    "19.7.22" : "Microsoft Edge",
    "19.7.23" : "Microsoft Management Console",
    "19.7.24" : "Microsoft User Experience Virtualization",
    "19.7.25" : "Multitasking",
    "19.7.26" : "NetMeeting",
    "19.7.27" : "Network Projector",
    "19.7.28" : "Network Sharing",
    "19.7.29" : "OOBE",
    "19.7.30" : "Presentation Settings",
    "19.7.31" : "Remote Desktop Services (formerly Terminal Services)",
    "19.7.32" : "RSS Feeds",
    "19.7.33" : "Search",
    "19.7.34" : "Sound Recorder",
    "19.7.35" : "Store",
    "19.7.36" : "Tablet PC",
    "19.7.37" : "Task Scheduler",
    "19.7.38" : "Windows Calendar",
    "19.7.39" : "Windows Color System",
    "19.7.40" : "Windows Defender SmartScreen",
    "19.7.41" : "Windows Error Reporting",
    "19.7.42" : "Windows Hello for Business (formerly Microsoft Passport for Work)",
    "19.7.43" : "Windows Installer",
    "19.7.44" : "Windows Logon Options",
    "19.7.45" : "Windows Mail",
    "19.7.46" : "Windows Media Center",
    "19.7.47" : "Windows Media Player",
    "19.7.47.1" : "Networking",
    "19.7.47.2" : "Playback"
}