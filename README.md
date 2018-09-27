# Deploy an HPC Pack cluster in Azure with Microsoft HPC Pack 2016 Update 1

### **Note:** 
see [Pre-Requisites](#prerequisites) section on this page before starting your deployment.

You can now deploy a Microsoft HPC Pack 2016 cluster in Azure. Choose one from the following templates and click "Deploy to Azure" button to deploy.

---
## Following templates are Active Directory Domain integrated
### Template 1: High-availability cluster for Windows workloads with new Active Directory Domain
This template deploys an HPC Pack cluster with high availability for Windows HPC workloads in Active Directory Domain forest. The cluster includes one domain controller, **three** head nodes, one Database Server with SQL Server 2016 Standard version, and a configurable number of **Windows** compute nodes.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FMsHpcPack%2FHPCPack2016%2Fupdate1%2Fnewcluster-templates%2Fthree-hns-wincn-ad.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### Template 2: High-availability cluster for Windows workloads with existing Active Directory Domain
This template deploys an HPC Pack cluster with high availability for Windows HPC workloads in an existing Active Directory Domain forest. The cluster includes **three** head nodes, one Database Server with SQL Server 2016 Standard version, and a configurable number of **Windows** compute nodes.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FMsHpcPack%2FHPCPack2016%2Fupdate1%2Fnewcluster-templates%2Fthree-hns-wincn-existing-ad.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### Template 3: High-availability cluster with Azure SQL databases for Windows workloads with existing Active Directory Domain
This template deploys an HPC Pack cluster with high availability for Windows HPC workloads in an existing Active Directory Domain forest. The cluster includes **three** head nodes, SQL Azure databases, and a configurable number of **Windows** compute nodes. 

***Note***: Make sure you have enabled **service endpoint for Azure SQL Database(Microsoft.Sql)** on the subnet in which you want to create the cluster.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FMsHpcPack%2FHPCPack2016%2Fupdate1%2Fnewcluster-templates%2Fthree-hns-wincn-existing-ad-sqlazure.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### Template 4: High-availability cluster for Windows workloads with existing Active Directory Domain (No public IP)
This template deploys an HPC Pack cluster with high availability for Windows HPC workloads in an existing Active Directory Domain forest. The cluster includes **three** head nodes, one Database Server with SQL Server 2016 Standard version, and a configurable number of **Windows** compute nodes. No public IP address is created for the head nodes. Use this template if you have a virtual network with Express Route configured and you want to join the cluster to your on-premises Active Directory Domain.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FMsHpcPack%2FHPCPack2016%2Fupdate1%2Fnewcluster-templates%2Fthree-hns-wincn-existing-ad-no-public-ip.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### Template 5: Single head node cluster for Windows workloads with new Active Directory Domain
This template deploys an HPC Pack cluster with one **single** head node for Windows HPC workloads in Active Directory Domain forest. The cluster includes one domain controller, one **single** head node with local databases (SQL server 2016 Express version), and a configurable number of **Windows** compute nodes.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FMsHpcPack%2FHPCPack2016%2Fupdate1%2Fnewcluster-templates%2Fsingle-hn-wincn-ad.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### Template 6: Single head node cluster for Windows workloads with existing Active Directory Domain
This template deploys an HPC Pack cluster with one **single** head node for Windows HPC workloads in an existing Active Directory Domain forest. The cluster includes one **single** head node with local databases (SQL server 2016 Express version), and a configurable number of **Windows** compute nodes.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FMsHpcPack%2FHPCPack2016%2Fupdate1%2Fnewcluster-templates%2Fsingle-hn-wincn-existing-ad.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### Template 7: Single head node cluster for Windows workloads with existing Active Directory Domain (No public IP)
This template deploys an HPC Pack cluster with one **single** head node for Windows HPC workloads in an existing Active Directory Domain forest. The cluster includes one **single** head node with local databases (SQL server 2016 Express version), and a configurable number of **Windows** compute nodes. No public IP address is created for the head nodes. Use this template if you have a virtual network with Express Route configured and you want to join the cluster to your on-premises Active Directory Domain.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FMsHpcPack%2FHPCPack2016%2Fupdate1%2Fnewcluster-templates%2Fsingle-hn-wincn-existing-ad-no-public-ip.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### Template 8: Single head node cluster for Linux workloads with existing Active Directory Domain (No public IP)
This template deploys an HPC Pack cluster with one **single** head node for Windows HPC workloads in an existing Active Directory Domain forest. The cluster includes one **single** head node with local databases (SQL server 2016 Express version), and a configurable number of **Linux** compute nodes. No public IP address is created for the head nodes. Use this template if you have a virtual network with Express Route configured and you want to join the cluster to your on-premises Active Directory Domain.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FMsHpcPack%2FHPCPack2016%2Fupdate1%2Fnewcluster-templates%2Fsingle-hn-lnxcn-existing-ad-no-public-ip.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

---
## Following templates are NOT Active Directory Domain integrated
### Template 1: High-availability cluster for Windows workloads
This template deploys an HPC Pack cluster with high availability for Windows HPC workloads. The cluster includes **three** head nodes, one Database Server with SQL Server 2016 Standard version, and a configurable number of **Windows** compute nodes.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FMsHpcPack%2FHPCPack2016%2Fupdate1%2Fnewcluster-templates%2Fthree-hns-wincn-noad.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### Template 2: High-availability cluster for Linux workloads
This template deploys an HPC Pack cluster with high availability for Windows HPC workloads. The cluster includes **three** head nodes, one Database Server with SQL Server 2016 Standard version, and a configurable number of **Linux** compute nodes.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FMsHpcPack%2FHPCPack2016%2Fupdate1%2Fnewcluster-templates%2Fthree-hns-lnxcn.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### Template 3: Single head node cluster for Windows workloads

This template deploys an HPC Pack cluster with one **single** head node and a configurable number of **Windows** compute nodes. The head node is with local databases (SQL server 2016 Express version).

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FMsHpcPack%2FHPCPack2016%2Fupdate1%2Fnewcluster-templates%2Fsingle-hn-wincn-noad.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

### Template 4: Single head node cluster for Linux workloads

This template deploys an HPC Pack cluster with one **single** head node and a configurable number of **Linux** compute nodes. The head node is with local databases (SQL server 2016 Express version).

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FMsHpcPack%2FHPCPack2016%2Fupdate1%2Fnewcluster-templates%2Fsingle-hn-lnxcn.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

---
## <a name="prerequisites"></a>Pre-Requisites:

### 1. Prepare a PFX certificate
Microsoft HPC Pack 2016 cluster requires a Personal Information Exchange (PFX) certificate to secure the communication between the HPC nodes. The certificate must meet the following requirements: 1.Have a private key capable of **key exchange**; 2.Key usage includes **Digital Signature** and **Key Encipherment**; 3.Enhanced key usage includes **Client Authentication** and **Server Authentication**.You can generate a self-signed certificate which meets the requirements with the following commands and export it as a PFX certificate.

For operating system **Windows 10 or Windows Server 2016**, just run the built-in ***New-SelfSignedCertificate*** command as following:

	New-SelfSignedCertificate -Subject "CN=HPC Pack 2016 Communication" -KeySpec KeyExchange -TextExtension @("2.5.29.37={text}1.3.6.1.5.5.7.3.1,1.3.6.1.5.5.7.3.2") -CertStoreLocation cert:\CurrentUser\My -KeyExportPolicy Exportable -NotAfter (Get-Date).AddYears(5) -NotBefore (Get-Date).AddDays(-1)

For operating system **earlier than Windows 10 or Windows Server 2016**, you can download the [Self-signed certificate generator](https://gallery.technet.microsoft.com/scriptcenter/Self-signed-certificate-5920a7c6/) from Microsoft Script Center. Extract Extract its contents and run the following command.

	Import-Module -Name c:\ExtractedModule\New-SelfSignedCertificateEx.ps1
	New-SelfSignedCertificateEx -Subject "CN=HPC Pack 2016 Communication" -KeySpec Exchange -KeyUsage "DigitalSignature,KeyEncipherment" -EnhancedKeyUsage "Server Authentication","Client Authentication" -StoreLocation CurrentUser -Exportable -NotAfter (Get-Date).AddYears(5) -NotBefore (Get-Date).AddDays(-1)

### 2. Upload the certificate to Azure Key Vault 
Before deploying the HPC cluster, you shall upload the PFX certificate to an Azure Key Vault as a secret, and remember the following information which will be used in deployment: key vault name, resource group name, secret Id, and certificate thumbprint. More details about uploading certificate to Azure Key Vault please see [description of vaultCertificates.certificateUrl]( https://msdn.microsoft.com/en-us/library/mt163591.aspx#bk_vaultcert), or you can refer to the PowerShell script as below.

    #Give the following values
    $VaultName = "mytestvault"
    $SecretName = "hpcpfxcert"
    $VaultRG = "myresourcegroup"
    $location = "westus"
    $PfxFile = "c:\Temp\mytest.pfx"
    $Password = "yourpfxkeyprotectionpassword"
    #Validate the pfx file
    try {
        $pfxCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2 -ArgumentList $PfxFile, $Password
    }
    catch [System.Management.Automation.MethodInvocationException]
    {
        throw $_.Exception.InnerException
    }
    $thumbprint = $pfxCert.Thumbprint
    $pfxCert.Dispose()
    # Create and encode the JSON object
    $pfxContentBytes = Get-Content $PfxFile -Encoding Byte
    $pfxContentEncoded = [System.Convert]::ToBase64String($pfxContentBytes)
    $jsonObject = @"
    {
    "data": "$pfxContentEncoded",
    "dataType": "pfx",
    "password": "$Password"
    }
    "@
    $jsonObjectBytes = [System.Text.Encoding]::UTF8.GetBytes($jsonObject)
    $jsonEncoded = [System.Convert]::ToBase64String($jsonObjectBytes)
    #Create an Azure key vault and upload the certificate as a secret
    $secret = ConvertTo-SecureString -String $jsonEncoded -AsPlainText -Force
    $rg = Get-AzureRmResourceGroup -Name $VaultRG -Location $location -ErrorAction SilentlyContinue
    if($null -eq $rg)
    {
        $rg = New-AzureRmResourceGroup -Name $VaultRG -Location $location
    }
    $hpcKeyVault = New-AzureRmKeyVault -VaultName $VaultName -ResourceGroupName $VaultRG -Location $location -EnabledForDeployment -EnabledForTemplateDeployment
    $hpcSecret = Set-AzureKeyVaultSecret -VaultName $VaultName -Name $SecretName -SecretValue $secret
    "The following Information will be used in the deployment template"
    "Vault Name             :   $VaultName"
    "Vault Resource Group   :   $VaultRG"
    "Certificate URL        :   $($hpcSecret.Id)"
    "Certificate Thumbprint :   $thumbprint"
