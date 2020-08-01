# docassemble.hmlrhelper (beta)

A docassemble extension that allows you to submit [HM Land Registry (HMLR) forms](https://www.gov.uk/topic/land-registration/searches-fees-forms) to [DocuSign](https://www.docusign.com) through the [DocuSign API](https://developers.docusign.com/) from inside Docassemble interviews.

This extension makes use of the awesome [docassemble.docusign](https://pypi.org/project/docassemble.docusign/) 
extension created by the lovely people at [Radiant Law](https://radiantlaw.com/).

## Current limitations

This implementation is currently limited to TR1's, and is intended to meet the 
requirements for electronic signatures as set out in the *13.3 Our Requirements* section 
of [Practice guide 8: execution of deeds ](https://www.gov.uk/government/publications/execution-of-deeds/practice-guide-8-execution-of-deeds#our-requirements).

* Works for person to person transfers only. There are different requirements and wording 
if the transfer is being signed by an attorney or company, or at the direction of the transferor.
* HMLR will accept up to four transferees listed on the TR1 ([see guidance](https://www.gov.uk/government/publications/registered-titles-whole-transfer-tr1/guidance-completing-form-tr1-for-the-transfer-of-registered-property)) however:
    * the size of Box 12 (Execution) on the sample TR1 that this interview populates means there is a 
    practical limitation of a maximum of 4 signatories and their and associated witnesses (counting both transferors 
    and transferees and noting that transferres don't always need to sign).
    * A simple way to improve on this would be the use of a template file where Box 12 (Execution) was extended to use 
    the full space available on page three.
* The conveyancer still needs to date the deed at the end of the process and submit it to HMLR 'manually'. 

## Installation & Prerequisites

1. Install [docassemble.docusign](https://pypi.org/project/docassemble.docusign/) first. Follow the setup and testing process within *docassemble.docusign* to ensure that you can psuh documents into DocuSign for signature successfully.

1. Install this package (docassemble.hmlrhelper) from within your Docassemble package management screen using either the GitHub or PyPi addresses:

    - [https://github.com/mattpennington/docassemble-hmlrhelper](https://github.com/mattpennington/docassemble-hmlrhelper)

    - [docassemble.hmlrhelper on PyPi](#)

## Configuration & Testing

After you've tested *docassemble.docusign* above, and with the extension still in 
test mode (`test-mode: True`) run the test interview at:

{YOUR SERVER BASE URL}/interview?i=docassemble.hmlrhelper:data/questions/test.yml.

1. The interview will allow you to push a sample populated TR1 into DocuSign and run through a working demo of the signatory process.
1. The DocuSign sandbox will send all emails to the the email address of the DocuSign sandbox user you created when setting up *docassemble.docusign*
1. The test interview asks for a mobile phone number that will be used for all SMS's for the Two Factor Authentication. Please use your own mobile number! :-)

## Interview Process within Docassemble

1. something...
1. Document is pushed to Docusign and workflow completed in Docassemble

## Process within Docusign

1. 1st **Transferor** clicks document link in email
1. 1st **Transferor** completes Two Factor Authentication by SMS to access document
1. 1st **Transferor** signs deed
1. 1st **Transferor Witness** clicks document link in email
1. 1st **Transferor Witness** completes Two Factor Authentication by SMS to access document
1. 1st **Transferor Witness** witnesses 1st **Transferor** signature and signs deed
1. (Repeat for all transferors)
1. If **Transferees** need to sign too...
    1. 1st **Transferee** clicks document link in email
    1. 1st **Transferee** completes Two Factor Authentication by SMS to access document
    1. 1st **Transferee** signs deed
    1. 1st **Transferee Witness** clicks document link in email
    1. 1st **Transferee Witness** completes Two Factor Authentication by SMS to access document
    1. 1st **Transferee Witness** witnesses 1st **Transferee** signature and signs deed
    1. (Repeat for all transferees)
1. The conveyancer is asked to review and approve the document

## Future Possible Improvements

* Using the HMLR API to lookup the property address/reference, though arguably the conveyancer should have these details to hand anyway 
so perhaps keying them in saves possible lookup errors at this stage. Equally pulling the data from a case management 
system would be great too.
* allow the buyer/seller to add their own witness details and invite them when the document 
reaches them and before they undertake the signing.
* Whilst this implementation of the helper uses Docusign's SMS functionality for Recipient Identity Authentication, its worth noting that Phone Authentication could be made available too for signatories/witnesses that are unable to receive SMS.
* Docusign also supports Knowledge-Based Authentication (KBA) which might prove useful in future.
* HMLR are looking to a future beyond Witnessed electronic signatures to [Qualified electronic signatures](https://www.gov.uk/government/news/hm-land-registry-to-accept-electronic-signatures), therefore further extension through Docusign may be needed in future.

## Disclaimer

This is a beta version and as such may contain bugs/unexpected output.

## Software License & Copyright Notice

Copyright (c) 2020 Matt Pennington - Tonic Workflows

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## TR1 Copyright Notice

The *Transfer of whole of registered titles (TR1)* form is (c) Crown copyright (ref: LR/HO).