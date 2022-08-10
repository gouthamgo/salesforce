# Store-Front Architecture (SFRA)

- A framework for the site desgin 
- CLient/ Sever desgin to offer SAS products 

* Lets understand what catridges are *

## Whats a Cartridge?

- A cartridge is a container for packaging and deploying program code and data. 
- Structured in  folders and sub-folders for maximum efficiency.
- A storefront needs atleast one catridge but typically it has multiple of them.

![catridges](/images/catridges.png)

* Generic Catridegs ==> Contain reusable business functionality ==> to deploy to many sites 
* Application specific catridges ==> Contain merchant-specific and site specific functionality 

### What catridges contain : 

```
Controllers
Form definitions
Scripts
Static content (text, images, CSS files, and client-side JavaScript files)
Templates
Web Services Description Language (WSDL) files
Page Designer experiences (SFRA only)
```
## Steps when working with catridges

```
Here are the steps to take when working with cartridges.

Configure the development environment.
Download reference architecture cartridges.
Review and structure cartridge files on the local drive.
Define and test a cartridge-upload process.
Customize, extend, or overwrite cartridges.
Upload changes to the server.
Register cartridges in Business Manager.
Run the storefront application to test changes.

It’s best practice to extend or override the base cartridges to streamline the development process and ongoing maintenance.
```